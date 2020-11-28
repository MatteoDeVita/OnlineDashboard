<template>
    <div v-if="show == true" v-draggable class="githubRepos">
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
            <ul>
                <li
                    v-for="item in searchResult" :key="item.name"
                >
                    <a target="_blank" v-bind:href="item.url">{{ item.name }}</a>
                    <p v-if="item.description != undefined">Description : {{ item.description }}</p>
                </li>
            </ul>
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
      axios.get(`http://localhost:5000/githubRepos/${this.searchedUsername}`)
        .then(res => {
          this.searchResult = res.data
          if (this.searchResult !== undefined) {
            this.searchResult = this.searchResult.slice(0, 5)
          }
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
    .githubRepos {
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
