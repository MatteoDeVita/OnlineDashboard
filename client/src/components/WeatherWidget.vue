<template>
    <div v-if="show == true" v-draggable class="weather">
        <div class="searchField">
            <md-field class="inputField">
                <label>Ville</label>
                <md-input v-model="cityQuerry"></md-input>
            </md-field>
            <div
                class="searchButton"
                @click="searchWeather"
                >
                Search
            </div>
            <div v-if="resultActive">
                <div>
                    <img class="icon" v-bind:src="searchResult.icon">
                    <p class="temperature">{{ searchResult.temp }} °C (ressentit {{ searchResult.feels_like }} °C)</p>
                </div>
                <div>
                    <p>{{ searchResult.description }}</p>
                </div>
                <div>
                    <p>Vent à {{ searchResult.wind_speed }} km/s</p>
                </div>
            </div>
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
  name: 'Weather',
  directives: {
    Draggable
  },
  data () {
    return {
      cityQuerry: '',
      searchResult: {},
      resultActive: false,
      show: true
    }
  },
  methods: {
    searchWeather () {
      this.searchResult = []
      if (this.cityQuerry === '') {
        this.resultActive = false
        return
      }
      axios.get(`http://localhost:5000/weather/${this.cityQuerry}`)
        .then(res => {
          this.searchResult = res.data
          this.resultActive = true
          console.log(this.searchResult)
        })
        .catch(err => {
          console.error(err)
          this.resultActive = false
        })
    }
  }
}
</script>

<style lang="scss" scoped>
    .weather {
        width: 50;
        background-color: rgba($color: #eccc16, $alpha: 1.0);
        width: 20%;
        height: 50%;
        border-radius: 10px;
        border-width: 1px;
        max-height: 28%;
    }
    .searchField {
        width: 100%;
        margin: 10px;
    }
    .inputField {
        display: inline-block;
        width: 60%;
        margin-right: 10px;
        padding-left: 10px;
    }
    .searchButton {
      margin-left: 20px;
      width: 25%;
      border-style: solid;
      margin-left: 10px;
      padding: 10px;
      border-radius: 10px;
      background-color: rgba($color: #eccc16, $alpha: 1.0);
      border-width: 2px;
      display: inline-block;
    }
    .searchButton:hover {
      background-color: rgba($color: #b87e00, $alpha: 1.0);
    }
    .searchButton:active {
      background-color: rgba($color: #b87e00, $alpha: 1.0);
    }
    .icon {
        display: inline-block;
    }
    .temperature {
        display: inline-block;
    }
    .closeButton {
      margin-left: 90%;
    }
</style>
