<template>
    <div>
        <p>{{ msg }}</p>
    </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Ping',
  data () {
    return {
      msg: 'Pong !!'
    }
  },
  created () {
    console.log('created')
    this.getMessage()
  },
  methods: {
    getMessage () {
      const path = 'http://localhost:5000/ping'
      axios.get(path)
        .then((res) => {
          console.log(res.data)
          this.msg = res.data
        })
        .catch((error) => {
          // eslint-disable-next-line
              console.error(error)
        })
    }
  }
}
</script>
