<script setup>
import { SaveOutlined } from '@ant-design/icons-vue'
</script>

<template>
  <a-card>
    <p style="text-align: center;font-size: large;font-weight: bold;">历史记录</p>
    <p style="text-align: center;">
      <a-button type="primary" shape="circle" size="large" style="height: 120px;width: 120px;" @click="turnpage">
        <template #icon>
          <SaveOutlined style="fontSize: 36px" />
        </template>
      </a-button>
    </p>
  </a-card>
</template>

<script>
export default {
  methods: {
    turnpage() {
      this.$router.push('/HistoryPaiZhao')
    }
  }
}
</script>
