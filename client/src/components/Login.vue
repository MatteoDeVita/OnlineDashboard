<template>
    <div class="login">
        <TopBar></TopBar>
        <div class="login-fields">
        <md-field
            class="md-field"
        >
            <label>Login</label>
            <md-input
                v-model="login"
                required=true
                placeholder=""
            ></md-input>
        </md-field>
        <md-field class="md-field">
            <label>Password</label>
            <md-input
                v-model="password"
                type="password"
                required=true
                placeholder=""
            >
            </md-input>
        </md-field>
        </div>
        <div
            class="button"
            @click="handleConnexionClick"
        >
            <p>{{ connexionButtonText }}</p>
        </div>
    </div>
</template>

<script>
import TopBar from './TopBar.vue'
import axios from 'axios'

export default {
  name: 'Login',
  components: {
    TopBar
  },
  data () {
    return {
      connexionButtonText: 'Connexion !',
      login: '',
      password: ''
    }
  },
  created () {

  },
  methods: {
    async handleConnexionClick () {
      const res = await axios.get(`http://localhost:5000/login/${this.login}/${this.password}`)
      if (res.data !== 'FAILURE') {
        this.$router.push('/dashboard')
      }
    }
  }
}
</script>

<style lang="scss" scoped>
    .button:hover {
        background-color: rgba($color: #5b8005, $alpha: 1.0);
        border-style: solid;
        color: rgb(218, 216, 216);
        border-width: 5px;
        border-radius: 15px;
        width: 12.5%;
        margin-left: 8%;
        margin-top: 3%;
        text-align: center;
        font-size: 1.5em;

    }
    .button:active {
        background-color: rgba($color: #5b8005, $alpha: 1.0);
        border-style: solid;
        color: rgb(218, 216, 216);
        border-width: 5px;
        border-radius: 15px;
        width: 12.5%;
        margin-left: 8%;
        margin-top: 3%;
        text-align: center;
        font-size: 1.5em;
    }
    .button {
        background-color: rgba($color: #84bd00, $alpha: 1.0);
        border-style: solid;
        color: white;
        // border-width: 1px;
        border-radius: 15px;
        width: 12.5%;
        margin-left: 8%;
        margin-top: 3%;
        text-align: center;
        font-size: 1.5em;

    }
    .login {
        position:fixed;
        padding:0;
        margin:0;
        top:0;
        left:0;
        width: 100%;
        height: 100%;
        background-color: rgba($color: #333131, $alpha: 1.0);
    }
    .topbar {
        top:0;
        left:0;
        z-index: 100;
        padding:0;
        margin:0;
        background-color: rgba($color: #84bd00, $alpha: 1.0);
        color: white;
        border-style: solid;
        border-width: 2px;
        border-bottom-left-radius: 15px;
        border-bottom-right-radius: 15px;
        font-size: 1.5em;
        text-align: center;

    }
    .login-fields {
        background-color: rgba($color: #84bd00, $alpha: 1.0);
        color: white;
        margin-top: 3.5%;
        margin-left: 2%;
        border-style: solid;
        border-radius: 40px;
        width: 25%;
        padding: 10px;
    }
</style>
