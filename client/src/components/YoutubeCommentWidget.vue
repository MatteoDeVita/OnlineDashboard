<template>
    <div v-if="show == true" v-draggable class="youtubeCommentWidget">
        <div
          class="connectButton"
          @click="searchVideos"
          >
            <a
              target="_blank"
              href="http://localhost:5000/test"
            >
              Connect to YouTube
            </a>
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

export default {
  name: 'YouTubeCommentWidget',
  directives: {
    Draggable
  },
  data () {
    return {
      searchResult: undefined,
      show: true
    }
  },
  methods: {
    searchVideos () {
      axios.get('http://localhost:5000/test')
        .then(res => {
          this.searchResult = res.data
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
    .connectButton {
      display: inline-block;
      border-style: solid;
      margin-left: 10px;
      padding: 10px;
      border-radius: 10px;
      background-color: rgba($color: #ff0000, $alpha: 1.0);
      border-width: 2px;
    }
    .connectButton:hover {
      background-color: rgba($color: #b80000, $alpha: 1.0);
    }
    .connectButton:active {
      background-color: rgba($color: #b80000, $alpha: 1.0);
    }
    .youtubeCommentWidget {
        width: 50;
        background-color: rgba($color: #ff0000, $alpha: 1.0);
        width: 20%;
        height: 28%;
        border-radius: 10px;
        border-width: 1px;
        padding: 10px
    }
    .closeButton {
      margin-left: 90%;
    }
</style>
