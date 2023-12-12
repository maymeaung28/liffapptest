import { createApp } from 'vue';
import App from './App.vue';
import router from './router/';
// import { BootstrapVue, BootstrapVueIcons } from 'bootstrap-vue'

//----------------------------------------------------
//import Bootstrap styles
//----------------------------------------------------
//Font Awesome
import '../node_modules/bootstrap/dist/css/bootstrap.css'
// import '../node_modules/bootstrap/dist/css/bootstrap-grid.css'
// import '../node_modules/bootstrap/dist/css/bootstrap-utilities.css'
// import '../node_modules/bootstrap/dist/css/bootstrap.rtl.css'
import '../node_modules/bootstrap-vue/dist/bootstrap-vue.css'

//----------------------------------------------------
//import booststrap scripts
//----------------------------------------------------
//jQuery
// import "../node_modules/admin-lte/plugins/jquery/jquery.min.js"
import '../node_modules/bootstrap/dist/js/bootstrap.bundle.js'
import '../node_modules/jquery/dist/jquery.min.js'

const app = createApp(App)
app.use(router)
app.mount('#app')
