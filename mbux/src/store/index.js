import Vue from 'vue'
import Vuex from 'vuex'

// We first import the module
import showcase from './showcase'

Vue.use(Vuex)

/*
 * If not building with SSR mode, you can
 * directly export the Store instantiation;
 *
 * The function below can be async too; either use
 * async/await or return a Promise which resolves
 * with the Store instance.
 */

export default function (/* { ssrContext } */) {
  const Store = new Vuex.Store({
    modules: {
      // example
      showcase
    },

    // enable strict mode (adds overhead!)
    // for dev mode only
    strict: process.env.DEV
  })

  if (process.env.DEV && module.hot) {
    module.hot.accept(['./showcase'], () => {
      const newShowcase = require('./showcase').default
      Store.hotUpdate({ modules: { showcase: newShowcase } })
    })
  }

  return Store
}
