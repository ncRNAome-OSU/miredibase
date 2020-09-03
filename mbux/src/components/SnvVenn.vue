<template>
  <div v-if="isObjectNotEmpty(snvData)" class="row q-pb-md">
    <div class="col-xs-12 col-sm-6 col-md-4 col-lg-4 q-pa-xs">

      <subset-table-viewer
        :title="wildtypeUniqueTitle"
        :data="table.wildtypeUniqueData"
        :columns="columns"
        first-columns-header-color="primary"
        row-key="name"
        :is-downloadable="isDownloadable"
        badge-color="light-blue"
        :special-columns="table.specialColumns"
        :tooltip-text="tooltipWildtypeUniqueText"
      />

    </div>
    <div class="col-xs-12 col-sm-6 col-md-4 col-lg-4 q-pa-xs">

        <subset-table-viewer
          :title="intersectionTitle"
          :data="table.intersectionData"
          :columns="columns"
          first-columns-header-color="primary"
          row-key="name"
          :is-downloadable="isDownloadable"
          badge-color="green"
          :special-columns="table.specialColumns"
          :tooltip-text="tooltipIntersectionText"
        />

    </div>
    <div class="col-xs-12 col-sm-6 col-md-4 col-lg-4 q-pa-xs">

        <subset-table-viewer
          :title="editedUniqueTitle"
          :data="table.editedUniqueData"
          :columns="columns"
          first-columns-header-color="primary"
          row-key="name"
          :is-downloadable="isDownloadable"
          badge-color="red"
          :special-columns="table.specialColumns"
          :tooltip-text="tooltipEditedUniqueText"
        />

    </div>
  </div>
</template>

<script>
import SubsetTableViewer from 'components/SubsetTableViewer'

export default {
  name: 'SnvVenn',
  components: {
    SubsetTableViewer
  },
  props: {
    snvData: {
      type: Object,
      default: null
    },
    columns: {
      type: Array,
      required: true
    },
    isDownloadable: {
      type: Boolean,
      default: true
    },
    wildtypeUniqueTitle: {
      type: String,
      default: ''
    },
    editedUniqueTitle: {
      type: String,
      default: ''
    },
    intersectionTitle: {
      type: String,
      default: ''
    },
    enrichmentType: {
      type: String,
      required: true
    },
    enrichmentSubtype: {
      type: String,
      default: ''
    },
    badgeColor: {
      type: String,
      default: 'grey'
    },
    tooltipWildtypeUniqueText: {
      type: String,
      required: true
    },
    tooltipEditedUniqueText: {
      type: String,
      required: true
    },
    tooltipIntersectionText: {
      type: String,
      required: true
    }
  },
  data () {
    return {
      table: {
        wildtypeUniqueData: [],
        editedUniqueData: [],
        intersectionData: [],
        specialColumns: []
      }
    }
  },
  mounted () {
    this.initDataTablesRows(this.snvData)
  },
  computed: {},
  methods: {

    isObjectNotEmpty (value) {
      return this.$utils.isObjectNotEmpty(value)
    },

    objectHasPropery (object, key) {
      return this.$utils.objectHasPropery(object, key)
    },

    addTableRowIndex (data) {
      const rows = []
      if (this.isObjectNotEmpty(data)) {
        data.forEach((item, index) => {
          item.name = index
          rows.push(item)
        })
      }
      return rows
    },

    initDataTablesRows (data) {
      switch (this.enrichmentType) {
        case 'go':
          this.table.specialColumns = [
            {
              name: 'goId',
              loop: false,
              link: 'https://www.ebi.ac.uk/QuickGO/term/',
              style: {}
            },
            {
              name: 'goName',
              loop: false,
              link: '',
              style: { 'max-width': '600px', whiteSpace: 'normal' }
            }
          ]

          if (this.objectHasPropery(data, this.enrichmentSubtype)) {
            if (this.objectHasPropery(data[this.enrichmentSubtype], 'wildtype_unique')) {
              this.table.wildtypeUniqueData = this.addTableRowIndex(data[this.enrichmentSubtype].wildtype_unique)
            }
            if (this.objectHasPropery(data[this.enrichmentSubtype], 'edited_unique')) {
              this.table.editedUniqueData = this.addTableRowIndex(data[this.enrichmentSubtype].edited_unique)
            }
            if (this.objectHasPropery(data[this.enrichmentSubtype], 'intersection')) {
              this.table.intersectionData = this.addTableRowIndex(data[this.enrichmentSubtype].intersection)
            }
          }

          break

        default:
          this.table.specialColumns = [
            {
              name: 'pathwayId',
              loop: false,
              link: this.enrichmentType === 'kegg' ? 'https://www.genome.jp/dbget-bin/www_bget?' : 'https://reactome.org/PathwayBrowser/#/',
              style: {}
            },
            {
              name: 'pathwayName',
              loop: false,
              link: '',
              style: { 'max-width': '600px', whiteSpace: 'normal' }
            }
          ]

          if (this.objectHasPropery(data, 'wildtype_unique')) {
            this.table.wildtypeUniqueData = this.addTableRowIndex(data.wildtype_unique)
          }
          if (this.objectHasPropery(data, 'edited_unique')) {
            this.table.editedUniqueData = this.addTableRowIndex(data.edited_unique)
          }
          if (this.objectHasPropery(data, 'intersection')) {
            this.table.intersectionData = this.addTableRowIndex(data.intersection)
          }
          break
      }
    }

  },
  watch: {}
}
</script>
