export const ColorPlugin = {
    install(Vue) {
        Vue.prototype.$colors = {
            one: '#6499E9',
            two: '#9EDDFF',
            three: '#A6F6FF',
            four: '#BEFFF7',
            five: '#E8FFFC',
            // six: '#',
        };
    },
};