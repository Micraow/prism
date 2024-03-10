import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
const app = createApp(App)
import { Divider, Layout, Menu, PageHeader,Card,Button } from 'ant-design-vue'

app.use(Divider)
app.use(Layout)
app.use(Menu)
app.use(PageHeader)
app.use(Card)
app.use(Button)
app.config.productionTip = false

app.use(router)

app.mount('#app')
