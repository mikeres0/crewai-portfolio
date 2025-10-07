from dotenv import load_dotenv
# Configure embeddings for memory (after the self.llm creation)
from chromadb.utils.embedding_functions import OpenAIEmbeddingFunction
import os

# Load environment variables FIRST
load_dotenv()

# Set ALL possible Azure environment variables that LiteLLM might look for
os.environ["AZURE_API_TYPE"] = "azure"
os.environ["AZURE_API_VERSION"] = os.getenv("AZURE_API_VERSION", "2024-02-15-preview")
os.environ["AZURE_API_KEY"] = os.getenv("AZURE_API_KEY", "")
os.environ["AZURE_API_BASE"] = os.getenv("AZURE_API_BASE", "")

# Also set the OpenAI-style variables that some libraries look for
os.environ["OPENAI_API_TYPE"] = "azure"
os.environ["OPENAI_API_VERSION"] = os.getenv("AZURE_API_VERSION", "2024-02-15-preview")
os.environ["OPENAI_API_KEY"] = os.getenv("AZURE_API_KEY", "")
os.environ["OPENAI_API_BASE"] = os.getenv("AZURE_API_BASE", "")

from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import FileReadTool, DirectoryReadTool
from langchain_openai import AzureOpenAIEmbeddings

# Import custom UTF-8 file writer
try:
    from custom_tools import write_file_utf8
    use_custom_writer = True
except ImportError:
    from crewai_tools import FileWriterTool
    use_custom_writer = False


@CrewBase
class PortfolioWebsiteCrew():
    """Portfolio Website Development Crew"""
    
    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    def __init__(self) -> None:
        super().__init__()
        # Initialize tools
        self.file_read_tool = FileReadTool()
        self.directory_read_tool = DirectoryReadTool()  # Add this line
        
        # Always use custom UTF-8 writer
        try:
            from custom_tools import write_file_utf8
            self.file_writer_tool = write_file_utf8
            print("✅ Using custom UTF-8 file writer")
        except ImportError as e:
            print(f"⚠️  Custom tools import failed: {e}")
            from crewai_tools import FileWriterTool
            self.file_writer_tool = FileWriterTool()
            print("⚠️  Falling back to standard FileWriterTool")

        # Create output directories if they don't exist
        os.makedirs('output/docs', exist_ok=True)
        os.makedirs('output/portfolio-website', exist_ok=True)
        
        # Force UTF-8 encoding for Python on Windows
        import sys
        if sys.platform == 'win32':
            import io
            sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
            sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')
        
        # Configure Azure OpenAI using CrewAI's LLM class
        # Remove trailing slash from base_url if present
        base_url = os.getenv("AZURE_API_BASE") or os.getenv("AZURE_OPENAI_ENDPOINT")
        if base_url and base_url.endswith('/'):
            base_url = base_url[:-1]

        # Configure Azure OpenAI - Let LiteLLM read from environment variables
        deployment_name = os.getenv('AZURE_DEPLOYMENT_NAME')
            
        # LLM instance - LiteLLM requires api_base, not base_url
        self.llm = LLM(
            model=f"azure/{deployment_name}",
            api_key=os.getenv("AZURE_API_KEY"),
            api_base=base_url,  # Changed from base_url to api_base
            api_version=os.getenv("AZURE_API_VERSION"),
            temperature=0.7
        )

        # Azure OpenAI embeddings configuration
        self.embedder_config = {
            "provider": "azure_openai",
            "config": {
                "model": os.getenv("AZURE_EMBEDDING_DEPLOYMENT_NAME", "text-embedding-3-small"),
                "deployment_name": os.getenv("AZURE_EMBEDDING_DEPLOYMENT_NAME", "text-embedding-3-small"),
                "api_key": os.getenv("AZURE_API_KEY"),
                "api_base": base_url,
                "api_type": "azure",
                "api_version": os.getenv("AZURE_API_VERSION")
            }
        }

    @agent
    def portfolio_designer(self) -> Agent:
        return Agent(
            config=self.agents_config['portfolio_designer'],
            llm=self.llm,
            verbose=True,
            allow_delegation=False,
            max_iter=20,
            tools=[self.file_writer_tool]
        )

    @agent
    def frontend_architect(self) -> Agent:
        return Agent(
            config=self.agents_config['frontend_architect'],
            llm=self.llm,
            verbose=True,
            allow_delegation=False,
            max_iter=20,
            tools=[self.file_writer_tool, self.file_read_tool]
        )

    @agent
    def nuxt_developer(self) -> Agent:
        return Agent(
            config=self.agents_config['nuxt_developer'],
            llm=self.llm,
            verbose=True,
            allow_delegation=False,
            max_iter=30,
            tools=[self.file_writer_tool, self.file_read_tool, self.directory_read_tool]
        )

    @agent
    def content_strategist(self) -> Agent:
        return Agent(
            config=self.agents_config['content_strategist'],
            llm=self.llm,
            verbose=True,
            allow_delegation=False,
            max_iter=18,
            tools=[self.file_writer_tool]
        )

    @task
    def design_concept_task(self) -> Task:
        return Task(
            config=self.tasks_config['design_concept_task']
        )

    @task
    def architecture_planning_task(self) -> Task:
        return Task(
            config=self.tasks_config['architecture_planning_task']
        )

    @task
    def content_creation_task(self) -> Task:
        return Task(
            config=self.tasks_config['content_creation_task']
        )

    @task
    def implementation_task(self) -> Task:
        return Task(
            config=self.tasks_config['implementation_task']
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Portfolio Website Development crew"""
        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,    # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            allow_delegation=True,
            #memory=True,
            planning=True,
            planning_llm=self.llm,
            # Output log file
            output_log_file='portfolio_crew_output.log'
        )