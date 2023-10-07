<template>
    <div class="px-8 lg:px-16 flex flex-col justify-center mt-[10rem] lg:mt-[15rem]">
        <div class="flex flex-col justify-center text-center w-full">
            <div class="text-3xl lg:text-6xl text-center font-bold font-robotoSlab fg-four">
                Your very own fully customizable links site is just a few clicks away!
            </div>
            <br>
            <div class="text-lg lg:text-2xl text-center font-robotoSlab fg-three lg:px-32">
                Get started now, absolutely for free, and explore the endless possibilities, where creativity is your only limit.
            </div>
            <br>
            <router-link to="/signup" class="text-xl md:text-xl lg:text-xl text-white px-4 md:px-8 lg:px-8 py-2 rounded-md text-center font-poppins bg-zero w-[15rem] lg:w-1/5 mx-auto font-semibold">
                Get Started
            </router-link>
        </div>
        <br><br>
        <div class="mt-20">
            <h1 class="text-4xl lg:text-6xl text-center font-bold font-robotoSlab fg-zero">Features</h1>
            <br>
            <div class="flex flex-col lg:grid grid-cols-3">
                <feature icon="nf-md-file_code">Free and open source for anyone to contribute</feature>
                <feature icon="nf-md-link">One link to access all your social links</feature>
                <feature icon="nf-seti-css">Control over page and element styles</feature>
            </div>
        </div>
        <br><br>
        <div class="mt-20">
            <h1 class="text-4xl lg:text-6xl text-center font-bold font-robotoSlab fg-zero">Reviews</h1>
            <br>
            <div class="flex flex-col lg:grid grid-cols-3 space-x-3">
                <review name="Foo">Nothing much to say</review>
                <review name="Bar">Dem. Just dem.</review>
                <review name="Baz">Cool theme!!</review>
            </div>
        </div>
        <br><br>
    </div>
</template>

<script>
    import Feature from '../components/home/Feature.vue';
    import Review from '../components/home/Review.vue';

    export default {
        components: {
            Feature,
            Review
        }
    }
</script>