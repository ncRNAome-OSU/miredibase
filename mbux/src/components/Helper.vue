<template>
  <q-icon
    name="info"
    class="text-grey-7 text-h6"
  >
    <q-tooltip
      anchor="top middle"
      self="bottom middle"
      :offset="[10, 10]"
      transition-show="scale"
      transition-hide="scale"
    >
      <div
        style="max-width: 250px"
        class="text-justify"
      >
        <slot></slot>
      </div>
    </q-tooltip>
  </q-icon>
</template>

<script>

export default {
  name: 'Helper',
  props: {},
  data () {
    return {}
  },
  computed: {},
  methods: {}
}
</script>
