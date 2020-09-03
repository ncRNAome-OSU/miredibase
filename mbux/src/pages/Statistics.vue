<template>
  <q-page padding>
    <!-- content -->
    <p class="text-h5 text-weight-light">Statistics</p>
    <q-separator spaced />
    <p class="text-weight-light text-justify">
      Descriptive statistics concerning the current version of MiREDiBase.
    </p>
    <q-card>
      <q-tabs
        v-model="panel"
        dense
        class="text-grey"
        active-color="primary"
        indicator-color="primary"
        align="justify"
        narrow-indicator
      >
        <q-tab no-caps name="humanTab" label="Human" />
        <q-tab no-caps name="chimpanzeeTab" label="Chimpanzee" />
        <q-tab no-caps name="gorillaTab" label="Gorilla" />
        <q-tab no-caps name="macaqueTab" label="Macaque" />
      </q-tabs>

      <q-separator />

      <q-tab-panels v-model="panel" animated>

        <q-tab-panel name="humanTab">
          <div class="row">
            <div class="col-xs-12 col-sm-12 col-md-6 col-lg-6 flex flex-center text-weight-light text-justify q-pa-lg">
              <q-img
                class="shadow-none"
                src="statistics/human_fig1.png"
                style="max-width: 400px"
              />
            </div>
            <div class="col-xs-12 col-sm-12 col-md-6 col-lg-6 flex flex-center text-weight-light text-justify q-pa-lg">
              <p>
                Distribution of A-to-I and C-to-U editing events per chromosome in the human genome.
                The numbers in brackets represent the number of edited miRNA transcripts per chromosome.
              </p>
              <q-img
                class="shadow-none"
                src="statistics/human_fig2.png"
              />
            </div>
          </div>

          <q-separator spaced />

          <div class="row">
            <div class="col-xs-12 col-sm-12 col-md-6 col-lg-6 flex flex-center text-weight-light text-justify q-pa-lg">
              <p>
                Distribution of A-to-I editing events across the three different regions of primary miRNA
                transcripts and distribution of editing sites falling into mature miRNAs across nucleotide
                positions. Editing sites falling in positions 24-27 were not shown in the mature sequence.
              </p>
              <q-img
                class="shadow-none"
                src="statistics/human_fig3.png"
              />
            </div>
            <div class="col-xs-12 col-sm-12 col-md-6 col-lg-6 flex flex-center text-weight-light text-justify q-pa-lg">
              <p>
                Distribution of C-to-U editing events across the three different regions of primary miRNA
                transcripts and distribution of editing sites falling into mature miRNAs across nucleotide
                positions. Editing sites falling in positions 24-27 were not shown in the mature sequence.
              </p>
              <q-img
                class="shadow-none"
                src="statistics/human_fig4.png"
              />
            </div>
          </div>

          <q-separator spaced />

          <div class="row">
            <div class="col-xs-12 col-sm-12 col-md-6 col-lg-6 flex flex-center text-weight-light text-justify q-pa-lg">
              <p>
                Fraction of functionally characterized A-to-I editing events in miRNAs.
              </p>
              <q-img
                class="shadow-none"
                src="statistics/human_fig5.png"
              />
            </div>
            <div class="col-xs-12 col-sm-12 col-md-6 col-lg-6 flex flex-center text-weight-light text-justify q-pa-lg">
              <p>
                Fraction of functionally characterized C-to-U editing events in miRNAs.
              </p>
              <q-img
                class="shadow-none"
                src="statistics/human_fig6.png"
              />
            </div>
          </div>

          <q-separator spaced />

          <div class="row">
            <div class="col-xs-12 col-sm-12 col-md-6 col-lg-6 flex flex-center text-weight-light text-justify q-pa-lg">
              Total number of adverse conditions, normal conditions and cell lines currently included in MiREDiBase.
              <q-img
                class="shadow-none"
                src="statistics/human_fig7.png"
                style="max-width: 600px"
              />
            </div>
            <div class="col-xs-12 col-sm-12 col-md-6 col-lg-6 text-weight-light text-justify q-pa-lg">
              <p class="text-center">
                Studies employed to build up the MiREDiBase database (no. studies: <span class="text-bold">{{ table.human.count }}</span>).
              </p>
              <statistics-studies-table-viewer
                title="Studies"
                :data="table.human.data"
                :columns="table.columns"
                first-columns-header-color="primary"
                row-key="name"
                :is-downloadable="table.isDownloadable"
              />
            </div>
          </div>

        </q-tab-panel>

        <q-tab-panel name="chimpanzeeTab">

          <div class="row">
            <div class="col-xs-12 col-sm-12 col-md-6 col-lg-6 flex flex-center text-weight-light text-justify q-pa-lg">
              <p>
                Distribution of A-to-I and C-to-U editing events per chromosome in the chimpanzee genome.
                The numbers in brackets represent the number of edited miRNA transcripts per chromosome.
              </p>
              <q-img
                class="shadow-none"
                src="statistics/chimpanzee_fig1.png"
              />
            </div>
            <div class="col-xs-12 col-sm-12 col-md-6 col-lg-6 text-weight-light text-justify q-pa-lg">
              <p>
                Distribution of A-to-I editing events across the three different regions of primary miRNA transcripts
                and distribution of editing sites falling into mature miRNAs across nucleotide positions.
                Editing sites falling in positions 24-27 were not shown in the mature sequence.
              </p>
              <center>
                <q-img
                  class="shadow-none"
                  src="statistics/chimpanzee_fig2.png"
                  style="max-width: 500px"
                />
              </center>
              <p>
                Total number of adverse conditions, normal conditions and cell lines currently included in MiREDiBase.
              </p>
              <center>
                <q-img
                  class="shadow-none"
                  src="statistics/chimpanzee_fig3.png"
                  style="max-width: 500px"
                />
              </center>
            </div>
          </div>

          <q-separator spaced />

          <div class="row">
            <div class="col-xs-12 col-sm-12 col-md-6 col-lg-6 text-weight-light text-justify q-pa-lg">
              <p>
                Studies employed to build up the MiREDiBase database (no. studies: <span class="text-bold">{{ table.chimpanzee.count }}</span>).
              </p>
              <statistics-studies-table-viewer
                title="Studies"
                :data="table.chimpanzee.data"
                :columns="table.columns"
                first-columns-header-color="primary"
                row-key="name"
                :is-downloadable="table.isDownloadable"
              />
            </div>
          </div>

        </q-tab-panel>

        <q-tab-panel name="gorillaTab">

          <div class="row">
            <div class="col-xs-12 col-sm-12 col-md-6 col-lg-6 flex flex-center text-weight-light text-justify q-pa-lg">
              <p>
                Distribution of A-to-I and C-to-U editing events per chromosome in the gorilla genome.
                The numbers in brackets represent the number of edited miRNA transcripts per chromosome.
              </p>
              <q-img
                class="shadow-none"
                src="statistics/gorilla_fig1.png"
              />
            </div>
            <div class="col-xs-12 col-sm-12 col-md-6 col-lg-6 text-weight-light text-justify q-pa-lg">
              <p>
                Distribution of A-to-I editing events across the three different regions of primary miRNA transcripts
                and distribution of editing sites falling into mature miRNAs across nucleotide positions.
                Editing sites falling in positions 24-27 were not shown in the mature sequence.
              </p>
              <center>
                <q-img
                  class="shadow-none"
                  src="statistics/gorilla_fig2.png"
                  style="max-width: 500px"
                />
              </center>
              <p>
                Total number of adverse conditions, normal conditions and cell lines currently included in MiREDiBase.
              </p>
              <center>
                <q-img
                  class="shadow-none"
                  src="statistics/gorilla_fig3.png"
                  style="max-width: 500px"
                />
              </center>
            </div>
          </div>

          <q-separator spaced />

          <div class="row">
            <div class="col-xs-12 col-sm-12 col-md-6 col-lg-6 text-weight-light text-justify q-pa-lg">
              <p>
                Studies employed to build up the MiREDiBase database (no. studies: <span class="text-bold">{{ table.gorilla.count }}</span>).
              </p>
              <statistics-studies-table-viewer
                title="Studies"
                :data="table.gorilla.data"
                :columns="table.columns"
                first-columns-header-color="primary"
                row-key="name"
                :is-downloadable="table.isDownloadable"
              />
            </div>
          </div>

        </q-tab-panel>

        <q-tab-panel name="macaqueTab">

          <div class="row">
            <div class="col-xs-12 col-sm-12 col-md-6 col-lg-6 flex flex-center text-weight-light text-justify q-pa-lg">
              <q-img
                class="shadow-none"
                src="statistics/macaque_fig1.png"
                style="max-width: 400px"
              />
            </div>
            <div class="col-xs-12 col-sm-12 col-md-6 col-lg-6 flex flex-center text-weight-light text-justify q-pa-lg">
              <p>
                Distribution of A-to-I and C-to-U editing events per chromosome in the macaque genome.
                The numbers in brackets represent the number of edited miRNA transcripts per chromosome.
              </p>
              <q-img
                class="shadow-none"
                src="statistics/macaque_fig2.png"
              />
            </div>
          </div>

          <q-separator spaced />

          <div class="row">
            <div class="col-xs-12 col-sm-12 col-md-6 col-lg-6 flex flex-center text-weight-light text-justify q-pa-lg">
              <p>
                Distribution of A-to-I editing events across the three different regions of primary miRNA
                transcripts and distribution of editing sites falling into mature miRNAs across nucleotide
                positions. Editing sites falling in positions 24-27 were not shown in the mature sequence.
              </p>
              <q-img
                class="shadow-none"
                src="statistics/macaque_fig3.png"
              />
            </div>
            <div class="col-xs-12 col-sm-12 col-md-6 col-lg-6 flex flex-center text-weight-light text-justify q-pa-lg">
              <p>
                Distribution of C-to-U editing events across the three different regions of primary miRNA
                transcripts and distribution of editing sites falling into mature miRNAs across nucleotide
                positions. Editing sites falling in positions 24-27 were not shown in the mature sequence.
              </p>
              <q-img
                class="shadow-none"
                src="statistics/macaque_fig4.png"
              />
            </div>
          </div>

          <q-separator spaced />

          <div class="row">
            <div class="col-xs-12 col-sm-12 col-md-6 col-lg-6 flex flex-center text-weight-light text-justify q-pa-lg">
              <p>
                Total number of adverse conditions, normal conditions and cell lines currently included in MiREDiBase.
              </p>
              <q-img
                class="shadow-none"
                src="statistics/macaque_fig5.png"
                style="max-width: 600px"
              />
            </div>
            <div class="col-xs-12 col-sm-12 col-md-6 col-lg-6 text-weight-light text-justify q-pa-lg">
              <p class="text-center">
                Studies employed to build up the MiREDiBase database (no. studies: <span class="text-bold">{{ table.macaque.count }}</span>).
              </p>
              <statistics-studies-table-viewer
                title="Studies"
                :data="table.macaque.data"
                :columns="table.columns"
                first-columns-header-color="primary"
                row-key="name"
                :is-downloadable="table.isDownloadable"
              />
            </div>
          </div>

        </q-tab-panel>

      </q-tab-panels>
    </q-card>

  </q-page>
</template>

<script>
import StatisticsStudiesTableViewer from 'components/StatisticsStudiesTableViewer'
export default {
  name: 'Statistics',
  components: {
    StatisticsStudiesTableViewer
  },
  data () {
    return {
      panel: 'humanTab',
      organisms: ['human', 'chimpanzee', 'gorilla', 'macaque'],
      table: {
        isDownloadable: true,
        human: {
          data: [],
          count: 0
        },
        chimpanzee: {
          data: [],
          count: 0
        },
        gorilla: {
          data: [],
          count: 0
        },
        macaque: {
          data: [],
          count: 0
        },
        columns: [
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
            name: 'organism',
            label: 'Organism',
            field: 'organism',
            sortable: true,
            align: 'center'
          },
          {
            name: 'modType',
            label: 'RNA modification type',
            field: 'mod_type',
            sortable: true,
            align: 'center'
          },
          {
            name: 'author',
            label: 'Author(s)',
            field: 'author',
            sortable: true,
            align: 'center'
          },
          {
            name: 'year',
            label: 'Year',
            field: 'year',
            sortable: true,
            align: 'center',
            sort: (a, b, rowA, rowB) => parseInt(a, 10) - parseInt(b, 10)
          },
          {
            name: 'pubmedId',
            label: 'Pubmed ID',
            field: 'pubmed_id',
            sortable: true,
            align: 'center',
            sort: (a, b, rowA, rowB) => parseInt(a, 10) - parseInt(b, 10)
          }
        ]
      }
    }
  },
  mounted () {
    this.loadOrganismsStudies()
  },
  methods: {

    isObjectNotEmpty (value) {
      return this.$utils.isObjectNotEmpty(value)
    },

    // Handle the mirna select box options
    formatOrganismDataTable (data) {
      if (this.isObjectNotEmpty(data)) {
        const pubmedIdsList = []
        let organism = ''
        data.forEach((item, index) => {
          organism = item.organism
          item.name = index
          this.table[item.organism].data.push(item)
          pubmedIdsList.push(item.pubmed_id)
        })
        this.table[organism].count = Array.from(new Set(pubmedIdsList)).length
      }
    },

    loadOrganismsStudies () {
      this.organisms.forEach(e => {
        const payload = {
          organism: e
        }
        this.$loadApiData(
          '/studies/',
          this.formatOrganismDataTable,
          payload
        )
      })
    }

  }
}
</script>
