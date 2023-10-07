import { createRouter, createWebHistory } from 'vue-router'
import LinkGen from '../components/LinkGen.vue'
import HomeView from '../views/HomeView.vue'

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes: [
        {
            path: '/',
            component: HomeView,
        },
        {
            path: '/signup',
            component: null
        },

        {
            path: '/:dynamicRoute',
            component: LinkGen,
        }
    ]
})

export default router
