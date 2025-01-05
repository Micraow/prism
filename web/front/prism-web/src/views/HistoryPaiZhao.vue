<template>
  <main>
    <a-page-header
      style="border: 1px solid rgb(235, 237, 240); margin-bottom: 24px;"
      title="拍照翻译历史"
      sub-title="查看历史记录"
    />
    <a-card
      :bordered="false"
      :style="{ boxShadow: '0 2px 8px rgba(0, 0, 0, 0.15)', borderRadius: '8px' }"
    >
      <a-list
        :data-source="history"
        :pagination="pagination"
        item-layout="vertical"
        :loading="loading"
      >
        <template #renderItem="{ item }">
          <a-list-item
            :style="{ padding: '16px 24px', borderBottom: '1px solid #f0f0f0', transition: 'all 0.3s' }"
            class="history-item"
          >
            <a-list-item-meta
              :description="`原文: ${item.original_text}`"
            >
              <template #title>
                <a :style="{ fontSize: '16px', fontWeight: '500' }">翻译结果</a>
              </template>
            </a-list-item-meta>

            <!-- 翻译结果卡片 -->
            <a-row :gutter="16" style="margin-top: 16px;">
              <a-col :span="6" v-for="(translation, key) in item.translation" :key="key">
                <a-card
                  :title="key"
                  :style="{ borderRadius: '8px', boxShadow: '0 2px 8px rgba(0, 0, 0, 0.1)' }"
                >
                  <p>{{ translation }}</p>
                </a-card>
              </a-col>
            </a-row>
          </a-list-item>
        </template>
      </a-list>
    </a-card>
  </main>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { message } from 'ant-design-vue';

const history = ref([]);
const loading = ref(false);
const pagination = ref({
  pageSize: 5, // 每页显示5条记录
  showSizeChanger: true,
  pageSizeOptions: ['5', '10', '20'],
  showTotal: (total) => `共 ${total} 条记录`,
  style: { marginTop: '24px', textAlign: 'right' }
});

const fetchHistory = () => {
  loading.value = true;
  fetch('/history/pai_zhao')
    .then(response => response.json())
    .then(data => {
      // 解析翻译结果
      history.value = data.map(item => ({
        ...item,
        translation: JSON.parse(item.translation.replace(/'/g, '"')) // 将单引号替换为双引号以正确解析 JSON
      }));
      loading.value = false;
    })
    .catch(error => {
      console.error('Error:', error);
      message.error('获取历史记录失败');
      loading.value = false;
    });
};

onMounted(() => {
  fetchHistory();
});
</script>

<style scoped>
.history-item:hover {
  background-color: #fafafa;
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
}

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

.ant-card {
  border-radius: 8px;
}

.ant-card-body {
  padding: 24px;
}

.ant-card-head-title {
  font-size: 14px;
  font-weight: 500;
}

.ant-card p {
  margin: 0;
  font-size: 14px;
  color: rgba(0, 0, 0, 0.85);
}
</style>