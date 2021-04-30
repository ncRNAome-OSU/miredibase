<template>
  <q-page padding>
    <span class="text-h5 text-weight-light">Variant details</span>
    <q-separator spaced/>
    <p class="text-justify text-weight-light">
      <helper>
        Click on the red icons to display the variant studies information.
      </helper>
      Here you can explore overview information and the
      list of available studies for the RNA modification site. Thermodynamic and functional predictions are
      also provided (whether available).
    </p>
    <div v-if="$store.state.showcase.renderSearchTabPanels">
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
          <snv-overview-details :study-data="snvDataDetails" />
          <q-separator spaced color="grey-1" />
          <snv-overview :snv-data="snvData" />
        </q-tab-panel>

        <q-tab-panel name="tab2" class="q-pa-xs">
          <snv-thermodynamics :snv-data="snvData" />
        </q-tab-panel>

        <q-tab-panel name="tab3" class="q-pa-xs">
          <snv-prediction :snv-data="snvData" />
        </q-tab-panel>

        <q-tab-panel name="tab4" class="q-pa-xs">
          <snv-enrichment :snv-data="snvData" />
        </q-tab-panel>
      </q-tab-panels>
    </div>
  </q-page>
</template>

<script>
import SnvOverview from 'components/SnvOverview'
import SnvOverviewDetails from 'components/SnvOverviewDetails'
import SnvThermodynamics from 'components/SnvThermodynamics'
import SnvPrediction from 'components/SnvPrediction'
import SnvEnrichment from 'components/SnvEnrichment'
import Helper from 'components/Helper'

export default {
  name: 'Variant',
  components: {
    Helper,
    SnvOverview,
    SnvOverviewDetails,
    SnvThermodynamics,
    SnvPrediction,
    SnvEnrichment
  },
  props: {
    vartype: {
      type: String,
      required: true
    },
    genpos: {
      type: Number,
      required: true
    },
    chrom: {
      type: String,
      required: true
    },
    strand: {
      type: String,
      required: true
    },
    organism: {
      type: String,
      required: true
    }
  },
  data () {
    return {
      isDownloadable: true,
      snvData: {},
      searchTabPanel: 'tab1',
      studyDataBeforePanelSwitch: {},
      snvDataDetails: {}
    }
  },
  created () {},
  mounted () {
    this.renderSnvData()
  },
  computed: {
  },
  methods: {

    isNotNull (value) {
      return this.$utils.isNotNull(value)
    },

    isObjectNotEmpty (value) {
      return this.$utils.isObjectNotEmpty(value)
    },

    objectHasPropery (object, key) {
      return this.$utils.objectHasPropery(object, key)
    },

    renderSnvData () {
      if (this.checkQueryParams()) {
        this.loadSNVData()
      } else {
        this.$q.notify({
          color: 'negative',
          position: 'top',
          message: 'Loading failed. No data available for your request',
          icon: 'report_problem'
        })
      }
    },

    checkQueryParams () {
      if (!this.isObjectNotEmpty(this.vartype)) {
        return false
      }
      if (isNaN(this.genpos)) {
        return false
      }
      if (!this.isObjectNotEmpty(this.chrom)) {
        return false
      }
      if (!this.isObjectNotEmpty(this.strand)) {
        return false
      }
      if (!this.isObjectNotEmpty(this.organism)) {
        return false
      }
      return true
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

    loadSNVData () {
      const payload = {
        organism: this.organism,
        mod_type: this.vartype,
        chromosome: this.chrom,
        strand: this.strand,
        genomic_position: this.genpos
      }

      this.$loadApiData(
        '/organisms/rnaeditingsites/detail/',
        this.setSingleSNVData,
        payload
      )
    }

  }
}
</script>
