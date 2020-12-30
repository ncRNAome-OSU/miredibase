<template>
  <div>

    <studies-table-viewer
      title="RNA modification site studies"
      :data="table.data"
      :columns="table.columns"
      first-columns-header-color="primary"
      row-key="name"
      :is-downloadable="isDownloadable"
    />

    <q-separator spaced />

    <study-details :study-data="$store.state.showcase.dataStudyDetailsTabPanel" />

  </div>
</template>

<script>
import StudiesTableViewer from 'components/StudiesTableViewer'
import StudyDetails from 'components/StudyDetails'

export default {
  name: 'SnvOverview',
  components: {
    StudiesTableViewer,
    StudyDetails
  },
  props: {
    snvData: {
      type: Object,
      default: null
    },
    isDownloadable: {
      type: Boolean,
      default: true
    }
  },
  data () {
    return {
      table: {
        data: [],
        columns: [
          {
            name: 'name',
            required: true,
            label: '',
            align: 'center',
            field: row => row.name,
            sortable: false,
            classes: 'bg-grey-2 ellipsis',
            format: val => `${val}`,
            headerClasses: 'text-white'
          },
          {
            name: 'pubmedID',
            label: 'Pubmed ID',
            field: 'pubmed_id',
            sortable: true,
            align: 'center',
            sort: (a, b, rowA, rowB) => parseInt(a, 10) - parseInt(b, 10)
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
            name: 'reportedEffect',
            label: 'Reported effect(s)',
            field: 'reported_effects',
            sortable: true,
            align: 'center'
          },
          {
            name: 'impairedTargeting',
            label: 'Impaired targeting (gene)',
            field: 'impaired_targeting',
            sortable: true,
            align: 'center',
            style: 'max-width: 50px'
          },
          {
            name: 'targetGaining',
            label: 'Target gaining (gene)',
            field: 'target_gaining',
            sortable: true,
            align: 'center'
          },
          {
            name: 'ngs',
            label: 'NGS',
            field: 'ngs',
            sortable: true,
            align: 'center'
          },
          {
            name: 'miRmmPCRSeq',
            label: 'miR-mmPCR-seq',
            field: 'mir_mmpcr_seq',
            sortable: true,
            align: 'center'
          },
          {
            name: 'ripSeq',
            label: 'RIP-Seq',
            field: 'rip_seq',
            sortable: true,
            align: 'center'
          },
          {
            name: 'enzymeKd',
            label: 'Enzyme KD',
            field: 'enzyme_kd',
            sortable: true,
            align: 'center'
          },
          {
            name: 'enzymeKo',
            label: 'Enzyme KO',
            field: 'enzyme_ko',
            sortable: true,
            align: 'center'
          },
          {
            name: 'differentialTransfection',
            label: 'Differential transfection',
            field: 'differential_transfection',
            sortable: true,
            align: 'center'
          },
          {
            name: 'sangerSequencing',
            label: 'Sanger sequencing',
            field: 'sanger_sequencing',
            sortable: true,
            align: 'center'
          },
          {
            name: 'snapshotAssay',
            label: 'SNaPshot assay',
            field: 'snapshot_assay',
            sortable: true,
            align: 'center'
          },
          {
            name: 'siteSpecificCleavage',
            label: 'Site specific cleavage',
            field: 'site_specific_cleavage',
            sortable: true,
            align: 'center'
          },
          {
            name: 'enzymeSelectivity',
            label: 'Enzyme selectivity',
            field: 'enzyme_selectivity',
            sortable: true,
            align: 'center'
          }
        ]
      }
    }
  },
  mounted () {
    this.setStudiesTableRows(this.snvData)
  },
  computed: {},
  methods: {

    isObjectNotEmpty (value) {
      return this.$utils.isObjectNotEmpty(value)
    },

    setStudiesTableRows (data) {
      this.table.data = []
      if (this.isObjectNotEmpty(data)) {
        data.studies.forEach((item, index) => {
          item.name = index
          this.table.data.push(item)
        })
      }
    }

  },
  watch: {
    snvData: function (newVal, oldVal) {
      this.setStudiesTableRows(newVal)
    }
  }
}
</script>
