<template>
  <div v-if="isObjectNotEmpty(data)">
    <q-table
      dense
      class="shadow-2"
      :title="title"
      :data="data"
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

      <template slot="header" slot-scope="props" :props="props" style="display: contents">
        <q-tr>
          <q-th colspan="1"></q-th>
          <q-th
            colspan="4"
            class="bg-deep-purple-9 text-white"
          >
            Target information
          </q-th>
          <q-th
            colspan="5"
            class="bg-light-blue-9 text-white"
          >
            Prediction tools
          </q-th>
          <q-th colspan="1"></q-th>
        </q-tr>
        <q-tr>
          <q-th key="name" :props="props">
            <helper>
              Results can be ordered by RefSeq or Ensemble ID, Gene name, Gene biotype, or consensus number.
              Click on the purple inscriptions to access external online resources.
            </helper>
          </q-th>
          <q-th
            key="refSeq" :props="props" class="bg-deep-purple-6 text-white">
            RefSeq
          </q-th>
          <q-th
            key="ensemblId" :props="props" class="bg-deep-purple-7 text-white">
            Ensembl ID
          </q-th>
          <q-th
            key="geneName" :props="props" class="bg-deep-purple-8 text-white">
            Gene name
          </q-th>
          <q-th
            key="geneBiotype" :props="props" class="bg-deep-purple-9 text-white">
            Gene biotype
          </q-th>
          <q-th key="miRanda" :props="props" class="bg-light-blue-5 text-white">
            miRanda
          </q-th>
          <q-th key="RNAhybrid" :props="props" class="bg-light-blue-6 text-white">
            RNAhybrid
          </q-th>
          <q-th key="TargetScan" :props="props" class="bg-light-blue-7 text-white">
            TargetScan
          </q-th>
          <q-th key="PITA" :props="props" class="bg-light-blue-8 text-white">
            PITA
          </q-th>
          <q-th key="miRmap" :props="props" class="bg-light-blue-9 text-white">
            miRmap
          </q-th>
          <q-th key="Consensus" :props="props">
            Consensus
          </q-th>
        </q-tr>
      </template>

      <q-td slot="body-cell-refSeq" slot-scope="props" :props="props">
        <q-btn
          v-if="isObjectNotEmpty(props.value)"
          no-caps
          square
          dense
          class="text-weigth-bold q-px-xs"
          type="a"
          :label="props.value"
          flat
          color="purple"
          @click="goToExternaResource(`https://www.ncbi.nlm.nih.gov/nuccore/${props.value}`)"
        />
      </q-td>

      <q-td slot="body-cell-ensemblId" slot-scope="props" :props="props">
        <q-btn
          v-if="isObjectNotEmpty(props.value)"
          no-caps
          square
          dense
          class="text-weigth-bold q-px-xs"
          type="a"
          :label="props.value"
          flat
          color="purple"
          @click="goToExternaResource(`https://useast.ensembl.org/Homo_sapiens/Gene/Summary?db=core;g=${props.value}`)"
        />
      </q-td>

      <q-td slot="body-cell-geneName" slot-scope="props" :props="props">
        <q-btn
          v-if="isObjectNotEmpty(props.value)"
          no-caps
          square
          dense
          class="text-weigth-bold q-px-xs"
          type="a"
          :label="props.value"
          flat
          color="purple"
          @click="goToExternaResource(`https://www.genecards.org/cgi-bin/carddisp.pl?gene=${props.value}`)"
        />
      </q-td>

    </q-table>

  </div>
</template>

<script>
import { openURL } from 'quasar'
import Helper from 'components/Helper'

export default {
  name: 'PredictionsTableViewer',
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
    }
  },
  data () {
    return {
      filter: '',
      pagination: {
        rowsPerPage: 10
      }
    }
  },
  mounted () {},
  computed: {},
  methods: {

    isObjectNotEmpty (value) {
      return this.$utils.isObjectNotEmpty(value)
    },

    exportTable () {
      return this.$exportDataTableAsCSV()
    },

    goToExternaResource (url) {
      openURL(url)
    }

  }
}
</script>
