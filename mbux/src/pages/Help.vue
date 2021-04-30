<template>
  <q-page padding>
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
                Searching into MiREDiBase has been rendered pretty simple. It requires no bioinformatics skills to perform accurate searches
                across the database, and its user-friendly interface allows to keep track of each search step, as to improve your experience.<br><br>

                Once in the "Search" section, you can retrieve validated and putative miRNA editing sites by providing specific information in the "Search form".
              </p>
              <center>
                <q-img
                  class="shadow-0"
                  src="documentation/fig1.png"
                  style="max-width:800px"
                />
              </center>

              <br>
              <q-separator spaced inset />
              <br>

              <p>
                <span class="text-bold" id="searchForm">1.1 Search Form</span><br>
                After the search form has shown up, you can explore RNA modifications using the basic form or the advanced one.
                The basic form provides a simple way to query RNA modifications associated with a specific miRNA or stem-loop.
                In the advanced form, you can filter by an organism or editing type. Then, you can provide a genomic region or
                a stem-loop/miRNA name in the specific field of the "search form". You can also optionally specify a biological
                source. Finally, click on the "Submit" button to show the query results.<br><br>

                NOTE: The "genomic region," "stem-loop," and "miRNA" fields are mutually exclusive. Once one of these fields has
                been filled, the others will be automatically deactivated. Instead, the "biological source" field allows filtering
                results by biological tissues or cell lines.
              </p>
              <center>
                <q-img
                  class="shadow-0"
                  src="documentation/fig2.1.png"
                  style="max-width:800px"
                />
                <br><br>
                <q-img
                  class="shadow-0"
                  src="documentation/fig2.2.png"
                  style="max-width:800px"
                />
              </center>
              <br><br>

              <p>
                Search by genomic region can include an entire chromosome or a restricted chromosome region. To retrieve editing
                sites falling into a chromosome, select the chromosome number in the field "Chromosome" and then click the "Submit"
                button. To retrieve editing sites falling into more restricted genomic regions, select a chromosome and then type
                a start and end position in the specific fields. Finally, choose the strand (+ or -).
              </p>
              <center>
                <q-img
                  class="shadow-0"
                  src="documentation/fig3.png"
                  style="max-width:800px"
                />
              </center>
              <br><br>

              <p>
                <b>Note</b>: The end position must be greater than the start position. If the end position is equal to or minor than the
                start position, an error message will appear in the search form.
              </p>
              <center>
                <q-img
                  class="shadow-0"
                  src="documentation/fig4.png"
                  style="max-width:800px"
                />
              </center>
              <br><br>

              <p>
                To retrieve editing events reported for individual miRNAs, click either on the "stem-loop" or "miRNA" field.
                A drop-down menu containing the complete list of miRNAs will show up. You can select the miRNA of interest
                from the drop-down menu or type a miRNA name and then select the miRNA of interest. Click on "Submit" to launch the search.
              </p>
              <center>
                <q-img
                  class="shadow-0"
                  src="documentation/fig5.png"
                  style="max-width:800px"
                />
              </center>
              <br><br>

              <p>
                Suppose you want to limit your search to one or a few biological sources. In that case, you can select one or multiple biological
                sources from the drop-down menu contained in the "biological source" field. As a consequence, MiREDiBase will return miRNA
                modification sites detected in the selected tissues/cell lines.
              </p>
              <center>
                <q-img
                  class="shadow-0"
                  src="documentation/fig6.png"
                  style="max-width:800px"
                />
              </center>
              <br><br>

              <p>
                After submitting the search form, MiREDiBase will return a table containing the list of retrieved unique miRNA modification sites.
                The table displays general information concerning each modification site, including the genomic position and information relative
                to the stem-loop.<br><br>

                By default, the table will show five records per page. However, it is possible to augment the number of records established per page.
              </p>
              <center>
                <q-img
                  class="shadow-0"
                  src="documentation/fig10.png"
                  style="max-width:800px"
                />
              </center>
              <br><br>

              <p>
                Information about the miRNA stem-loop is subdivided as reported in the table.
              </p>
              <center>
                <q-img
                  class="shadow-0"
                  src="documentation/fig12.png"
                  style="max-width:800px"
                />
              </center>
              <br><br>

              <p>
                Results can be filtered by typing appropriate keywords or numerical values in the "Search within the table" (e.g., a miRNA name, a
                genomic position, chromosome number, etc.). Results can be downloaded as a .CSV (comma-separated data) file by clicking the "Export"
                button.<br><br>

                Clicking the red icons on the left side of the table will open a new page containing the list of published original papers that
                have detected the selected modification site.
              </p>
              <center>
                <q-img
                  class="shadow-0"
                  src="documentation/fig13.png"
                  style="max-width:800px"
                />
              </center>
              <br><br>

              <p>
                The information available in the "RNA Modification site study" section.
              </p>
              <center>
                <q-img
                  class="shadow-0"
                  src="documentation/fig14.png"
                  style="max-width:800px"
                />
              </center>
              <br><br>

              <p>
                Above the "RNA Modification site studies" table, a summary bar will be displayed, summing up basic information about the selected
                editing site. Four selecting boxes are shown in between, allowing you to navigate across four distinct sections. The "RNA Modification
                site studies" table is included in the "Overview" section, which is showed by default. The other three areas are dedicated to predictive
                information and are illustrated in the following subsection (<span class="text-bold">1.2 Predictions</span>).
              </p>
              <center>
                <q-img
                  class="shadow-0"
                  src="documentation/fig15.png"
                  style="max-width:800px"
                />
              </center>
              <br><br>

              <p>
                Values in the column "Is it putative?" indicate whether an editing site is putative or not. In particular:
              </p>
                <ul>
                  <li>Yes = putative (i.e., it was detected by high-throughput sequencing methods but has never been validated by targeted methods);</li>
                  <li>No = validated (i.e., it has been validated by targeted methods at least by one study).</li>
                </ul>
              <p>
                We assumed that the presence of enzyme perturbation experiments is not enough to state that an editing site is validated. Values in the columns
                "high-throughput methods" and "targeted methods" represent the number of studies that identified the editing site in question by high-throughput
                and low-throughput sequencing, respectively.<br>
                The "enzyme perturbation" values represent the number of studies that carried out enzyme perturbation experiments to increase the reliability
                of editing site detection
              </p>
              <center>
                <q-img
                  class="shadow-0"
                  src="documentation/fig15.1.png"
                  style="max-width:800px"
                />
              </center>
              <br><br>

              <p>
                For each editing site, information about detection methods and enzyme perturbation experiments is shown in more detail under the
                "RNA modification site studies" section. Specifically:
              </p>
                <ul>
                  <li>High-throughput methods are subdivided in NGS, miR-mmPCR-seq, and RIP-seq;</li>
                  <li>Targeted methods are subdivided in Sanger sequencing, SNaPshot assay, and site-specific cleavage;</li>
                  <li>Enzyme perturbation experiments are subdivided in enzyme knockdown (KD), enzyme knockout (KO), and differential transfection.</li>
                </ul>
              <p>
                The "RNA modification site studies" section shows information regarding the functional effects on miRNA biogenesis/target-binding ability
                (see the "Functional consequences" column). In addition, it is reported the enzyme affinity for the editing site (see the "Enzyme selectivity" column).
              </p>
              <center>
                <q-img
                  class="shadow-0"
                  src="documentation/fig15.2.png"
                  style="max-width:800px"
                />
              </center>
              <br><br>

              <p>
                Clicking on the red icons on the left side of the "RNA Modification site study" table will open the "Additional info" section containing detailed
                information about the authors' findings for the selected miRNA editing site. Moreover, it displays information about detection and validation methods
                for identifying the editing site and validation methods for the eventual retargeting.
              </p>
              <center>
                <q-img
                  class="shadow-0"
                  src="documentation/fig16.png"
                  style="max-width:800px"
                />
              </center>
              <br><br>

              <p>
                <b>Note</b>: If the modification consists of nucleotide substitution, the editing level columns report the minimum (from) and the maximum (to the) value of
                the editing level for the selected editing site, according to information provided by the authors. Editing level values are rounded and shown as
                multiples of five.<br><br>

                <b>Note</b>: Ff the "Compared with" column reports a biological source (meaning that an intra-study comparison was made between adverse and normal conditions
                of the same tissue), you can find detailed information about the comparison in the "Compare" section (<span class="text-bold">2.1 Comparing editing levels in
                adverse vs. normal conditions</span>&nbsp;
                <q-btn no-caps dense class="q-px-xs" color="primary" label="Go To" @click="goToSection('compareTab', 'compareHowTo')" />).
              </p>
              <center>
                <q-img
                  class="shadow-0"
                  src="documentation/fig17.png"
                  style="max-width:800px"
                />
              </center>

              <br>
              <q-separator spaced inset />
              <br>

              <p>
                <span class="text-bold" id="searchPredictions">1.2 Predictions</span><br>
                To help users in interpreting the molecular/biological implications, MiREDiBase provides the thermodynamic of the miRNA stem-loop secondary structure and
                functional predictions of modified miRNAs.<br><br>

                <span class="text-bold" id="searchThermodynamicPrediction">1.2.1 Thermodynamic prediction</span><br>
                Thermodynamic predictions are computed via the RNAfold tool of the ViennaRNA package.<br><br>

                For each modification falling within the pre-miRNA primary sequence, minimum free energy (MFE) secondary structure is realized for both the wild-type and
                edited version of the miRNA transcript.
              </p>
              <center>
                <q-img
                  class="shadow-0"
                  src="documentation/fig18.png"
                  style="max-width:800px"
                />
              </center>
              <br><br>

              <p>
                A standardized color scale represents the positional entropy for both versions of the transcripts. The color legend is reported at the bottom left of the
                MFE structure. Finally, the calculated MFE and prediction accuracy level are provided at the bottom of the "Thermodynamic prediction" panel.
              </p>
              <center>
                <q-img
                  class="shadow-0"
                  src="documentation/fig19.png"
                  style="max-width:800px"
                />
              </center>
              <br><br>

              <p>
                <span class="text-bold" id="searchIsoTarPredictions">1.2.2 isoTar predictions</span><br>
                Single nucleotide substitutions in the primary miRNA sequence can lead to functional consequences by causing a shift in the set of miRNA targets.
                Thus, MiREDiBase includes an entire section dedicated to miRNA-targeting predictions, performed using our web-based containerized application isoTar.
              </p>
              <center>
                <q-img
                  class="shadow-0"
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
                  class="shadow-0"
                  src="documentation/fig21.png"
                  style="max-width:800px"
                />
              </center>

              <br>
              <q-separator spaced inset />
              <br>

              <p>
                <span class="text-bold" id="searchIsoTarFunctionalPredictions">1.2.3 Functional prediction</span><br>
                As in the "isoTar predictions" section, the initial screen of the "Functional prediction" section
                only presents a descriptive box on the top side. Click the "Load enrichment results" to load results from our server.
              </p>
              <center>
                <q-img
                  class="shadow-0"
                  src="documentation/fig22.png"
                  style="max-width:800px"
                />
              </center>
              <br><br>

              <p>
                The GO section is in turn composed of three subsections, namely "Biological processes," "Cellular components," and
                "Molecular function." You can switch the subsections by clicking the respective selecting box. For each subsection,
                the page will display three different summary tables, containing:

                <ol>
                  <li>The unique list of predicted GO terms for the wild-type miRNA;</li>
                  <li>The shared list of GO terms for the two miRNA versions;</li>
                  <li>The unique list of GO terms for the edited miRNA, from left to right, respectively.</li>
                </ol>
                The summary tables are exportable independently from each other.
              </p>
              <center>
                <q-img
                  class="shadow-0"
                  src="documentation/fig23.png"
                  style="max-width:800px"
                />
              </center>
              <br><br>

              <p>
                Similar to miRNA-target predictions, all the results included in the three summary tables are reported in two additional tables below. These provide additional
                information, including the list of predicted miRNA targets involved in each GO term and P-values.
              </p>
              <center>
                <q-img
                  class="shadow-0"
                  src="documentation/fig24.png"
                  style="max-width:800px"
                />
              </center>
              <br><br>

              <p>
                The exact format is found in the "Pathway" section below.
              </p>
              <center>
                <q-img
                  class="shadow-0"
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
                RNA editing sites can be differentially edited in adverse vs. normal conditions. Hence, editing of specific RNA
                sites might represent a biomarker of disease. For this reason, MiREDiBase is provided with a dedicated section
                that allows to evidence trends in editing levels of particular RNA editing sites when comparing matched adverse
                vs. normal conditions. In the "Compare" section, you can use the "Compare form" to retrieve intra-study
                comparisons of editing levels of specific miRNA editing sites.
              </p>
              <center>
                <q-img
                  class="shadow-0"
                  src="documentation/fig26.png"
                  style="max-width:800px"
                />
              </center>
              <br><br>

              <p>
                <span class="text-bold" id="compareForm">2.1 Compare Form</span><br>
                After the compare form has shown up, select an organism and specify the editing type. Then, provide either a
                disease or a stem-loop name. Finally, click on the "Submit" button to show the query results.<br><br>
                <b>Note</b>: The "Disease" and "stem-loop" fields are mutually exclusive.
              </p>
              <center>
                <q-img
                  class="shadow-0"
                  src="documentation/fig27.png"
                  style="max-width:800px"
                />
              </center>
              <br><br>

              <p>
                Perform the search by selecting a disease. MiREDiBase will show comparisons for editing sites detected in the
                specified pathological condition. Editing levels will also be reported for the matched normal condition in the
                same study. Comparisons will be made across editing sites falling into different stem-loops.<br><br>
              </p>
              <center>
                <q-img
                  class="shadow-0"
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
                  class="shadow-0"
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
                  class="shadow-0"
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
                  class="shadow-0"
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
                  class="shadow-0"
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
                  class="shadow-0"
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
                  class="shadow-0"
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
                  class="shadow-0"
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
