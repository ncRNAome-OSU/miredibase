<template>
  <div>
    <q-card>
      <q-card-section class="bg-grey-2">
        <q-item-label class="text-h6 text-weight-light">
          <helper>
            The modification site overview. Click on the purple inscriptions to access external resources.
          </helper>
          RNA modification summary
        </q-item-label>
      </q-card-section>
      <q-separator />
      <q-card-section>
        <q-list dense>
          <q-item v-for="item in snvDataDetails" :key="item.key">
            <q-item-section>
              <q-item-label class="text-weight-bold text-weight-light">{{ item.label }}</q-item-label>
            </q-item-section>
            <q-item-section v-if="isObjectNotEmpty(item.link)" side>
              <q-btn
                no-caps
                square
                dense
                class="text-weigth-bold q-px-xs"
                type="a"
                :label="item.value"
                flat
                color="purple"
                @click="goToExternaResource(item.link)"
              />
            </q-item-section>
            <q-item-section v-else side>
              <q-item-label caption class="text-weight-light text-grey-10">{{ item.value }}</q-item-label>
            </q-item-section>
          </q-item>
        </q-list>
      </q-card-section>
      <q-separator />
      <q-card-section v-if="isObjectNotEmpty(studyData.uri.darned) || isObjectNotEmpty(studyData.uri.rediportal) || isObjectNotEmpty(studyData.uri.radar)">
        <q-btn
          v-if="isObjectNotEmpty(studyData.uri.darned)"
          no-caps
          square
          dense
          class="text-weigth-bold q-px-xs q-mr-xs"
          type="a"
          label="Darned"
          color="purple"
          icon="all_inbox"
          @click="goToExternaResource(studyData.uri.darned)"
        />
        <q-btn
          v-if="isObjectNotEmpty(studyData.uri.radar)"
          no-caps
          square
          dense
          class="text-weigth-bold q-px-xs q-mr-xs"
          type="a"
          label="Radar"
          color="purple"
          icon="all_inbox"
          @click="goToExternaResource(studyData.uri.radar)"
        />
        <q-btn
          v-if="isObjectNotEmpty(studyData.uri.rediportal)"
          no-caps
          square
          dense
          class="text-weigth-bold q-px-xs q-mr-xs"
          type="a"
          label="REDIportal"
          color="purple"
          icon="all_inbox"
          @click="goToExternaResource(studyData.uri.rediportal)"
        />
      </q-card-section>
    </q-card>

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
        'stemloop_local_pos',
        'stemloop_region_involved',
        'mirna',
        'mirna_local_pos'
      ],
      snvDataDetails: []
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

    goToExternaResource (url) {
      openURL(url)
    },

    initListData (data) {
      this.snvDataDetails = []

      if (this.isObjectNotEmpty(data)) {
        this.snvDataDetails = this.$utils.setSnvDetailsList(data, this.svnDataDetailsLabelsOrdering)
      }
    }
  },
  watch: {
    studyData: function (newVal, oldVal) {
      this.initListData(newVal)
    }
  }
}
</script>
