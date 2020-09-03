<template>
  <div class="fixed-center text-center">
    <p>
      <img
        src="~assets/docker-compose.png"
        style="width:30vw;max-width:200px;"
      >
    </p>
    <p class="text-faded">Sorry, something went wrong. Please, try again.</p>
    <q-btn
      color="primary"
      style="width:200px;"
      @click="$router.push('/')"
    >Go back</q-btn>
  </div>
</template>

<script>
export default {
  name: 'NoData',
  props: {},
  data () {
    return {}
  }
}
</script>
