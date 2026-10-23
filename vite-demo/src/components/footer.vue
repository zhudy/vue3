<template>
    <h3>footer</h3>
    {{ props.user}}
    {{ props.url }}
</template>

<script setup>
    const props = defineProps({
        user: Number,
        url: String
    })
    console.log(props)
</script>

<style lang="scss" scoped>

</style>