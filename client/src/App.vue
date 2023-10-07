<template>
    <div class="flex flex-row justify-center text-center">
        <nav class="flex flex-row justify-between align-middle w-4/5 rounded-md shadow-lg p-5 fixed top-0 m-10 bg-one border-2 border-[var(--one)]">
            <span class="text-lg md:text-2xl lg:text-2xl font-bold poppins text-white">Linkaholic</span>

            <div class="space-x-4">
                <router-link to="/login" class="text-xl w-30 px-10 hidden md:inline-block lg:inline-block text-white">Log In</router-link>
                <router-link to="/signup"
                    class="text-md md:text-xl lg:text-xl bg-zero text-white w-30 px-4 md:px-8 lg:px-8 py-2 rounded-md">Sign Up</router-link>
            </div>
        </nav>
        <router-view></router-view>
    </div>
    <div class="flex flex-row justify-center text-center w-full p-2 bg-white text-md text-gray-400">
        <span class="font-montserrat uppercase">
            Made with love by 
        </span>&nbsp;
        <span class="font-jetbrains">
            &lt;/hackerspace&gt;
        </span>
    </div>
</template>


<script>
import { RouterLink, RouterView } from 'vue-router';
</script>