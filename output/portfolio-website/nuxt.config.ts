import { defineNuxtConfig } from 'nuxt/config';

export default defineNuxtConfig({
  ssr: true,
  devtools: { enabled: true },
  typescript: {
    strict: true,
    shim: false
  },
  modules: [
    '@nuxt/content',
    '@nuxtjs/tailwindcss',
    'nuxt-seo-kit',
    '@nuxtjs/sitemap',
    '@nuxtjs/robots',
    '@pinia/nuxt'
  ],
  tailwindcss: {
    cssPath: '~/assets/css/main.css',
    configPath: 'tailwind.config.ts',
    viewer: false
  },
  seoKit: {
    siteUrl: 'https://yourdomain.com',
    title: 'Senior C# Developer & .NET Architect | 12 Years Experience',
    description: 'Award-winning C# developer and .NET architect with 12 years’ experience building scalable, cloud-native enterprise solutions. Explore projects, skills, and contact for new opportunities.',
    image: '/og-default.png',
    twitter: {
      card: 'summary_large_image',
      site: '@yourhandle'
    },
    canonical: true,
    openGraph: {
      type: 'website',
      locale: 'en_US'
    },
    jsonLd: {
      '@type': 'Person',
      'name': 'Your Name',
      'jobTitle': 'Senior C# Developer & .NET Architect',
      'image': '/profile.jpg',
      'worksFor': { '@type': 'Organization', 'name': 'Finlytics Cloud' },
      'sameAs': [
        'https://github.com/yourprofile',
        'https://linkedin.com/in/yourprofile'
      ]
    }
  },
  sitemap: {
    hostname: 'https://yourdomain.com',
    gzip: true
  },
  robots: {
    UserAgent: '*',
    Disallow: '',
    Sitemap: 'https://yourdomain.com/sitemap.xml'
  },
  runtimeConfig: {
    public: {
      siteName: 'C# Developer Portfolio',
      contactEmail: 'your.email@example.com'
    },
    emailServiceApiKey: '',
    emailServiceFrom: '',
    emailServiceTo: ''
  },
  app: {
    head: {
      charset: 'utf-8',
      viewport: 'width=device-width, initial-scale=1',
      title: 'Senior C# Developer & .NET Architect | 12 Years Experience',
      meta: [
        { name: 'description', content: 'Award-winning C# developer and .NET architect with 12 years’ experience building scalable, cloud-native enterprise solutions.' },
        { name: 'theme-color', content: '#1DE9B6' },
        { name: 'color-scheme', content: 'dark light' }
      ],
      link: [
        { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' },
        { rel: 'preload', as: 'font', href: '/fonts/SpaceGrotesk-Bold.woff2', type: 'font/woff2', crossorigin: 'anonymous' },
        { rel: 'preload', as: 'font', href: '/fonts/Inter-Regular.woff2', type: 'font/woff2', crossorigin: 'anonymous' }
      ]
    }
  },
  experimental: {
    payloadExtraction: true
  }
});
