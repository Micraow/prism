import { createRouter, createWebHistory } from 'vue-router'
import LayOut from '../views/LayOut.vue'
import HomeView from '../views/HomeView.vue'
import HuaCi from '../views/HuaCi.vue'
import PaiZhao from '../views/PaiZhao.vue'
import CuoTi from '../views/CuoTi.vue'
import About from '../views/AboutView.vue'
import InternetConnection from '../views/InternetConnection.vue'
import HistoryPaiZhao from '../views/HistoryPaiZhao.vue'
import CuoTiSaving from '../views/CuoTiSaving.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'layout',
      component: LayOut,
      redirect: 'home',
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
        },
        {
          path: '/about',
          name: '关于',
          component: About
        },
        {
          path: '/internetconnection',
          name: '网络连接',
          component: InternetConnection
        },
        {
          path: '/historypaizhao',
          name: '拍照翻译历史',
          component: HistoryPaiZhao
        },
        {
          path: '/cuotisaving',
          name: '历史记录，已保存的错题',
          component: CuoTiSaving
        },
      ]
    }
  ]
})

export default router
