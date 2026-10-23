<template>
  <Header propsName="头" propsUrl="https://baidu.com"/>
  <Footer v-bind="propsWeb"/> 
  {{ propsWeb.user }}
  <button @click="addUser">增加用户</button>
</template>

<script setup>
  import Header from './components/header.vue';
  import Footer from './components/footer.vue';
  import { reactive } from 'vue';
  
  // const propsWeb = {
  //   user: 10,
  //   url: "m.baidu.com"
  // }
  const propsWeb = reactive({
    user: 10,
    url: "m.baidu.com"
  })

  const addUser = () => {
    propsWeb.user++
    console.log(propsWeb.user)
  }
</script>

<style lang="scss" scoped>

</style>