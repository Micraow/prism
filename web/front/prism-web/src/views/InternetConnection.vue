<template>
  <main>
    <a-space direction="vertical" style="width: 100%;">
      <a-page-header style="border: 1px solid rgb(235, 237, 240)" title="网络连接" sub-title="请连接至局域网" />
      <a-card>
        <a-button type="primary" @click="scanWifi">Scan Wi-Fi</a-button>
        <a-list :data-source="wifiList">
          <template #renderItem="{ item }">
            <a-list-item>
              <a-list-item-meta :description="item">
                <template #title>
                  <a @click="connectWifi(item)">{{ item }}</a>
                </template>
              </a-list-item-meta>
            </a-list-item>
          </template>
        </a-list>
      </a-card>
    </a-space>
  </main>
</template>

<script setup>
import { ref } from 'vue';

const wifiList = ref([]);

const scanWifi = () => {
  fetch('/network/scan')
    .then(response => response.json())
    .then(data => {
      wifiList.value = data;
    })
    .catch(error => console.error('Error:', error));
};

const connectWifi = (ssid) => {
  const password = prompt('请输入密码:');
  if (password) {
    fetch('/network/connect', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/x-www-form-urlencoded',
      },
      body: `SSID=${encodeURIComponent(ssid)}&Password=${encodeURIComponent(password)}`,
    })
    .then(response => response.json())
    .then(data => {
      if (data.Result === "OK") {
        alert('Connected successfully');
      } else {
        alert('Connection failed');
      }
    })
    .catch(error => console.error('Error:', error));
  }
};
</script>