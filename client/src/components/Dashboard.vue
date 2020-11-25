<template>
    <div
      class="dashboard"
    >
      <TopBar></TopBar>
      <div>
        <vue-fab
            class="fab-main-button"
            mainBtnColor="#84bd00"
            size="big"
        >
            <fab-item
              :idx="0"
              title="YouTube"
              icon="play_circle_filled"
              size="big"
              color="#ff0000"
              v-on:click.native="youtubeOnClick"
            />
            <fab-item
              :idx="1"
              title="Weather"
              icon="brightness_7"
              size="big"
              color="#eccc16"
              v-on:click.native="weatherOnClick"
            />
        </vue-fab>
      </div>
      <YouTuveWidget v-if="youtubeActive"></YouTuveWidget>
      <WeatherWidget v-if="weatherActive"></WeatherWidget>
    </div>
</template>

<script>
import TopBar from './TopBar'
import YouTuveWidget from './YoutubeWidget'
import WeatherWidget from './WeatherWidget'

export default {
  name: 'Dashboard',
  components: {
    TopBar,
    YouTuveWidget,
    WeatherWidget
  },
  data () {
    return {
      youtubeActive: false,
      weatherActive: false
    }
  },
  methods: {
    youtubeOnClick () {
      this.youtubeActive = !this.youtubeActive
    },
    weatherOnClick () {
      this.weatherActive = !this.weatherActive
    }
  }
}
</script>

<style  lang="scss" scoped>
    .fab-main-button {
        left: 95%;
    }
    .dashboard {
        position:fixed;
        padding:0;
        margin:0;
        top:0;
        left:0;
        width: 100%;
        height: 100%;
        background-color: rgba($color: #333331, $alpha: 1.0);
    }
</style>
