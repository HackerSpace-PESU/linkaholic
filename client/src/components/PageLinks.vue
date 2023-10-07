<template>
    <div class="space-y-4" v-for="x in content">
        <template v-if="x.type === 'heading'">
            <br>
            <h2 class="text-2xl md:text-3xl lg:text-4xl" :style="styles['head']">{{ x.content }}</h2><br>
        </template>

        <template v-else-if="x.type === 'button'">
            <button class="w-full md:w-3/4 lg:w-1/2 px-10 py-3 text-2xl lg:text-2xl text-center content-center" :style="styles['button']" @click="openLink(x.link)">
                {{ x.content }}
            </button>
            <br><br>
        </template>
    </div>
</template>

<script>
    export default {
        props: {
            styles: Object,
            content: Array
        },
        methods: {
            openLink(link) {
                window.open(link, '_blank');
            }
        }
    }
</script>