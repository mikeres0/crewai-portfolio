# Senior C# Developer Portfolio

A visually striking, production-ready Nuxt 3 portfolio showcasing 12 years of C#/.NET expertise. Features glassmorphism, kinetic typography, advanced animations, accessibility, SEO, and robust form/email integration.

## Features
- Nuxt 3 + TypeScript (strict mode)
- Tailwind CSS (custom config, glassmorphism, gradients)
- Advanced GSAP animations, scroll triggers, micro-interactions
- Responsive, mobile-first, WCAG 2.1 AA accessible
- Dynamic SEO, Open Graph, Twitter Cards, JSON-LD schema
- Project, experience, skills, testimonials, and contact sections
- Contact form: validation, honeypot, rate limit, Nodemailer/Resend integration
- Static generation, optimized images/fonts, critical CSS
- Lighthouse 95+ ready, cross-browser, reduced motion support
- Pinia state management, composables, persistent dark mode
- Component, E2E, accessibility, and coverage tests
- Full documentation and deployment guides

## Setup & Development
1. Install dependencies:
   ```bash
   npm install
   ```
2. Start development server:
   ```bash
   npm run dev
   ```
   App runs on http://localhost:3000

## Build & Generate
- Production build:
  ```bash
  npm run build
  ```
- Static generation:
  ```bash
  npm run generate
  ```
- Output is in `.output/` (ready for Netlify/Vercel/Cloudflare)

## Deployment
- Deploy `.output/` to Netlify, Vercel, or Cloudflare Pages
- See [docs/DEPLOYMENT.md](docs/DEPLOYMENT.md) for step-by-step instructions

## Environment Variables
Copy `.env.example` to `.env` and fill:
```
EMAIL_SERVICE_API_KEY=<your_api_key>
EMAIL_SERVICE_FROM=<your_from_email>
EMAIL_SERVICE_TO=<your_destination_email>
```

## Testing
- Run all tests:
  ```bash
  npm test
  ```
- Lint & format:
  ```bash
  npm run lint
  npm run format
  ```
- Test coverage:
  ```bash
  npm run test:coverage
  ```

## Documentation
- [docs/DEVELOPMENT.md](docs/DEVELOPMENT.md): Component, code, and workflow documentation
- [docs/DEPLOYMENT.md](docs/DEPLOYMENT.md): Production, hosting, and domain setup

## Project Structure
```
|-- app.vue
|-- nuxt.config.ts
|-- tsconfig.json
|-- tailwind.config.ts
|-- .env.example
|-- package.json
|-- README.md
|-- .eslintrc.js
|-- .prettierrc
|-- .gitignore
|-- pages/
|-- layouts/
|-- components/
|-- composables/
|-- types/
|-- assets/
|-- public/
|-- server/
|-- docs/
```

## Key Technologies
Nuxt 3, TypeScript, Tailwind, GSAP, Chart.js, Pinia, Nodemailer, Resend, Plausible Analytics

## License
MIT
