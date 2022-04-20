import JQuery from 'jquery'
import Axios from 'axios'
import Vue from 'vue'

import '@popperjs/core'
import 'bootstrap'

import '../scss/index.scss'

// Setup JQuery load globaly
const $         = JQuery
window.jQuery   = $

// Setup axios to match Django XSRF naming
Axios.defaults.xsrfCookieName = 'csrftoken'
Axios.defaults.xsrfHeaderName = "X-CSRFTOKEN"
Axios.defaults.headers = {'X-Requested-With': 'XMLHttpRequest'}

export { Vue, Axios, JQuery, $ }
