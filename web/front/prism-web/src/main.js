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
  Avatar,
  Modal,
  Input,
  message
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
app.use(Modal);
app.use(Input);
app.config.productionTip = false

app.config.globalProperties.$message = message

app.use(router)

app.mount('#app')
