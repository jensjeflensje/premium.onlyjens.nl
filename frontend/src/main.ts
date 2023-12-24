import { createApp } from 'vue'
import App from './App.vue'
import PrimeVue from 'primevue/config';
import 'primevue/resources/themes/lara-dark-blue/theme.css'
import 'primeicons/primeicons.css'
import './style.css'

import { library } from '@fortawesome/fontawesome-svg-core'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import { faGithub, faYoutube, faDiscord, faLinkedin } from '@fortawesome/free-brands-svg-icons'

library.add(faGithub, faYoutube, faDiscord, faLinkedin)

createApp(App)
    .use(PrimeVue)
    .component('font-awesome-icon', FontAwesomeIcon)
    .mount('#app')
