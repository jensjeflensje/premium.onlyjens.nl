import { createApp } from 'vue'
import App from './App.vue'
import PrimeVue from 'primevue/config';
import 'primevue/resources/themes/lara-dark-blue/theme.css'
import 'primeicons/primeicons.css'
import './style.css'

import router from '@/router'

import { library } from '@fortawesome/fontawesome-svg-core'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import { faGithub, faYoutube, faDiscord, faLinkedin, faTiktok } from '@fortawesome/free-brands-svg-icons'

library.add(faGithub, faYoutube, faDiscord, faLinkedin, faTiktok)

createApp(App)
    .use(router)
    .use(PrimeVue)
    .component('font-awesome-icon', FontAwesomeIcon)
    .mount('#app')
