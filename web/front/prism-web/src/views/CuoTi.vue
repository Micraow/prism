<template>
  <main>
    <a-space direction="vertical" style="width: 100%;">
      <a-page-header style="border: 1px solid rgb(235, 237, 240)" title="错题保存" sub-title="错题是你的财富，我是你的银行" />
      <a-card>
        <p style="text-align: center;font-size: large;font-weight: bold;">点击下方按钮即可保存错题</p>
        <p style="text-align: center;">
          <a-button type="primary" shape="circle" size="large" style="height: 120px;width: 120px;" @click="saveCuoTi">
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
import { ref } from 'vue';
import { PlusSquareOutlined } from '@ant-design/icons-vue';
import { message } from 'ant-design-vue';

const saveCuoTi = () => {
  fetch('/enhance', {
    method: 'GET',
  })
    .then(response => response.json())
    .then(data => {
      if (data.result) {
        message.success('错题保存成功');
        console.log('保存的图片路径:', data.result);
      } else {
        message.error('错题保存失败');
      }
    })
    .catch(error => {
      console.error('Error:', error);
      message.error('错题保存失败');
    });
};
</script>