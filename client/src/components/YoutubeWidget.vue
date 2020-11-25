<template>
    <div v-draggable class="youtubeWidget">
        <md-list :md-expand-single="expandSingle">
            <md-list-item md-expand :md-expanded.sync="expandNews">
                <md-icon>search</md-icon>
                <span class="md-list-item-text">Search for a video</span>
                    <md-list slot="md-expand">
                        <md-list-item>
                            <md-field>
                              <label>Type here!</label>
                              <md-input v-model="searchQuerry"></md-input>
                            </md-field>
                              <div
                                class="searchButton"
                                @click="searchVideos"
                              >
                                Search
                              </div>
                        </md-list-item>
                        <md-list-item>
                              <div v-dragscroll class="videoPlayerContainer">
                                <youtube v-for="result in searchResult" :key="result" :video-id="result.id" ref="youtube"></youtube>
                                <ul>
                                  <li v-for="result in searchResult" :key="result" >
                                    <youtube
                                      :video-id="result.id"
                                      ref="youtube"
                                      height=15
                                    />
                                  </li>
                                </ul>
                              </div>
                        </md-list-item>
                </md-list>
            </md-list-item>
        </md-list>
    </div>
</template>

<script>
import { Draggable } from 'draggable-vue-directive'
import axios from 'axios'
import { dragscroll } from 'vue-dragscroll'

export default {
  name: 'YouTubeWidget',
  directives: {
    Draggable,
    dragscroll
  },
  data () {
    return {
      searchQuerry: '',
      searchResult: []
    }
  },
  methods: {
    searchVideos () {
      this.searchResult = []
      if (this.searchQuerry === '') {
        return
      }
      axios.get(`http://localhost:5000/youtubeSearch/${this.searchQuerry}`)
        .then(res => {
          this.searchResult = res.data
        })
        .catch(err => { console.error(err) })
    }
  }
}
</script>

<style lang="scss" scoped>
    .searchButton {
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
    .youtubeWidget {
        width: 50;
        background-color: rgba($color: #ff0000, $alpha: 1.0);
        width: 20%;
        height: 50%;
        border-radius: 10px;
        border-width: 1px;
    }
</style>
