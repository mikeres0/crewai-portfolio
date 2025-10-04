import type { Config } from 'tailwindcss';
import defaultTheme from 'tailwindcss/defaultTheme';

const colors = {
  electric: '#1DE9B6',
  deepblue: '#181F2B',
  vividpurple: '#8A60F6',
  crystalwhite: '#F5F8FA',
  coral: '#FF6B4A',
  cobalt: '#247CFF',
  emerald: '#37D67A',
  amber: '#FFC542',
  error: '#FF3B30',
  info: '#4ABFFD',
  darkbg: '#11151C',
  glass: 'rgba(255,255,255,0.12)'
};

const config: Config = {
  darkMode: 'class',
  content: [
    './components/**/*.{vue,js,ts}',
    './pages/**/*.{vue,js,ts}',
    './layouts/**/*.{vue,js,ts}',
    './composables/**/*.{ts}',
    './app.vue'
  ],
  theme: {
    extend: {
      colors: {
        electric: colors.electric,
        deepblue: colors.deepblue,
        vividpurple: colors.vividpurple,
        crystalwhite: colors.crystalwhite,
        coral: colors.coral,
        cobalt: colors.cobalt,
        emerald: colors.emerald,
        amber: colors.amber,
        error: colors.error,
        info: colors.info,
        darkbg: colors.darkbg,
        glass: colors.glass
      },
      fontFamily: {
        heading: ['Space Grotesk', ...defaultTheme.fontFamily.sans],
        body: ['Inter', ...defaultTheme.fontFamily.sans],
        code: ['Fira Mono', ...defaultTheme.fontFamily.mono]
      },
      spacing: {
        '8': '8px',
        '16': '16px',
        '24': '24px',
        '32': '32px',
        '48': '48px',
        '64': '64px',
        '96': '96px'
      },
      borderRadius: {
        card: '24px',
        btn: '12px',
        glass: '16px'
      },
      backdropBlur: {
        glass: '16px',
        card: '14px'
      },
      boxShadow: {
        glass: '0 8px 32px rgba(31, 38, 135, 0.15)',
        neumorph: 'inset 2px 2px 8px #181F2B, inset -2px -2px 8px #232A36'
      },
      backgroundImage: {
        'hero-gradient': 'linear-gradient(135deg, #1DE9B6 0%, #8A60F6 100%)',
        'button-gradient': 'linear-gradient(90deg, #1DE9B6 0%, #4ABFFD 100%)',
        'glass': "rgba(255,255,255,0.12)"
      },
      screens: {
        'sm': '600px',
        'md': '1024px',
        'lg': '1440px',
        'xl': '1920px'
      }
    }
  },
  plugins: [
    require('@tailwindcss/forms'),
    function({ addUtilities }) {
      addUtilities({
        '.glass': {
          'backdrop-filter': 'blur(16px)',
          'background': 'rgba(255,255,255,0.12)',
        },
        '.neumorph': {
          'box-shadow': 'inset 2px 2px 8px #181F2B, inset -2px -2px 8px #232A36'
        }
      });
    }
  ]
};

export default config;
