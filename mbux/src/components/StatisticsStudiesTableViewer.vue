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
            Studies information
          </q-th>
        </q-tr>
        <q-tr>
          <q-th key="name" :props="props"></q-th>
          <q-th key="organism" :props="props">
            Organism
          </q-th>
          <q-th key="modType" :props="props">
            RNA modification type
          </q-th>
          <q-th key="author" :props="props" class="bg-light-blue-6 text-white">
            Author(s)
          </q-th>
          <q-th key="year" :props="props" class="bg-light-blue-7 text-white">
            Year
          </q-th>
          <q-th
            key="pubmedId" :props="props" class="bg-light-blue-8 text-white">
            Pubmed ID
          </q-th>
        </q-tr>
      </template>

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

    </q-table>

  </div>
</template>

<script>
import { openURL } from 'quasar'

export default {
  name: 'StatisticsStudiesTableViewer',
  components: {},
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
      filter: ''
    }
  },
  mounted () {},
  computed: {},
  methods: {

    exportTable () {
      return this.$exportDataTableAsCSV()
    },

    isObjectNotEmpty (value) {
      return this.$utils.isObjectNotEmpty(value)
    },

    goToExternaResource (url) {
      openURL(url)
    }

  }
}
</script>
