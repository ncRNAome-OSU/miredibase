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
      { path: 'contactus', component: () => import('pages/ContactUs.vue') },
      {
        path: 'variant/:vartype/:genpos/:chrom/:strand/:organism',
        component: () => import('pages/Variant.vue'),
        props: castRouteParams
      }
    ]
  },

  // Always leave this as last one,
  // but you can also remove it
  {
    path: '*',
    component: () => import('pages/Error404.vue')
  }
]

function castRouteParams (route) {
  return {
    vartype: route.params.vartype.replace(/[^A-Za-z0-9]/g, ''),
    genpos: Number(route.params.genpos),
    chrom: route.params.chrom.replace(/[^A-Za-z0-9]/g, '').toUpperCase(),
    strand: route.params.strand.replace(/[^\-+]/g, ''),
    organism: route.params.organism.replace(/[^A-Za-z]/g, '').toLowerCase()
  }
}

export default routes
