<script setup>
import { ref, onMounted, onBeforeUnmount } from 'vue'
import WelcomePage from '../components/WelcomePage.vue';
/**
 * 显示实时时间
 */

const nowTime = ref('')
/**
 * 将小于10的数字前面补0
 * @function
 * @param {number} value
 * @returns {string} 返回补0后的字符串
 */
const complement = (value) => {
    return value < 10 ? `0${value}` : value.toString()
}
/**
 * 格式化时间为XXXX年XX月XX日XX时XX分XX秒
 * @function
 * @returns {string} 返回格式化后的时间
 */
const formateDate = () => {
    const time = new Date()
    const year = time.getFullYear()
    const month = complement(time.getMonth() + 1)
    const day = complement(time.getDate())
    const hour = complement(time.getHours())
    const minute = complement(time.getMinutes())
    const second = complement(time.getSeconds())
    const week = '星期' + '日一二三四五六'.charAt(time.getDay());
    return `${year}年${month}月${day}日 ${hour}:${minute}:${second} ${week}`
}
let timer = 0
/**
 * 设置定时器
 */
onMounted(() => {
    timer = setInterval(() => {
        nowTime.value = formateDate()
    }, 1000)
})
/**
 * 取消定时器
 */
onBeforeUnmount(() => {
    clearInterval(timer) //清除定时器,防止切换到其他页面时继续计时
    timer = 0
})

</script>

<template>
  <main>
    <a-page-header
    style="border: 1px solid rgb(235, 237, 240)"
    title="主页"
    sub-title="很高兴见到你"
  />
    <WelcomePage />
    <p id="clock">{{ nowTime }}</p>
  </main>
</template>

<style>
#clock{
    font-weight: bolder;
    font-family: Verdana, Geneva, Tahoma, sans-serif;
    text-align: center;
    font-size: 3em;
    color: crimson;
    justify-content: center;
    align-items: center;
}</style>
