<template>
  <main>
    <a-page-header style="border: 1px solid rgb(235, 237, 240)" title="划词翻译" sub-title="笔下有神" />
    <a-card>
      <p style="text-align: center;font-size: large;font-weight: bold;">点击下方按钮即可划词翻译</p>
      <p style="text-align: center;">
        <a-button type="primary" shape="circle" size="large" style="height: 120px;width: 120px;" @click="startLiveTranslate">
          <template #icon>
            <PlayCircleOutlined style="fontSize: 36px" />
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
    </a-collapse>
  </main>
</template>

<script setup>
import { ref } from 'vue';
import { PlayCircleOutlined } from '@ant-design/icons-vue';

const activeKey = ref(['1', '2', '3', '4']);
const bing = ref('has not finished');
const wangyi = ref('has not finished');
const deepl = ref('has not finished');
const lixian = ref('has not finished');

const startLiveTranslate = () => {
  fetch('/livetranslate/start')
    .then(response => response.json())
    .then(data => {
      if (data.Result === "Success") {
        alert('Live translation started');
        queryLiveTranslate();
      } else {
        alert('Live translation is already running');
      }
    })
    .catch(error => console.error('Error:', error));
};

const queryLiveTranslate = () => {
  fetch('/livetranslate/query')
    .then(response => response.json())
    .then(data => {
      if (data.Result === "No translation available") {
        bing.value = 'No translation available';
        wangyi.value = 'No translation available';
        deepl.value = 'No translation available';
        lixian.value = 'No translation available';
      } else {
        bing.value = data.bing || 'No result';
        wangyi.value = data.youdao || 'No result';
        deepl.value = data.deepl || 'No result';
        lixian.value = data.offline || 'No result';
      }
    })
    .catch(error => console.error('Error:', error));
};
</script>