<template>
  <q-card class="text-weight-light q-mb-xs">

    <q-card-section horizontal>
      <q-card-section style="min-width: 18em;, max-width: 18em" class="q-py-xs bg-grey-3 text-weight-bold text-grey-9">
        <q-item-label class="text-title  q-mt-xs q-mb-xs">
          <q-icon size="xs" v-if="icon" :name="icon" :color="icon === 'star' ? 'light-blue-9' : 'deep-orange-9'" />
          {{ name }}
        </q-item-label>
        <q-item-label caption class="text-deep-orange-7">{{ bio }}</q-item-label>
      </q-card-section>

      <q-separator vertical />

      <q-card-section class="q-py-xs">
        <p class="q-mb-xs">
          <span v-if="department"><q-icon name="business_center" /> {{ department }}&nbsp;&nbsp;&nbsp;&nbsp;<br></span>
          <span v-if="institution"><q-icon name="account_balance" /> {{ institution }}<br></span>
          <span v-if="institution2"><q-icon name="account_balance" /> {{ institution2 }}<br></span>
        </p>
        <p v-if="institution" class="q-mb-xs">
          <q-icon size="xs" name="email" /> {{ sanitizeEmail(email) }}
        </p>
      </q-card-section>
    </q-card-section>

  </q-card>
</template>

<script>
import { openURL } from 'quasar'

export default {
  name: 'ContactItem',
  props: {
    name: {
      type: String,
      required: true
    },
    bio: {
      type: String,
      required: true
    },
    icon: {
      type: String,
      required: true
    },
    role: {
      type: String,
      default: ''
    },
    department: {
      type: String,
      default: ''
    },
    division: {
      type: String,
      default: ''
    },
    institution: {
      type: String,
      default: ''
    },
    institution2: {
      type: String,
      default: ''
    },
    picture: {
      type: String,
      default: ''
    },
    email: {
      type: String,
      default: ''
    }
  },
  data () {
    return {}
  },
  computed: {},
  methods: {

    exportTable () {
      return this.$exportDataTableAsCSV()
    },

    sanitizeEmail (value) {
      return this.$utils.sanitizeEmail(value)
    },

    goToExternaResource (url) {
      openURL(url)
    },

    showSNVDetails (idx) {
      this.$emit('loadSNVData', this.data[idx])
    }
  }
}
</script>
