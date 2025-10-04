#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Portfolio Website Generator - Main Entry Point

This script orchestrates the CrewAI agents to generate a complete portfolio website.
"""

# Force UTF-8 encoding on Windows BEFORE any other imports
import sys
import os

if sys.platform == 'win32':
    # Set console to UTF-8
    os.system('chcp 65001 > nul')
    # Force UTF-8 for file operations
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

# Set environment variable for Python
os.environ['PYTHONIOENCODING'] = 'utf-8'

from dotenv import load_dotenv
from datetime import datetime
from pathlib import Path

# Add the current directory to the Python path
current_dir = Path(__file__).parent.absolute()
project_root = current_dir.parent.parent if 'src' in str(current_dir) else current_dir
sys.path.insert(0, str(project_root))
sys.path.insert(0, str(current_dir))

# Load environment variables FIRST
load_dotenv(dotenv_path=project_root / '.env')
if not os.getenv('AZURE_API_KEY'):
    # Try loading from current directory
    load_dotenv()

# Set LiteLLM environment variables explicitly
os.environ["AZURE_API_TYPE"] = "azure"
os.environ["AZURE_API_VERSION"] = os.getenv("AZURE_API_VERSION", "2024-02-15-preview")

# Import crew - try different paths
PortfolioWebsiteCrew = None
import_error = None

try:
    # Try direct import (if in same directory)
    from crew import PortfolioWebsiteCrew as Crew
    PortfolioWebsiteCrew = Crew
except ImportError as e:
    import_error = e
    try:
        # Try relative import (if in package structure)
        from .crew import PortfolioWebsiteCrew as Crew
        PortfolioWebsiteCrew = Crew
    except ImportError:
        try:
            # Try importing from latest_ai_development package
            from latest_ai_development.crew import PortfolioWebsiteCrew as Crew
            PortfolioWebsiteCrew = Crew
        except ImportError:
            pass

if PortfolioWebsiteCrew is None:
    print("❌ Error: Cannot find crew.py")
    print(f"\nSearched in:")
    print(f"  - {current_dir}")
    print(f"  - {project_root}")
    print(f"\nOriginal error: {import_error}")
    print(f"\nCurrent directory: {Path.cwd()}")
    print(f"\nFiles in current directory:")
    for f in Path.cwd().iterdir():
        print(f"  - {f.name}")
    print("\n💡 Make sure crew.py is in the same directory as main.py")
    print("   Or run from the project root directory")
    sys.exit(1)


def print_banner():
    """Print welcome banner"""
    banner = """
    ╔══════════════════════════════════════════════════════════════╗
    ║                                                              ║
    ║          Portfolio Website Generator v1.0                    ║
    ║          Powered by CrewAI                                   ║
    ║                                                              ║
    ╚══════════════════════════════════════════════════════════════╝
    """
    print(banner)


def check_environment():
    """Check if required environment variables are set"""
    required_vars = [
        "AZURE_API_KEY",
        "AZURE_API_BASE",
        "AZURE_DEPLOYMENT_NAME"
    ]
    
    missing_vars = []
    for var in required_vars:
        if not os.getenv(var):
            missing_vars.append(var)
    
    if missing_vars:
        print("❌ Error: Missing required environment variables:")
        for var in missing_vars:
            print(f"   - {var}")
        print("\nPlease set these in your .env file")
        print(f"\nLooking for .env in: {project_root}")
        return False
    
    print("✅ Environment variables configured")
    print(f"   - Azure Endpoint: {os.getenv('AZURE_API_BASE')}")
    print(f"   - Deployment: {os.getenv('AZURE_DEPLOYMENT_NAME')}")
    print(f"   - API Version: {os.getenv('AZURE_API_VERSION', '2024-02-15-preview')}")
    return True


def run_crew():
    """Run the portfolio website generation crew"""
    print("\n" + "="*70)
    print("🚀 Starting Portfolio Website Generation")
    print("="*70 + "\n")
    
    start_time = datetime.now()
    
    # Developer information
    inputs = {
        'developer_experience': '12 years of C# web development experience',
        'tech_stack': 'C#, .NET Core, ASP.NET, Entity Framework, SQL Server, Azure, Docker, Microservices',
        'framework_preference': 'Nuxt.js',
        'design_requirement': 'Visually striking, modern, uses contemporary design trends (glassmorphism, 3D effects, animations)',
        'target_audience': 'Technical recruiters, hiring managers, and fellow developers',
        'portfolio_goal': 'Land senior/lead developer positions at top tech companies'
    }
    
    print("📋 Project Configuration:")
    for key, value in inputs.items():
        print(f"   • {key.replace('_', ' ').title()}: {value}")
    
    print("\n" + "="*70 + "\n")
    
    try:
        # Initialize and run the crew
        portfolio_crew = PortfolioWebsiteCrew().crew()
        result = portfolio_crew.kickoff(inputs=inputs)
        
        end_time = datetime.now()
        duration = end_time - start_time
        
        print("\n" + "="*70)
        print("✅ Portfolio Website Generation Complete!")
        print("="*70)
        print(f"\n⏱️  Total Time: {duration}")
        print(f"📁 Output Location: ./output/")
        print(f"\n📄 Generated Files:")
        print(f"   • output/docs/DESIGN_SPECIFICATION.md")
        print(f"   • output/docs/TECHNICAL_ARCHITECTURE.md")
        print(f"   • output/docs/WEBSITE_CONTENT.md")
        print(f"   • output/docs/IMPLEMENTATION_SUMMARY.md")
        print(f"   • output/portfolio-website/ (complete Nuxt.js project)")
        
        print(f"\n🎯 Next Steps:")
        print(f"   1. cd output/portfolio-website")
        print(f"   2. npm install")
        print(f"   3. npm run dev")
        print(f"   4. Open http://localhost:3000")
        
        print("\n" + "="*70 + "\n")
        
        return result
        
    except Exception as e:
        print("\n" + "="*70)
        print("❌ Error During Generation")
        print("="*70)
        print(f"\n{type(e).__name__}: {str(e)}")
        print("\n💡 Troubleshooting:")
        print("   1. Check your .env file has correct Azure credentials")
        print("   2. Verify Azure OpenAI deployment is active")
        print("   3. Check API quota limits")
        print("   4. Review logs in portfolio_crew_output.log")
        print("\n" + "="*70 + "\n")
        raise


def train_crew(iterations: int = 3):
    """Train the crew for better performance"""
    print("\n" + "="*70)
    print(f"🎓 Training Crew ({iterations} iterations)")
    print("="*70 + "\n")
    
    inputs = {
        'developer_experience': '12 years of C# web development experience',
        'tech_stack': 'C#, .NET Core, ASP.NET, Entity Framework, SQL Server, Azure',
        'framework_preference': 'Nuxt.js',
        'design_requirement': 'Visually striking, modern, uses contemporary design trends'
    }
    
    try:
        portfolio_crew = PortfolioWebsiteCrew().crew()
        portfolio_crew.train(
            n_iterations=iterations,
            inputs=inputs,
            filename='portfolio_training_data.pkl'
        )
        print(f"\n✅ Training complete! Data saved to portfolio_training_data.pkl")
    except Exception as e:
        print(f"\n❌ Training failed: {e}")
        raise


def replay_task(task_id: str = None):
    """Replay a specific task from previous run"""
    print("\n" + "="*70)
    print(f"🔄 Replaying Task: {task_id or 'Last Task'}")
    print("="*70 + "\n")
    
    try:
        portfolio_crew = PortfolioWebsiteCrew().crew()
        portfolio_crew.replay(task_id=task_id)
        print(f"\n✅ Replay complete!")
    except Exception as e:
        print(f"\n❌ Replay failed: {e}")
        raise


def test_crew(iterations: int = 1):
    """Test the crew with specified iterations"""
    print("\n" + "="*70)
    print(f"🧪 Testing Crew ({iterations} iteration(s))")
    print("="*70 + "\n")
    
    inputs = {
        'developer_experience': '12 years of C# web development experience',
        'tech_stack': 'C#, .NET Core, ASP.NET, Entity Framework, SQL Server, Azure',
        'framework_preference': 'Nuxt.js',
        'design_requirement': 'Visually striking, modern, uses contemporary design trends'
    }
    
    try:
        portfolio_crew = PortfolioWebsiteCrew().crew()
        portfolio_crew.test(
            n_iterations=iterations,
            openai_model_name='gpt-4o-mini',
            inputs=inputs
        )
        print(f"\n✅ Test complete!")
    except Exception as e:
        print(f"\n❌ Test failed: {e}")
        raise


def main():
    """Main entry point"""
    print_banner()
    
    # Check environment
    if not check_environment():
        sys.exit(1)
    
    # Parse command line arguments
    if len(sys.argv) > 1:
        command = sys.argv[1].lower()
        
        if command == 'train':
            iterations = int(sys.argv[2]) if len(sys.argv) > 2 else 3
            train_crew(iterations)
            
        elif command == 'replay':
            task_id = sys.argv[2] if len(sys.argv) > 2 else None
            replay_task(task_id)
            
        elif command == 'test':
            iterations = int(sys.argv[2]) if len(sys.argv) > 2 else 1
            test_crew(iterations)
            
        elif command == 'help' or command == '--help' or command == '-h':
            print("\n📖 Usage:")
            print("   python main.py              # Run the full crew")
            print("   python main.py train [n]    # Train the crew (n iterations, default: 3)")
            print("   python main.py replay [id]  # Replay a specific task")
            print("   python main.py test [n]     # Test the crew (n iterations, default: 1)")
            print("   python main.py help         # Show this help message")
            print()
            
        else:
            print(f"❌ Unknown command: {command}")
            print("Run 'python main.py help' for usage information")
            sys.exit(1)
    else:
        # Default: run the crew
        run_crew()


if __name__ == "__main__":
    main()