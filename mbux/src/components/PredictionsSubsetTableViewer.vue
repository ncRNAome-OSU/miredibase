<template>
  <div v-if="isObjectNotEmpty(data)">
    <q-card class="text-weigth-light">
      <q-card-section>
        <div class="text-center text-h3">{{ data.length }}</div>
      </q-card-section>

      <q-card-section class="q-pt-none text-center">
        <helper>
          {{ tooltipText }}
        </helper>
        <span :class="`text-${badgeColor} q-pa-sm text-uppercase text-weight-bold`">
          {{ title }}
        </span>
      </q-card-section>

      <q-separator />

      <q-card-section class="q-pa-none">
        <q-table
          dense
          flat
          :data="data"
          :columns="columns"
          :color="firstColumnsHeaderColor"
          :row-key="rowKey"
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
          </template>

          <template slot="header" slot-scope="props" :props="props" style="display: contents">
            <q-tr>
              <q-th colspan="1"></q-th>
              <q-th
                colspan="2"
                :class="`bg-${badgeColor}-9 text-white`"
              >
                Target information
              </q-th>
            </q-tr>
            <q-tr>
              <q-th key="name" :props="props"></q-th>
              <q-th
                key="refSeq" :props="props" :class="`bg-${badgeColor}-6 text-white`">
                RefSeq
              </q-th>
              <q-th
                key="geneName" :props="props" :class="`bg-${badgeColor}-8 text-white`">
                Gene name
              </q-th>
            </q-tr>
          </template>

          <q-td slot="body-cell-refSeq" slot-scope="props" :props="props">
            <q-btn
              v-if="isObjectNotEmpty(props.value)"
              no-caps
              square
              dense
              class="text-weigth-bold q-px-xs"
              type="a"
              :label="props.value"
              flat
              color="purple"
              @click="goToExternaResource(`https://www.ncbi.nlm.nih.gov/nuccore/${props.value}`)"
            />
          </q-td>

          <q-td slot="body-cell-geneName" slot-scope="props" :props="props">
            <q-btn
              v-if="isObjectNotEmpty(props.value)"
              no-caps
              square
              dense
              class="text-weigth-bold q-px-xs"
              type="a"
              :label="props.value"
              flat
              color="purple"
              @click="goToExternaResource(`https://www.genecards.org/cgi-bin/carddisp.pl?gene=${props.value}`)"
            />
          </q-td>

        </q-table>

        <q-btn v-if="isDownloadable"
          color="orange-9"
          icon-right="archive"
          label="Export to .CSV"
          no-caps
          @click="exportTable"
        />
      </q-card-section>
    </q-card>
  </div>
</template>

<script>
import { openURL } from 'quasar'
import Helper from 'components/Helper'

export default {
  name: 'PredictionsSubsetTableViewer',
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
    badgeColor: {
      type: String,
      default: 'grey'
    },
    tooltipText: {
      type: String,
      required: true
    }
  },
  data () {
    return {
      filter: '',
      pagination: {
        rowsPerPage: 5
      }
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
    }

  }
}
</script>
