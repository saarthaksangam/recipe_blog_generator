// tailwind.config.js
/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      typography: {
        DEFAULT: {
          css: {
            maxWidth: 'none',
            color: '#334155',
            h1: {
              fontWeight: '800',
              fontSize: '2.25em',
              marginTop: '0',
              marginBottom: '0.8em',
              lineHeight: '1.1',
              color: '#111827',
            },
            h2: {
              fontWeight: '700',
              fontSize: '1.5em',
              marginTop: '2em',
              marginBottom: '1em',
              lineHeight: '1.3',
              color: '#111827',
            },
            h3: {
              fontWeight: '600',
              fontSize: '1.25em',
              marginTop: '1.6em',
              marginBottom: '0.6em',
              lineHeight: '1.6',
              color: '#111827',
            },
            a: {
              color: '#2563eb',
              textDecoration: 'underline',
              fontWeight: '500',
              '&:hover': {
                color: '#1d4ed8',
              },
            },
            p: {
              marginTop: '1.25em',
              marginBottom: '1.25em',
            },
            img: {
              marginTop: '1.5rem',
              marginBottom: '1.5rem',
              borderRadius: '0.5rem',
            },
            table: {
              width: '100%',
              tableLayout: 'auto',
              textAlign: 'left',
              marginTop: '2em',
              marginBottom: '2em',
              borderCollapse: 'collapse',
            },
            thead: {
              borderBottomWidth: '1px',
              borderBottomColor: '#e2e8f0',
            },
            'thead th': {
              padding: '0.75em',
              verticalAlign: 'bottom',
              fontWeight: '600',
              color: '#1f2937',
              backgroundColor: '#f8fafc',
            },
            'tbody tr': {
              borderBottomWidth: '1px',
              borderBottomColor: '#e2e8f0',
            },
            'tbody tr:last-child': {
              borderBottomWidth: '0',
            },
            'tbody td': {
              padding: '0.75em',
              verticalAlign: 'top',
            },
            code: {
              fontFamily: 'Menlo, Monaco, Consolas, monospace',
              fontSize: '0.875em',
              backgroundColor: '#f1f5f9',
              padding: '0.2em 0.4em',
              borderRadius: '0.25em',
            },
            pre: {
              backgroundColor: '#f1f5f9',
              borderRadius: '0.375rem',
              padding: '1rem',
              overflowX: 'auto',
              fontFamily: 'Menlo, Monaco, Consolas, monospace',
              fontSize: '0.875em',
              lineHeight: '1.7',
              marginTop: '1.5em',
              marginBottom: '1.5em',
            },
            'pre code': {
              backgroundColor: 'transparent',
              padding: '0',
              borderRadius: '0',
              fontSize: '0.9em',
            },
          },
        },
      },
    },
  },
  plugins: [
    require('@tailwindcss/typography'),
  ],
}