
const routes = [
  {
    path: '/',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '', component: () => import('pages/Index.vue') },
      { path: 'search', component: () => import('pages/Search.vue') },
      { path: 'compare', component: () => import('pages/Compare.vue') },
      { path: 'stats', component: () => import('pages/Statistics.vue') },
      { path: 'download', component: () => import('pages/Download.vue') },
      { path: 'help', component: () => import('pages/Help.vue') },
      { path: 'changelog', component: () => import('pages/ChangeLog.vue') },
      { path: 'contactus', component: () => import('pages/ContactUs.vue') }
    ]
  },

  // Always leave this as last one,
  // but you can also remove it
  {
    path: '*',
    component: () => import('pages/Error404.vue')
  }
]

export default routes
