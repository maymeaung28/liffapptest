

<script setup>
import NavBar from '/src/components/NavBar.vue';
import axios from "axios";
import { ref } from "vue";
import liff from "@line/liff";


const message  = ref();
const error  = ref();
const accessToken  = ref();
const iDToken  = ref();
const isLoggedIn  = ref();
const userId  = ref();
const displayName  = ref();


const getLineData = () => {
    console.log("this is getLineData function");
    liff
        .init({
            liffId: import.meta.env.VITE_LIFF_ID,
            withLoginOnExternalBrowser: true,
        })
        .then(() => {
            message.value = "LIFF init succeeded.";

            accessToken.value = liff.getAccessToken();
            iDToken.value = liff.getIDToken();
            isLoggedIn.value = liff.isLoggedIn();

            if (liff.isLoggedIn()) { //チェックしないと、getProfileメソッドが上手く処理しない
            liff
                .getProfile()
                .then((profile) => {
                    userId.value = profile.userId;
                    displayName.value = profile.displayName;
                })
                .catch((err) => {
                    error.value = err;
                });
            }

        })
        .catch((e) => {
            message.value = "LIFF init failed（涙）";
            error.value = `${e}`;
        });
    }

const sendToServer = async () => {
    var config = {
        method: 'get',
        url: 'http://127.0.1.1:8000/token',
        // headers: {'Content-Type': 'multipart/form-data'},
        params: {access_token_data: accessToken.value}
    };
    await axios(config)
        .then((response) => {
        console.log("this is response", response)
        })
        .catch((error) => {
        console.log("this is error", error)
    });
}

</script>

<template>
    <div>
        <h1>create-liff-app</h1>
        <p v-if="message">{{ message }}</p>
        <p v-if="error">
        <code>{{ error }}</code>
        </p>
        <p>
        ユーザID ::{{userId}} <br><br>
        ユーザ名 ::{{displayName}} <br><br>
        アクセストークン::{{accessToken}} <br><br>
        IDトークン::{{iDToken}} <br><br>
        ログイン済みか::{{isLoggedIn}} <br><br>
        </p>
        <div class="d-flex justify-content-center mt-2">
            <button type="button" class="btn btn-primary pl-3 pr-3 my-3" @click="getLineData()">データ取得</button>
            <button type="button" class="btn btn-primary pl-3 pr-3 m-3" @click="sendToServer()">データ送信</button>
        </div>
    </div>
</template>

<script>
// import liff from "@line/liff";

// export default {
//   data() {
//     return {
//       message: "",
//       error: "",
//       accessToken: "",
//       iDToken: "",
//       isLoggedIn: "",
//       userId: "",
//       displayName: "",
//     };
//   },
//   mounted() {
    // liff
    //   .init({
    //     liffId: import.meta.env.VITE_LIFF_ID
    //   })
    //   .then(() => {
    //     this.message = "LIFF init succeeded.";
    //     this.accessToken = liff.getAccessToken();
    //     this.iDToken = liff.getIDToken();
    //     this.isLoggedIn = liff.isLoggedIn();

    //     if (liff.isLoggedIn()) { //チェックしないと、getProfileメソッドが上手く処理しない
    //       liff
    //         .getProfile()
    //         .then((profile) => {
    //           this.userId = profile.userId;
    //           this.displayName = profile.displayName;
    //         })
    //         .catch((err) => {
    //           this.error = err;
    //         });
    //     }

    //   })
    //   .catch((e) => {
    //     this.message = "LIFF init failed.";
    //     this.error = `${e}`;
    //   });
//       console.log("this is onmounted");
//     }
// };
</script>

<style>
#app {
    font-family: Avenir, Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
    margin-top: 60px;
}
</style>
