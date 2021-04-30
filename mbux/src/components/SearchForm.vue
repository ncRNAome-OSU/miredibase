<template>
  <div>
    <span class="text-h5 text-weight-light">Search</span>

    <q-separator spaced />

    <q-btn
      flat
      dense
      label="Click me"
      icon="search"
      color="primary"
      @click="openDialogSearchForm"
    />

    <span class="text-weight-light text-justify"> to show the proper <i>Search Form</i>.</span>

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
            RNA modification sites searching form
          </div>
          <q-space />
          <q-btn icon="close" flat round dense v-close-popup />
        </q-card-section>

        <q-card-section>
          <p class="text-weight-light text-justify">
            Here you can explore available RNA modification sites by: simple specify
            a miRNA (<i>basic</i> search) or via the <i>advanced</i> search, in which
            you can seach by chromosome, a stem-loop, or a miRNA. Finally, results can
            be filtered by biological source(s). The chromosome, stem-loop, and miRNA
            fields are mutually exclusive.
          </p>

          <q-card>
            <q-tabs
              v-model="tab"
              dense
              class="bg-grey-8 text-white"
              active-color="white"
              indicator-color="red"
              align="justify"
            >
              <q-tab name="bssearch" label="Basic" />
              <q-tab name="advsearch" label="Advanced" />
            </q-tabs>

            <q-tab-panels v-model="tab" animated>
              <q-tab-panel name="bssearch">
                <q-form
                  @submit.prevent.stop="onSubmit"
                  class="q-gutter-md"
                  id="basicSearchForm"
                >
                  <q-card>
                    <q-card-section horizontal>
                      <q-card-section style="width: 100%">
                        <q-select
                          clearable
                          use-input
                          input-debounce="0"
                          v-model="filter.basicmirna"
                          label="miRNA"
                          :options="formField.basicmirna"
                          hint="** Required **"
                          name="basicMirnaSearchField"
                          id="basicMirnaSearchField"
                          @filter="filterBasicMirnas"
                        >
                          <template v-slot:no-option>
                            <q-item>
                              <q-item-section class="text-grey">
                                No results
                              </q-item-section>
                            </q-item>
                          </template>
                        </q-select>
                      </q-card-section>
                      <q-separator vertical />
                      <q-card-section class="flex flex-center">
                        <q-btn label="Submit" type="submit" color="primary"/>
                      </q-card-section>
                    </q-card-section>
                  </q-card>

                </q-form>
                <br>
                <q-form
                  @submit.prevent.stop="onSubmit"
                  class="q-gutter-md"
                  id="basicSearchForm2"
                >
                  <q-card>
                    <q-card-section horizontal>
                      <q-card-section style="width: 100%">
                        <q-select
                          clearable
                          use-input
                          input-debounce="0"
                          v-model="filter.basicpremirna"
                          label="Stem-loop"
                          :options="formField.basicpremirna"
                          hint="** Required **"
                          name="basicPremirnaSearchField"
                          id="basicPremirnaSearchField"
                          @filter="filterBasicPremirnas"
                        >
                          <template v-slot:no-option>
                            <q-item>
                              <q-item-section class="text-grey">
                                No results
                              </q-item-section>
                            </q-item>
                          </template>
                        </q-select>
                      </q-card-section>
                      <q-separator vertical />
                      <q-card-section class="flex flex-center">
                        <q-btn label="Submit" type="submit" color="primary"/>
                      </q-card-section>
                    </q-card-section>
                  </q-card>

                </q-form>
              </q-tab-panel>

              <q-tab-panel name="advsearch">
                <span class="text-weight-light text-justify">Load one of the following examples: </span>
                <q-btn label="Example 1" color="primary" class="q-ml-sm" flat dense v-on:click="loadExample(1)" />
                <q-btn label="Example 2" color="primary" class="q-ml-sm" flat dense v-on:click="loadExample(2)" />
                <q-separator />
                <br>

                <q-form
                  @submit.prevent.stop="onSubmit"
                  @reset="onReset"
                  class="q-gutter-md"
                  id="advancedSearchForm"
                >

                  <q-card>
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
                              hint="** Required **"
                              @input="loadOrganismData($event)"
                              name="organismSearchField"
                              id="organismSearchField"
                            />
                          </div>
                          <div class="col">
                            <q-select
                              v-model="filter.rnaModification"
                              label="RNA Modification type"
                              hint="** Optional **"
                              @input="loadOrganismRNAModificationData($event)"
                              :options="formField.rnaModification"
                              name="rnaModificationSearchField"
                              id="rnaModificationSearchField"
                            />
                          </div>
                        </div>
                      </q-card-section>
                    </q-card-section>
                  </q-card>

                  <q-card>
                    <q-card-section horizontal>
                      <q-card-section class="flex flex-center text-weight-light text-center bg-deep-orange">
                        <q-chip outline square color="white" label="Step 2" class="text-bold" />
                      </q-card-section>
                      <q-separator vertical />
                      <q-card-section style="width: 100%">
                        <span class="text-weight-light text-grey-7">
                          NOTE: Fields Chromosome, Stem-loop, and miRNA are mutually exclusive.
                        </span>
                        <div class="row q-gutter-md">
                          <div class="col">
                            <q-select
                              clearable
                              use-input
                              input-debounce="0"
                              v-model="filter.chromosome.chromosome"
                              label="Chromosome"
                              hint="** Optional **"
                              :options="formField.chromosome"
                              @input="onSearchFieldUpdate($event, 'chromosome')"
                              name="chromsomeSearchField"
                              id="chromsomeSearchField"
                              :disable="fieldStatus.chromosome.chromosome"
                              @filter="filterChromosomas"
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
                            <q-input
                              clearable
                              type="number"
                              v-model.number="filter.chromosome.start"
                              label="Start position"
                              hint="** Optional **"
                              min=0
                              name="chromosomeStartSearchField"
                              id="chromosomeStartSearchField"
                              :disable="fieldStatus.chromosome.start"
                              :error="!isRangeValid"
                            >
                              <template v-slot:error>
                                The <i>Start</i> must be lower then <i>End</i>.
                              </template>
                            </q-input>
                          </div>
                          <div class="col">
                            <q-input
                              clearable
                              type="number"
                              v-model.number="filter.chromosome.end"
                              label="End position"
                              hint="** Optional **"
                              min="0"
                              name="chromosomeEndSearchField"
                              id="chromosomeEndSearchField"
                              :disable="fieldStatus.chromosome.end"
                              :error="!isRangeValid"
                            >
                              <template v-slot:error>
                                The <i>End</i> must be higher then <i>Start</i>.
                              </template>
                            </q-input>
                          </div>
                          <div class="col">
                            <q-select
                              clearable
                              v-model="filter.chromosome.strand"
                              label="Strand"
                              hint="** Optional **"
                              :options="formField.strand"
                              menu-anchor="top left"
                              name="strandSearchField"
                              id="strandSearchField"
                              :disable="fieldStatus.chromosome.strand"
                            />
                          </div>
                        </div>

                        <div class="row q-gutter-md">
                          <div class="col">
                            <q-select
                              clearable
                              use-input
                              input-debounce="0"
                              v-model="filter.premirna"
                              label="Stem-loop"
                              hint="** Optional **"
                              :options="formField.premirna"
                              @input="onSearchFieldUpdate($event, 'premirna')"
                              name="premirnaSearchField"
                              id="premirnaSearchField"
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
                          <div class="col">
                            <q-select
                              clearable
                              use-input
                              input-debounce="0"
                              v-model="filter.mirna"
                              label="miRNA"
                              hint="** Optional **"
                              :options="formField.mirna"
                              @input="onSearchFieldUpdate($event, 'mirna')"
                              name="mirnaSearchField"
                              id="mirnaSearchField"
                              :disable="fieldStatus.mirna"
                              @filter="filterMirnas"
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

                  <q-card>
                    <q-card-section horizontal>
                      <q-card-section class="flex flex-center text-weight-light text-center bg-purple">
                        <q-chip outline square color="white" label="Step 3" class="text-bold" />
                      </q-card-section>
                      <q-separator vertical />
                      <q-card-section style="width: 100%">
                        <div class="row q-gutter-md">
                          <div class="col">
                            <q-select
                              ref="qselectbiologicalsource"
                              multiple
                              clearable
                              use-input
                              input-debounce="0"
                              v-model="filter.biologicalSource"
                              label="Biological source"
                              hint="** Optional **"
                              :options="formField.biologicalSource"
                              name="biologicalSourceSearchField"
                              id="biologicalSourceSearchField"
                              :disable="fieldStatus.biologicalSource"
                              @filter="filterBiologicalSource"
                              @input="clearFilter"
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
                    <q-btn label="Reset" type="reset" color="grey-6" class="q-ml-xs q-px-xs" />
                  </div>
                </q-form>
              </q-tab-panel>

            </q-tab-panels>
          </q-card>

          <q-separator />

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
      tab: 'bssearch',
      dialog: true,
      position: 'top',
      formField: {
        organism: [],
        rnaModification: [],
        chromosome: [],
        strand: [
          { label: '+', value: '+' },
          { label: '-', value: '-' }
        ],
        basicpremirna: [],
        premirna: [],
        basicmirna: [],
        mirna: [],
        biologicalSource: []
      },
      formOptionValues: {
        chromosome: [],
        basicpremirna: [],
        premirna: [],
        mirna: [],
        basicmirna: [],
        biologicalSource: []
      },
      filter: {
        organism: null,
        rnaModification: null,
        chromosome: {
          chromosome: null,
          start: null,
          end: null,
          strand: null
        },
        basicpremirna: null,
        premirna: null,
        basicmirna: null,
        mirna: null,
        biologicalSource: null
      },
      fieldStatus: {
        chromosome: {
          chromosome: false,
          start: true,
          end: true,
          strand: true
        },
        basicpremirna: false,
        premirna: false,
        basicmirna: false,
        mirna: false,
        biologicalSource: false,
        organism: false,
        rnaModification: false
      }
    }
  },

  mounted () {
    this.loadOrganismOpts()
    this.loadBasicPremirnaOpts()
    this.loadBasicMirnaOpts()
  },

  methods: {

    isObjectNotEmpty (value) {
      return this.$utils.isObjectNotEmpty(value)
    },

    loadExample (number) {
      this.onReset()
      switch (number) {
        case 1:
          this.filter.organism = {
            label: 'Human',
            value: 'human'
          }
          this.loadEditingOpts(this.filter.organism.value)
          this.filter.rnaModification = {
            label: 'A-to-I',
            value: 'ai'
          }
          this.filter.chromosome.chromosome = '1'
          this.onSearchFieldUpdate(this.filter.chromosome.chromosome, 'chromosome')
          this.filter.biologicalSource = [
            'BLCA (bladder carcinoma)',
            'BG01 (Embryonic Stem Cells)',
            'Amyotrophic lateral sclerosis (ALS) (spinal cord)'
          ]
          break
        case 2:
          this.filter.organism = {
            label: 'Human',
            value: 'human'
          }
          this.loadEditingOpts(this.filter.organism.value)
          this.filter.rnaModification = {
            label: 'A-to-I',
            value: 'ai'
          }
          this.filter.premirna = 'hsa-let-7f-1'
          this.onSearchFieldUpdate(this.filter.premirna, 'premirna')
          break
        default:
          break
      }

      const payload = {
        organism: this.filter.organism.value,
        mod_type: this.filter.rnaModification.value,
        chromosome: this.filter.chromosome.chromosome,
        stemloop: this.filter.premirna,
        mirna: this.filter.mirna
      }
      this.loadBiologicalSourceOpts(payload)
    },

    objectHasPropery (object, key) {
      return this.$utils.objectHasPropery(object, key)
    },

    filterChromosomas (value, update) {
      if (value === '') {
        update(() => {
          this.formField.chromosome = this.formOptionValues.chromosome
        })
        return
      }

      update(() => {
        const needle = value.toLowerCase()
        this.formField.chromosome = this.formOptionValues.chromosome.filter(
          v => v.toLowerCase().indexOf(needle) > -1
        )
      })
    },

    filterBasicPremirnas (value, update) {
      if (value === '') {
        update(() => {
          this.formField.basicpremirna = this.formOptionValues.basicpremirna
        })
        return
      }

      update(() => {
        const needle = value.toLowerCase()
        this.formField.basicpremirna = this.formOptionValues.basicpremirna.filter(
          v => v.toLowerCase().indexOf(needle) > -1
        )
      })
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

    filterBiologicalSource (value, update) {
      if (value === '') {
        update(() => {
          this.formField.biologicalSource = this.formOptionValues.biologicalSource
        })
        return
      }

      update(() => {
        const needle = value.toLowerCase()
        this.formField.biologicalSource = this.formOptionValues.biologicalSource.filter(
          v => v.toLowerCase().indexOf(needle) > -1
        )
      })
    },

    filterBasicMirnas (value, update) {
      if (value === '') {
        update(() => {
          this.formField.basicmirna = this.formOptionValues.basicmirna
        })
        return
      }

      update(() => {
        const needle = value.toLowerCase()
        this.formField.basicmirna = this.formOptionValues.basicmirna.filter(
          v => v.toLowerCase().indexOf(needle) > -1
        )
      })
    },

    filterMirnas (value, update) {
      if (value === '') {
        update(() => {
          this.formField.mirna = this.formOptionValues.mirna
        })
        return
      }

      update(() => {
        const needle = value.toLowerCase()
        this.formField.mirna = this.formOptionValues.mirna.filter(
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
        '/organisms/',
        this.formatOrganismOpts
      )
    },

    formatEditingOpts (data) {
      this.formField.rnaModification = this.$utils.selectOpt(data, 'editing')
    },

    loadEditingOpts (value) {
      this.$loadApiData(
        '/organisms/rnaenditingtypes/',
        this.formatEditingOpts,
        { organism: value }
      )
    },

    formatChromosomeOpts (data) {
      this.formOptionValues.chromosome = this.$utils.selectOpt(data)
      this.formField.chromosome = this.$utils.selectOpt(data)
    },

    loadChromosomeOpts (payload) {
      this.$loadApiData(
        '/organisms/chromosomes/',
        this.formatChromosomeOpts,
        payload
      )
    },

    formatBasicPremirnaOpts (data) {
      this.formOptionValues.basicpremirna = this.$utils.selectOpt(data)
      this.formField.basicpremirna = this.$utils.selectOpt(data)
    },

    loadBasicPremirnaOpts () {
      this.$loadApiData(
        '/premirnas/',
        this.formatBasicPremirnaOpts
      )
    },

    formatPremirnaOpts (data) {
      this.formOptionValues.premirna = this.$utils.selectOpt(data)
      this.formField.premirna = this.$utils.selectOpt(data)
    },

    loadPremirnaOpts (payload) {
      this.$loadApiData(
        '/organisms/premirnas/',
        this.formatPremirnaOpts,
        payload
      )
    },

    formatMirnaOpts (data) {
      this.formOptionValues.mirna = this.$utils.selectOpt(data)
      this.formField.mirna = this.$utils.selectOpt(data)
    },

    loadMirnaOpts (payload) {
      this.$loadApiData(
        '/organisms/mirnas/',
        this.formatMirnaOpts,
        payload
      )
    },

    formatBasicMirnaOpts (data) {
      this.formOptionValues.basicmirna = this.$utils.selectOpt(data)
      this.formField.basicmirna = this.$utils.selectOpt(data)
    },

    loadBasicMirnaOpts () {
      this.$loadApiData(
        '/mirnas/',
        this.formatBasicMirnaOpts
      )
    },

    formatBiologicalSourceOpts (data) {
      this.formOptionValues.biologicalSource = this.$utils.selectOpt(data)
      this.formField.biologicalSource = this.$utils.selectOpt(data)
    },

    loadBiologicalSourceOpts (payload) {
      this.$loadApiData(
        '/organisms/biologicalsources/',
        this.formatBiologicalSourceOpts,
        payload
      )
    },

    loadOrganismData (event) {
      if (this.isObjectNotEmpty(event)) {
        this.releaseFormFields(['organism', 'strand'])
        this.loadEditingOpts(event.value)
        const payload = {
          organism: this.filter.organism.value
        }
        this.loadChromosomeOpts(payload)
        this.loadPremirnaOpts(payload)
        this.loadMirnaOpts(payload)
        this.loadBiologicalSourceOpts(payload)
      }
    },

    loadOrganismRNAModificationData (event) {
      if (this.isObjectNotEmpty(event) &&
        this.isNotNull(this.filter.organism)) {
        const payload = {
          organism: this.filter.organism.value,
          mod_type: event.value
        }
        this.releaseFormFields(['organism', 'rnaModification', 'strand'])
        this.loadChromosomeOpts(payload)
        this.loadPremirnaOpts(payload)
        this.loadMirnaOpts(payload)
        this.loadBiologicalSourceOpts(payload)
      }
    },

    openDialogSearchForm () {
      this.dialog = !this.dialog
    },

    onSubmit (e) {
      e.preventDefault()
      const response = {}

      if (e.target.id === 'advancedSearchForm') {
        if (this.isNotNull(this.filter.organism)) {
          response.organism = this.filter.organism.value
        }

        if (this.isNotNull(this.filter.rnaModification)) {
          response.mod_type = this.filter.rnaModification.value
        }

        if (this.isNotNull(this.filter.chromosome.chromosome)) {
          response.chromosome = this.filter.chromosome.chromosome
          if (this.isNotNull(this.filter.chromosome.start)) {
            response.start = this.filter.chromosome.start
          }

          if (this.isNotNull(this.filter.chromosome.end)) {
            response.end = this.filter.chromosome.end
          }

          if (this.isNotNull(this.filter.chromosome.strand)) {
            response.strand = this.filter.chromosome.strand.value
          }
        }

        if (this.isNotNull(this.filter.premirna)) {
          response.stemloop = this.filter.premirna
        }

        if (this.isNotNull(this.filter.mirna)) {
          response.mirna = this.filter.mirna
        }

        if (this.isObjectNotEmpty(this.filter.biologicalSource)) {
          response.biological_source = this.filter.biologicalSource.join(';')
        }
      } else if (e.target.id === 'basicSearchForm') {
        if (this.isNotNull(this.filter.basicmirna)) {
          response.mirna = this.filter.basicmirna
        }
      } else if (e.target.id === 'basicSearchForm2') {
        if (this.isNotNull(this.filter.basicpremirna)) {
          response.stemloop = this.filter.basicpremirna
        }
      }

      if (!this.isObjectNotEmpty(response)) {
        this.$q.notify({
          color: 'red-7',
          textColor: 'white',
          icon: 'warning',
          message: 'Error. Please, fill out the form.',
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

        this.$emit('sendSearchResponse', response)
        this.$store.commit('showcase/updateSearchTabPanels', false)
        this.$store.commit('showcase/updateDataStudyDetailsTabPanel', {})
        this.$store.commit('showcase/updateWildtypeTargetPredictionData', [])
        this.$store.commit('showcase/updateEditedTargetPredictionData', [])
        this.$store.commit('showcase/updateWildtypeUniqueTargetPredictionData', [])
        this.$store.commit('showcase/updateEditedUniqueTargetPredictionData', [])
        this.$store.commit('showcase/updateIntersectionUniqueTargetPredictionData', [])
        this.$store.commit('showcase/updateTargetEnrichmentData', {})
        this.onReset()
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
      this.loadBasicMirnaOpts()
      this.loadBasicPremirnaOpts()
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

    updateFieldAccess (key, discard = []) {
      for (const [k1] of Object.entries(this.fieldStatus)) {
        if (!discard.includes(k1)) {
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
      }
    },

    clearFilter () {
      if (this.$refs.qselectbiologicalsource !== null) {
        this.$refs.qselectbiologicalsource.updateInputValue('')
      }
    },

    onSearchFieldUpdate (event, key) {
      this.formOptionValues.biologicalSource = []
      if (this.isObjectNotEmpty(event)) {
        this.updateFieldAccess(key, ['biologicalSource'])
        const payload = {
          organism: this.filter.organism.value,
          mod_type: this.isObjectNotEmpty(this.filter.rnaModification) ? this.filter.rnaModification.value : null,
          chromosome: this.filter.chromosome.chromosome,
          stemloop: this.filter.premirna,
          mirna: this.filter.mirna
        }
        this.loadBiologicalSourceOpts(payload)
      } else {
        this.releaseFormFields([
          'organism', 'rnaModification', 'strand'
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
