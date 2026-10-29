import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

export default defineConfig({
  plugins: [react()],
  server: {
    port: 5173,
    proxy: {
      '/api': {
        target: 'http://127.0.0.1:8080',
        changeOrigin: true,
      },
      '/health': 'http://127.0.0.1:8080',
      '/lots': 'http://127.0.0.1:8080',
      '/reconcile': 'http://127.0.0.1:8080',
      '/audit': 'http://127.0.0.1:8080',
      '/optimize': 'http://127.0.0.1:8080',
      '/disputes': 'http://127.0.0.1:8080',
      '/quantum': 'http://127.0.0.1:8080',
      '/runs': 'http://127.0.0.1:8080',
      '/evidence': 'http://127.0.0.1:8080',
      '/attacks': 'http://127.0.0.1:8080',
    }
  }
})