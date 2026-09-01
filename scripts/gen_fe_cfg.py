from writer_util import write_f

def write_frontend_config():
    write_f("frontend/package.json", '''{
  "name": "enterprise-school-college-erp-frontend",
  "private": true,
  "version": "1.0.0",
  "type": "module",
  "scripts": {
    "dev": "vite",
    "build": "tsc && vite build",
    "preview": "vite preview"
  },
  "dependencies": {
    "react": "^18.2.0",
    "react-dom": "^18.2.0",
    "lucide-react": "^0.359.0"
  },
  "devDependencies": {
    "@types/react": "^18.2.66",
    "@types/react-dom": "^18.2.22",
    "@vitejs/plugin-react": "^4.2.1",
    "autoprefixer": "^10.4.19",
    "postcss": "^8.4.38",
    "tailwindcss": "^3.4.1",
    "typescript": "^5.2.2",
    "vite": "^5.1.6"
  }
}''')

    write_f("frontend/vite.config.ts", '''import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";
export default defineConfig({
  plugins: [react()],
  server: { port: 3000, host: "0.0.0.0" }
});''')

    write_f("frontend/tsconfig.json", '''{
  "compilerOptions": {
    "target": "ES2020",
    "lib": ["ES2020", "DOM", "DOM.Iterable"],
    "module": "ESNext",
    "skipLibCheck": true,
    "moduleResolution": "bundler",
    "jsx": "react-jsx"
  },
  "include": ["src"]
}''')

    write_f("frontend/tailwind.config.js", '''export default {
  content: ["./index.html", "./src/**/*.{js,ts,jsx,tsx}"],
  theme: { extend: {} },
  plugins: [],
};''')

    write_f("frontend/postcss.config.js", '''export default {
  plugins: { tailwindcss: {}, autoprefixer: {} }
};''')

    write_f("frontend/index.html", '''<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <title>Enterprise School & College ERP</title>
  </head>
  <body class="bg-slate-50 text-slate-900 font-sans">
    <div id="root"></div>
    <script type="module" src="/src/main.tsx"></script>
  </body>
</html>''')

    write_f("frontend/src/index.css", '''@tailwind base;
@tailwind components;
@tailwind utilities;''')

if __name__ == '__main__':
    write_frontend_config()
