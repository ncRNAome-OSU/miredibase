<template>
  <div v-if="isObjectNotEmpty(snvData)">
    <q-table
      dense
      class="shadow-2"
      :title="title"
      :data="table.data"
      :columns="columns"
      :color="firstColumnsHeaderColor"
      :row-key="rowKey"
      :filter="filter"
      :pagination.sync="pagination"
    >
      <template v-slot:top-right>
        <q-input
          size="xs"
          outlined
          rounded
          dense
          debounce="300"
          v-model="filter"
          placeholder="Search within the table"
        >
          <template v-slot:append>
            <q-icon name="search" />
          </template>
        </q-input>
        <q-btn class="q-ml-md" v-if="isDownloadable"
          color="orange-9"
          icon-right="archive"
          label="Export to .CSV"
          no-caps
          @click="exportTable"
        />
      </template>

      <q-th slot="header-cell-name">
        <helper>
          {{ tooltipText }}
        </helper>
      </q-th>

      <template v-for="(item) in table.specialColumns" :slot="`body-cell-${item.name}`" slot-scope="props" :props="props">
        <q-td
          :props="props"
          :key="item.name"
          class="fill-area-content flexbox-item-grow col-2"
          :style="item.style"
        >
          <template v-if="isObjectNotEmpty(item.link) && item.link !== ''">
            <template v-if="!item.loop">
              <q-btn
                no-caps
                square
                dense
                class="text-weigth-bold q-px-xs"
                type="a"
                :label="props.value"
                flat
                color="purple"
                @click="goToExternaResource(`${item.link}${props.value}`)"
              />
            </template>
            <template v-else>
              <q-btn
                v-for="name in props.value"
                no-caps
                square
                dense
                class="text-weigth-bold q-px-xs"
                type="a"
                :label="name"
                :key="name"
                flat
                color="purple"
                @click="goToExternaResource(`${item.link}${name}`)"
              />
            </template>
          </template>
          <template v-else>
            {{ props.value }}
          </template>
        </q-td>
      </template>

    </q-table>

  </div>
</template>

<script>
import { openURL } from 'quasar'
import Helper from 'components/Helper'

export default {
  name: 'EnrichmentTableViewer',
  components: {
    Helper
  },
  props: {
    title: {
      type: String,
      required: true
    },
    snvData: {
      type: Array,
      required: true
    },
    columns: {
      type: Array,
      required: true
    },
    firstColumnsHeaderColor: {
      type: String,
      default: ''
    },
    rowKey: {
      type: String,
      required: true
    },
    isDownloadable: {
      type: Boolean,
      default: true
    },
    enrichmentType: {
      type: String,
      required: true
    },
    enrichmentSubtype: {
      type: String,
      default: ''
    },
    tooltipText: {
      type: String,
      required: true
    }
  },
  data () {
    return {
      table: {
        data: [],
        specialColumns: []
      },
      filter: '',
      pagination: {
        rowsPerPage: 5
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

    exportTable () {
      return this.$exportDataTableAsCSV()
    },

    goToExternaResource (url) {
      openURL(url)
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
              style: { 'max-width': '150px', whiteSpace: 'normal' }
            },
            {
              name: 'targetsList',
              loop: true,
              link: 'https://www.genecards.org/cgi-bin/carddisp.pl?gene=',
              style: { 'max-width': '800px', whiteSpace: 'normal' }
            }
          ]
          if (this.isObjectNotEmpty(data)) {
            this.table.data = this.addTableRowIndex(data)
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
            },
            {
              name: 'targetsList',
              loop: true,
              link: 'https://www.genecards.org/cgi-bin/carddisp.pl?gene=',
              style: { 'max-width': '800px', whiteSpace: 'normal' }
            }
          ]

          if (this.isObjectNotEmpty(data)) {
            this.table.data = this.addTableRowIndex(data)
          }
          break
      }
    }

  }
}
</script>
