<script>
//------------------------------------------------
// Import Section
//------------------------------------------------
import { defineComponent } from "vue";

//------------------------------------------------
// 遷移前処理
//------------------------------------------------
export default defineComponent({
    async beforeRouteEnter(to, from, next) {
        console.log(from, to)
        next();
    },
});
</script>

<script setup>
//import packages
import { ref, onMounted } from "vue";
import liff from "@line/liff";
import NavBar from '/src/components/NavBar.vue';

const message  = ref();
const error  = ref();
const accessToken  = ref();
const iDToken  = ref();
const isLoggedIn  = ref();
const userId  = ref();
// const displayName  = ref();

const show_data    = ref(false);

const getLineData = () => {
    console.log("this is getLineData function");
    liff
        .init({
            liffId: import.meta.env.VITE_LIFF_ID
        })
        .then(() => {
            show_data.value = true;
            message.value = "LIFF init succeeded.";
            accessToken.value = liff.getAccessToken();
            iDToken.value = liff.getIDToken();
            isLoggedIn.value = liff.isLoggedIn();

            if (liff.isLoggedIn()) { //チェックしないと、getProfileメソッドが上手く処理しない
            liff
                .getProfile()
                .then((profile) => {
                    userId.value = profile.userId;
                    // displayName.value = profile.displayName;
                })
                .catch((err) => {
                    error.value = err;
                });
            }

        })
        .catch((e) => {
            message.value = "LIFF init failed.";
            error.value = `${e}`;
        });
    }

</script>

<template>
    <NavBar />
    <div class="d-flex justify-content-center mt-2">
        <button type="button" class="btn btn-primary pl-3 pr-3" @click="getLineData()">データ取得</button>
    </div>
    <div v-if="show_data">
        <h1>create-liff-app</h1>
        <p v-if="message">{{ message }}</p>
        <p v-if="error">
            <code>{{ error }}</code>
        </p>
        <p>
            ユーザID ::{{userId}} <br><br>
            <!-- ユーザ名 ::{{displayName}} <br><br> -->
            アクセストークン::{{accessToken}} <br><br>
            IDトークン::{{iDToken}} <br><br>
            ログイン済みか::{{isLoggedIn}} <br><br>
        </p>
    </div>
</template>

<style>
/* */
</style>
