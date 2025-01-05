<template>
  <main>
    <a-page-header
      style="border: 1px solid rgb(235, 237, 240)"
      title="历史记录"
      sub-title="已保存的错题"
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
              :description="`图片路径: ${item.path}`"
            >
              <template #title>
                <a>错题 ID: {{ item.id }}</a>
              </template>
            </a-list-item-meta>
            <template #actions>
              <span @click="viewImage(item.path)">
                <a-icon type="eye" /> 查看图片
              </span>
            </template>
          </a-list-item>
        </template>
      </a-list>
    </a-card>

    <!-- 图片预览模态框 -->
    <a-modal
      v-model:visible="imageModalVisible"
      title="图片预览"
      :footer="null"
      @cancel="closeImageModal"
    >
      <img :src="currentImagePath" alt="错题图片" style="width: 100%;" />
    </a-modal>
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

const imageModalVisible = ref(false);
const currentImagePath = ref('');

const fetchHistory = () => {
  fetch('/history/cuo_ti')
    .then(response => response.json())
    .then(data => {
      history.value = data;
    })
    .catch(error => {
      console.error('Error:', error);
      message.error('获取错题记录失败');
    });
};

const viewImage = (path) => {
  currentImagePath.value = path;
  imageModalVisible.value = true;
};

const closeImageModal = () => {
  imageModalVisible.value = false;
  currentImagePath.value = '';
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