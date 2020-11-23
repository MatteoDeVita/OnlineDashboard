<template>
    <div class="login">
        <div class="login-fields">
        <md-field class="md-field">
            <label>Login</label>
            <md-input v-model="type"></md-input>
        </md-field>
        <md-field class="md-field">
            <label>Password</label>
            <md-input v-model="password" type="password"></md-input>
        </md-field>
        </div>
    </div>
</template>

<script>
export default {
  name: 'Login',
  data () {
    return {
      login: '',
      password: ''
    }
  },
  created () {

  }
}
</script>

<style lang="scss" scoped>
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
    .login-fields {
        color: white;
        margin-top: 5%;
        margin-left: 2%;
        border-style: solid;
        border-radius: 40px;
        width: 25%;
        padding: 10px;
    }
</style>
