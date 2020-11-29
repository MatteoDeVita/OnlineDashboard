<template>
    <div v-if="show == true" v-draggable class="youtubeSearchWidget">
          <div class="searchContainer">
            <md-field class="searchField">
              <label>Type here!</label>
              <md-input v-model="searchQuerry"></md-input>
            </md-field>
              <div
                class="searchButton"
                @click="searchVideos"
              >
                Search
              </div>
          </div>
              <div v-if="searchResult != undefined">
                <youtube class="youtubePlayer" :video-id="searchResult.id" ref="youtube"></youtube>
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
  name: 'YouTubeSearchWidget',
  directives: {
    Draggable,
    dragscroll
  },
  data () {
    return {
      searchQuerry: '',
      searchResult: undefined,
      show: true
    }
  },
  methods: {
    searchVideos () {
      if (this.searchQuerry === '') {
        return
      }
      axios.get(`http://localhost:5000/youtubeSearch/${this.searchQuerry}`)
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
      background-color: rgba($color: #ff0000, $alpha: 1.0);
      border-width: 2px;
    }
    .searchButton:hover {
      background-color: rgba($color: #b80000, $alpha: 1.0);
    }
    .searchButton:active {
      background-color: rgba($color: #b80000, $alpha: 1.0);
    }
    .youtubeSearchWidget {
        width: 50;
        background-color: rgba($color: #ff0000, $alpha: 1.0);
        width: 20%;
        height: 32%;
        border-radius: 10px;
        border-width: 1px;
        padding: 10px
    }
    .closeButton {
      margin-left: 90%;
    }
</style>
