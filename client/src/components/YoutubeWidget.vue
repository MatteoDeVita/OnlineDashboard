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
                    </md-list-item>
                    <md-list-item>
                            <md-field>
                              <p>salut</p>
                            </md-field>
                    </md-list-item>
                </md-list>
            </md-list-item>
        </md-list>
    </div>
</template>

<script>
import { Draggable } from 'draggable-vue-directive'
import axios from 'axios'

export default {
  name: 'YouTubeWidget',
  directives: {
    Draggable
  },
  data () {
    return {
      searchQuerry: '',
      searchResult: []
    }
  },
  methods: {
    searchVideos () {
      this.searchResult.clear()
      axios.get(`http://localhost:5000/youtubeSearch/${this.searchQuerry}`)
        .then(data => {
          this.searchResult = data.items
          console.log(this.searchResult)
        })
        .catch(err => { console.error(err) })
    }
  }
}
</script>

<style lang="scss" scoped>
    .youtubeWidget {
        width: 50;
        background-color: rgba($color: #ff0000, $alpha: 1.0);
        width: 20%;
        height: 50%;
        border-radius: 10px;
        border-width: 1px;
    }
</style>
