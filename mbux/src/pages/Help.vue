<template>
  <q-page padding>
    <!-- content -->
    <span class="text-h5 text-weight-light" id="documentHeader">Documentation</span>
    <q-separator spaced />
    <div class="row">
      <div class="col-xs-12 col-sm-12 col-md-4 col-lg-3 text-weight-light text-justify">
        <q-page-sticky position="top-left" :offset="[0, 50]">
          <q-card flat class="transparent">

            <q-card-section>
              <q-list dense>
                <q-item-label header class="text-weight-light">Search</q-item-label>
                <q-item clickable v-ripple @click="goToSection('searchTab', 'searchHowTo')">
                  <q-item-section>
                    How to start
                  </q-item-section>
                </q-item>

                <q-item clickable v-ripple @click="goToSection('searchTab', 'searchForm')">
                  <q-item-section>
                    1.1 Search Form
                  </q-item-section>
                </q-item>

                <q-item clickable v-ripple @click="goToSection('searchTab', 'searchPredictions')">
                  <q-item-section>
                    1.2 Predictions
                  </q-item-section>
                </q-item>
                <q-item>
                  <q-list flat dense style="min-width: 200px">
                    <q-item clickable v-ripple @click="goToSection('searchTab', 'searchThermodynamicPrediction')">
                      <q-item-section>
                        1.2.1 Thermodynamic prediction
                      </q-item-section>
                    </q-item>
                    <q-item clickable v-ripple @click="goToSection('searchTab', 'searchIsoTarPredictions')">
                      <q-item-section>
                        1.2.2 isoTar predictions
                      </q-item-section>
                    </q-item>
                    <q-item clickable v-ripple @click="goToSection('searchTab', 'searchIsoTarFunctionalPredictions')">
                      <q-item-section>
                        1.2.3 isoTar functional predictions
                      </q-item-section>
                    </q-item>
                  </q-list>
                </q-item>

                <q-item-label header class="text-weight-light">Compare</q-item-label>
                <q-item clickable v-ripple @click="goToSection('compareTab', 'compareHowTo')">
                  <q-item-section>
                    How to start
                  </q-item-section>
                </q-item>
                <q-item clickable v-ripple @click="goToSection('compareTab', 'compareForm')">
                  <q-item-section>
                    2.1 Compare Form
                  </q-item-section>
                </q-item>

                <q-item-label header class="text-weight-light">RESTful API</q-item-label>
                <q-item clickable v-ripple @click="goToSection('restApiTab', 'restfulHowTo')">
                  <q-item-section>
                    How to start
                  </q-item-section>
                </q-item>
              </q-list>
            </q-card-section>

          </q-card>
        </q-page-sticky>
      </div>
      <div class="col-xs-12 col-sm-12 col-md-8 col-lg-9 text-weight-light text-justify">
        <q-card>
          <q-tabs
            v-model="panel"
            dense
            class="text-grey"
            active-color="primary"
            indicator-color="primary"
            align="justify"
            narrow-indicator
          >
            <q-tab no-caps name="searchTab" label="Search" />
            <q-tab no-caps name="compareTab" label="Compare" />
            <q-tab no-caps name="restApiTab" label="RESTful API(s)" />
          </q-tabs>

          <q-separator />
          <q-tab-panels v-model="panel" animated>

            <q-tab-panel name="searchTab">
              <p class="text-h6 text-weight-light text-justify">How to use <i>Search</i>.</p>
              <p id="searchHowTo">
                Searching into MiREDiBase has been rendered pretty simple. It requires no bioinformatics skills to perform accurate
                searches across the database, and its user-friendly interface allows to keep track of each search step, as to improve your experience.<br><br>

                Once in the "Search" section, you can retrieve miRNA editing sites by providing specific information in the "Search form".
              </p>
              <center>
                <q-img
                  class="shadow-1"
                  src="documentation/fig1.png"
                  style="max-width:800px"
                />
              </center>

              <br>
              <q-separator spaced inset />
              <br>

              <p>
                <span class="text-bold" id="searchForm">1.1 Search Form</span><br>
                After the search form has showed up, select an organism and specify the editing type. Then, provide a genomic
                region or a stem-loop/miRNA name in the apposite field of the "search form". Then, you can also optionally
                specify a biological source. The search will be activated by clicking the “Submit” button.<br><br>

                NOTE: The "genomic region", "stem-loop", and "miRNA" fields are mutually exclusive. Once one of these fields
                has been filled, the others will be automatically disactivated. The "biological source" field, instead, allows
                to filter results by biological tissues and/or cell lines. By clicking the "Reset" button, information will be
                deleted and all fields will be re-activated.
              </p>
              <center>
                <q-img
                  class="shadow-1"
                  src="documentation/fig2.png"
                  style="max-width:800px"
                />
              </center>
              <br><br>

              <p>
                Search by genomic region can include an entire chromosome or a restricted chromosome region. To retrieve editing
                sites falling into a chromosome, just select the chromosome number in the field "Chromosome" and then click the
                "Submit" button. To retrieve editing sites falling into more restricted genomic regions, select a chromosome and
                then type a start and end position in the apposite fields. Finally, select the strand on the DNA (+ or -).
              </p>
              <center>
                <q-img
                  class="shadow-1"
                  src="documentation/fig3.png"
                  style="max-width:800px"
                />
              </center>
              <br><br>

              <p>
                NOTE: The end position must be greater than the start position. In case the end position is equal or minor than
                the start position, an error message will appear in the search form.
              </p>
              <center>
                <q-img
                  class="shadow-1"
                  src="documentation/fig4.png"
                  style="max-width:800px"
                />
              </center>
              <br><br>

              <p>
                To retrieve editing events reported for individual miRNAs, click either on the "stem-loop" or "miRNA" field.
                A drop-down menu containing the complete list of miRNAs will show up. You can just select the miRNA of interest
                from the drop-down menu or type a miRNA name and then select the miRNA of interest. Click on "Submit" to launch the search.
              </p>
              <center>
                <q-img
                  class="shadow-1"
                  src="documentation/fig5.png"
                  style="max-width:800px"
                />
              </center>
              <br><br>

              <p>
                In case you want to limit your search to one or few biological sources, you can select one or multiple biological
                sources from the drop-down menu contained in the "biological source" field. As a consequence, MiREDiBase will return
                miRNA modification sites detected in the selected tissues/cell lines.
              </p>
              <center>
                <q-img
                  class="shadow-1"
                  src="documentation/fig6.png"
                  style="max-width:800px"
                />
              </center>
              <br><br>

              <p>
                After submitting the seach form, MiREDiBase will return a table containing the list of retrieved unique miRNA modification sites.
                The table displays general information concerning each modification site, including the genomic position and information relative to the stem-loop.<br><br>

                By default, the table will show 5 records per page. However, it is possible to augment the number of records showed per page.
              </p>
              <center>
                <q-img
                  class="shadow-1"
                  src="documentation/fig10.png"
                  style="max-width:800px"
                />
              </center>
              <br><br>

              <p>
                How to visualize more records per page.
              </p>
              <center>
                <q-img
                  class="shadow-1"
                  src="documentation/fig11.png"
                  style="max-width:800px"
                />
              </center>
              <br><br>

              <p>
                Information about the miRNA stem-loop are subdivided as reported in the table.
              </p>
              <center>
                <q-img
                  class="shadow-1"
                  src="documentation/fig12.png"
                  style="max-width:800px"
                />
              </center>
              <br><br>

              <p>
                Results can be filtered by typing appropriate key words or numerical values in the "Search within the table" (e.g.,
                a miRNA name, a genomic position, chromosome number, etc). Results can be downloaded as a .CSV (comma-separated data) file by clicking the "Export" button.<br><br>

                Clicking the red icons on the left side of the table, it will open a new table containing the list of published original papers that
                have detected the selected modification site.
              </p>
              <center>
                <q-img
                  class="shadow-1"
                  src="documentation/fig13.png"
                  style="max-width:800px"
                />
              </center>
              <br><br>

              <p>
                Information available in the "RNA Modification site study" section.
              </p>
              <center>
                <q-img
                  class="shadow-1"
                  src="documentation/fig14.png"
                  style="max-width:800px"
                />
              </center>
              <br><br>

              <p>
                Right above the "RNA Modification site studies" table, a summary bar will be displayed, summing up basic information about the selected editing site.
                Four selecting boxes are displayed in between, allowing you to navigate across four distinc sections. The "RNA Modification site studies" table is
                included in the "Overview" section, which is showed by default. The other three sections are dedicated to predictive information and are illustrated
                in the next subsection (<span class="text-bold">1.2 Predictions</span>).
              </p>
              <center>
                <q-img
                  class="shadow-1"
                  src="documentation/fig15.png"
                  style="max-width:800px"
                />
              </center>
              <br><br>

              <p>
                Clicking the red icons on the left side of the "RNA Modification site study" table, it will open the "Additional info" section containing detailed
                information about the authors’ findings for the selected miRNA editing site. Moreover, it displays information about detection and validation methods
                for the identification of the editing site, and validation methods for the eventual retargeting.
              </p>
              <center>
                <q-img
                  class="shadow-1"
                  src="documentation/fig16.png"
                  style="max-width:800px"
                />
              </center>
              <br><br>

              <p>
                NOTE: in case the modification consists of a nucleotide substitution, the editing level columns report the minimum (from)
                and the maximum (to) value of editing level for the selected editing site, according to information provided by the authors. Editing level values are
                rounded and showed as multiples of five.<br><br>NOTE: if the "Compared with" column reports a biological source (meaning that an intra-study comparison
                was made between adverse and normal conditions of the same tissue), you can find detailed information about the comparison in the "Compare" section
                (<span class="text-bold">2.1 Comparing editing levels in adverse vs. normal conditions</span>&nbsp;
                <q-btn no-caps dense class="q-px-xs" color="primary" label="Go To" @click="goToSection('compareTab', 'compareHowTo')" />).
              </p>
              <center>
                <q-img
                  class="shadow-1"
                  src="documentation/fig17.png"
                  style="max-width:800px"
                />
              </center>

              <br>
              <q-separator spaced inset />
              <br>

              <p>
                <span class="text-bold" id="searchPredictions">1.2 Predictions</span><br>
                As to help users to interpret the molecular/biological function of specific miRNA modification sites, MiREDiBase provides thermodynamic of the miRNA
                stem-loop secondary structure and functional predicions of edited miRNAs.<br><br>

                <span class="text-bold" id="searchThermodynamicPrediction">1.2.1 Thermodynamic prediction</span><br>
                Thermodynamic predictions were computed by the RNAfold tool of the ViennaRNA package, and are very simple to interpret.<br><br>

                For each editing site falling into the pre-miRNA primary sequence, a minimum free energy (MFE) secondary structure was realized for both the wild-type
                and edited version of the miRNA transcript.
              </p>
              <center>
                <q-img
                  class="shadow-1"
                  src="documentation/fig18.png"
                  style="max-width:800px"
                />
              </center>
              <br><br>

              <p>
                The positional entropy for both versions of the transcripts is represented by a standardized color scale. The color legend is reported at the bottom
                left of the MFE structure. Finally, the calculated MFE and prediction accuracy level are provided at the bottom of the "Thermodynamic prediction" panel.
              </p>
              <center>
                <q-img
                  class="shadow-1"
                  src="documentation/fig19.png"
                  style="max-width:800px"
                />
              </center>
              <br><br>

              <p>
                <span class="text-bold" id="searchIsoTarPredictions">1.2.2 isoTar predictions</span><br>
                Single nucleotide substitutions in the primary miRNA sequence can lead to functional consequences by causing a shift in the set of miRNA targets.
                Thus, MiREDiBase includes an entire section dedicated to miRNA-targeting predictions, performed by using our web-based containerized application isoTar.
              </p>
              <center>
                <q-img
                  class="shadow-1"
                  src="documentation/fig20.png"
                  style="max-width:800px"
                />
              </center>
              <br><br>

              <p>
                The two tables below provide greater details about the predicted targets, including the gene biotype and the consensus for each predicted miRNA target -
                minimum is 1; maximum is 5. These additional tables are exportable as well.
              </p>
              <center>
                <q-img
                  class="shadow-1"
                  src="documentation/fig21.png"
                  style="max-width:800px"
                />
              </center>

              <br>
              <q-separator spaced inset />
              <br>

              <p>
                <span class="text-bold" id="searchIsoTarFunctionalPredictions">1.2.3 Functional prediction</span><br>
                As in the case of the "isoTar predictions" section, the initial screen of the "Functional prediction" section
                only presents a descriptive box on the top side. Click the "Load enrichment results" to load results from our server.
              </p>
              <center>
                <q-img
                  class="shadow-1"
                  src="documentation/fig22.png"
                  style="max-width:800px"
                />
              </center>
              <br><br>

              <p>
                The results in this section derive from Gene Ontology (GO) and pathway analysis performed by isoTar.<br><br>
                The GO section is in turn composed of three subsections, namely "Biological processes", "Cellular components", and "Molecular function". You can switch the subsections
                by clicking the respective selecting box. For each subsection, the page will display three distinct summary tables, containing (i) the unique list of predicted GO terms
                for the wild-type miRNA, (ii) the shared list of GO terms for the two miRNA version, and (iii) the unique list of GO terms for the edited miRNA, from left to right,
                respectively. The summary tables are exportable independently from each other.
              </p>
              <center>
                <q-img
                  class="shadow-1"
                  src="documentation/fig23.png"
                  style="max-width:800px"
                />
              </center>
              <br><br>

              <p>
                Similarly to miRNA-target predictions, all the results included in the three summary tables are reported in two additional tables below. These provide additional
                information, including the list of predicted miRNA targets involved in each GO term and P-values.
              </p>
              <center>
                <q-img
                  class="shadow-1"
                  src="documentation/fig24.png"
                  style="max-width:800px"
                />
              </center>
              <br><br>

              <p>
                The same format is found in the "Pathway" section below.
              </p>
              <center>
                <q-img
                  class="shadow-1"
                  src="documentation/fig25.png"
                  style="max-width:800px"
                />
              </center>
              <br><br>

            </q-tab-panel>

            <q-tab-panel name="compareTab">
              <p class="text-h6 text-weight-light text-justify">How to use <i>Compare</i>.</p>

              <p>
                <span class="text-bold" id="compareHowTo">Comparing editing levels in adverse vs. normal conditions</span><br>
                Certain RNA editing sites can be differentially edited in adverse vs normal condition. Hence, editing of specific RNA sites might
                represent a biomarker of disease. For this reason, MiREDiBase is provided of a dedicated section that gives the opportunity to
                evidence trends in editing levels of specific RNA editing sites, when comparing matched adverse vs. normal conditions.

                In the "Compare" section, you can use the "Compare form" to retrieve intra-study comparisons of editing levels of specific miRNA editing sites.
              </p>
              <center>
                <q-img
                  class="shadow-1"
                  src="documentation/fig26.png"
                  style="max-width:800px"
                />
              </center>
              <br><br>

              <p>
                <span class="text-bold" id="compareForm">2.1 Compare Form</span><br>
                After the compare form has showed up, select an organism and specify the editing type. Then, provide either a disease or a stem-loop name.
                The search will be activated by clicking the "Submit" button.<br><br>
                NOTE: The "Disease" and "stem-loop" fields are mutually exclusive. Once one of these fields has been filled, the other one will be automatically disactivated.
              </p>
              <center>
                <q-img
                  class="shadow-1"
                  src="documentation/fig27.png"
                  style="max-width:800px"
                />
              </center>
              <br><br>

              <p>
                If you perform the search by selecting a stem-loop, MiREDiBase will show comparisons for editing sites falling along the primary sequence of the selected
                stem-loop. Comparisons will be made across editing sites identified in different adverse conditions.<br><br>
                If you perform the search by selecting a disease, MiREDiBase will show comparisons for editing sites detected in the specified pathological condition -
                assuming that editing levels were reported also for the matched normal condition in the same study. Comparisons will be made across editing sites falling
                into different stem-loops.
              </p>
              <center>
                <q-img
                  class="shadow-1"
                  src="documentation/fig28.png"
                  style="max-width:800px"
                />
              </center>
              <br><br>

              <p>
                As a result, MiREDiBase will return an exportable table containing the list of retrieved intra-study comparisons.<br><br>
                Here, you can observe differences in editing levels of single editing sites in adverse vs. normal conditions by comparing the arithmetic means of editing
                levels reported for each condition. The arithmetic means, reported under the "Avg. (%) Editing Level" columns, were extracted from the respective studies.
                Row by row, the highest numerical value is colored in orange, while the lowest one is colored in black.
              </p>
              <center>
                <q-img
                  class="shadow-1"
                  src="documentation/fig29.png"
                  style="max-width:800px"
                />
              </center>
              <br><br>

            </q-tab-panel>

            <q-tab-panel class="text-weight-light" name="restApiTab">
              <p class="text-h6 text-weight-light" id="restfulHowTo">MiREDiBase <i>RESTful API</i>.</p>
              <p>
                This section explains how users can interact with the MiREDiBase RESTful  (REpresentational State Transfer)
                Web Service to retrieve data used throughout the MiREDiBase Web Application. The RESTful Web Service provides
                a collection of APIs (Application Program Interface) to explore the MiREDiBase database through simple HTTP calls
                (Hypertext Transfer Protocol). APIs allow users to import MiREDiBase data directly into their code, as the
                MiREDiBase APIs are independent of any Programming Language. APIs data are compliant to the JSON (JavaScript
                Object Notation) data format.
              </p>
              <br>

              <p>
                MiREDiBase RESTful API(s). Click on a specific API to show its interface to play with it.
              </p>
              <center>
                <q-img
                  class="shadow-1"
                  src="documentation/fig30.png"
                  style="max-width:800px"
                />
              </center>
              <br><br>

              <p>
                The API interface is composed of different sections:
                <ul>
                  <li>A "Parameters" section, which eventually reports an example of parameters required by the API.</li>
                  <li>A "Try it out" button to allow users to customize the API.</li>
                  <li>An "Example value" section reporting the API data format returned.</li>
                  <li>An "Execute" button to run the API.</li>
                </ul>
              </p>
              <center>
                <q-img
                  class="shadow-1"
                  src="documentation/fig31.png"
                  style="max-width:800px"
                />
              </center>
              <br><br>

              <p>
                An example of API output. Here, the specified API returns a list of organisms currently available.
              </p>
              <center>
                <q-img
                  class="shadow-1"
                  src="documentation/fig32.png"
                  style="max-width:800px"
                />
              </center>
              <br><br>

              <p>
                An example of API, in which users can customize its parameters. In this example, we request a list
                of miRNA(s) associated with the "human" organism.
              </p>
              <center>
                <q-img
                  class="shadow-1"
                  src="documentation/fig33.png"
                  style="max-width:800px"
                />
              </center>
              <br><br>

              <p>
                By clicking on the "Try it out" button, the system allows users to customize the request body example.
              </p>
              <center>
                <q-img
                  class="shadow-1"
                  src="documentation/fig34.png"
                  style="max-width:800px"
                />
              </center>
              <br><br>

              <p>
                The API results.
              </p>
              <center>
                <q-img
                  class="shadow-1"
                  src="documentation/fig35.png"
                  style="max-width:800px"
                />
              </center>
              <br><br>

            </q-tab-panel>
          </q-tab-panels>
        </q-card>
      </div>
    </div>
  </q-page>
</template>

<script>
export default {
  name: 'Help',
  data () {
    return {
      panel: 'searchTab'
    }
  },
  methods: {

    goToSection (panelId, elementId) {
      this.panel = panelId
      this.$utils.scrollToElement(elementId)
    }

  }
}
</script>
