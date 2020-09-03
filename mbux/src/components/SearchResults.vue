<template>
  <q-page>
    <div v-if="isObjectNotEmpty(data)">
      <div class="row">
        <div class="col-xs-12 col-sm-12 col-md-12 col-lg-9 q-pa-xs">
          <p class="text-justify text-weight-light">
            <helper>
              Click on the red icons to display summary tables.
            </helper>
            Here you can explore overview information and the
            list of available studies for each RNA modification site. Thermodynamic and functional predictions are
            also provided (whether available).
          </p>

          <table-viewer
            title="RNA modification sites"
            :data="data"
            :columns="columns"
            first-columns-header-color="primary"
            row-key="name"
            :is-downloadable="isDownloadable"
            @loadSNVData="loadSNVData($event)"
            :visible-columns="visibleColumns"
          />

        </div>
        <div class="col-xs-12 col-sm-12 col-md-12 col-lg-3 q-pa-xs">
          <div v-if="$store.state.showcase.renderSearchTabPanels">
            <snv-overview-details :study-data="snvDataDetails" />
          </div>
        </div>
      </div>

      <div v-if="$store.state.showcase.renderSearchTabPanels">
        <q-separator spaced />
        <q-option-group
          v-model="searchTabPanel"
          inline
          :options="[
            { label: 'Overview', value: 'tab1' },
            { label: 'Thermodynamics in Secondary Structure', value: 'tab2' },
            { label: 'miRNA-Target Prediction (isoTar)', value: 'tab3' },
            { label: 'Functional Enrichment (isoTar)', value: 'tab4' }
          ]"
        />
        <q-tab-panels
          v-model="searchTabPanel"
          class="bg-grey-1 no-shadow"
        >
          <q-tab-panel name="tab1" class="q-pa-xs">
            <q-space />
            <snv-overview :snv-data="snvData" />
          </q-tab-panel>

          <q-tab-panel name="tab2" class="q-pa-xs">
            <q-space />
            <snv-thermodynamics :snv-data="snvData" />
          </q-tab-panel>

          <q-tab-panel name="tab3" class="q-pa-xs">
            <q-space />
            <snv-prediction :snv-data="snvData" />
          </q-tab-panel>

          <q-tab-panel name="tab4" class="q-pa-xs">
            <q-space />
            <snv-enrichment :snv-data="snvData" />
          </q-tab-panel>
        </q-tab-panels>
      </div>

    </div>
  </q-page>
</template>

<script>
import TableViewer from 'components/TableViewer'
import SnvOverview from 'components/SnvOverview'
import SnvOverviewDetails from 'components/SnvOverviewDetails'
import SnvThermodynamics from 'components/SnvThermodynamics'
import SnvPrediction from 'components/SnvPrediction'
import SnvEnrichment from 'components/SnvEnrichment'
import Helper from 'components/Helper'

export default {
  name: 'SearchResults',
  components: {
    TableViewer,
    SnvOverview,
    SnvOverviewDetails,
    SnvThermodynamics,
    SnvPrediction,
    SnvEnrichment,
    Helper
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
      snvData: {},
      searchTabPanel: 'tab1',
      studyDataBeforePanelSwitch: {},
      svnDataDetailsLabelsOrdering: [
        'organism',
        'mod_type',
        'chromosome',
        'strand',
        'genomic_position',
        'stemloop',
        'stemloop_local_pos',
        'mirna',
        'mirna_local_pos'
      ],
      snvDataDetails: {}
    }
  },
  mounted () {},
  computed: {},
  methods: {

    isObjectNotEmpty (value) {
      return this.$utils.isObjectNotEmpty(value)
    },

    isNotNull (value) {
      return this.$utils.isNotNull(value)
    },

    setSingleSNVData (data) {
      if (this.isObjectNotEmpty(data)) {
        this.snvData = data
        this.snvDataDetails = data
        this.searchTabPanel = 'tab1'
        this.$store.commit('showcase/updateSearchTabPanels', true)
        this.$store.commit('showcase/updateDataStudyDetailsTabPanel', {})
        this.$store.commit('showcase/updateWildtypeTargetPredictionData', [])
        this.$store.commit('showcase/updateEditedTargetPredictionData', [])
        this.$store.commit('showcase/updateWildtypeUniqueTargetPredictionData', [])
        this.$store.commit('showcase/updateEditedUniqueTargetPredictionData', [])
        this.$store.commit('showcase/updateIntersectionUniqueTargetPredictionData', [])
        this.$store.commit('showcase/updateTargetEnrichmentData', {})
      }
    },

    loadSNVData (event) {
      if (this.isObjectNotEmpty(event)) {
        const payload = {
          organism: event.organism,
          mod_type: event.mod_type,
          chromosome: event.chromosome,
          strand: event.strand,
          genomic_position: event.genomic_position
        }

        if (this.isNotNull(this.$store.state.showcase.filterByBiologicalSources)) {
          payload.biological_source = this.$store.state.showcase.filterByBiologicalSources
        }
        this.$loadApiData(
          '/organisms/rnaeditingsites/detail/',
          this.setSingleSNVData,
          payload
        )
      }
    }

  }
}
</script>