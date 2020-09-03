<template>
  <q-page padding>

    <!-- content -->
    <search-form
      @sendSearchResponse="loadResultsData"
    />

    <search-results
      :data="table.data"
      :columns="table.columns"
      :visible-columns="table.visibleColumns"
    />

  </q-page>
</template>

<script>
import SearchForm from 'components/SearchForm'
import SearchResults from 'components/SearchResults'

export default {
  name: 'Search',
  components: {
    SearchForm,
    SearchResults
  },
  data () {
    return {
      table: {
        visibleColumns: [
          'name',
          'organism',
          'modType',
          'chromosome',
          'strand',
          'genomicPosition',
          'stemloop',
          'transcriptRegion',
          'stemloopRegionInvolved',
          'stemloopLocalPos',
          'mirnaLocalPos'
        ],
        data: [],
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
            name: 'organism',
            label: 'Organism',
            field: 'organism',
            sortable: true,
            align: 'center'
          },
          {
            name: 'modType',
            label: 'RNA Editing type',
            field: 'mod_type',
            sortable: true,
            align: 'center'
          },
          {
            name: 'chromosome',
            label: 'Chromosome',
            field: 'chromosome',
            sortable: true,
            align: 'center'
          },
          {
            name: 'strand',
            label: 'DNA Strand',
            field: 'strand',
            sortable: true,
            align: 'center'
          },
          {
            name: 'genomicPosition',
            label: 'Genomic position',
            field: 'genomic_position',
            sortable: true,
            align: 'center',
            sort: (a, b, rowA, rowB) => parseInt(a, 10) - parseInt(b, 10)
          },
          {
            name: 'stemloop',
            label: 'Name',
            field: 'stemloop',
            sortable: true,
            align: 'center'
          },
          {
            name: 'stemloopAccNumber',
            label: 'Accession N.',
            field: 'stemloop_acc_number',
            align: 'center'
          },
          {
            name: 'transcriptRegion',
            label: 'Transcript region',
            field: 'transcript_region',
            sortable: true,
            align: 'center'
          },
          {
            name: 'stemloopRegionInvolved',
            label: 'Region involved',
            field: 'stemloop_region_involved',
            sortable: true,
            align: 'center'
          },
          {
            name: 'stemloopLocalPos',
            label: 'Local pos.',
            field: 'stemloop_local_pos',
            sortable: true,
            align: 'center',
            sort: (a, b, rowA, rowB) => parseInt(a, 10) - parseInt(b, 10)
          },
          {
            name: 'mirnaLocalPos',
            label: 'Local pos. (miRNA)',
            field: 'mirna_local_pos',
            sortable: true,
            align: 'center',
            sort: (a, b, rowA, rowB) => parseInt(a, 10) - parseInt(b, 10)
          }
        ]
      }
    }
  },
  created () {},
  mounted () {},
  computed: {},
  methods: {

    isObjectNotEmpty (value) {
      return this.$utils.isObjectNotEmpty(value)
    },

    objectHasPropery (object, key) {
      return this.$utils.objectHasPropery(object, key)
    },

    setSnvsTableRows (data) {
      this.table.data = []
      if (this.isObjectNotEmpty(data)) {
        data.forEach((item, index) => {
          item.name = index
          this.table.data.push(item)
        })
      }
      this.$store.commit('showcase/updateSearchTabPanels', false)
      this.$store.commit('showcase/updateDataStudyDetailsTabPanel', {})
      this.$store.commit('showcase/updateWildtypeTargetPredictionData', [])
      this.$store.commit('showcase/updateEditedTargetPredictionData', [])
      this.$store.commit('showcase/updateWildtypeUniqueTargetPredictionData', [])
      this.$store.commit('showcase/updateEditedUniqueTargetPredictionData', [])
      this.$store.commit('showcase/updateIntersectionUniqueTargetPredictionData', [])
    },

    loadResultsData (data) {
      if (this.isObjectNotEmpty(data)) {
        this.$loadApiData(
          '/organisms/rnaeditingsites/',
          this.setSnvsTableRows,
          data
        )

        if (this.objectHasPropery(data, 'biological_source')) {
          this.$store.commit('showcase/updateFilterByBiologicalSource', data.biological_source)
        }
      } else {
        this.table.data = []
      }
    }

  }
}
</script>
