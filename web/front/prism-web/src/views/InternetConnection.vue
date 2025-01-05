<template>
  <main>
    <a-space direction="vertical" style="width: 100%;">
      <a-page-header style="border: 1px solid rgb(235, 237, 240)" title="网络连接" sub-title="请连接至局域网" />
      <a-card>
        <a-button type="primary" @click="scanWifi">扫描周围的无线热点</a-button>
        <a-list :data-source="wifiList">
          <template #renderItem="{ item }">
            <a-list-item>
              <a-list-item-meta :description="`需要密码: ${item.need_password ? '是' : '否'}`">
                <template #title>
                  <a @click="showPasswordModal(item.ssid)">{{ item.ssid }}</a>
                </template>
              </a-list-item-meta>
            </a-list-item>
          </template>
        </a-list>
      </a-card>
    </a-space>

    <!-- 密码输入模态框 -->
    <a-modal
      v-model:visible="passwordModalVisible"
      :title="`连接 Wi-Fi: ${selectedSsid}`"
      @ok="connectWifi"
      @cancel="closePasswordModal"
      :ok-text="'连接'"
      :cancel-text="'取消'"
    >
      <a-input
        v-model:value="password"
        placeholder="请输入密码"
        type="password"
      />
    </a-modal>
  </main>
</template>

<script setup>
import { ref } from 'vue';
import { message } from 'ant-design-vue';

const wifiList = ref([]);
const passwordModalVisible = ref(false);
const selectedSsid = ref('');
const password = ref('');

const scanWifi = () => {
  fetch('/network/scan')
    .then(response => response.json())
    .then(data => {
      // 将对象转换为数组
      wifiList.value = Object.values(data).map(wifi => ({
        ssid: wifi.ssid,
        need_password: wifi.need_password,
      }));
    })
    .catch(error => console.error('Error:', error));
};

const showPasswordModal = (ssid) => {
  selectedSsid.value = ssid;
  passwordModalVisible.value = true;
};

const closePasswordModal = () => {
  passwordModalVisible.value = false;
  password.value = '';
};

const connectWifi = () => {
  if (!password.value) {
    message.error('请输入密码');
    return;
  }

  fetch('/network/connect', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/x-www-form-urlencoded',
    },
    body: `SSID=${encodeURIComponent(selectedSsid.value)}&Password=${encodeURIComponent(password.value)}`,
  })
    .then(response => response.json())
    .then(data => {
      if (data.Result === "OK") {
        message.success('连接成功');
      } else {
        message.error('连接失败');
      }
      closePasswordModal();
    })
    .catch(error => {
      console.error('Error:', error);
      message.error('连接失败');
      closePasswordModal();
    });
};
</script>

<style scoped>
.ant-list-item {
  border-bottom: 1px solid #f0f0f0;
  padding: 16px 0;
}
.ant-list-item-meta {
  align-items: center;
}
.ant-list-item-actions {
  margin-top: 12px;
}
</style>