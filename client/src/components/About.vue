<template>
    <div>
        <json-viewer
            :value="about"
            :expand-depth=5
        >
        </json-viewer>
    </div>
</template>

<script>
import aboutJSON from '../../about'
import JsonViewer from 'vue-json-viewer'
import axios from 'axios'

export default {
  name: 'About',
  components: {
    JsonViewer
  },
  created () {
    this.updateIpAdress()
  },
  data () {
    return {
      about: aboutJSON
    }
  },
  methods: {
    updateIpAdress () {
      axios.get('http://localhost:5000/getIpAdress')
        .then(res => {
          this.about.client.host = res.data
        })
    }
  }
}
</script>
