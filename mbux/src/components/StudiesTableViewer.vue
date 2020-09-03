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
          <q-th colspan="4"></q-th>
          <q-th colspan="3" class="bg-light-blue-9 text-white">
            Functional consequences
          </q-th>
          <q-th colspan="1"></q-th>
        </q-tr>
        <q-tr>
          <q-th key="name" :props="props">
            <helper>
              Click on the left-sided red icons to display detailed information for each listed study.
              Click on the purple inscriptions to access external resources.
            </helper>
          </q-th>
          <q-th
            key="pubmedID" :props="props">
            Pubmed ID
          </q-th>
          <q-th key="author" :props="props">
            Author(s)
          </q-th>
          <q-th key="year" :props="props">
            Year
          </q-th>
          <q-th key="reportedEffect" :props="props" class="bg-light-blue-5 text-white">
            Reported effect(s)
          </q-th>
          <q-th key="impairedTargeting" :props="props" class="bg-light-blue-7 text-white">
            Impaired targeting (gene)
          </q-th>
          <q-th key="targetGaining" :props="props" class="bg-light-blue-9 text-white">
            Target gaining (gene)
          </q-th>
          <q-th key="enzymeSelectivity" :props="props">
            Enzyme selectivity
          </q-th>
        </q-tr>
      </template>

      <q-td slot="body-cell-name" slot-scope="props" :props="props">
        <q-btn
          round
          size="sm"
          color="red-7"
          icon="view_headline"
          @click="loadStudyDetails(props.value)"
        >
        </q-btn>
      </q-td>

      <q-td slot="body-cell-pubmedID" slot-scope="props" :props="props">
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
import Helper from 'components/Helper'

export default {
  name: 'StudiesTableViewer',
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
    },

    loadStudyDetails (idx) {
      this.$store.commit('showcase/updateDataStudyDetailsTabPanel', this.data[idx])
    }

  }
}
</script>
