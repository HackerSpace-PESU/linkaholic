<template>
    <div class="flex flex-col justify-center text-center p-10">
        <i :class="classList"></i><br>
        <span class="fg-two font-bold text-xl font-poppins"><slot></slot></span>
    </div>
</template>

<script>
    export default {
        data() {
            return {
                classList: ['nf', 'text-7xl', 'fg-one']
            }
        },

        props: {
            icon: String
        },

        mounted() {
            this.classList.push(this.icon);
        }
    }
</script>