<template>
    <span class="text-8xl mt-10">
        <span v-for="d in data" :style="d.styles">{{ d.text }}</span>
    </span>
    <!-- <h1 class="text-8xl mt-10" :style="{ color: textColor, fontFamily: font }"><slot></slot></h1> -->
</template>

<script>
    export default {
        props: {
            data: Array
        }
    }
</script>