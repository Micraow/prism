<template>
  <main>
    <a-space direction="vertical" style="width: 100%;">
      <a-page-header style="border: 1px solid rgb(235, 237, 240)" title="拍照翻译" sub-title="让我做你的眼睛" />

      <a-card>
        <p style="text-align: center; font-size: large; font-weight: bold">点击下方按钮即可拍照翻译</p>
        <p style="text-align: center">
          <a-button type="primary" shape="circle" size="large" style="height: 120px; width: 120px" @click="captureAndTranslate">
            <template #icon>
              <CameraOutlined style="fontsize: 36px" />
            </template>
          </a-button>
        </p>
      </a-card>

      <a-collapse v-model:activeKey="activeKey" :bordered="false">
        <a-collapse-panel key="1" header="必应翻译">
          <p>{{ bing }}</p>
        </a-collapse-panel>
        <a-collapse-panel key="2" header="有道翻译">
          <p>{{ wangyi }}</p>
        </a-collapse-panel>
        <a-collapse-panel key="3" header="DeepL翻译">
          <p>{{ deepl }}</p>
        </a-collapse-panel>
        <a-collapse-panel key="4" header="离线翻译">
          <p>{{ lixian }}</p>
        </a-collapse-panel>
        <a-collapse-panel key="5" header="必应词典">
          <p>{{ bing_dict }}</p>
        </a-collapse-panel>
        <a-collapse-panel key="6" header="谷歌翻译">  
          <p>{{ google }}</p>
        </a-collapse-panel>
      </a-collapse>

      <TurnToHistoryPaiZhao />

    </a-space>
  </main>
</template>

<script setup>
import { ref } from 'vue';
import { CameraOutlined } from '@ant-design/icons-vue';
import TurnToHistoryPaiZhao from '../components/TurnToHistoryPaiZhao.vue';

const activeKey = ref(['1', '2', '3', '4','5','6']);
const bing = ref('has not finished');
const wangyi = ref('has not finished');
const deepl = ref('has not finished');
const lixian = ref('has not finished');
const bing_dict = ref('has not finished');
const google = ref('has not finished');

const captureAndTranslate = () => {
  fetch('/translate/photo')
    .then(response => response.json())
    .then(data => {
      bing.value = data.bing || 'No result';
      wangyi.value = data.\u6709\u9053\u7ffb\u8bd1 || 'No result';
      deepl.value = data.deepl || 'No result';
      lixian.value = data.\u79bb\u7ebf\u7ffb\u8bd1 || 'No result';
      bing_dict.value = data.bing\u8bcd\u5178 || 'No result';
      google.value = data.google || 'No result';
    })
    .catch(error => console.error('Error:', error));
};
</script>