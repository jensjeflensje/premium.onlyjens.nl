import {createRouter, createWebHistory} from 'vue-router'

import HomeView from '@/views/HomeView.vue'
import AppLayout from '@/layouts/AppLayout.vue';
import EmptyLayout from '@/layouts/EmptyLayout.vue';
import BrowserSourceView from '@/views/BrowserSourceView.vue';

const routes = [
  {
    path: '/',
    component: AppLayout,
    children: [
      {
        path: '',
        name: 'home',
        component: HomeView,
      },
    ],
  },
  {
    path: '/browser-source',
    component: EmptyLayout,
    children: [
      {
        path: '',
        name: 'browser-source',
        component: BrowserSourceView,
      },
    ],
  },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router;