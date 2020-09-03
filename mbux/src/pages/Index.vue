<template>
  <q-page padding class="text-weight-light">
    <p class="text-h5 text-weight-light">Homepage</p>

    <q-card>
      <q-card-section horizontal>
        <q-card-section class="col-sm-8 col-md-9 col-lg-10 text-justify">
          <p>
            Welcome to MiREDiBase (<span style="text-decoration: underline">miR</span>NA
            <span style="text-decoration: underline">Edi</span>ting Data<span style="text-decoration: underline">base</span>),
            a catalog of known miRNA editing sites and an online resource for functional prediction of
            miRNA editing. Here, users can explore
            multiple features related to miRNA modification events, such as detection and
            validation methods, experiment type, biological sources, enzyme affinity,
            and much more. Have fun!
          </p>
          <p class="text-bold">About miRNA Editing</p>
          <p>
            RNA editing refers to enzymatic modifications occurring on specific nucleosides
            of an RNA molecule. MiRNA editing, in particular, refers to RNA modification events
            occurring in miRNA transcripts, which currently represent the best characterized
            class of regulatory small non-coding RNAs. The importance of miRNA editing
            consists in the fact that such an event often results in the blockage of miRNA
            biogenesis or in the alteration of its mature sequence, likely causing a
            functional shift. This would then lead towards various implications on the cell
            physiopathology.
          </p>
          <p class="text-bold">About the Database</p>
          <p>
            Besides being a tool for the study of miRNA editing, MiREDiBase also provides
            useful information for the study of modified miRNAs as potential biomarkers of
            specific physiopathological conditions. It allows the users to infer associations
            between specific modification events and organ dysfunctions, the biological function
            of modified mature miRNAs, and to compare editing levels between matched normal
            and adverse conditions.
          </p>
          <p class="text-justify">
            The current version of the database contains information on A-to-I (Adenosine-to-Inosine)
            and C-to-U (Cytosine-to-Uracil) miRNA modifications in humans and primates.
          </p>
          <div class="text-right">
            <p>
              <!-- https://cen.acs.org/business/start-ups/WatchCRISPR-RNA-editing-race/97/i12 -->
              Thank you for visiting us!
            </p>
            <p>
              <b>Privacy notice</b><br>
              We reserve the right to use information about visitors (location), date/time visited, page visited,
              referring website, etc. to improve our services. This information is used for site usage statistics only.
            </p>
            <script
              type="application/javascript"
              src="//rf.revolvermaps.com/0/0/4.js?i=51o620se5z6&amp;m=5&amp;h=210&amp;c=ff0000&amp;r=0"
              async="async"
            />
          </div>
        </q-card-section>

        <q-card-section class="bg-grey-2 col-sm-4 col-md-3 col-lg-2 text-center">
          <div class="text-h5">Search</div>
          <div class="text-caption">
            Search for RNA Modification Sites in microRNAs.
          </div>
          <q-btn
            no-caps
            to="/search"
            label="Go to"
            color="purple"
          />

          <q-separator spaced />

          <div class="text-h5">Compare</div>
          <div class="text-caption">
            Compare editing levels between adverse and normal conditions.
          </div>
          <q-btn
            no-caps
            to="/compare"
            label="Go to"
            color="purple"
          />

          <q-separator spaced />

          <div class="text-h5">Statistics</div>
          <div class="text-caption">
            Descriptive statistics about the current version.
          </div>
          <q-btn
            no-caps
            to="/stats"
            label="Go to"
            color="purple"
          />

          <q-separator spaced />

          <div class="text-h5">Documentation</div>
          <div class="text-caption">
            Find supportive information.
          </div>
          <q-btn
            no-caps
            to="/help"
            label="Go to"
            color="purple"
          />

          <q-separator spaced />

          <div class="text-h5">Download</div>
          <div class="text-caption">
            Download the current database release.
          </div>
          <q-btn
            no-caps
            to="/download"
            label="Go to"
            color="purple"
          />

          <q-separator spaced />
          <q-separator spaced />

          <div class="text-h5">RESTful APIs</div>
          <div class="text-caption">
            MiREDiBase RESTful APIs for data retrieving.
          </div>
          <q-btn
            type="a"
            no-caps
            label="Go to"
            color="deep-orange"
            @click="goToExternaResource('https://ncrnaome.osumc.edu/miredibaseapi/docs')"
          />

        </q-card-section>
      </q-card-section>

      <q-separator />

      <q-card-actions>
      </q-card-actions>
    </q-card>

  </q-page>
</template>

<script>
import { openURL } from 'quasar'

export default {
  name: 'PageIndex',
  components: {},
  data () {
    return {}
  },
  mounted () {
    this.loadCookieMessage()
  },
  methods: {

    goToExternaResource (url) {
      openURL(url)
    },

    loadCookieMessage () {
      this.$q.notify({
        message: 'MiREDiBase uses cookies only for functional and analytical purposes. ',
        color: 'primary',
        position: 'top',
        role: 'alertdialog',
        type: 'info',
        actions: [
          { label: 'Got it!', color: 'white', handler: () => { /* ... */ } }
        ],
        timeout: 0
      })
    }

  }
}
</script>
