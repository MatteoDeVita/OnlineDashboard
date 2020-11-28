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
              title="YouTube comment"
              icon="speaker_notes"
              size="big"
              color="#ff0000"
              v-on:click.native="youtubeCommentOnClick"
            />
            <fab-item
              :idx="2"
              title="YouTube channel info"
              icon="account_box"
              size="big"
              color="#ff0000"
              v-on:click.native="youtubeChannelOnClick"
            />
            <fab-item
              :idx="3"
              title="Weather"
              icon="brightness_7"
              size="big"
              color="#eccc16"
              v-on:click.native="weatherOnClick"
            />
            <fab-item
              :idx="4"
              title="Weather forecast"
              icon="timeline"
              size="big"
              color="#257cff"
              v-on:click.native="weatherForecastOnClick"
            />
            <fab-item
              :idx="5"
              title="GitHub Account"
              icon="contact_page"
              size="big"
              color="#000000"
              v-on:click.native="gitHubAccounOnClick"
            />
            <fab-item
              :idx="6"
              title="GitHub Account Repositories"
              icon="featured_play_list"
              size="big"
              color="#000000"
              v-on:click.native="gitHubRepositoriesOnClick"
            />
        </vue-fab>
      </div>
        <div v-for="youtubeSearch in youtubeSearchArray" :key="youtubeSearch">
          <YouTubeSearchWidget/>
        </div>
        <div v-for="youtubeComment in youtubeCommentArray" :key="youtubeComment">
          <YoutubeCommentWidget/>
        </div>
        <div v-for="youtubeChannel in youtubeChannelArray" :key="youtubeChannel">
          <YoutubeChannelWidget/>
        </div>
        <div v-for="weatherWidget in weatherWidgetArray" :key="weatherWidget">
          <WeatherWidget/>
        </div>
        <div v-for="weatherForecast in weatherForecastArray" :key="weatherForecast">
          <WeatherForecast/>
        </div>
        <div v-for="gitHubAccount in gitHubAccountArray" :key="gitHubAccount">
          <GithubAccountWidget/>
        </div>
        <div v-for="gihubRepositories in gihubRepositoriesArray" :key="gihubRepositories">
          <GihubRepositoriesWidget/>
        </div>
    </div>
</template>

<script>
import TopBar from './TopBar'
import YouTubeSearchWidget from './YoutubeSearchWidget'
import YoutubeCommentWidget from './YoutubeCommentWidget'
import YoutubeChannelWidget from './YoutubeChannelWidget'
import WeatherWidget from './WeatherWidget'
import WeatherForecast from './WeatherForecastWidget'
import GithubAccountWidget from './GithubAccountWidget'
import GihubRepositoriesWidget from './GithubRepositoriesWidget'

export default {
  name: 'Dashboard',
  components: {
    TopBar,
    YouTubeSearchWidget,
    YoutubeCommentWidget,
    YoutubeChannelWidget,
    WeatherWidget,
    WeatherForecast,
    GithubAccountWidget,
    GihubRepositoriesWidget
  },
  data () {
    return {
      youtubeSearchArray: [],
      youtubeCommentArray: [],
      youtubeChannelArray: [],
      weatherWidgetArray: [],
      weatherForecastArray: [],
      gitHubAccountArray: [],
      gihubRepositoriesArray: []
    }
  },
  methods: {
    youtubeSearchOnClick () {
      this.youtubeSearchArray.push(YouTubeSearchWidget)
    },
    youtubeCommentOnClick () {
      this.youtubeCommentArray.push(YoutubeCommentWidget)
    },
    youtubeChannelOnClick () {
      this.youtubeChannelArray.push(YoutubeChannelWidget)
    },
    weatherOnClick () {
      this.weatherWidgetArray.push(WeatherWidget)
    },
    weatherForecastOnClick () {
      this.weatherForecastArray.push(WeatherForecast)
    },
    gitHubAccounOnClick () {
      this.gitHubAccountArray.push(GithubAccountWidget)
    },
    gitHubRepositoriesOnClick () {
      this.gihubRepositoriesArray.push(GihubRepositoriesWidget)
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
