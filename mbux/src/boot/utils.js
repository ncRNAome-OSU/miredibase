import Vue from 'vue'
import loadApiData from 'src/utils/LoadApiData.js'
import exportDataTableAsCSV from 'src/utils/ExportTable.js'
import utils from 'src/utils/DataFormatter.js'

Vue.prototype.$loadApiData = loadApiData
Vue.prototype.$exportDataTableAsCSV = exportDataTableAsCSV
Vue.prototype.$utils = utils
