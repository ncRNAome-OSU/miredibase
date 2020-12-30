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
          <q-th rowspan="2" colspan="4"></q-th>
          <q-th rowspan="2" colspan="3" class="bg-light-blue-9 text-white">
            Functional consequences
          </q-th>
          <q-th colspan="9" class="bg-teal-10 text-white">
            Detection methods
          </q-th>
        </q-tr>
        <q-tr>
          <q-th colspan="3" class="bg-teal-4">
            High throughput
          </q-th>
          <q-th colspan="3" class="bg-teal-7 text-white">
            Enzyme perturbation
          </q-th>
          <q-th colspan="3" class="bg-teal-10 text-white">
            Targeted detection methods
          </q-th>
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
          <q-th key="reportedEffect" :props="props" class="bg-light-blue-5 text-white text-center">
            Reported&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<br>effect(s)
          </q-th>
          <q-th key="impairedTargeting" :props="props" class="bg-light-blue-7 text-white text-center">
            Impaired&nbsp;&nbsp;&nbsp;<br>targeting&nbsp;&nbsp;<br>(gene)
          </q-th>
          <q-th key="targetGaining" :props="props" class="bg-light-blue-9 text-white text-center">
            Target&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<br>gaining&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<br>(gene)
          </q-th>
          <q-th key="ngs" :props="props" class="text-left bg-teal-2">
            NGS
          </q-th>
          <q-th key="miRmmPCRSeq" :props="props" class="text-left bg-teal-3">
            miR-mmPCR-seq
          </q-th>
          <q-th key="ripSeq" :props="props" class="text-left bg-teal-4">
            RIP-Seq
          </q-th>
          <q-th key="enzymeKd" :props="props" class="text-left bg-teal-5 text-white">
            Enzyme<br>KD
          </q-th>
          <q-th key="enzymeKo" :props="props" class="text-left bg-teal-6 text-white">
            Enzyme<br>KO
          </q-th>
          <q-th key="differentialTransfection" :props="props" class="text-left bg-teal-7 text-white">
            Differential<br>transfection
          </q-th>
          <q-th key="sangerSequencing" :props="props" class="text-left bg-teal-8 text-white">
            Sanger<br>sequencing
          </q-th>
          <q-th key="snapshotAssay" :props="props" class="text-left bg-teal-9 text-white">
            SNaPshot<br>assay
          </q-th>
          <q-th key="siteSpecificCleavage" :props="props" class="text-left bg-teal-10 text-white">
            Site specific<br>cleavage
          </q-th>
          <q-th key="enzymeSelectivity" :props="props" class="text-center">
            Enzyme&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<br>selectivity
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

      <q-td slot="body-cell-ngs" slot-scope="props" :props="props">
        {{ props.row.site_specific_detection_methods.ngs }}
      </q-td>

      <q-td slot="body-cell-miRmmPCRSeq" slot-scope="props" :props="props">
        {{ props.row.site_specific_detection_methods.mir_mmpcr_seq }}
      </q-td>

      <q-td slot="body-cell-ripSeq" slot-scope="props" :props="props">
        {{ props.row.site_specific_detection_methods.rip_seq }}
      </q-td>

      <q-td slot="body-cell-enzymeKd" slot-scope="props" :props="props">
        {{ props.row.enzyme_perturbation.enzyme_kd }}
      </q-td>

      <q-td slot="body-cell-enzymeKo" slot-scope="props" :props="props">
        {{ props.row.enzyme_perturbation.enzyme_ko }}
      </q-td>

      <q-td slot="body-cell-differentialTransfection" slot-scope="props" :props="props">
        {{ props.row.enzyme_perturbation.differential_transfection }}
      </q-td>

      <q-td slot="body-cell-sangerSequencing" slot-scope="props" :props="props">
        {{ props.row.targeted_detection_methods.sanger_sequencing }}
      </q-td>

      <q-td slot="body-cell-snapshotAssay" slot-scope="props" :props="props">
        {{ props.row.targeted_detection_methods.snapshot_assay }}
      </q-td>

      <q-td slot="body-cell-siteSpecificCleavage" slot-scope="props" :props="props">
        {{ props.row.targeted_detection_methods.site_specific_cleavage }}
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
