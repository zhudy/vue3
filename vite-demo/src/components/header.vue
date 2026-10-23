<template>
    <h3>header {{ props.propsName}} {{props.propsUrl }}</h3>
</template>

<script setup>
  const props = defineProps(["propsName", "propsUrl"])
  console.log(props.prposName, props.propsUrlrl)
</script>

<style lang="scss" scoped>

</style>