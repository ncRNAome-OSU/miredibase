<template>
  <div>

    <q-table
      dense
      flat
      bordered
      card-class="bg-grey-2"
      :title="table.title"
      :data="table.data"
      :columns="table.columns"
      :color="table.firstColumnsHeaderColor"
      :row-key="table.rowKey"
      :visible-columns="table.visibleColumns"
      :hide-pagination="table.hidePagination"
    >

      <template v-slot:top></template>

      <template slot="header" slot-scope="props" :props="props" style="display: contents">
        <q-tr>
          <q-th colspan="5" class="text-left">
            <helper>
              The modification site overview. Click on the purple inscriptions to access external resources.
            </helper>
            <span class="q-pl-xs">{{ table.title }}</span>
          </q-th>
          <q-th colspan="5" class="bg-deep-orange-9 text-white">
            Stem-loop information
          </q-th>
          <q-th colspan="3"></q-th>
        </q-tr>
        <q-tr>
          <q-th key="name" :props="props">
          </q-th>
          <q-th
            key="organism" :props="props" class="text-center">
            Organism
          </q-th>
          <q-th key="modType" :props="props" class="text-center">
            RNA modification<br>type
          </q-th>
          <q-th key="chromosome" :props="props" class="text-center">
            Chromosome
          </q-th>
          <q-th key="strand" :props="props" class="text-center">
            Strand
          </q-th>
          <q-th key="genomicPosition" :props="props" class="text-center">
            Genomic position<br>(UCSC)
          </q-th>
          <q-th key="stemloop" :props="props" class="bg-deep-orange-5 text-white text-center">
            Stem-loop
          </q-th>
          <q-th key="transcriptRegion" :props="props" class="bg-deep-orange-6 text-white text-center">
            Edited transcript<br>region&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
          </q-th>
          <q-th key="stemloopRegionInvolved" :props="props" class="bg-deep-orange-7 text-white text-center">
            Region&nbsp;&nbsp;&nbsp;<br>involved
          </q-th>
          <q-th key="stemloopLocalPos" :props="props" class="bg-deep-orange-8 text-white text-center">
            Local position<br>in stem-loop&nbsp;&nbsp;
          </q-th>
          <q-th key="mirnaLocalPos" :props="props" class="bg-deep-orange-9 text-white text-center">
            GLocal position<br>in miRNA&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
          </q-th>
          <q-th key="isPutative" :props="props" class="bg-light-green-9 text-white text-center">
            Is it putative?
          </q-th>
          <q-th colspan="3" rowspan="1" class="bg-deep-purple-8 text-white text-center">
            External resources
          </q-th>
        </q-tr>
      </template>

      <q-td slot="body-cell-chromosome" slot-scope="props" :props="props">
        <q-chip square outline color="green-6 text-weight-bold">
          {{ props.value }}
        </q-chip>
      </q-td>

      <q-td slot="body-cell-genomicPosition" slot-scope="props" :props="props">
        <q-btn
          no-caps
          square
          class="text-weigth-bold"
          type="a"
          :label="props.value.value"
          flat
          color="purple"
          @click="goToExternaResource(`${props.value.link}`)"
        />
      </q-td>

      <q-td slot="body-cell-stemloop" slot-scope="props" :props="props">
        <q-btn
          no-caps
          square
          class="text-weigth-bold"
          type="a"
          :label="props.value.value"
          flat
          color="purple"
          @click="goToExternaResource(`${props.value.link}`)"
        />
      </q-td>

      <q-td slot="body-cell-isPutative" slot-scope="props" :props="props">
        <q-chip :color="setIsPutativeColor(props.value)" text-color="white">{{ isPutative(props.value) }}</q-chip>
      </q-td>

      <q-td slot="body-cell-externalResources" slot-scope="props" :props="props">
        <q-btn
          v-if="objectHasPropery(props.row, 'ucsc')"
          no-caps
          square
          dense
          class="text-weigth-bold q-px-xs q-mr-xs"
          type="a"
          :label="props.row.ucsc.value"
          color="deep-purple"
          icon="all_inbox"
          @click="goToExternaResource(`${props.row.ucsc.link}`)"
        />

        <q-btn
          v-if="objectHasPropery(props.row, 'darned')"
          no-caps
          square
          dense
          class="text-weigth-bold q-px-xs q-mr-xs"
          type="a"
          :label="props.row.darned.value"
          color="deep-purple"
          icon="all_inbox"
          @click="goToExternaResource(`${props.row.darned.link}`)"
        />

        <q-btn
          v-if="objectHasPropery(props.row, 'radar')"
          no-caps
          square
          dense
          class="text-weigth-bold q-px-xs q-mr-xs"
          type="a"
          :label="props.row.radar.value"
          color="deep-purple"
          icon="all_inbox"
          @click="goToExternaResource(`${props.row.radar.link}`)"
        />

        <q-btn
          v-if="objectHasPropery(props.row, 'rediportal')"
          no-caps
          square
          dense
          class="text-weigth-bold q-px-xs q-mr-xs"
          type="a"
          :label="props.row.rediportal.value"
          color="deep-purple"
          icon="all_inbox"
          @click="goToExternaResource(`${props.row.rediportal.link}`)"
        />
      </q-td>
    </q-table>

  </div>
</template>

<script>
import { openURL } from 'quasar'
import Helper from 'components/Helper'

export default {
  name: 'SnvOverviewDetails',
  components: {
    Helper
  },
  props: {
    studyData: {
      type: Object,
      required: true
    }
  },
  data () {
    return {
      svnDataDetailsLabelsOrdering: [
        'organism',
        'mod_type',
        'chromosome',
        'strand',
        'genomic_position',
        'stemloop',
        'transcript_region',
        'stemloop_local_pos',
        'stemloop_region_involved',
        'mirna',
        'mirna_local_pos',
        'is_putative',
        'uri'
      ],
      table: {
        hidePagination: true,
        rowKey: 'name',
        title: 'RNA modification summary',
        visibleColumns: [
          'organism',
          'modType',
          'chromosome',
          'strand',
          'genomicPosition',
          'stemloop',
          'transcriptRegion',
          'stemloopLocalPos',
          'stemloopRegionInvolved',
          'mirna',
          'mirnaLocalPos',
          'isPutative',
          'externalResources'
        ],
        data: [],
        columns: [
          {
            name: 'name',
            required: false,
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
            sortable: false,
            align: 'center'
          },
          {
            name: 'modType',
            label: 'RNA Editing type',
            field: 'mod_type',
            sortable: false,
            align: 'center'
          },
          {
            name: 'chromosome',
            label: 'Chromosome',
            field: 'chromosome',
            sortable: false,
            align: 'center'
          },
          {
            name: 'strand',
            label: 'DNA Strand',
            field: 'strand',
            sortable: false,
            align: 'center'
          },
          {
            name: 'genomicPosition',
            label: 'Genomic position',
            field: 'genomic_position',
            sortable: false,
            align: 'center',
            sort: (a, b, rowA, rowB) => parseInt(a, 10) - parseInt(b, 10)
          },
          {
            name: 'stemloop',
            label: 'Name',
            field: 'stemloop',
            sortable: false,
            align: 'center'
          },
          {
            name: 'transcriptRegion',
            label: 'Transcript region',
            field: 'transcript_region',
            sortable: false,
            align: 'center'
          },
          {
            name: 'stemloopRegionInvolved',
            label: 'Region involved',
            field: 'stemloop_region_involved',
            sortable: false,
            align: 'center'
          },
          {
            name: 'stemloopLocalPos',
            label: 'Local position in stem-loop',
            field: 'stemloop_local_pos',
            sortable: false,
            align: 'center',
            sort: (a, b, rowA, rowB) => parseInt(a, 10) - parseInt(b, 10)
          },
          {
            name: 'mirnaLocalPos',
            label: 'Local position in miRNA',
            field: 'mirna_local_pos',
            sortable: false,
            align: 'center',
            sort: (a, b, rowA, rowB) => parseInt(a, 10) - parseInt(b, 10)
          },
          {
            name: 'isPutative',
            label: 'Is it putative?',
            field: 'is_putative',
            sortable: false,
            align: 'center'
          },
          {
            name: 'externalResources',
            label: 'External resources',
            field: 'uri',
            sortable: false,
            align: 'center'
          }
        ]
      }
    }
  },
  mounted () {
    this.initListData(this.studyData)
  },
  methods: {

    isObjectNotEmpty (value) {
      return this.$utils.isObjectNotEmpty(value)
    },

    isNotNull (value) {
      return this.$utils.isNotNull(value)
    },

    isPutative (value) {
      return value ? 'yes' : 'no'
    },

    setIsPutativeColor (value) {
      return value ? 'amber-14' : 'light-green-8'
    },

    objectHasPropery (value, property) {
      return this.$utils.objectHasPropery(value, property)
    },

    goToExternaResource (url) {
      openURL(url)
    },

    initListData (data) {
      this.table.data = []
      if (this.isObjectNotEmpty(data)) {
        this.table.data.push(this.$utils.setSnvDetailstableRow(data, this.svnDataDetailsLabelsOrdering))
      }
    }

  },
  watch: {
    studyData: function (newVal, oldVal) { // watch it
      this.initListData(newVal)
    }
  }
}
</script>
