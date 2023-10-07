<template>
    <div class="flex flex-col justify-center text-center p-10">
        <page-title 
            :data="meta?.['page-title']?.data || []">
        </page-title>
        <br />
        <page-content 
            :styles="meta?.['page-content']?.styles || {}">
            {{ meta?.['page-content']?.value || '' }}
        </page-content>
        <br />
        <page-links 
            :styles="meta?.['links']?.styles || []" 
            :content="meta?.['links']?.content || []">
        </page-links>
    </div>
</template>
  
  


<script>
import axios from 'axios';

// themes
// import hackerspace from './themes/hackerspace.json'
// import pinky from './themes/pinky.json'

// components
import PageTitle from './PageTitle.vue';
import PageContent from './PageContent.vue';
import PageLinks from './PageLinks.vue';

export default {
    components: {
        PageTitle,
        PageContent,
        PageLinks
    },

    data() {
        return {
            // themes: {
            //     'hackerspace': hackerspace,
            //     'pinky': pinky
            // },

            meta: ''
        }
    },

    created() {
        const dynamicRoute = this.$route.params.dynamicRoute;
        axios.get(`http://localhost:5000/${dynamicRoute}`)
            .then(response => {
                this.meta = response.data;
                document.title = `Linkhub - ${this.meta?.['name']}` || "Default lmao";
                document.body.style.backgroundColor = this.meta['body-styles']?.['background'] || 'white';
            })
            .catch(error => {
                console.error('Oops, something went wrong!', error);
            });
    },

    mounted() {
        this.importFonts();
        // console.log(this.meta);
    },

    methods: {
        importFonts() {
            const style = document.createElement('style');
            style.textContent = this.meta?.['body-styles']?.['font-imports'];
            document.head.appendChild(style);
        }
    }
}
</script>



<style scoped></style>
