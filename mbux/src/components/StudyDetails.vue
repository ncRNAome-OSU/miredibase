<template>
  <q-card
    v-if="isObjectNotEmpty(studyData)"
  >
    <q-card-section class="q-pa-lg">
      <div class="text-h6 text-weight-light">
        Additional info for this study (Pubmed ID: <b>{{ pubmedId }}</b>)
      </div>

      <q-separator spaced />
      <span class="text-weight-light text-justify">
        Find detailed information about biological sources, experiment type, detection/validation methods,
        comparisons between normal and adverse conditions, and editing levels. Information on techniques
        for functional characterization is related to edited mature miRNAs only.
      </span>
    </q-card-section>
    <q-card-section class="q-pa-none">
      <q-table
        dense
        flat
        :title="table.title"
        :data="data"
        :columns="columns"
        :color="table.firstColumnsHeaderColor"
        :row-key="table.rowKey"
        :filter="table.filter"
      >
        <template v-slot:top-right>
          <q-input
            size="xs"
            outlined
            rounded
            dense
            debounce="300"
            v-model="table.filter"
            placeholder="Search within the table"
          >
            <template v-slot:append>
              <q-icon name="search" />
            </template>
          </q-input>
          <q-btn class="q-ml-md" v-if="table.isDownloadable"
            color="orange-9"
            icon-right="archive"
            label="Export to .CSV"
            no-caps
            @click="exportTable"
          />
        </template>

        <template slot="header" slot-scope="props" :props="props" style="display: contents">
          <q-tr>
            <q-th colspan="1"></q-th>
            <q-th colspan="3" class="bg-blue-grey-9 text-white">
              Physiological/pathological condition
            </q-th>
            <q-th colspan="3" class="bg-light-blue-9 text-white">
              Experiment types in this study
            </q-th>
            <q-th colspan="2" class="bg-amber-9 text-white">
              Editing in pri-miRNA (%)
            </q-th>
            <q-th colspan="2" class="bg-orange-9 text-white">
              Editing in pre-miRNA (%)
            </q-th>
            <q-th colspan="2" class="bg-deep-orange-9 text-white">
              Editing in miRNA (%)
            </q-th>
            <q-th colspan="1" class="bg-lime-9 text-white">
              Adverse condition
            </q-th>
          </q-tr>
          <q-tr>
            <q-th key="name" :props="props">#</q-th>
            <q-th
              key="biologicalSource" :props="props" class="bg-blue-grey-7 text-white">
              Biological<br/>Source
            </q-th>
            <q-th key="origin" :props="props" class="bg-blue-grey-8 text-white">
              Origin
            </q-th>
            <q-th key="condition" :props="props" class="bg-blue-grey-9 text-white">
              Condition
            </q-th>
            <q-th key="inVitro" :props="props" class="bg-light-blue-3 text-grey-9">
              In vitro
            </q-th>
            <q-th key="exVivo" :props="props" class="bg-light-blue-6 text-white">
              Ex vivo
            </q-th>
            <q-th key="inVivo" :props="props" class="bg-light-blue-9 text-white">
              In vivo
            </q-th>
            <q-th key="editPrimirnaFrom" :props="props" class="bg-amber-7 text-white">
              From
            </q-th>
            <q-th key="editPrimirnaTo" :props="props" class="bg-amber-8 text-white">
              To
            </q-th>
            <q-th key="editPremirnaFrom" :props="props" class="bg-orange-7 text-white">
              From
            </q-th>
            <q-th key="editPremirnaTo" :props="props" class="bg-orange-8 text-white">
              To
            </q-th>
            <q-th key="editMirnaFrom" :props="props" class="bg-deep-orange-7 text-white">
              From
            </q-th>
            <q-th key="editMirnaTo" :props="props" class="bg-deep-orange-8 text-white">
              To
            </q-th>
            <q-th key="ppcComparedWith" :props="props" class="bg-lime-9 text-white">
              Compared with
            </q-th>
          </q-tr>
        </template>
      </q-table>
    </q-card-section>
  </q-card>
</template>

<script>
export default {
  name: 'StudyDetails',
  props: {
    studyData: {
      type: Object,
      required: true
    }
  },
  data () {
    return {
      data: [],
      columns: [
        {
          name: 'name',
          required: false,
          label: '#',
          align: 'center',
          field: row => row.name,
          sortable: false,
          classes: 'bg-grey-2'
        },
        {
          name: 'biologicalSource',
          label: 'Biological Source',
          field: 'biological_source',
          sortable: true,
          align: 'left'
        },
        {
          name: 'origin',
          label: 'Origin',
          field: 'origin',
          sortable: true,
          align: 'left'
        },
        {
          name: 'condition',
          label: 'Condition',
          field: 'condition',
          sortable: true,
          align: 'center'
        },
        {
          name: 'inVitro',
          label: 'In vitro',
          field: 'in_vitro',
          sortable: true,
          align: 'center'
        },
        {
          name: 'exVivo',
          label: 'Ex vivo',
          field: 'ex_vivo',
          sortable: true,
          align: 'center'
        },
        {
          name: 'inVivo',
          label: 'In vivo',
          field: 'in_vivo',
          sortable: true,
          align: 'center'
        },
        {
          name: 'editPrimirnaFrom',
          label: 'From',
          field: 'edit_primirna_from',
          sortable: true,
          align: 'center',
          sort: (a, b, rowA, rowB) => parseInt(a, 10) - parseInt(b, 10)
        },
        {
          name: 'editPrimirnaTo',
          label: 'To',
          field: 'edit_primirna_to',
          sortable: true,
          align: 'center',
          sort: (a, b, rowA, rowB) => parseInt(a, 10) - parseInt(b, 10)
        },
        {
          name: 'editPremirnaFrom',
          label: 'From',
          field: 'edit_premirna_from',
          sortable: true,
          align: 'center',
          sort: (a, b, rowA, rowB) => parseInt(a, 10) - parseInt(b, 10)
        },
        {
          name: 'editPremirnaTo',
          label: 'To',
          field: 'edit_premirna_to',
          sortable: true,
          align: 'center',
          sort: (a, b, rowA, rowB) => parseInt(a, 10) - parseInt(b, 10)
        },
        {
          name: 'editMirnaFrom',
          label: 'From',
          field: 'edit_mirna_from',
          sortable: true,
          align: 'center',
          sort: (a, b, rowA, rowB) => parseInt(a, 10) - parseInt(b, 10)
        },
        {
          name: 'editMirnaTo',
          label: 'To',
          field: 'edit_mirna_to',
          sortable: true,
          align: 'center',
          sort: (a, b, rowA, rowB) => parseInt(a, 10) - parseInt(b, 10)
        },
        {
          name: 'ppcComparedWith',
          label: 'Compared with',
          field: 'ppc_compared_with',
          sortable: true,
          align: 'center'
        }
      ],
      table: {
        filter: '',
        firstColumnsHeaderColor: '',
        rowKey: 'name',
        isDownloadable: true,
        title: 'Biological sources details'
      },
      pubmedId: ''
    }
  },
  mounted () {
    this.initDialogData(this.studyData)
  },
  computed: {},
  methods: {

    isObjectNotEmpty (value) {
      return this.$utils.isObjectNotEmpty(value)
    },

    isNotNull (value) {
      return this.$utils.isNotNull(value)
    },

    exportTable () {
      return this.$exportDataTableAsCSV()
    },

    initDataTableRows (data) {
      this.pubmedId = data.pubmed_id
      this.data = []

      let biologicalSource = []
      if (this.isNotNull(this.$store.state.showcase.filterByBiologicalSource)) {
        if (this.isNotNull(this.$store.state.showcase.filterByBiologicalSources)) {
          biologicalSource = this.$store.state.showcase.filterByBiologicalSources.split(';')
        }
      }

      if (this.isObjectNotEmpty(data) &&
        this.objectHasPropery(data, 'physiological_pathological_condition')) {
        if (this.isObjectNotEmpty(biologicalSource)) {
          data.physiological_pathological_condition.forEach((item, index) => {
            if (biologicalSource.includes(item.biological_source)) {
              this.data.push({
                name: index,
                biological_source: item.biological_source,
                origin: item.origin,
                condition: item.condition,
                in_vitro: item.experiment_type.in_vitro,
                ex_vivo: item.experiment_type.ex_vivo,
                in_vivo: item.experiment_type.in_vivo,
                ppc_comparison_results: item.pathological_vs_physiological_comparison.comparison_results,
                ppc_compared_with: item.pathological_vs_physiological_comparison.compared_with,
                edit_primirna_from: item.editing.primirna.el_from,
                edit_primirna_to: item.editing.primirna.el_to,
                edit_premirna_from: item.editing.premirna.el_from,
                edit_premirna_to: item.editing.premirna.el_to,
                edit_mirna_from: item.editing.mirna.el_from,
                edit_mirna_to: item.editing.mirna.el_to
              })
            }
          })
        } else {
          data.physiological_pathological_condition.forEach((item, index) => {
            this.data.push({
              name: index,
              biological_source: item.biological_source,
              origin: item.origin,
              condition: item.condition,
              in_vitro: item.experiment_type.in_vitro,
              ex_vivo: item.experiment_type.ex_vivo,
              in_vivo: item.experiment_type.in_vivo,
              ppc_comparison_results: item.pathological_vs_physiological_comparison.comparison_results,
              ppc_compared_with: item.pathological_vs_physiological_comparison.compared_with,
              edit_primirna_from: item.editing.primirna.el_from,
              edit_primirna_to: item.editing.primirna.el_to,
              edit_premirna_from: item.editing.premirna.el_from,
              edit_premirna_to: item.editing.premirna.el_to,
              edit_mirna_from: item.editing.mirna.el_from,
              edit_mirna_to: item.editing.mirna.el_to
            })
          })
        }
      }
    },

    objectHasPropery (object, property) {
      return this.$utils.objectHasPropery(object, property)
    },

    initDialogData (data) {
      if (this.isObjectNotEmpty(data)) {
        this.initDataTableRows(data)
      }
    }
  },
  watch: {
    studyData: function (newVal, oldVal) {
      this.initDialogData(newVal)
    }
  }
}
</script>
