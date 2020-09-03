<template>
  <div class="q-gutter-xs">
    <div v-if="isObjectNotEmpty(snvData) && isObjectNotEmpty(snvData.mirna) && snvData.enrichment" class="text-weight-light">
      <q-card class="q-mb-lg">
        <q-card-section horizontal>
          <q-card-section class="flex flex-center">
            <q-btn
              style="width: 200px"
              no-caps
              dense
              class="q-px-xs"
              color="primary"
              icon="cloud_download"
              label="Load enrichment results"
              @click="loadSNVData()"
            />
          </q-card-section>

          <q-separator spaced inset vertical />

          <q-card-section>
            Target enrichment is available for the selected miRNA modification site. You can load the results
            on-demand by clicking on the left-placed button due to a large number of enriched targets.<br>
            MiRNA target enrichment were provided by isoTar
            <q-btn
              no-caps
              type="a"
              size="sm"
              dense
              flat
              color="purple"
              label="Explore isoTar"
              @click="goToExternaResource('https://ncrnaome.osumc.edu/isotar/')"
            />
          </q-card-section>

        </q-card-section>
      </q-card>

      <div v-show="isLoading" class="flex flex-center q-pt-lg">
        <p class="text-weight-light text-h6">
          <q-spinner-dots
            color="primary"
            size="2em"
            :thickness="2"
          />
          Please wait, miRNA target enrichment loading...
        </p>
      </div>

      <enrichment-viewer
        :snv-data="$store.state.showcase.targetEnrichmentData"
      />

    </div>
    <div v-else class="text-weight-light">
      No miRNA target enrichment available for the selected RNA Editing site.
    </div>
  </div>
</template>

<script>
import EnrichmentViewer from 'components/EnrichmentViewer'
import { openURL } from 'quasar'

export default {
  name: 'SnvEnrichment',
  components: {
    EnrichmentViewer
  },
  props: {
    snvData: {
      type: Object,
      default: null
    }
  },
  data () {
    return {
      isLoading: false
    }
  },
  mounted () {},
  computed: {},
  methods: {

    isObjectNotEmpty (value) {
      return this.$utils.isObjectNotEmpty(value)
    },

    goToExternaResource (url) {
      openURL(url)
    },

    loadSNVData () {
      this.$store.commit('showcase/updateTargetEnrichmentData', {})
      if (this.isObjectNotEmpty(this.snvData)) {
        this.isLoading = true
        const payload = {
          organism: this.snvData.organism,
          mod_type: this.snvData.mod_type,
          chromosome: this.snvData.chromosome,
          strand: this.snvData.strand,
          genomic_position: this.snvData.genomic_position
        }
        this.$loadApiData(
          '/organisms/rnaeditingsites/enrichment/',
          this.initEnrichmentData,
          payload
        )
      }
    },

    initEnrichmentData (data) {
      if (this.isObjectNotEmpty(data) &&
        this.isObjectNotEmpty(data.target_enrichment)) {
        this.$store.commit('showcase/updateTargetEnrichmentData', data)
      }
      this.isLoading = false
    }

  }
}
</script>
