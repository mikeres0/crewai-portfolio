# C# Developer Portfolio — Technical Architecture

---

## Table of Contents
1. [System Overview & Philosophy](#system-overview--philosophy)
2. [Project Structure & Organization](#project-structure--organization)
    - [Directory Structure](#directory-structure)
    - [Mermaid Project Structure Diagram](#mermaid-project-structure-diagram)
    - [Rationale](#structure-rationale)
3. [Component Architecture](#component-architecture)
    - [Atomic Design Breakdown](#atomic-design-breakdown)
    - [Responsibility Matrix](#component-responsibility-matrix)
    - [Prop Interfaces & TypeScript](#prop-interfaces--typescript)
    - [Communication Patterns & Reusability](#communication-patterns--reusability)
4. [State Management Strategy](#state-management-strategy)
    - [Global vs Local State](#global-vs-local-state)
    - [Pinia Store Structure](#pinia-store-structure)
    - [Composables Design](#composables-design)
    - [Persistence](#state-persistence)
5. [Rendering Strategy](#rendering-strategy)
    - [SSG/SSR Analysis](#ssgssr-analysis)
    - [Static/Dynamic Routing](#staticdynamic-routing)
    - [Hybrid & Caching](#hybrid--caching)
6. [Animation Architecture](#animation-architecture)
    - [Library Choices](#library-choices)
    - [Animation Hooks & Patterns](#animation-hooks--patterns)
    - [Performance & Reduced Motion](#performance--reduced-motion)
7. [Performance Optimization](#performance-optimization)
    - [Code Splitting & Lazy Loading](#code-splitting--lazy-loading)
    - [Assets & Fonts](#assets--fonts)
    - [CSS & JS Optimization](#css--js-optimization)
    - [Performance Budgets](#performance-budgets)
8. [SEO & Meta Management](#seo--meta-management)
    - [Meta, OG, Twitter, JSON-LD](#meta-og-twitter-json-ld)
    - [Sitemap, Robots, Canonical](#sitemap-robots-canonical)
9. [Form Handling & API Integration](#form-handling--api-integration)
    - [Client/Server Validation](#clientserver-validation)
    - [Email Service, Rate Limiting, Spam Prevention](#email-service-rate-limiting-spam-prevention)
10. [Content Management](#content-management)
    - [Markdown & Frontmatter](#markdown--frontmatter)
    - [@nuxt/content & Static JSON](#nuxtcontent--static-json)
11. [Styling & Design Tokens](#styling--design-tokens)
    - [Tailwind Config](#tailwind-config)
    - [Dark Mode](#dark-mode)
    - [Design Tokens Example](#design-tokens-example)
12. [TypeScript Integration](#typescript-integration)
    - [Strictness, Interfaces](#strictness-interfaces)
    - [Example Types](#example-types)
13. [Testing Strategy](#testing-strategy)
    - [Unit/Component/E2E/Accessibility/Visual](#unitcomponente2eaccessibilityvisual)
14. [Development Workflow](#development-workflow)
15. [Deployment Architecture](#deployment-architecture)
16. [Monitoring & Analytics](#monitoring--analytics)
17. [Technology Stack Matrix & Justification](#technology-stack-matrix--justification)
18. [Migration & Future Enhancements](#migration--future-enhancements)
19. [Code Example Gallery](#code-example-gallery)
20. [Performance Budgets & Measurement](#performance-budgets--measurement)

---

## 1. System Overview & Philosophy

This portfolio is a showcase of technical excellence, designed to impress both recruiters and engineers. The architecture prioritizes:
- Scalability & Maintainability: Feature-based modular structure, atomic component design, clear boundaries.
- Performance: SSG-first, lazy loading, optimized assets, strict performance budgets.
- Interactivity & Animations: GSAP/Motion One-powered animations, micro-interactions, smooth transitions.
- Accessibility: WCAG 2.1 AA, reduced motion, keyboard navigation, semantic markup.
- SEO: Nuxt SEO Kit/meta, structured data, Open Graph, robust sitemap.
- DX: TypeScript strict mode, auto-imports, clear composable patterns, extensive documentation.

---

## 2. Project Structure & Organization

### Directory Structure

```
/ (root)
├── app.vue
├── nuxt.config.ts
├── tsconfig.json
├── .env, .env.production, .env.example
├── package.json
├── tailwind.config.ts
├── README.md
├── public/
│   ├── favicon.ico
│   └── robots.txt
├── assets/
│   ├── images/
│   ├── fonts/
│   └── styles/
├── components/
│   ├── atoms/
│   ├── molecules/
│   ├── organisms/
│   ├── templates/
│   └── ui/
├── composables/
│   ├── useTheme.ts
│   ├── useScrollAnimation.ts
│   ├── useContactForm.ts
│   ├── useIntersectionObserver.ts
│   └── ...
├── stores/
│   ├── theme.ts
│   ├── user.ts
│   └── ...
├── layouts/
│   ├── default.vue
│   ├── minimal.vue
│   └── error.vue
├── pages/
│   ├── index.vue
│   ├── about.vue
│   ├── projects/
│   │   └── [slug].vue
│   ├── blog/
│   │   └── [slug].vue
│   ├── contact.vue
│   └── ...
├── content/
│   ├── projects/
│   │   └── project-1.md
│   ├── blog/
│   └── ...
├── server/
│   ├── api/
│   │   └── contact.ts
│   └── middleware/
├── utils/
│   ├── formatDate.ts
│   ├── constants.ts
│   └── ...
├── tests/
│   ├── unit/
│   ├── components/
│   ├── e2e/
│   └── accessibility/
└── static/
```

### Mermaid Project Structure Diagram

```mermaid
graph TD
  A[app.vue] -->|uses| B[layouts/]
  B --> C[components/]
  C --> D1[atoms/]
  C --> D2[molecules/]
  C --> D3[organisms/]
  C --> D4[templates/]
  C --> D5[ui/]
  B --> E[pages/]
  E --> F1[index.vue]
  E --> F2[about.vue]
  E --> F3[projects/[slug].vue]
  E --> F4[contact.vue]
  B --> G[composables/]
  B --> H[stores/]
  B --> I[utils/]
  B --> J[assets/]
  B --> K[public/]
  B --> L[content/]
  B --> M[server/]
  B --> N[tests/]
```

### Structure Rationale
- Feature-based with atomic layering: Promotes reusability and clarity. UI primitives are available for all features; complex UI is composed up the chain.
- Composables: All composable logic (hooks, custom utilities) lives in /composables and is auto-imported by Nuxt.
- Separation of concerns: Pages for routing, layouts for wrappers, content for markdown/blog, server for API.
- Type organization: Types colocated with modules or in a /types directory for large apps.
- Testing mirrors structure: /tests matches /components, /composables, etc.

---

## 3. Component Architecture

### Atomic Design Breakdown
```
components/
├── atoms/       # Buttons, icons, input fields, badge, chip, avatar
├── molecules/   # Input groups, nav links, card base, skill badge
├── organisms/   # Nav bar, hero, skill graph, timeline, project card, testimonial slider, contact form
├── templates/   # Page-level (e.g., HomePageTemplate.vue)
├── ui/          # Shared primitives: Modal, Tooltip, Popover, Loader
```

### Component Responsibility Matrix

| Layer      | Example Component           | Responsibility                                        |
|------------|----------------------------|-------------------------------------------------------|
| Atoms      | Button, Icon, Input        | Single-purpose, no business logic                     |
| Molecules  | NavLink, InputGroup        | Group basic atoms, add simple validation/interaction  |
| Organisms  | Navbar, ProjectCard        | Complex UI, manage state/logic, connect to store      |
| Templates  | HomePageTemplate           | Arrange organisms, page layout, fetch data            |
| UI         | Modal, Tooltip             | Shared UI primitives, accessible, style-agnostic      |

### Prop Interfaces & TypeScript

Example (ProjectCard):
```ts
// components/organisms/ProjectCard.vue
type ProjectCardProps = {
  title: string;
  description: string;
  image: string;
  tags: string[];
  link: string;
  techStack: string[];
};
```
- Best practice: All props are typed, use `defineProps<T>()` in SFCs.
- Events: Use `defineEmits` with TypeScript signatures (e.g., `(click: MouseEvent) => void`).

### Communication Patterns & Reusability
- Props-down, events-up for parent-child.
- Provide/inject for theme context, modal context.
- Pinia for global/shared state (theme, user preferences).
- Slots for high composability.
- Configurable via props: e.g., `<Button variant="primary" size="lg" />`
- Reusable UI: Atoms/molecules have no business logic, style via Tailwind classes and tokens.

---

## 4. State Management Strategy

### Global vs Local State
- Global (Pinia):
    - Theme (dark/light/system, persisted)
    - User preferences (reduced motion, color scheme)
    - Contact form UI state (submission, feedback)
- Local:
    - Section-specific toggles (modal open, accordion, etc.)
    - Animation state (revealed, active)
    - Form values (before submit)

### Pinia Store Structure

`/stores/theme.ts`:
```ts
import { defineStore } from 'pinia';
export const useThemeStore = defineStore('theme', {
  state: () => ({
    theme: 'system' as 'light' | 'dark' | 'system',
    reducedMotion: false
  }),
  actions: {
    setTheme(theme) { this.theme = theme; },
    setReducedMotion(val) { this.reducedMotion = val; }
  }
});
```

### Composables Design
- `useTheme`: Reads from Pinia, applies theme class to `<html>`, persists in `localStorage`.
- `useScrollAnimation`: Sets up IntersectionObserver, triggers animations.
- `useContactForm`: Manages form state, validation, API call, loading/errors.

### State Persistence
- Theme & preferences: LocalStorage via composable.
- Contact form anti-spam: Store last submit time in local/session storage.
- Pinia-persistedstate plugin optional for more complex needs.

---

## 5. Rendering Strategy

### SSG/SSR Analysis
- SSG (Static Site Generation):
    - Home, About, Projects, Blog (main content)
    - All content can be statically pre-rendered for speed/SEO.
- SSR (Server-Side Rendering):
    - Contact form (on submit), server API routes (email, rate-limiting).
- SPA/CSR:
    - Interactive demos, code playgrounds (client-only components).

### Static/Dynamic Routing
- Dynamic routes:
    - `/projects/[slug].vue` and `/blog/[slug].vue` (SSG, use content/markdown sources).
- Hybrid:
    - Use Nuxt's hybrid rendering for pages with both static and dynamic data.
- Caching:
    - CDN caching (Netlify/Vercel), HTTP cache headers for assets.

---

## 6. Animation Architecture

### Library Choices
- GSAP (for complex timelines, scroll-linked, 3D/parallax)
- Motion One (for lightweight, performant UI interactions)
- Native CSS (for basic transforms, transitions, prefers-reduced-motion)
- IntersectionObserver (for scroll-triggered entrances)

### Animation Hooks & Patterns
- `useScrollAnimation`: IntersectionObserver, triggers GSAP/Motion One entrance animations.
- Page transitions: Nuxt's `<NuxtPage transition="fade-slide" />`, custom transitions for major routes.
- Micro-interactions: CSS transitions for hover/active, ripple via JS/CSS.

### Performance & Reduced Motion
- `will-change`, transform/opacity only for GPU acceleration.
- Prefers-reduced-motion:
    - All composables check `window.matchMedia('(prefers-reduced-motion)')`.
    - Animations pause/disable if set.

---

## 7. Performance Optimization

### Code Splitting & Lazy Loading
- Route-based splitting: Nuxt auto-chunks per page.
- Component lazy loading: `defineAsyncComponent()` for heavy/rarely-used organisms.
- Dynamic imports: For code demos, charts, 3D backgrounds.

### Assets & Fonts
- Images: AVIF/WebP preferred, responsive `srcset`, CDN delivered.
- Fonts: Self-hosted, `preload` for headings, `font-display: swap`.
- SVGs: Inline for icons, optimized via SVGO.

### CSS & JS Optimization
- Tailwind jit/purge: Only used classes included in build.
- Critical CSS: Nuxt automatically inlines above-the-fold styles.
- Bundle analysis: Use `nuxt build --analyze`, reduce vendor chunk size.

### Performance Budgets
- LCP: < 2.5s
- FID: < 100ms
- CLS: < 0.1
- JS bundle: < 100kb initial
- Image payload: < 300kb above-the-fold

---

## 8. SEO & Meta Management

### Meta, OG, Twitter, JSON-LD
- Use nuxt-seo-kit or @nuxtjs/seo for dynamic meta tags.
- Per-page meta:
```js
export default definePageMeta({
  title: 'Home | John Doe - C# Developer',
  description: 'Portfolio of John Doe, expert in C#, .NET, Azure...'
});
```
- Open Graph:
```html
<meta property="og:title" :content="pageTitle" />
<meta property="og:description" :content="pageDesc" />
<meta property="og:image" :content="ogImageUrl" />
<meta property="og:type" content="website" />
```
- Twitter Card:
```html
<meta name="twitter:card" content="summary_large_image" />
<meta name="twitter:title" :content="pageTitle" />
```
- JSON-LD:
```json
{
  "@context": "https://schema.org",
  "@type": "Person",
  "name": "John Doe",
  "url": "https://johndoe.dev",
  "sameAs": ["https://github.com/johndoe", "..."]
}
```

### Sitemap, Robots, Canonical
- @nuxtjs/sitemap for auto sitemap generation
- `public/robots.txt` with `Sitemap:` directive
- Canonical URLs via meta

---

## 9. Form Handling & API Integration

### Client/Server Validation
- Client: Schema-based (zod/yup), live feedback, ARIA errors
- Server: Validate on API, sanitize, rate-limit
- Error Boundaries: UI for global and field errors

### Email Service, Rate Limiting, Spam Prevention
- Server route: `server/api/contact.ts` calls Resend/SendGrid/Nodemailer
- Rate limiting: IP-based, store last submit timestamp per session
- Spam prevention: Hidden honeypot field, reCAPTCHA v3, server-side validation
- Feedback: Success/failure states, animated feedback

---

## 10. Content Management

### Markdown & Frontmatter
- Projects/blog: Markdown with frontmatter (`title`, `summary`, `tags`, `date`, etc.)
- Parsed with @nuxt/content or static import for simple data

### @nuxt/content & Static JSON
- For more dynamic needs, use [@nuxt/content](https://content.nuxtjs.org/).
- For static sections (skills, experience), use `/content/data.json` or `/utils/constants.ts`.

---

## 11. Styling & Design Tokens

### Tailwind Config
- Custom colors: Mirrors design palette (see design spec)
- Fonts: Space Grotesk, Inter, Fira Mono
- Spacing/Size scale: 8px base, extended via config
- Border radius: 24px for cards, 12px for buttons, etc.
- Glassmorphism utilities: Custom utilities for backdrop-blur, bg-opacity

### Dark Mode
- Class-based: `dark` class toggled on `<html>`
- Persisted: via Pinia/composable + localStorage
- Tokens: CSS variables for color, referenced in Tailwind config

### Design Tokens Example
```ts
// utils/constants.ts
export const COLORS = {
  primary: '#1DE9B6',
  secondary: '#8A60F6',
  background: '#181F2B',
  // ...
};
```

---

## 12. TypeScript Integration

### Strictness, Interfaces
- Strict mode: `strict: true` in tsconfig.json
- Prop types: All props are typed via `defineProps<T>()`
- API types: All server responses are typed
- Composable return types: Explicitly typed

### Example Types
```ts
export interface Project {
  slug: string;
  title: string;
  summary: string;
  description: string;
  image: string;
  tags: string[];
  techStack: string[];
  links: {
    demo: string;
    repo?: string;
  };
}
```

---

## 13. Testing Strategy

### Unit/Component/E2E/Accessibility/Visual
- Unit tests: Vitest, colocated in `/tests/unit`
- Component tests: Vue Test Utils, `/tests/components`
- E2E: Playwright or Cypress, `/tests/e2e`
- Accessibility: axe-core integrated in E2E
- Visual regression: Percy/Chromatic optional
- Coverage: >90% critical components
- CI/CD: GitHub Actions runs all checks on PR

---

## 14. Development Workflow

- Hot module reload: Nuxt HMR
- .env handling: `.env`, `.env.production`, `.env.example`
- ESLint/Prettier: Strict config, auto-fix on save
- Git hooks: Husky + lint-staged, pre-commit lint/test
- Commitlint: Conventional commits enforced
- Docs: `/README.md`, code comments, Storybook for components (optional)

---

## 15. Deployment Architecture

- Static hosting: Netlify, Vercel, Cloudflare Pages (all SSG-ready, fast CDN)
- Build optimization: `nuxt build --prerender`
- Custom domain: Managed via host dashboard
- SSL: Automatic, enforced
- Environment variables: Nuxt runtime config, `.env.*`
- CDN: Images/fonts/assets via host CDN
- Preview deployments: Per-PR (Netlify/Vercel)

Recommendation:
- Vercel: Best Nuxt integration, fast preview/CDN, easy serverless API.
- Netlify: Excellent for SSG, generous free tier.

---

## 16. Monitoring & Analytics

- Analytics: Plausible (privacy-respecting), fallback Google Analytics
- Error tracking: Sentry integration (Nuxt module)
- Performance: Web Vitals via Vercel Analytics/Google
- User behavior: Optional (Hotjar/Fullstory), use only with consent
- Dashboard: Vercel/Netlify dashboards for deploys, analytics, error logs

---

## 17. Technology Stack Matrix & Justification

| Area             | Chosen Tech         | Alternatives         | Rationale                                 |
|------------------|--------------------|----------------------|-------------------------------------------|
| Framework        | Nuxt 3             | Next.js, Astro       | Vue 3, SSR/SSG, auto-imports, DX          |
| Language         | TypeScript         | JavaScript           | Type safety, maintainability              |
| CSS Framework    | Tailwind CSS       | SCSS, CSS Modules    | Utility-first, rapid prototyping, tokens  |
| Animations       | GSAP, Motion One   | Framer Motion        | Power (GSAP), lightness (Motion One)      |
| State Mgmt       | Pinia, Composables | Vuex, Redux          | Modern, modular, composable               |
| Content          | @nuxt/content      | Sanity, headless CMS | Simplicity, markdown, file-based          |
| Forms/API        | Nuxt server routes | Express, Lambda      | Native to Nuxt, simple API integration    |
| Lint/Test        | ESLint, Vitest     | Jest, Mocha          | Fast, Vue 3 support                       |
| E2E Test         | Playwright         | Cypress              | Speed, modern browser support             |
| Hosting/CDN      | Vercel             | Netlify, Cloudflare  | Fast, simple, preview deploys             |
| Monitoring       | Sentry, Plausible  | GA, LogRocket        | Privacy, error reporting                  |

---

## 18. Migration & Future Enhancements

- Blog: Expand `/content/blog`, add `/pages/blog/[slug].vue`.
- Headless CMS: Migrate to Sanity/Contentful for non-developer editability.
- i18n: Add @nuxtjs/i18n for multilingual support.
- Portfolio features: Real-time chat, booking calendar, etc.
- SSR for gated content: For auth-required or dynamic features.

---

## 19. Code Example Gallery

### 1. Scroll-triggered Animation Composable
```ts
// composables/useScrollAnimation.ts
import { ref, onMounted, onUnmounted } from 'vue';
export function useScrollAnimation(elRef: Ref<HTMLElement | null>, onEnter: () => void) {
  let observer: IntersectionObserver | null = null;
  onMounted(() => {
    observer = new IntersectionObserver(([entry]) => {
      if (entry.isIntersecting) onEnter();
    }, { threshold: 0.2 });
    if (elRef.value) observer.observe(elRef.value);
  });
  onUnmounted(() => {
    if (observer && elRef.value) observer.unobserve(elRef.value);
  });
}
```

### 2. Async Project Card Loading
```vue
<script setup lang="ts">
const ProjectCard = defineAsyncComponent(() => import('~/components/organisms/ProjectCard.vue'));
</script>
<template>
  <Suspense>
    <ProjectCard v-for="p in projects" :key="p.slug" :project="p" />
    <template #fallback>
      <SkeletonCard v-for="n in 3" :key="n" />
    </template>
  </Suspense>
</template>
```

### 3. Tailwind Glassmorphism Utility
```js
// tailwind.config.ts
module.exports = {
  theme: {
    extend: {
      backdropBlur: {
        glass: '16px',
      },
      colors: {
        glass: 'rgba(255,255,255,0.12)',
      },
    },
  },
  plugins: [
    require('@tailwindcss/forms'),
    function({ addUtilities }) {
      addUtilities({
        '.glass': {
          'backdrop-filter': 'blur(16px)',
          'background': 'rgba(255,255,255,0.12)',
        }
      });
    },
  ],
};
```

### 4. Contact API Route (server/api/contact.ts)
```ts
import { H3Event, sendError } from 'h3';
import { z } from 'zod';
const schema = z.object({ name: z.string(), email: z.string().email(), message: z.string().min(5) });
export default defineEventHandler(async (event: H3Event) => {
  const body = await readBody(event);
  const result = schema.safeParse(body);
  if (!result.success) return sendError(event, createError({ statusCode: 400, statusMessage: 'Invalid input' }));
  // Rate limit/spam check logic here
  // Send email with Resend/SendGrid
  return { status: 'ok' };
});
```

---

## 20. Performance Budgets & Measurement

- LCP: < 2.5s (audit with Lighthouse, Web Vitals)
- FID: < 100ms
- CLS: < 0.1
- JS bundle: < 100kb initial (analyze with nuxt build --analyze)
- Image payload: < 300kb above-the-fold (check with Chrome DevTools)
- CI: Automated Lighthouse in CI, fail build if budgets exceeded

---

# END OF TECHNICAL ARCHITECTURE