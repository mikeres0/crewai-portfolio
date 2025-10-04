<script setup lang="ts">
import { useHead } from '@unhead/vue';

useHead({
  title: 'Engineering Scalable Impact: 12 Years of C# Innovation, System Design, and Delivery',
  meta: [
    { name: 'description', content: 'Award-winning C# developer and .NET architect with 12 years’ experience building scalable, cloud-native enterprise solutions.' },
    { property: 'og:title', content: 'Senior C# Developer & .NET Architect | 12 Years Experience' },
    { property: 'og:description', content: 'Award-winning C# developer and .NET architect with 12 years’ experience building scalable, cloud-native enterprise solutions.' },
    { property: 'og:type', content: 'website' },
    { property: 'og:image', content: '/og-default.png' },
    { name: 'twitter:card', content: 'summary_large_image' },
    { name: 'twitter:title', content: 'Senior C# Developer & .NET Architect' },
    { name: 'twitter:description', content: 'Award-winning C# developer and .NET architect with 12 years’ experience.' }
  ],
  link: [
    { rel: 'canonical', href: 'https://yourdomain.com/' }
  ],
  script: [
    {
      type: 'application/ld+json',
      innerHTML: `{
        "@context": "https://schema.org",
        "@type": "Person",
        "name": "Your Name",
        "jobTitle": "Senior C# Developer & .NET Architect",
        "image": "/profile.jpg",
        "sameAs": ["https://linkedin.com/in/yourprofile", "https://github.com/yourprofile"],
        "worksFor": {"@type": "Organization", "name": "Finlytics Cloud"},
        "alumniOf": {"@type": "CollegeOrUniversity", "name": "Your University"},
        "knowsAbout": ["C#", ".NET", "Azure", "Microservices", "CQRS", "DDD"]
      }`
    }
  ]
});
</script>

<template>
  <main id="main-content" tabindex="-1" class="bg-darkbg text-crystalwhite min-h-screen">
    <Hero />
    <About />
    <Skills />
    <Experience />
    <Projects />
    <Testimonials />
    <Contact />
  </main>
</template>

<script lang="ts">
import Hero from '@/components/sections/Hero.vue';
import About from '@/components/sections/About.vue';
import Skills from '@/components/sections/Skills.vue';
import Experience from '@/components/sections/Experience.vue';
import Projects from '@/components/sections/Projects.vue';
import Testimonials from '@/components/sections/Testimonials.vue';
import Contact from '@/components/sections/Contact.vue';

export default {
  components: {
    Hero,
    About,
    Skills,
    Experience,
    Projects,
    Testimonials,
    Contact
  }
};
</script>
