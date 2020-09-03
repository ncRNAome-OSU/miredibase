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
          <q-th colspan="3"></q-th>
          <q-th colspan="3" class="bg-light-blue-9 text-white">
            Study information
          </q-th>
          <q-th colspan="5" class="bg-deep-orange-9 text-white">
            Stem-loop information
          </q-th>
          <q-th colspan="2" class="bg-green-9 text-white">
            Normal condition
          </q-th>
           <q-th colspan="2" class="bg-deep-purple-9 text-white">
            Adverse condition
          </q-th>
        </q-tr>
        <q-tr>
          <q-th key="name" :props="props">
            <helper>
              Compare the arithmetic means of editing levels between normal and adverse conditions
              for each editing site. The higher value for each comparison is colored in red.
              Click on the purple inscriptions to access external online resources.
            </helper>
          </q-th>
          <q-th
            key="organism" :props="props">
            Organism
          </q-th>
          <q-th key="modType" :props="props" class="text-left">
            RNA modification<br>type
          </q-th>
          <q-th key="author" :props="props" class="bg-light-blue-6 text-white">
            Author(s)
          </q-th>
          <q-th key="year" :props="props" class="bg-light-blue-7 text-white">
            Year
          </q-th>
          <q-th key="pubmedId" :props="props" class="bg-light-blue-8 text-white">
            Pubmed ID
          </q-th>
          <q-th key="stemloop" :props="props" class="bg-deep-orange-4 text-white">
            Stem-loop
          </q-th>
          <q-th key="transcriptRegion" :props="props" class="bg-deep-orange-5 text-white text-left">
            Edited transcript<br>region
          </q-th>
          <q-th key="stemloopRegionInvolved" :props="props" class="bg-deep-orange-6 text-white text-left">
            Region<br>involved
          </q-th>
          <q-th key="stemloopLocalPos" :props="props" class="bg-deep-orange-7 text-white text-left">
            Local position<br>in stem-loop
          </q-th>
          <q-th key="mirna" :props="props" class="bg-deep-orange-8 text-white">
            miRNA
          </q-th>
          <q-th key="mirnaLocalPos" :props="props" class="bg-deep-orange-9 text-white text-left">
            Local position<br>in miRNA
          </q-th>
          <q-th key="normalCondition" :props="props" class="bg-green-7 text-white text-left">
            Biological<br>source
          </q-th>
          <q-th key="percEditingInNormalCondition" :props="props" class="bg-green-8 text-white text-left">
            Avg. (%) Editing<br>Level
          </q-th>
           <q-th key="adverseCondition" :props="props" class="bg-deep-purple-7 text-white text-left">
            Biological<br>source
          </q-th>
          <q-th key="percEditingInAdverseCondition" :props="props" class="bg-deep-purple-8 text-white text-left">
            Avg. (%) Editing<br>Level
          </q-th>
        </q-tr>
      </template>

      <q-td slot="body-cell-modType" slot-scope="props" :props="props">
        {{ prettifySnvType(props.value) }}
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

      <q-td slot="body-cell-mirna" slot-scope="props" :props="props">
        <q-btn
          no-caps
          square
          class="text-weigth-bold"
          type="a"
          :label="props.value"
          flat
          color="purple"
          @click="goToExternaResource(`http://www.mirbase.org/cgi-bin/mirna_entry.pl?acc=${props.row.mirna_acc_number}`)"
        />
      </q-td>

      <q-td slot="body-cell-percEditingInAdverseCondition" slot-scope="props" :props="props">
        <span :class="props.row.perc_el_adverse_style">{{ props.value }}</span>
      </q-td>

      <q-td slot="body-cell-percEditingInNormalCondition" slot-scope="props" :props="props">
        <span :class="props.row.perc_el_normal_style">{{ props.value }}</span>
      </q-td>

      <q-td slot="body-cell-pubmedId" slot-scope="props" :props="props">
        <q-btn
          no-caps
          square
          class="text-weigth-bold"
          type="a"
          :label="props.value"
          flat
          color="purple"
          @click="goToExternaResource(`https://pubmed.ncbi.nlm.nih.gov/${props.value}`)"
        />
      </q-td>

      <q-td slot="body-cell-normalCondition"
        slot-scope="props"
        :props="props"
        :style="{ 'max-width': '200px', whiteSpace: 'normal' }"
      >
        {{ props.value }}
      </q-td>

      <q-td slot="body-cell-adverseCondition"
        slot-scope="props"
        :props="props"
        :style="{ 'max-width': '200px', whiteSpace: 'normal' }"
      >
        {{ props.value }}
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
      filter: ''
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
