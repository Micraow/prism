<template>
  <!--顶级Laytou 容器-->
  <a-layout id="components-layout" style="min-height: 100vh">
    <!--侧边栏容器-->
    <a-layout-sider>
      <!--
                :default-selected-keys="['1']"   初始选中的 子菜单项
                mode   菜单模式  inline为内嵌模式
            -->
      <a-menu theme="dark" :default-selected-keys="['1']" mode="inline">
        <a-menu-item key="1" @click="changeMenu('home')"> 首页 </a-menu-item>
        <a-menu-item key="2" @click="changeMenu('huaci')"> 划词翻译 </a-menu-item>
        <a-menu-item key="3" @click="changeMenu('paizhao')"> 拍照翻译 </a-menu-item>
        <a-menu-item key="4" @click="changeMenu('cuoti')"> 错题保存 </a-menu-item>
        <a-menu-item key="5" @click="changeMenu('about')"> 关于我们 </a-menu-item>
      </a-menu>
    </a-layout-sider>
    <!--右边主要内容-->
    <a-layout>
      <!--右边内容-->
      <a-layout-content style="margin: 0 16px">
        <!--内容头部title-->
        <div :style="{ padding: '24px', background: '#fff', minHeight: '360px' }">
          <!--定义路由出口-->
          <router-view v-slot="{ Component, route }">
            <transition name="animation" mode="out-in">
              <component :is="Component" :key="route.path" />
            </transition>
          </router-view>
        </div>
      </a-layout-content>
      <!--右边页脚-->
      <a-layout-footer style="text-align: center">
        Made with Love ©2024 Created by Prism Team from JLHS G2-11
      </a-layout-footer>
    </a-layout>
  </a-layout>
</template>
<script>
export default {
  data() {
    return {}
  },
  methods: {
    //路由内容切换
    changeMenu(route) {
      console.log(route)
      //获取路由对象并切换
      if (this.$route.path !== route) {
        this.$router.push(route)
      }
    }
  }
}

</script>

<style>
.animation-enter-from,
.animation-leave-to {
	transform: translateX(20px);
	opacity: 0;
}
.animation-enter-to,
.animation-leave-from {
	opacity: 1;
}
.animation-enter-active {
	transition: all 0.7s ease;
}
.animation-leave-active {
	transition: all 0.3s cubic-bezier(1, 0.6, 0.6, 1);
}
</style>
