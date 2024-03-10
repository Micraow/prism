import { createRouter, createWebHistory } from 'vue-router'
import LayOut from '../views/LayOut.vue'
import HomeView from '../views/HomeView.vue'
import HuaCi from '../views/HuaCi.vue'
import PaiZhao from '../views/PaiZhao.vue'
import CuoTi from '../views/CuoTi.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'layout',
      component: LayOut,
      children: [
        {
          path: '/home',
          name: '主页面',
          component: HomeView
          // route level code-splitting
          // this generates a separate chunk (About.[hash].js) for this route
          // which is lazy-loaded when the route is visited.
          // component: () => import('../views/AboutView.vue')
        },
        {
          path: '/huaci',
          name: '划词翻译',
          component: HuaCi
        },
        {
          path: '/paizhao',
          name: '拍照翻译',
          component: PaiZhao
        },
        {
          path: '/cuoti',
          name: '错题保存',
          component: CuoTi
        }
      ]
    }
  ]
})

export default router
