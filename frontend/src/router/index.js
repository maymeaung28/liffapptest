//import packages
import * as vueRouter from "vue-router";

//import views
import GetToken from "../views/GetToken.vue";
import Welcome from "../views/Welcome.vue";
import Wel from '/src/components/Wel.vue';

//route setting
const routes = [
    {
    path: "/getToken",
    name: "GetToken",
    component: () => GetToken,
    meta: { requiresAuth: false }
    },
    {
    path: "/",
    name: "Welcome",
    component: () => Wel,
    meta: { requiresAuth: false }
    },
];

//create router
const router = vueRouter.createRouter({
    history: vueRouter.createWebHistory(),
    routes,
});

export default router;
