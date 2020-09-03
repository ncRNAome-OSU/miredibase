import Vue from 'vue'
import axios from 'axios'

axios.defaults.baseURL = 'http://localhost:9001'

Vue.prototype.$axios = axios
