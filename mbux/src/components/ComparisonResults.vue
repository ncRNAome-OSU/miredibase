<template>
  <q-page>
    <div v-if="isObjectNotEmpty(data)">
      <p class="text-justify text-weight-light q-py-sm">
        Here you can compare intra-study information for a specific RNA modification type in diseases or stem-loops (adverse versus normal condition).
      </p>

      <comparison-table-viewer
        title=""
        :data="data"
        :columns="columns"
        first-columns-header-color="primary"
        row-key="name"
        :is-downloadable="isDownloadable"
        :visible-columns="visibleColumns"
      />

    </div>
  </q-page>
</template>

<script>
import ComparisonTableViewer from 'components/ComparisonTableViewer'

export default {
  name: 'ComparisonResults',
  components: {
    ComparisonTableViewer
  },
  props: {
    columns: {
      type: Array,
      required: true,
      default: () => []
    },
    data: {
      type: Array,
      required: true,
      default: () => []
    },
    visibleColumns: {
      type: Array,
      required: true
    }
  },
  data () {
    return {
      isDownloadable: true,
      snvData: {}
    }
  },
  mounted () {},
  computed: {},
  methods: {

    isObjectNotEmpty (value) {
      return this.$utils.isObjectNotEmpty(value)
    }

  }
}
</script>
