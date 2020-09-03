<template>
  <div>
    <div v-if="isObjectNotEmpty(snvData) && isObjectNotEmpty(snvData.mirna) && snvData.prediction" class="text-weight-light">
      <div class="row">
        <div class="col-xs-12 col-sm-12 col-md-12 col-lg-3 q-pr-xs">

          <q-card>
            <q-card-section class="text-justify">
              Target predictions are available for the selected miRNA modification site. You can load the results
              on-demand by clicking on the button below due to a large number of predicted targets.<br /><br />
              <q-btn
                no-caps
                dense
                class="q-px-xs"
                color="primary"
                icon="cloud_download"
                label="Load prediction results"
                @click="loadSNVData()"
              />
            </q-card-section>

            <q-separator spaced />

            <q-card-section>
              MiRNA target predictions were provided by isoTar
              <q-btn
                no-caps
                type="a"
                size="sm"
                dense
                flat
                color="purple"
                label="Explore isoTar"
                @click="goToExternaResource('https://ncrnaome.osumc.edu/isotar/')"
              /><br /><br />

              To generate the displayed miRNA target predictions in isoTar, `copy` the following input (min. consensus: <b>3</b>):<br />
              <pre>
&gt;{{ snvData.mirna }} {{ snvData.stemloop }} {{ snvData.mirna_local_pos }}:A|G
{{ snvData.mirna_seq }}</pre>
            </q-card-section>
          </q-card>
          <br />

        </div>
        <div class="col-xs-12 col-sm-12 col-md-12 col-lg-9 q-pr-xs">

          <div v-show="isLoading" class="flex flex-center q-pt-lg">
            <p class="text-weight-light text-h6">
              <q-spinner-dots
                color="primary"
                size="2em"
                :thickness="2"
              />
              Please wait, miRNA target predictions loading...
            </p>
          </div>

          <div class="row q-pb-md">
            <div class="col-xs-12 col-sm-4 col-md-4 col-lg-4 q-pr-xs">

              <predictions-subset-table-viewer
                title="Wild-type unique targets"
                :data="$store.state.showcase.wtUniqueTargetPredictionData"
                :columns="table.subsetColumns"
                first-columns-header-color="primary"
                row-key="name"
                :is-downloadable="isDownloadable"
                badge-color="light-blue"
                tooltip-text="List of putative target genes for the wild-type miRNA. Results can be ordered by RefSeq ID or Gene name. Click on the purple inscriptions to access external online resources."
              />

            </div>
            <div class="col-xs-12 col-sm-4 col-md-4 col-lg-4 q-pr-xs">

              <predictions-subset-table-viewer
                title="Wild-type/Edited common targets"
                :data="$store.state.showcase.interTargetPredictionData"
                :columns="table.subsetColumns"
                first-columns-header-color="primary"
                row-key="name"
                :is-downloadable="isDownloadable"
                badge-color="green"
                tooltip-text="List of putative target genes shared by both miRNA versions. Results can be ordered by RefSeq ID or Gene name. Click on the purple inscriptions to access external online resources."
              />

            </div>
            <div class="col-xs-12 col-sm-4 col-md-4 col-lg-4 q-pr-xs">

              <predictions-subset-table-viewer
                title="Edited unique targets"
                :data="$store.state.showcase.edUniqueTargetPredictionData"
                :columns="table.subsetColumns"
                first-columns-header-color="primary"
                row-key="name"
                :is-downloadable="isDownloadable"
                badge-color="red"
                tooltip-text="List of putative target genes for the edited miRNA. Results can be ordered by RefSeq ID or Gene name. Click on the purple inscriptions to access external online resources."
              />

            </div>
          </div>

          <predictions-table-viewer
            :title="`${snvData.mirna} (wild-type) target predictions`"
            :data="$store.state.showcase.wtTargetPredictionData"
            :columns="table.columns"
            first-columns-header-color="primary"
            row-key="name"
            :is-downloadable="isDownloadable"
          />

          <q-space class="q-pb-xs"/>

          <predictions-table-viewer
            :title="`${snvData.mirna} (${prettifySnvType(snvData.mod_type)}, position ${snvData.mirna_local_pos}) target predictions`"
            :data="$store.state.showcase.edTargetPredictionData"
            :columns="table.columns"
            first-columns-header-color="primary"
            row-key="name"
            :is-downloadable="isDownloadable"
          />

        </div>
      </div>
    </div>
    <div v-else class="text-weight-light">
      No miRNA target predictions available for the selected RNA Editing site.
    </div>
  </div>
</template>

<script>
import PredictionsTableViewer from 'components/PredictionsTableViewer'
import PredictionsSubsetTableViewer from 'components/PredictionsSubsetTableViewer'
import { openURL } from 'quasar'

export default {
  name: 'SnvPrediction',
  components: {
    PredictionsTableViewer,
    PredictionsSubsetTableViewer
  },
  props: {
    snvData: {
      type: Object,
      default: null
    }
  },
  data () {
    return {
      table: {
        columns: [
          {
            name: 'name',
            required: true,
            label: 'Explore',
            align: 'center',
            field: row => row.name,
            sortable: false,
            classes: 'bg-grey-2 ellipsis',
            format: val => `${val}`,
            headerClasses: 'text-grey-10'
          },
          {
            name: 'refSeq',
            label: 'RefSeq',
            field: 'refseq',
            sortable: true,
            align: 'center'
          },
          {
            name: 'ensemblId',
            label: 'Ensembl ID',
            field: 'ensembl_id',
            sortable: true,
            align: 'center'
          },
          {
            name: 'geneName',
            label: 'Gene name',
            field: 'gene_name',
            sortable: true,
            align: 'center'
          },
          {
            name: 'geneBiotype',
            label: 'Gene biotype',
            field: 'gene_biotype',
            sortable: true,
            align: 'center'
          },
          {
            name: 'miRanda',
            label: 'miRanda',
            field: 'miranda',
            sortable: true,
            align: 'center',
            sort: (a, b, rowA, rowB) => parseInt(a, 10) - parseInt(b, 10)
          },
          {
            name: 'RNAhybrid',
            label: 'RNAhybrid',
            field: 'rnahybrid',
            sortable: true,
            align: 'center',
            sort: (a, b, rowA, rowB) => parseInt(a, 10) - parseInt(b, 10)
          },
          {
            name: 'TargetScan',
            label: 'TargetScan',
            field: 'targetscan',
            sortable: true,
            align: 'center',
            sort: (a, b, rowA, rowB) => parseInt(a, 10) - parseInt(b, 10)
          },
          {
            name: 'PITA',
            label: 'PITA',
            field: 'pita',
            sortable: true,
            align: 'center',
            sort: (a, b, rowA, rowB) => parseInt(a, 10) - parseInt(b, 10)
          },
          {
            name: 'miRmap',
            label: 'miRmap',
            field: 'mirmap',
            sortable: true,
            align: 'center',
            sort: (a, b, rowA, rowB) => parseInt(a, 10) - parseInt(b, 10)
          },
          {
            name: 'Consensus',
            label: 'Consensus',
            field: 'consensus',
            sortable: true,
            align: 'center',
            sort: (a, b, rowA, rowB) => parseInt(a, 10) - parseInt(b, 10)
          }
        ],
        subsetColumns: [
          {
            name: 'name',
            required: true,
            label: 'Explore',
            align: 'left',
            field: row => row.name,
            sortable: false,
            classes: 'bg-grey-2 ellipsis',
            format: val => `${val}`,
            headerClasses: 'text-grey-10'
          },
          {
            name: 'refSeq',
            label: 'RefSeq',
            field: 'refseq',
            sortable: true,
            align: 'center'
          },
          {
            name: 'geneName',
            label: 'Gene name',
            field: 'gene_name',
            sortable: true,
            align: 'center'
          }
        ]
      },
      isLoading: false,
      isDownloadable: true
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
    },

    prettifySnvType (value) {
      return this.$utils.prettifySnvType(value)
    },

    objectHasPropery (object, key) {
      return this.$utils.objectHasPropery(object, key)
    },

    initDataTableRows (data) {
      const keysList = [
        'wildtype', 'edited', 'intersection', 'wildtype_unique', 'edited_unique'
      ]

      keysList.forEach(key => {
        const rows = []
        if (
          this.isObjectNotEmpty(data) &&
          this.objectHasPropery(data, 'target_prediction') &&
          this.objectHasPropery(data.target_prediction, key) &&
          this.isObjectNotEmpty(data.target_prediction[key])
        ) {
          data.target_prediction[key].forEach((item, index) => {
            item.name = index
            rows.push(item)
          })
        }

        switch (key) {
          case 'wildtype':
            this.$store.commit('showcase/updateWildtypeTargetPredictionData', rows)
            break
          case 'edited':
            this.$store.commit('showcase/updateEditedTargetPredictionData', rows)
            break
          case 'wildtype_unique':
            this.$store.commit('showcase/updateWildtypeUniqueTargetPredictionData', rows)
            break
          case 'edited_unique':
            this.$store.commit('showcase/updateEditedUniqueTargetPredictionData', rows)
            break
          case 'intersection':
            this.$store.commit('showcase/updateIntersectionUniqueTargetPredictionData', rows)
            break
          default:
            break
        }
      })
      this.isLoading = false
    },

    loadSNVData () {
      this.$store.commit('showcase/updateWildtypeTargetPredictionData', [])
      this.$store.commit('showcase/updateEditedTargetPredictionData', [])
      this.$store.commit('showcase/updateWildtypeUniqueTargetPredictionData', [])
      this.$store.commit('showcase/updateEditedUniqueTargetPredictionData', [])
      this.$store.commit('showcase/updateIntersectionUniqueTargetPredictionData', [])
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
          '/organisms/rnaeditingsites/predictions/',
          this.initDataTableRows,
          payload
        )
      }
    }
  }
}
</script>
