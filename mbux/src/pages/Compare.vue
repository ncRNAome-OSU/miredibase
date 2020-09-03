<template>
  <q-page padding>

    <!-- content -->
    <compare-form
      @sendSearchResponse="loadResultsData"
    />

    <comparison-results
      :data="table.data"
      :columns="table.columns"
      :visible-columns="table.visibleColumns"
    />

  </q-page>
</template>

<script>
import CompareForm from 'components/CompareForm'
import ComparisonResults from 'components/ComparisonResults'

export default {
  name: 'Search',
  components: {
    CompareForm,
    ComparisonResults
  },
  data () {
    return {
      table: {
        visibleColumns: [
          'name',
          'organism',
          'modType',
          'author',
          'year',
          'pubmedId',
          'stemloop',
          'transcriptRegion',
          'stemloopLocalPos',
          'mirna',
          'mirnaLocalPos',
          'adverseCondition',
          'percEditingInAdverseCondition',
          'normalCondition',
          'percEditingInNormalCondition'
        ],
        data: [],
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
            label: 'RNA Editing type',
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
            name: 'stemloopLocalPos',
            label: 'Local pos.',
            field: 'stemloop_local_pos',
            sortable: true,
            align: 'center',
            sort: (a, b, rowA, rowB) => parseInt(a, 10) - parseInt(b, 10)
          },
          {
            name: 'mirna',
            label: 'miRNA',
            field: 'mirna',
            sortable: true,
            align: 'center'
          },
          {
            name: 'mirnaLocalPos',
            label: 'Local pos. (miRNA)',
            field: 'mirna_local_pos',
            sortable: true,
            align: 'center',
            sort: (a, b, rowA, rowB) => parseInt(a, 10) - parseInt(b, 10)
          },
          {
            name: 'normalCondition',
            label: 'Biological source',
            field: 'normal_condition',
            sortable: true,
            align: 'center'
          },
          {
            name: 'percEditingInNormalCondition',
            label: 'Avg. (%) Editing Level',
            field: 'perc_editing_in_normal_condition',
            sortable: true,
            align: 'center',
            format: val => `${val.toFixed(2)}`,
            sort: (a, b, rowA, rowB) => parseFloat(a) - parseFloat(b)
          },
          {
            name: 'adverseCondition',
            label: 'Biological source',
            field: 'adverse_condition',
            sortable: true,
            align: 'center'
          },
          {
            name: 'percEditingInAdverseCondition',
            label: 'Avg. (%) Editing Level',
            field: 'perc_editing_in_adverse_condition',
            sortable: true,
            align: 'center',
            format: val => `${val.toFixed(2)}`,
            sort: (a, b, rowA, rowB) => parseFloat(a) - parseFloat(b)
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

    setSnvsTableRows (data) {
      this.table.data = []
      if (this.isObjectNotEmpty(data)) {
        data.forEach((item, index) => {
          const pElAdv = item.physiological_pathological_condition.pathological_vs_physiological_comparison.avg_perc_editing_in_adverse
          const pElNor = item.physiological_pathological_condition.pathological_vs_physiological_comparison.avg_perc_editing_in_normal
          item.name = index
          item.perc_el_adverse_style = pElAdv > pElNor ? 'text-weight-bold text-deep-orange' : ''
          item.perc_el_normal_style = pElNor > pElAdv ? 'text-weight-bold text-deep-orange' : ''
          item.adverse_condition = item.physiological_pathological_condition.biological_source
          item.perc_editing_in_adverse_condition = pElAdv
          item.normal_condition = item.physiological_pathological_condition.pathological_vs_physiological_comparison.compared_with
          item.perc_editing_in_normal_condition = pElNor
          this.table.data.push(item)
        })
      }
    },

    loadResultsData (data) {
      if (this.isObjectNotEmpty(data)) {
        this.$loadApiData(
          '/organisms/comparison/',
          this.setSnvsTableRows,
          data
        )
      } else {
        this.table.data = []
      }
    }

  }
}
</script>
