import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
const app = createApp(App)
import {
  Divider,
  Flex,
  Layout,
  Menu,
  PageHeader,
  Card,
  Button,
  List,
  Collapse,
  Space,
  Avatar
} from 'ant-design-vue'

app.use(Divider)
app.use(Flex)
app.use(Layout)
app.use(Menu)
app.use(PageHeader)
app.use(Card)
app.use(Button)
app.use(List)
app.use(Collapse)
app.use(Space)
app.use(Avatar)
app.config.productionTip = false

app.use(router)

app.mount('#app')
