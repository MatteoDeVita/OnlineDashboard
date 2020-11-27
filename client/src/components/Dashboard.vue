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
              title="YouTube search"
              icon="play_circle_filled"
              size="big"
              color="#ff0000"
              v-on:click.native="youtubeSearchOnClick"
            />
            <fab-item
              :idx="1"
              title="Weather"
              icon="brightness_7"
              size="big"
              color="#eccc16"
              v-on:click.native="weatherOnClick"
            />
            <fab-item
              :idx="2"
              title="Weather forecast"
              icon="timeline"
              size="big"
              color="#257cff"
              v-on:click.native="weatherForecastOnClick"
            />
        </vue-fab>
      </div>
      <YouTubeSearchWidget v-if="youtubeSearchActive"></YouTubeSearchWidget>
      <WeatherWidget v-if="weatherActive"></WeatherWidget>
      <WeatherForecast v-if="weatherForecastActive"></WeatherForecast>
    </div>
</template>

<script>
import TopBar from './TopBar'
import YouTubeSearchWidget from './YoutubeSearchWidget'
import WeatherWidget from './WeatherWidget'
import WeatherForecast from './WeatherForecastWidget'

export default {
  name: 'Dashboard',
  components: {
    TopBar,
    YouTubeSearchWidget,
    WeatherWidget,
    WeatherForecast
  },
  data () {
    return {
      youtubeSearchActive: false,
      weatherActive: false,
      weatherForecastActive: false
    }
  },
  methods: {
    youtubeSearchOnClick () {
      this.youtubeSearchActive = !this.youtubeSearchActive
    },
    weatherOnClick () {
      this.weatherActive = !this.weatherActive
    },
    weatherForecastOnClick () {
      this.weatherForecastActive = !this.weatherForecastActive
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
        background-color: rgba($color: #313233, $alpha: 1.0);
    }
</style>
