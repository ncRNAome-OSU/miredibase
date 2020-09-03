<template>
  <div>
    <q-table
      dense
      :title="title"
      :data="data"
      :columns="columns"
      :color="firstColumnsHeaderColor"
      :row-key="rowKey"
      :visible-columns="visibleColumns"
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

      <template slot="header" slot-scope="props" :props="props" style="display: contents">
        <q-tr>
          <q-th colspan="6"></q-th>
          <q-th colspan="5" class="bg-deep-orange-9 text-white">
            Stem-loop information
          </q-th>
        </q-tr>
        <q-tr>
          <q-th key="name" :props="props">
            <helper>
              Click on the left-sided red icons to display summary tables. Click on the purple
              inscriptions to access external resources.
            </helper>
          </q-th>
          <q-th
            key="organism" :props="props">
            Organism
          </q-th>
          <q-th key="modType" :props="props" class="text-left">
            RNA modification<br>type
          </q-th>
          <q-th key="chromosome" :props="props">
            Chromosome
          </q-th>
          <q-th key="strand" :props="props">
            Strand
          </q-th>
          <q-th key="genomicPosition" :props="props" class="text-left">
            Genomic position<br>(UCSC)
          </q-th>
          <q-th key="stemloop" :props="props" class="bg-deep-orange-5 text-white">
            Stem-loop
          </q-th>
          <q-th key="transcriptRegion" :props="props" class="bg-deep-orange-6 text-white text-left">
            Edited transcript<br>region
          </q-th>
          <q-th key="stemloopRegionInvolved" :props="props" class="bg-deep-orange-7 text-white text-left">
            Region<br>involved
          </q-th>
          <q-th key="stemloopLocalPos" :props="props" class="bg-deep-orange-8 text-white text-left">
            Local position<br>in stem-loop
          </q-th>
          <q-th key="mirnaLocalPos" :props="props" class="bg-deep-orange-9 text-white text-left">
            Local position<br>in miRNA
          </q-th>
        </q-tr>
      </template>

      <q-td slot="body-cell-name" slot-scope="props" :props="props">
        <q-btn
          round
          size="sm"
          color="red-7"
          icon="view_headline"
          @click="showSNVDetails(props.value)"
        >
        </q-btn>
      </q-td>

      <q-td slot="body-cell-modType" slot-scope="props" :props="props">
        {{ prettifySnvType(props.value) }}
      </q-td>

      <q-td slot="body-cell-chromosome" slot-scope="props" :props="props">
        <q-chip square outline color="green-6 text-weight-bold">
          {{ props.value }}
        </q-chip>
      </q-td>

      <q-td slot="body-cell-genomicPosition" slot-scope="props" :props="props">
        <q-btn
          no-caps
          square
          class="text-weigth-bold"
          type="a"
          :label="props.value"
          flat
          color="purple"
          @click="goToExternaResource(`${props.row.uri.ucsc}`)"
        />
      </q-td>

      <q-td slot="body-cell-stemloop" slot-scope="props" :props="props">
        <q-btn
          no-caps
          square
          class="text-weigth-bold"
          type="a"
          :label="props.value"
          flat
          color="purple"
          @click="goToExternaResource(`http://www.mirbase.org/cgi-bin/mirna_entry.pl?acc=${props.row.stemloop_acc_number}`)"
        />
      </q-td>

    </q-table>
  </div>
</template>

<script>
import { openURL } from 'quasar'
import Helper from 'components/Helper'

export default {
  name: 'TableViewer',
  components: {
    Helper
  },
  props: {
    title: {
      type: String,
      required: true
    },
    data: {
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
    visibleColumns: {
      type: Array,
      required: true
    }
  },
  data () {
    return {
      filter: '',
      pagination: {
        rowsPerPage: 5
      }
    }
  },
  computed: {},
  methods: {

    exportTable () {
      return this.$exportDataTableAsCSV()
    },

    prettifySnvType (value) {
      return this.$utils.prettifySnvType(value)
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
