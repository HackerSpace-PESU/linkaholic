<template>
    <span class="text-xl md:text-2xl lg:text-3xl" :style="styles"><slot></slot></span>
</template>

<script>
    export default {
        props: {
            styles: Object
        }
    }
</script>