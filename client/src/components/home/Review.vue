<template>
    <div class="flex flex-col justify-center text-center p-5 lg:p-8 bg-three rounded-md shadow-md my-5">
        <i class="nf text-5xl fg-one nf-fa-quote_left text-left"></i><br>
        <span class="fg-five font-bold text-xl font-poppins">
            <slot></slot>
        </span><br>
        <i class="nf text-5xl fg-one nf-fa-quote_right text-right"></i><br>
        <span class="fg-five font-bold text-lg font-poppins text-right">- {{ name }}</span>
    </div>
</template>

<script>
    export default {
        props: {
            name: String,
        },
        
        data() {
            return {
                classList: ['nf', 'text-7xl', 'fg-one']
            }
        }
    }
</script>