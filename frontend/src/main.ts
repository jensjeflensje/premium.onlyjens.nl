import { createApp } from 'vue'
import App from './App.vue'
import PrimeVue from 'primevue/config';
import 'primevue/resources/themes/lara-dark-blue/theme.css'
import 'primeicons/primeicons.css'
import './style.css'

createApp(App)
    .use(PrimeVue)
    .mount('#app')
