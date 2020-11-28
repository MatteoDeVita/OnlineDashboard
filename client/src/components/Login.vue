<template>
    <div class="login">
    <TopBar></TopBar>
     <md-dialog :md-active.sync="error" class="dialog">
      <md-dialog-title>Erreur</md-dialog-title>
          <p id="dialogText">Une erreur a eu lieu lors de la connexion</p>
          <p id="dialogText">Le nom d'utilisateur ou le mot de passe est incorrect</p>
          <p id="dialogText">Veuillez réessayer</p>
      <md-dialog-actions>
        <md-button class="md-primary" @click="error = false">OK</md-button>
      </md-dialog-actions>
    </md-dialog>
        <div class="loginElements">
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
            <div>
        </div>
        </div>
        <div>
            <img
                class="img"
                src="../assets/mainScreenImage.png"
            >
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
      password: '',
      error: false
    }
  },
  created () {

  },
  methods: {
    async handleConnexionClick () {
      const res = await axios.get(`http://localhost:5000/login/${this.login}/${this.password}`)
      if (res.data !== 'FAILURE') {
        this.error = false
        this.$router.push('/dashboard')
      } else {
        this.error = true
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
        max-width: 12.5%;
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
        display: inline-block;
    }
    .loginElements {
        width: 100%;
        height: 100%;
        position: absolute;
    }
    .img {
        width: 70%;
        // height: 80%;
        position: absolute;
        top: 20%;
        left: 28%;
        border-radius: 10px;
        border-style: solid;
        border-color: white;
        border-width: 5px;
        z-index: 10;
    }
    .dialog {
        width: 75%;
        max-width: 1500px;
    }
    #dialogText {
        margin-left: 50px;
        margin-right: 50px;
    }
</style>
