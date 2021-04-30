<template>
  <div>
    <span class="text-h5 text-weight-light">Compare</span>
    <q-separator spaced />
    <q-btn
      flat
      dense
      label="Click me"
      icon="search"
      color="primary"
      @click="openDialogSearchForm"
    />
    <span class="text-weight-light text-justify"> to show the proper <i>Compare Form</i>.</span>

    <q-dialog v-model="dialog" position="top" persistent>
      <q-card
        class="q-pa-md"
        style="width: 900px; max-width: 90vw;"
      >
        <q-card-section class="row items-center q-pb-none">
          <div class="text-h6 text-weight-light">
            <helper>
              Select the desired information by following the steps in numerical order.
            </helper>
            Case versus Control comparison form
          </div>
          <q-space />
          <q-btn icon="close" flat round dense v-close-popup />
        </q-card-section>

        <q-card-section>
          <p class="text-weight-light text-justify">
            Here you can compare for information on RNA modification sites by: (i)
            selecting a disease, or (ii) a stem-loop. The disease and stem-loop
            fields are mutually exclusive.
          </p>

          <q-separator />
          <span class="text-weight-light text-justify">Load one of the following examples: </span>
          <q-btn label="Example 1" color="primary" class="q-ml-sm" flat dense v-on:click="loadExample(1)" />
          <q-btn label="Example 2" color="primary" class="q-ml-sm" flat dense v-on:click="loadExample(2)" />
          <q-separator />
          <br>

          <q-form
            @submit.prevent.stop="onSubmit"
            @reset="onReset"
            class="q-gutter-md"
          >

            <q-card flat bordered>
              <q-card-section horizontal>
                <q-card-section class="flex flex-center text-weight-light text-center bg-green">
                  <q-chip outline square color="white" label="Step 1" class="text-bold" />
                </q-card-section>
                <q-separator vertical />
                <q-card-section style="width: 100%">
                  <div class="row q-gutter-md">
                    <div class="col">
                      <q-select
                        v-model="filter.organism"
                        label="Organism"
                        :options="formField.organism"
                        hint="(Select an Organism)"
                        @input="loadOrganismData($event)"
                        name="organismSearchField"
                        id="organismSearchField"
                      />
                    </div>
                    <div class="col">
                      <q-select
                        v-model="filter.rnaModification"
                        label="RNA Editing type"
                        :options="formField.rnaModification"
                        hint="(Select an Editing Type)"
                        @input="loadOrganismRNAModificationData($event)"
                        name="rnaModificationSearchField"
                        id="rnaModificationSearchField"
                      />
                    </div>
                  </div>
                </q-card-section>
              </q-card-section>
            </q-card>

            <q-card flat bordered>
              <q-card-section horizontal>
                <q-card-section class="flex flex-center text-weight-light text-center bg-deep-orange">
                  <q-chip outline square color="white" label="Step 2" class="text-bold" />
                </q-card-section>
                <q-separator vertical />
                <q-card-section style="width: 100%">
                  <span class="text-weight-light text-grey-7">NOTE: Fields Disease and Stem-loop are mutually exclusive.</span>
                  <div class="row q-gutter-md">
                    <div class="col">
                      <q-select
                        clearable
                        use-input
                        input-debounce="0"
                        v-model="filter.disease"
                        label="Disease"
                        :options="formField.disease"
                        hint="(Select a desease)"
                        @input="onSearchFieldUpdate($event, 'disease')"
                        name="diseaseSearchField"
                        id="diseaseSearchField"
                        :disable="fieldStatus.disease"
                        @filter="filterDisease"
                      >
                        <template v-slot:no-option>
                          <q-item>
                            <q-item-section class="text-grey">
                              No results
                            </q-item-section>
                          </q-item>
                        </template>
                      </q-select>
                    </div>
                    <div class="col">
                      <q-select
                        clearable
                        use-input
                        input-debounce="0"
                        v-model="filter.premirna"
                        label="Stem-loop"
                        :options="formField.premirna"
                        hint="(Select a stem-loop)"
                        @input="onSearchFieldUpdate($event, 'premirna')"
                        name="prediseaseSearchField"
                        id="prediseaseSearchField"
                        :disable="fieldStatus.premirna"
                        @filter="filterPremirnas"
                      >
                        <template v-slot:no-option>
                          <q-item>
                            <q-item-section class="text-grey">
                              No results
                            </q-item-section>
                          </q-item>
                        </template>
                      </q-select>
                    </div>
                  </div>
                </q-card-section>
              </q-card-section>
            </q-card>

            <div>
              <q-btn label="Submit" type="submit" color="primary"/>
              <q-btn label="Reset" type="reset" color="primary" flat class="q-ml-sm" />
            </div>
          </q-form>

        </q-card-section>
      </q-card>
    </q-dialog>
  </div>
</template>

<script>
import Helper from 'components/Helper'

export default {
  name: 'SearchForm',
  props: {},
  components: {
    Helper
  },
  data () {
    return {
      dialog: true,
      position: 'top',
      formField: {
        organism: [],
        rnaModification: [],
        premirna: [],
        disease: []
      },
      formOptionValues: {
        premirna: [],
        disease: []
      },
      filter: {
        organism: null,
        rnaModification: null,
        premirna: null,
        disease: null
      },
      fieldStatus: {
        premirna: false,
        disease: false,
        organism: false,
        rnaModification: false
      }
    }
  },

  mounted () {
    this.loadOrganismOpts()
  },

  methods: {

    isObjectNotEmpty (value) {
      return this.$utils.isObjectNotEmpty(value)
    },

    loadExample (number) {
      this.onReset()
      switch (number) {
        case 1:
          this.filter.organism = { label: 'Human', value: 'human' }
          this.loadEditingOpts(this.filter.organism.value)
          this.filter.rnaModification = { label: 'A-to-I', value: 'ai' }
          this.loadOrganismRNAModificationData(this.filter.rnaModification)
          this.filter.disease = 'AML (acute myeloid leukemia)'
          this.onSearchFieldUpdate(this.filter.disease, 'disease')
          break
        case 2:
          this.filter.organism = { label: 'Human', value: 'human' }
          this.loadEditingOpts(this.filter.organism.value)
          this.filter.rnaModification = { label: 'A-to-I', value: 'ai' }
          this.loadOrganismRNAModificationData(this.filter.rnaModification)
          this.filter.premirna = 'hsa-let-7f-1'
          this.onSearchFieldUpdate(this.filter.premirna, 'premirna')
          break
        default:
          break
      }
    },

    objectHasPropery (object, key) {
      return this.$utils.objectHasPropery(object, key)
    },

    filterPremirnas (value, update) {
      if (value === '') {
        update(() => {
          this.formField.premirna = this.formOptionValues.premirna
        })
        return
      }

      update(() => {
        const needle = value.toLowerCase()
        this.formField.premirna = this.formOptionValues.premirna.filter(
          v => v.toLowerCase().indexOf(needle) > -1
        )
      })
    },

    filterDisease (value, update) {
      if (value === '') {
        update(() => {
          this.formField.disease = this.formOptionValues.disease
        })
        return
      }

      update(() => {
        const needle = value.toLowerCase()
        this.formField.disease = this.formOptionValues.disease.filter(
          v => v.toLowerCase().indexOf(needle) > -1
        )
      })
    },

    isNotNull (value) {
      return this.$utils.isNotNull(value)
    },

    formatOrganismOpts (data) {
      this.formField.organism = this.$utils.selectOpt(data, 'organism')
    },

    loadOrganismOpts () {
      this.$loadApiData(
        '/comparison/organisms/',
        this.formatOrganismOpts
      )
    },

    formatEditingOpts (data) {
      this.formField.rnaModification = this.$utils.selectOpt(data, 'editing')
    },

    loadEditingOpts (value) {
      this.$loadApiData(
        '/comparison/rnaenditingtypes/',
        this.formatEditingOpts,
        { organism: value }
      )
    },

    formatPremirnaOpts (data) {
      this.formOptionValues.premirna = this.$utils.selectOpt(data)
      this.formField.premirna = this.$utils.selectOpt(data)
    },

    loadPremirnaOpts (payload) {
      this.$loadApiData(
        '/comparison/premirnas/',
        this.formatPremirnaOpts,
        payload
      )
    },

    formatDiseaseOpts (data) {
      this.formOptionValues.disease = this.$utils.selectOpt(data)
      this.formField.disease = this.$utils.selectOpt(data)
    },

    loadDiseaseOpts (payload) {
      this.$loadApiData(
        '/comparison/diseases/',
        this.formatDiseaseOpts,
        payload
      )
    },

    loadOrganismData (event) {
      if (this.isObjectNotEmpty(event)) {
        this.releaseFormFields(['organism'])
        this.loadEditingOpts(event.value)
      }
    },

    loadOrganismRNAModificationData (event) {
      if (this.isObjectNotEmpty(event) &&
        this.isNotNull(this.filter.organism)) {
        const payload = {
          organism: this.filter.organism.value,
          mod_type: event.value
        }
        this.releaseFormFields(['organism', 'rnaModification'])
        this.loadPremirnaOpts(payload)
        this.loadDiseaseOpts(payload)
      }
    },

    openDialogSearchForm () {
      this.dialog = !this.dialog
    },

    onSubmit (e) {
      e.preventDefault()

      if (!(
        this.isNotNull(this.filter.organism) &&
        this.isNotNull(this.filter.rnaModification) &&
        (
          this.isNotNull(this.filter.premirna) ||
          this.isNotNull(this.filter.disease)
        ))) {
        this.$q.notify({
          color: 'red-7',
          textColor: 'white',
          icon: 'warning',
          message: 'Error. Please, select among the options pre-miRNA or disease.',
          position: 'top',
          progress: true
        })
      } else {
        this.openDialogSearchForm()

        this.$q.notify({
          color: 'green-4',
          textColor: 'white',
          icon: 'cloud_download',
          message: 'Fetching data...',
          position: 'top',
          progress: true
        })

        const response = {}

        if (this.isNotNull(this.filter.organism)) {
          response.organism = this.filter.organism.value
        }

        if (this.isNotNull(this.filter.rnaModification)) {
          response.mod_type = this.filter.rnaModification.value
        }

        if (this.isNotNull(this.filter.premirna)) {
          response.stemloop = this.filter.premirna
        }

        if (this.isNotNull(this.filter.disease)) {
          response.disease = this.filter.disease
        }

        this.$emit('sendSearchResponse', response)
      }
    },

    onReset () {
      for (const [key] of Object.entries(this.fieldStatus)) {
        switch (typeof this.fieldStatus[key]) {
          case 'object':
            for (const [k] of Object.entries(this.fieldStatus[key])) {
              this.fieldStatus[key][k] = !(key === k)
              this.filter[key][k] = null
            }
            break
          default:
            this.filter[key] = null
            this.fieldStatus[key] = false
            break
        }
        this.formField[key] = []

        if (this.objectHasPropery(this.formOptionValues, key)) {
          this.formOptionValues[key] = []
        }
      }
      this.loadOrganismOpts()
    },

    releaseFormFields (discard = []) {
      for (const [key] of Object.entries(this.fieldStatus)) {
        if (!discard.includes(key)) {
          switch (typeof this.fieldStatus[key]) {
            case 'object':
              for (const [k] of Object.entries(this.fieldStatus[key])) {
                this.fieldStatus[key][k] = !(key === k)
                this.filter[key][k] = null
              }
              break
            default:
              this.filter[key] = null
              this.fieldStatus[key] = false
              break
          }
        }
      }
    },

    updateFieldAccess (key) {
      for (const [k1] of Object.entries(this.fieldStatus)) {
        switch (typeof this.fieldStatus[k1]) {
          case 'object':
            for (const [k2] of Object.entries(this.fieldStatus[k1])) {
              this.fieldStatus[k1][k2] = !(key === k1)
            }
            break
          default:
            this.fieldStatus[k1] = !(key === k1)
            break
        }
      }
    },

    onSearchFieldUpdate (event, key) {
      if (this.isObjectNotEmpty(event)) {
        this.updateFieldAccess(key)
      } else {
        this.releaseFormFields([
          'organism', 'rnaModification'
        ])
      }
    }

  },
  computed: {

    isRangeValid () {
      const start = this.filter.chromosome.start
      const end = this.filter.chromosome.end
      return (start && end) ? (start < end) : true
    }

  }

}
</script>
