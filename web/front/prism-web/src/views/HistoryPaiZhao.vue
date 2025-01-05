<template>
  <main>
    <a-page-header
      style="border: 1px solid rgb(235, 237, 240)"
      title="拍照翻译历史"
      sub-title="查看历史记录"
    />
    <a-card>
      <a-list
        :data-source="history"
        :pagination="pagination"
        item-layout="vertical"
      >
        <template #renderItem="{ item }">
          <a-list-item>
            <a-list-item-meta
              :description="`翻译结果: ${item.translation}`"
            >
              <template #title>
                <a>{{ item.original_text }}</a>
              </template>
            </a-list-item-meta>
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
const pagination = ref({
  pageSize: 5, // 每页显示5条记录
  showSizeChanger: true,
  pageSizeOptions: ['5', '10', '20'],
  showTotal: (total) => `共 ${total} 条记录`,
});

const fetchHistory = () => {
  fetch('/history/pai_zhao')
    .then(response => response.json())
    .then(data => {
      history.value = data;
    })
    .catch(error => {
      console.error('Error:', error);
      message.error('获取历史记录失败');
    });
};

onMounted(() => {
  fetchHistory();
});
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