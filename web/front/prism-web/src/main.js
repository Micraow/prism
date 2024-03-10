import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
const app = createApp(App)
import { Divider, Layout, Menu, PageHeader } from 'ant-design-vue'
app.use(Divider)
app.use(Layout)
app.use(Menu)
app.use(PageHeader)
app.config.productionTip = false

app.use(router)

app.mount('#app')
