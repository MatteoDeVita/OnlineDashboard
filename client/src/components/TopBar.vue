<template>
  <div class="topbar">
    <p>DASHBOARD</p>
  </div>
</template>

<script>
export default {
  name: 'TopBar'
}
</script>

<style lang="scss" scoped>
    .topbar {
        top:0;
        left:0;
        z-index: 100;
        padding:0;
        margin:0;
        background-color: rgba($color: #84bd00, $alpha: 1.0);
        color: white;
        border-style: solid;
        border-width: 2px;
        border-bottom-left-radius: 15px;
        border-bottom-right-radius: 15px;
        font-size: 1.5em;
        text-align: center;
    }
</style>
