<template>
  <div v-if="isObjectNotEmpty(snvData) && isObjectNotEmpty(snvData.rnafold_stemloop.wildtype_rna_2d_structure)">
    <p class="text-weight-light text-h4 text-center">{{ snvData.stemloop }} (2D Structure)</p>
    <div class="row text-weight-light">
      <div class="col-xs-12 col-sm-12 col-md-6 col-lg-6 q-pr-xs">

        <q-card class="my-card">
          <q-card-section>
            <div class="text-weight-light text-h4 text-center">
              Wild-type
            </div>
            <div class="text-weight-light text-subtitle2">Powered by RNAfold</div>
          </q-card-section>

          <q-separator />

          <q-btn
            type="a"
            class="q-ma-xs"
            color="deep-orange-9"
            icon="cloud_download"
            label="Download"
            @click="downloadStructure(formatURL(snvData, 'wildtype'))"
          />

          <q-card-section>
            <q-img
              sizes="(max-width: 400px) 400w,
                (min-width: 400px) and (max-width: 800px) 800w,
                (min-width: 800px) and (max-width: 1200px) 1200w,
                (min-width: 1200px) 1600w"
              :src="formatURL(snvData, 'wildtype')"
              error="No structure available"
            />
          </q-card-section>

          <q-separator />

          <q-card-section>
            <q-list>
              <q-item>
                <q-item-section>
                  <q-item-label>Stem-loop sequence</q-item-label>
                  <q-item-label caption lines="2">
                    <pre>{{ seq.ref.pre }}<span class="text-bold" style="color: red">{{ seq.ref.mod }}</span>{{ seq.ref.next }}</pre>
                  </q-item-label>
                </q-item-section>
              </q-item>
              <q-item>
                <q-item-section>
                  <q-item-label>Stem-loop 2D structure (RNAfold)</q-item-label>
                  <q-item-label caption lines="2"><pre>{{ snvData.rnafold_stemloop.wildtype_rna_2d_structure }}</pre>
                  </q-item-label>
                </q-item-section>
              </q-item>
              <q-item>
                <q-item-section>
                  <q-item-label>
                    Free energy:
                    <q-chip square outline color="deep-orange-9" text-color="white" class="text-weight-bold">
                      {{ snvData.rnafold_stemloop.wildtype_free_energy }}
                    </q-chip>
                  </q-item-label>
                </q-item-section>
                <q-item-section side>
                  <q-item-label>
                    MEA (maximum expected accuracy):
                    <q-chip square outline color="deep-orange-9" text-color="white" class="text-weight-bold">
                      {{ snvData.rnafold_stemloop.wildtype_mea }}
                    </q-chip>
                  </q-item-label>
                </q-item-section>
              </q-item>
            </q-list>
          </q-card-section>

          <q-separator />
          <br />
        </q-card>

        <br/>

      </div>
      <div class="col-xs-12 col-sm-12 col-md-6 col-lg-6 q-pr-xs">

        <q-card class="my-card">
          <q-card-section>
            <div class="text-weight-light text-h4 text-center">
              Edited ({{ prettifySnvType(snvData.mod_type) }}, position {{ snvData.stemloop_local_pos }})
            </div>
            <div class="text-weight-light text-subtitle2">Powered by RNAfold</div>
          </q-card-section>

          <q-separator />

          <q-btn
            type="a"
            class="q-ma-xs"
            color="deep-orange-9"
            icon="cloud_download"
            label="Download"
            @click="downloadStructure(formatURL(snvData, 'edited'))"
          />

          <q-card-section>
            <q-img
              sizes="(max-width: 400px) 400w,
                (min-width: 400px) and (max-width: 800px) 800w,
                (min-width: 800px) and (max-width: 1200px) 1200w,
                (min-width: 1200px) 1600w"
              :src="formatURL(snvData, 'edited')"
              error="No structure available"
            />
          </q-card-section>

          <q-separator />

          <q-card-section>
            <q-list>
              <q-item>
                <q-item-section>
                  <q-item-label>Stem-loop sequence</q-item-label>
                  <q-item-label caption lines="2">
                    <pre>{{ seq.mod.pre }}<span class="text-bold" style="color: red">{{ seq.mod.mod }}</span>{{ seq.mod.next }}</pre>
                  </q-item-label>
                </q-item-section>
              </q-item>
              <q-item>
                <q-item-section>
                  <q-item-label>Stem-loop 2D structure (RNAfold)</q-item-label>
                  <q-item-label caption lines="2"><pre>{{ snvData.rnafold_stemloop.edited_rna_2d_structure }}</pre>
                  </q-item-label>
                </q-item-section>
              </q-item>
              <q-item>
                <q-item-section>
                  <q-item-label>
                    Free energy:
                    <q-chip square outline color="deep-orange-9" text-color="white" class="text-weight-bold">
                      {{ snvData.rnafold_stemloop.edited_free_energy }}
                    </q-chip>
                  </q-item-label>
                </q-item-section>
                <q-item-section side>
                  <q-item-label>
                    MEA (maximum expected accuracy):
                    <q-chip square outline color="deep-orange-9" text-color="white" class="text-weight-bold">
                      {{ snvData.rnafold_stemloop.edited_mea }}
                    </q-chip>
                  </q-item-label>
                </q-item-section>
              </q-item>
            </q-list>
          </q-card-section>

          <q-separator />
          <br />
        </q-card>

      </div>
    </div>
  </div>
  <div v-else class="text-weight-light">
    No RNA 2D structures available for the selected RNA Editing site.
  </div>
</template>

<script>
import { openURL } from 'quasar'

export default {
  name: 'SnvThermodynamics',
  components: {},
  props: {
    snvData: {
      type: Object,
      default: null
    }
  },
  data () {
    return {
      seq: {
        ref: {
          pre: '',
          next: '',
          mod: ''
        },
        mod: {
          pre: '',
          next: '',
          mod: ''
        }
      }
    }
  },
  mounted () {
    this.showModificationSite()
  },
  computed: {},
  methods: {

    isObjectNotEmpty (value) {
      return this.$utils.isObjectNotEmpty(value)
    },

    prettifySnvType (value) {
      return this.$utils.prettifySnvType(value)
    },

    showModificationSite () {
      this.seq.ref.pre = this.snvData.rnafold_stemloop.wildtype_seq.substr(0, this.snvData.stemloop_local_pos - 1)
      this.seq.ref.mod = this.snvData.rnafold_stemloop.wildtype_seq.substr(this.snvData.stemloop_local_pos - 1, 1)
      this.seq.ref.next = this.snvData.rnafold_stemloop.wildtype_seq.substr(this.snvData.stemloop_local_pos)

      this.seq.mod.pre = this.snvData.rnafold_stemloop.edited_seq.substr(0, this.snvData.stemloop_local_pos - 1)
      this.seq.mod.mod = this.snvData.rnafold_stemloop.edited_seq.substr(this.snvData.stemloop_local_pos - 1, 1)
      this.seq.mod.next = this.snvData.rnafold_stemloop.edited_seq.substr(this.snvData.stemloop_local_pos)
    },

    formatURL (data, target) {
      let url = null
      if (this.isObjectNotEmpty(data)) {
        let label = null
        switch (target) {
          case 'wildtype':
            label = `${data.organism}_${data.stemloop}`
            break
          case 'edited':
            label = `${data.organism}_${data.mod_type}_${data.stemloop}_${data.genomic_position}`
            break
          default:
            break
        }
        url = `rna_2d_structures/${data.organism}/${data.mod_type}/${label}.png`
      }
      return url
    },

    downloadStructure (url) {
      openURL(url)
    }

  }
}
</script>
