<template>
    <div
      class="dashboard"
    >
      <TopBar></TopBar>
      <v-button large>
        Button
      </v-button>
      <div>
        <vue-fab
            class="fab-main-button"
            mainBtnColor="#84bd00"
            size="big"
            globalOptions="{spacing: 40}"
        >
            <fab-item
              idx="0"
              title="YouTube"
              icon="play_circle_filled"
              size="big"
              color="#ff0000"
              v-on:click.native="youtubeOnClick"
            />
        </vue-fab>
      </div>
      <YouTuveWidget v-if="youtubeActive"></YouTuveWidget>
    </div>
</template>

<script>
import TopBar from './TopBar'
import YouTuveWidget from './YoutubeWidget'

export default {
  name: 'Dashboard',
  components: {
    TopBar,
    YouTuveWidget
  },
  data () {
    return {
      youtubeActive: false
    }
  },
  methods: {
    youtubeOnClick () {
      this.youtubeActive = !this.youtubeActive
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
        background-color: rgba($color: #333131, $alpha: 1.0);
    }
</style>
