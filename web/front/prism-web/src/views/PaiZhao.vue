<template>
  <main>
    <a-page-header
      style="border: 1px solid rgb(235, 237, 240)"
      title="拍照翻译"
      sub-title="让我做你的眼睛"
    />
    <a-card>
      <p style="text-align: center;font-size: large;font-weight: bold;">点击下方按钮即可拍照翻译</p>
      <p style="text-align: center;">
      <a-button type="primary" shape="circle" size="large" style="height: 120px;width: 120px;">
        <template #icon>
          <PlayCircleOutlined />
        </template>
      </a-button>
    </p>
    </a-card>
  </main>
</template>
