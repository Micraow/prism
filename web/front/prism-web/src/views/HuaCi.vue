<template>
  <main>
    <a-page-header style="border: 1px solid rgb(235, 237, 240)" title="划词翻译" sub-title="笔下有神" />
    <a-card>
      <p style="text-align: center;font-size: large;font-weight: bold;">点击下方按钮即可划词翻译</p>
      <p style="text-align: center;">
        <a-button 
          type="primary" 
          shape="circle" 
          size="large" 
          style="height: 120px;width: 120px;" 
          @click="toggleLiveTranslate"
        >
          <template #icon>
            <PlayCircleOutlined v-if="!isTranslating" style="fontSize: 36px" />
            <StopOutlined v-else style="fontSize: 36px" />
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
      <a-collapse-panel key="5" header="Google翻译">
        <p>{{ google }}</p>
      </a-collapse-panel>
    </a-collapse>
  </main>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue';
import { PlayCircleOutlined, StopOutlined } from '@ant-design/icons-vue';
import { message } from 'ant-design-vue';

const activeKey = ref(['1', '2', '3', '4', '5']);
const bing = ref('has not finished');
const wangyi = ref('has not finished');
const deepl = ref('has not finished');
const lixian = ref('has not finished');
const google = ref('has not finished');
const isTranslating = ref(false);
let queryInterval = null;

const startLiveTranslate = () => {
  fetch('/livetranslate/start')
    .then(response => response.json())
    .then(data => {
      if (data.Result === "Success") {
        message.success('实时翻译已开始');
        isTranslating.value = true;
      } else {
        message.error('实时翻译已在进行中');
      }
    })
    .catch(error => {
      console.error('Error:', error);
      message.error('启动实时翻译失败');
    });
};

const endLiveTranslate = () => {
  fetch('/livetranslate/end')
    .then(response => response.json())
    .then(data => {
      if (data.Result === "Success") {
        message.success('实时翻译已结束');
        isTranslating.value = false;
        startQuerying();
      } else {
        message.error('结束实时翻译失败');
      }
    })
    .catch(error => {
      console.error('Error:', error);
      message.error('结束实时翻译失败');
    });
};

const toggleLiveTranslate = () => {
  if (isTranslating.value) {
    endLiveTranslate();
  } else {
    startLiveTranslate();
  }
};

const startQuerying = () => {
  queryInterval = setInterval(() => {
    fetch('/livetranslate/query')
      .then(response => response.json())
      .then(data => {
        if (data.Result === "No translation available") {
          bing.value = 'No translation available';
          wangyi.value = 'No translation available';
          deepl.value = 'No translation available';
          lixian.value = 'No translation available';
          google.value = 'No translation available';
        } else {
          bing.value = data.bing || 'No result';
          wangyi.value = data.youdao || 'No result';
          deepl.value = data.deepl || 'No result';
          lixian.value = data.offline || 'No result';
          google.value = data.google || 'No result';
        }
      })
      .catch(error => console.error('Error:', error));
  }, 1000); // 每1秒查询一次
};

const stopQuerying = () => {
  if (queryInterval) {
    clearInterval(queryInterval);
    queryInterval = null;
  }
};

onUnmounted(() => {
  stopQuerying();
});
</script>