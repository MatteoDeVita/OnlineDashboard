<template>
    <div v-if="show == true" v-draggable class="githubAccountWidget">
          <div class="searchContainer">
            <md-field class="searchField">
              <label>Username</label>
              <md-input v-model="searchedUsername"></md-input>
            </md-field>
              <div
                class="searchButton"
                @click="searchVideos"
              >
                Search
              </div>
          </div>
          <div
            v-if="searchResult != undefined"
            class="displayer"
          >
            <p v-if="searchResult.name != undefined">Nom : {{ searchResult.name }}</p>
            <img v-if="searchResult.icon_url != undefined" class="accountIcon" v-bind:src="searchResult.icon_url"/>
            <p v-if="searchResult.location != undefined">Ville : {{ searchResult.location }}</p>
            <p v-if="searchResult.email != undefined">Mail : {{ searchResult.email }}</p>
            <a v-if="searchResult.url" target="_blank" v-bind:href="searchResult.url">Voir le profil</a>
          </div>
        <div>
            <md-button @click="show = false" class="md-icon-button closeButton">
              <md-icon>close</md-icon>
            </md-button>
        </div>
    </div>
</template>

<script>
import { Draggable } from 'draggable-vue-directive'
import axios from 'axios'
import { dragscroll } from 'vue-dragscroll'

export default {
  name: 'GithubAccountWidget',
  directives: {
    Draggable,
    dragscroll
  },
  data () {
    return {
      searchedUsername: '',
      searchResult: undefined,
      show: true
    }
  },
  methods: {
    searchVideos () {
      if (this.searchedUsername === '') {
        return
      }
      axios.get(`http://localhost:5000/githubAccount/${this.searchedUsername}`)
        .then(res => {
          this.searchResult = res.data
          console.log(this.searchResult)
        })
        .catch(err => {
          console.error(err)
          this.searchResult = undefined
        })
    }
  }
}
</script>

<style lang="scss" scoped>
    .searchContainer {
      background-color: white;
      border-style: solid;
      border-radius: 20px;
      border-width: 0;
      margin-top: 10px;
      margin-left: 5px;
      margin-right: 5px;
      margin-bottom: 10px;
    }
    .searchField {
      display: inline-block;
      width: 70%;
      margin-left: 5px;
      margin-right: 5px;
    }
    .searchButton {
      display: inline-block;
      border-style: solid;
      margin-left: 10px;
      padding: 10px;
      border-radius: 10px;
      background-color: rgba($color: #ffffff, $alpha: 1.0);
      border-width: 2px;
    }
    .searchButton:hover {
      background-color: rgba($color: #a1a0a0, $alpha: 1.0);
    }
    .searchButton:active {
      background-color: rgba($color: #a1a0a0, $alpha: 1.0);
    }
    .githubAccountWidget {
        width: 50;
        background-color: rgba($color: #ffffff, $alpha: 1.0);
        width: 20%;
        height: 62%;
        border-radius: 10px;
        border-width: 1px;
        padding: 10px
    }
    .counts {
        margin-left: 20px;
        display: inline-block;
        vertical-align: top;
    }
    .accountIcon {
        padding-top: 10px;
        vertical-align: top;
        display: inline-block;
    }
    .closeButton {
      margin-left: 90%;
    }
</style>
