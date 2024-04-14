<template>
  <main>
    <a-page-header style="border: 1px solid rgb(235, 237, 240)" title="划词翻译" sub-title="笔下有神" />
    <a-card>
      <p style="text-align: center;font-size: large;font-weight: bold;">点击下方按钮即可划词翻译</p>
      <p style="text-align: center;">
        <a-button type="primary" shape="circle" size="large" style="height: 120px;width: 120px;">
          <template #icon>
            <PlayCircleOutlined style="fontSize: 36px" />
          </template>
        </a-button>
      </p>
    </a-card>
  </main>
</template>
<script setup>
import { PlayCircleOutlined } from '@ant-design/icons-vue'
</script>