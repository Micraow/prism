<script setup>
</script>

<template>
  <a-card>
    <p style="text-align: center; font-size: large; font-weight: bold">点击下方按钮即可拍照翻译</p>
    <p style="text-align: center">
      <a-button type="primary" shape="circle" size="large" style="height: 120px; width: 120px" @click="turnpage">
        <template #icon>
          <CameraOutlined style="fontsize: 36px" />
        </template>
      </a-button>
    </p>
  </a-card>
</template>

<script>
import { CameraOutlined } from '@ant-design/icons-vue'
  export default {
    methods: {
      turnpage() {
        this.$router.push('/HistoryPaiZhao')
      }
    }
  }
</script>
