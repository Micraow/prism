<script setup>
import { ref } from 'vue';
const justify = ref("space-around")

</script>

<template>
  <main>
    <a-page-header style="border: 1px solid rgb(235, 237, 240)" title="关于我们" sub-title="超强的开发者阵容" />
    <p>按贡献量从高到低排序</p>
    <a-flex :justify="justify">
      <a-card>
        <p>
          <a-avatar :size=90 src="./src/assets/pengbo.jpg" />
        </p>
        <a href="https://pengs.top">
          <p style="text-align: center;">彭勃</p>
        </a>
        <p>组长</p>
        <p>主体程序的编写与技术指导，监制</p>
        <p>pengs.top运营者</p>

      </a-card>
      <a-card>
        <p>
        <a-avatar :size="90" style="color: #f56a00; background-color: #fde3cf">沈锦良</a-avatar>
        </p>
        <p>沈锦良</p>
        <p>组员</p>
        <p>web前端</p>
        <p>爱好文学，能作诗赋</p>
      </a-card>
      <a-card>
        <p>
        <a-avatar :size="90" style="color: #1a72e6; background-color: #29d0fa">赵陈晨</a-avatar></p>
        <p>赵陈晨</p>
        <p>组员</p>
        <p>web后端</p>
        <p>提议用web技术重构，但目前没有什么贡献</p>
      </a-card>
      <a-card>
        <p>
        <a-avatar :size="90" style="color: #b668da; background-color: #d8bef0">盛宇博</a-avatar></p>
        <p>盛宇博</p>
        <p>潜水组员</p>
        <p>给部分代码加了注释</p>
        <p>立志考上海交大人工智能系</p>
      </a-card>
    </a-flex>
  </main>
</template>
<style scoped>
p {
  text-align: center;
}
</style>