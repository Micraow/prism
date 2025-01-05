import { fileURLToPath, URL } from 'node:url';
import { defineConfig } from 'vite';
import vue from '@vitejs/plugin-vue';

// https://vitejs.dev/config/
export default defineConfig({
  base: './',
  minify: true, // 是否压缩代码
  sourceMap: true, // 是否生成sourceMap
  plugins: [vue()],
  server: {
    host: '0.0.0.0',
    proxy: {
      // 将所有请求代理到 Flask 后端
      '^/(livetranslate|network|history|translate|enhance)': {
        target: 'http://localhost:5000', // Flask 后端地址
        changeOrigin: true,
        rewrite: (path) => path, // 保持路径不变
      },
    },
  },
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url)),
    },
  },
});