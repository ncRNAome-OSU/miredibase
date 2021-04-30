<template>
  <div>
    <q-table
      dense
      :title="title"
      :data="data"
      :columns="columns"
      :color="firstColumnsHeaderColor"
      :row-key="rowKey"
      :visible-columns="visibleColumns"
      :filter="filter"
      :pagination.sync="pagination"
    >

      <template v-slot:top-right>
        <q-input
          size="xs"
          outlined
          rounded
          dense
          debounce="300"
          v-model="filter"
          placeholder="Search within the table"
        >
          <template v-slot:append>
            <q-icon name="search" />
          </template>
        </q-input>
        <q-btn class="q-ml-md" v-if="isDownloadable"
          color="orange-9"
          icon-right="archive"
          label="Export to .CSV"
          no-caps
          @click="exportTable"
        />
      </template>

      <template slot="header" slot-scope="props" :props="props" style="display: contents">
        <q-tr>
          <q-th colspan="7"></q-th>
          <q-th colspan="6" class="bg-deep-orange-9 text-white">
            Stem-loop information
          </q-th>
          <q-th colspan="3" class="bg-light-blue-9 text-white">
            No. studies per detection method
          </q-th>
          <q-th></q-th>
        </q-tr>
        <q-tr>
          <q-th key="name" :props="props">
            <helper>
              Click on the left-sided red icons to display summary tables. Click on the purple
              inscriptions to access external resources.
            </helper>
          </q-th>
          <q-th
            key="organism" :props="props">
            Organism
          </q-th>
          <q-th key="modType" :props="props" class="text-center">
            RNA modification<br>type
          </q-th>
          <q-th key="chromosome" :props="props">
            Chromosome
          </q-th>
          <q-th key="strand" :props="props">
            Strand
          </q-th>
          <q-th key="genomicPosition" :props="props" class="text-center">
            Genomic&nbsp;&nbsp;&nbsp;&nbsp;<br>position&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<br>(UCSC)
          </q-th>
          <q-th key="conservation" :props="props">
            Conservation
          </q-th>
          <q-th key="stemloop" :props="props" class="bg-deep-orange-4 text-white">
            Stem-loop
          </q-th>
          <q-th key="transcriptRegion" :props="props" class="bg-deep-orange-5 text-white text-center">
            Edited&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<br>transcript<br>
            &nbsp;region
          </q-th>
          <q-th key="stemloopRegionInvolved" :props="props" class="bg-deep-orange-6 text-white text-center">
            Region&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<br>involved
          </q-th>
          <q-th key="stemloopLocalPos" :props="props" class="bg-deep-orange-7 text-white text-center">
            Local position&nbsp;&nbsp;&nbsp;&nbsp;<br>in stem-loop
          </q-th>
          <q-th key="miRNA" :props="props" class="bg-deep-orange-8 text-white">
            miRNA
          </q-th>
          <q-th key="mirnaLocalPos" :props="props" class="bg-deep-orange-9 text-white text-center">
            Local position<br>in miRNA
          </q-th>
          <q-th key="numberHighThroughputStudies" :props="props" class="bg-light-blue-3 text-grey-9 text-center">
            High&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<br>
            throughput<br>&nbsp;&nbsp;&nbsp;methods
          </q-th>
          <q-th key="numberEnzymePerturbationStudies" :props="props" class="bg-light-blue-6 text-white text-center">
            Enzyme&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<br>perturbation
          </q-th>
          <q-th key="numberTargetedMethodStudies" :props="props" class="bg-light-blue-9 text-white text-center">
            Targeted&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<br>methods
          </q-th>
          <q-th key="isPutative" :props="props" class="bg-light-green-9 text-white text-center">
            Putative?
          </q-th>
        </q-tr>
      </template>

      <q-td slot="body-cell-name" slot-scope="props" :props="props">
        <q-btn
          round
          size="sm"
          color="red-7"
          icon="view_headline"
          @click="goToExternaResource(`/miredibase/variant/${props.row.mod_type}/${props.row.genomic_position}/${props.row.chromosome}/${props.row.strand}/${props.row.organism_code}`)"
        />
      </q-td>

      <q-td slot="body-cell-modType" slot-scope="props" :props="props">
        {{ prettifySnvType(props.value) }}
      </q-td>

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
          :label="props.value"
          flat
          color="purple"
          @click="goToExternaResource(`${props.row.uri.ucsc}`)"
        />
      </q-td>

      <q-td slot="body-cell-conservation" slot-scope="props" :props="props">
        <template>
          <q-list dense>
            <q-item
              v-for="(item, index) in props.value"
              :key="index"
            >
              <q-item-section>
                <q-btn
                  dense
                  flat
                  color="purple-7"
                  @click="goToExternaResource(`/miredibase/variant/${item.mod_type}/${item.genomic_position}/${item.chromosome}/${item.strand}/${item.organism_code}`)"
                >
                  {{item.organism_code}}
                </q-btn>
              </q-item-section>
            </q-item>
          </q-list>
        </template>
      </q-td>

      <q-td slot="body-cell-stemloop" slot-scope="props" :props="props">
        {{ props.value }}
        <br>
        <q-btn
          v-if="isNotNull(props.row.stemloop_acc_number)"
          no-caps
          square
          class="text-weigth-bold"
          type="a"
          label="miRBase"
          dense
          flat
          color="purple"
          @click="goToExternaResource(`http://www.mirbase.org/cgi-bin/mirna_entry.pl?acc=${props.row.stemloop_acc_number}`)"
        />
        <br>
        <q-btn
          v-if="isNotNull(props.row.stemloop_rnacentral_acc_number)"
          no-caps
          square
          class="text-weigth-bold"
          type="a"
          label="RNAcentral"
          dense
          flat
          color="purple"
          @click="goToExternaResource(`https://rnacentral.org/rna/${props.row.stemloop_rnacentral_acc_number}/${props.row.organism_id}`)"
        />
      </q-td>

      <q-td slot="body-cell-miRNA" slot-scope="props" :props="props">
        {{ props.value }}
        <br>
        <q-btn
          v-if="isNotNull(props.row.mirna_acc_number)"
          no-caps
          square
          class="text-weigth-bold"
          type="a"
          label="miRBase"
          dense
          flat
          color="purple"
          @click="goToExternaResource(`http://www.mirbase.org/cgi-bin/mirna_entry.pl?acc=${props.row.mirna_acc_number}`)"
        />
        <br>
        <q-btn
          v-if="isNotNull(props.row.mirna_rnacentral_acc_number)"
          no-caps
          square
          class="text-weigth-bold"
          type="a"
          label="RNAcentral"
          dense
          flat
          color="purple"
          @click="goToExternaResource(`https://rnacentral.org/rna/${props.row.mirna_rnacentral_acc_number}/${props.row.organism_id}`)"
        />
      </q-td>

      <q-td slot="body-cell-isPutative" slot-scope="props" :props="props">
        <q-chip :color="setIsPutativeColor(props.value)" text-color="white">{{ isPutative(props.value) }}</q-chip>
      </q-td>

    </q-table>
  </div>
</template>

<script>
import { openURL } from 'quasar'
import Helper from 'components/Helper'

export default {
  name: 'TableViewer',
  components: {
    Helper
  },
  props: {
    title: {
      type: String,
      required: true
    },
    data: {
      type: Array,
      required: true
    },
    columns: {
      type: Array,
      required: true
    },
    firstColumnsHeaderColor: {
      type: String,
      default: ''
    },
    rowKey: {
      type: String,
      required: true
    },
    isDownloadable: {
      type: Boolean,
      default: true
    },
    visibleColumns: {
      type: Array,
      required: true
    }
  },
  data () {
    return {
      filter: '',
      pagination: {
        rowsPerPage: 20
      }
    }
  },
  computed: {},
  methods: {

    isNotNull (value) {
      return this.$utils.isNotNull(value)
    },

    exportTable () {
      return this.$exportDataTableAsCSV()
    },

    prettifySnvType (value) {
      return this.$utils.prettifySnvType(value)
    },

    isPutative (value) {
      return value ? 'yes' : 'no'
    },

    setIsPutativeColor (value) {
      return value ? 'amber-14' : 'light-green-8'
    },

    goToExternaResource (url) {
      openURL(url)
    },

    showSNVDetails (idx) {
      this.$emit('loadSNVData', this.data[idx])
    }
  }
}
</script>
