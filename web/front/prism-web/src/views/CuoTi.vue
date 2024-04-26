<template>
  <main>
    <a-space direction="vertical" style="width: 100%;">
      <a-page-header style="border: 1px solid rgb(235, 237, 240)" title="错题保存" sub-title="错题是你的财富，我是你的银行" />
      <a-card>
        <p style="text-align: center;font-size: large;font-weight: bold;">点击下方按钮即可保存错题</p>
        <p style="text-align: center;">
          <a-button type="primary" shape="circle" size="large" style="height: 120px;width: 120px;">
            <template #icon>
              <PlusSquareOutlined style="fontSize: 36px" />
            </template>
          </a-button>
        </p>
      </a-card>

      <SaveCuoTi />
    </a-space>
  </main>
</template>

<script setup>
import SaveCuoTi from '../components/SaveCuoTi.vue'
import { PlusSquareOutlined } from '@ant-design/icons-vue'
</script>