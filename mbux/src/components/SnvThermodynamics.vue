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
                  <q-item-label caption>
                    (In <span style="font-weight: bold; color: red">red</span> the reference nucleotide;
                    in <span style="font-weight: bold; background-color: yellow">yellow</span> the canonical miRNA sequence, if involved)
                  </q-item-label>
                  <q-item-label caption class="text-left">
<pre v-for="item in seq.ref" :key="item.start">
<b>{{ printSpaces(item.spacesStart) }}{{ item.start }}</b> <span v-for="nt in item.nts" :key="nt.idx" :style="nt.style">{{ nt.nt }}</span> <b>{{ printSpaces(item.spacesEnd) }}{{ item.end }}</b>
</pre>
                  </q-item-label>
                </q-item-section>
              </q-item>
              <q-item>
                <q-item-section>
                  <q-item-label>Stem-loop 2D structure (RNAfold)</q-item-label>
                  <q-item-label caption>
<pre v-for="item in seq.ref" :key="item.idx">
<b>{{ printSpaces(item.spacesStart) }}{{ item.start }}</b> {{ item.brackets }} <b>{{ printSpaces(item.spacesEnd) }}{{ item.end }}</b>
</pre>
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
                  <q-item-label caption>
                    (In <span style="font-weight: bold; color: red">red</span> the modified nucleotide;
                    in <span style="font-weight: bold; background-color: yellow">yellow</span> the canonical miRNA sequence, if involved)
                  </q-item-label>
                  <q-item-label caption>
<pre v-for="item in seq.mod" :key="item.start">
<b>{{ printSpaces(item.spacesStart) }}{{ item.start }}</b> <span v-for="nt in item.nts" :key="nt.idx" :style="nt.style">{{ nt.nt }}</span> <b>{{ printSpaces(item.spacesEnd) }}{{ item.end }}</b>
</pre>
                  </q-item-label>
                </q-item-section>
              </q-item>
              <q-item>
                <q-item-section>
                  <q-item-label>Stem-loop 2D structure (RNAfold)</q-item-label>
<q-item-label caption>
<pre v-for="item in seq.mod" :key="item.idx">
<b>{{ printSpaces(item.spacesStart) }}{{ item.start }}</b> {{ item.brackets }} <b>{{ printSpaces(item.spacesEnd) }}{{ item.end }}</b>
</pre>
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
        ref: [],
        mod: []
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

    getSpaces (index, length) {
      switch (index) {
        case 0:
          return length > 3 ? 2 : 1
        case 1:
          return length > 3 ? 1 : 0
        default:
          return 0
      }
    },

    printSpaces (value) {
      return ' '.repeat(value)
    },

    showModificationSite () {
      if (this.isObjectNotEmpty(this.snvData.rnafold_stemloop.wildtype_seq) &&
        this.isObjectNotEmpty(this.snvData.rnafold_stemloop.edited_seq)) {
        let mirSeqStart = -1
        let mirSeqEnd = -1
        if (this.isObjectNotEmpty(this.snvData.mirna_seq)) {
          const mirseq = this.snvData.mirna_seq.replace(/U/g, 'T')
          mirSeqStart = this.snvData.rnafold_stemloop.wildtype_seq.indexOf(mirseq)
          mirSeqEnd = mirSeqStart + mirseq.length - 1
        }
        const limit = 40
        const refseq = this.snvData.rnafold_stemloop.wildtype_seq.match(/.{1,40}/g)
        const modseq = this.snvData.rnafold_stemloop.edited_seq.match(/.{1,40}/g)
        const refbrackets = this.snvData.rnafold_stemloop.wildtype_rna_2d_structure.match(/.{1,40}/g)
        const modbrackets = this.snvData.rnafold_stemloop.edited_rna_2d_structure.match(/.{1,40}/g)

        for (let i = 0; i < refseq.length; i++) {
          const ref = {
            start: i * limit + 1,
            end: (i * limit) + refseq[i].length,
            nts: [],
            brackets: refbrackets[i],
            spacesStart: this.getSpaces(i, refseq.length),
            spacesEnd: limit - refseq[i].length
          }
          const mod = {
            start: i * limit + 1,
            end: (i * limit) + modseq[i].length,
            nts: [],
            brackets: modbrackets[i],
            spacesStart: this.getSpaces(i, modseq.length),
            spacesEnd: limit - modseq[i].length
          }

          for (let j = 0; j < refseq[i].length; j++) {
            let style = {}
            if ((i * limit + j) === (this.snvData.stemloop_local_pos - 1)) {
              style = { color: 'red', 'font-size': '1.3em' }
            } else if ((i * limit + j) >= mirSeqStart && (i * limit + j) <= mirSeqEnd) {
              style = { 'background-color': 'yellow' }
            }
            ref.nts.push({
              nt: refseq[i][j],
              style: style,
              idx: i * limit + j
            })
            mod.nts.push({
              nt: modseq[i][j],
              style: style,
              idx: i * limit + j
            })
          }
          this.seq.ref.push(ref)
          this.seq.mod.push(mod)
        }
      }
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
