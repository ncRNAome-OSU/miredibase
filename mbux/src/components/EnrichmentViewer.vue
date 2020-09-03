<template>
  <div v-if="isObjectNotEmpty(snvData)">
    <q-card
      class="bg-grey-1"
      elevation
    >
      <q-card-section
        class="text-h5 text-weight-bold text-weight-light bg-deep-orange-7 text-white"
      >
        <div>
          <q-icon name="star" /> GO Terms
        </div>
      </q-card-section>

      <q-card-section>
        <q-option-group
          v-model="goTermTab"
          inline
          :options="[
            { label: 'Biological Process (BP)', value: 'goBpTab' },
            { label: 'Cellular Component (CC)', value: 'goCcTab' },
            { label: 'Molecular Function (MF)', value: 'goMfTab' }
          ]"
        />

        <q-tab-panels
          flat
          v-model="goTermTab"
          class="bg-grey-1"
        >
          <q-tab-panel name="goBpTab">
            <p class="text-weight-light text-h6">Biological Process (BP)</p>

            <snv-venn
              :snv-data="snvData.target_enrichment.go"
              :columns="table.goSubtableColumns"
              enrichment-type="go"
              enrichment-subtype="bp"
              wildtype-unique-title="Wild-type unique GO Terms"
              edited-unique-title="Edited unique GO Terms"
              intersection-title="Wild-type/Edited common GO Terms"
              badge-color="light-blue"
              tooltip-wildtype-unique-text="List of putative GO terms regulated by the wild-type miRNA. Results can be ordered by GO term or name. Click on the purple inscriptions to access external online resources."
              tooltip-edited-unique-text="List of putative GO terms regulated by both miRNA versions. Results can be ordered by GO term or name. Click on the purple inscriptions to access external online resources."
              tooltip-intersection-text="List of putative GO terms regulated by both miRNA versions. Results can be ordered by GO term or name. Click on the purple inscriptions to access external online resources."
            />

            <enrichment-table-viewer
              :title="`${snvData.mirna} (wild-type) target enrichment`"
              :snv-data="snvData.target_enrichment.go.bp.wildtype"
              :columns="table.goTableColumns"
              enrichment-type="go"
              enrichment-subtype="bp"
              first-columns-header-color="primary"
              row-key="name"
              :is-downloadable="table.isDownloadable"
              tooltip-text="Results can be ordered by GO term, GO name, Gene name, or (adjusted) P-value. Click on the purple inscriptions to access external online resources."
            />

            <br>

            <enrichment-table-viewer
              :title="`${snvData.mirna} (${prettifySnvType(snvData.mod_type)}, position ${snvData.mirna_local_pos}) target enrichment`"
              :snv-data="snvData.target_enrichment.go.bp.edited"
              :columns="table.goTableColumns"
              enrichment-type="go"
              enrichment-subtype="bp"
              first-columns-header-color="primary"
              row-key="name"
              :is-downloadable="table.isDownloadable"
              tooltip-text="Results can be ordered by GO term, GO name, Gene name, or (adjusted) P-value. Click on the purple inscriptions to access external online resources."
            />

          </q-tab-panel>

          <q-tab-panel name="goCcTab">
            <p class="text-weight-light text-h6">Cellular Component (CC)</p>

            <snv-venn
              :snv-data="snvData.target_enrichment.go"
              :columns="table.goSubtableColumns"
              enrichment-type="go"
              enrichment-subtype="cc"
              wildtype-unique-title="Wild-type unique GO Terms"
              edited-unique-title="Edited unique GO Terms"
              intersection-title="Wild-type/Edited common GO Terms"
              badge-color="green"
              tooltip-wildtype-unique-text="List of putative GO terms regulated by the wild-type miRNA. Results can be ordered by GO term or name. Click on the purple inscriptions to access external online resources."
              tooltip-edited-unique-text="List of putative GO terms regulated by both miRNA versions. Results can be ordered by GO term or name. Click on the purple inscriptions to access external online resources."
              tooltip-intersection-text="List of putative GO terms regulated by both miRNA versions. Results can be ordered by GO term or name. Click on the purple inscriptions to access external online resources."
            />

            <enrichment-table-viewer
              :title="`${snvData.mirna} (wild-type) target enrichment`"
              :snv-data="snvData.target_enrichment.go.cc.wildtype"
              :columns="table.goTableColumns"
              enrichment-type="go"
              enrichment-subtype="cc"
              first-columns-header-color="primary"
              row-key="name"
              :is-downloadable="table.isDownloadable"
              tooltip-text="Results can be ordered by GO term, GO name, Gene name, or (adjusted) P-value. Click on the purple inscriptions to access external online resources."
            />

            <br>

            <enrichment-table-viewer
              :title="`${snvData.mirna} (${prettifySnvType(snvData.mod_type)}, position ${snvData.mirna_local_pos}) target enrichment`"
              :snv-data="snvData.target_enrichment.go.cc.edited"
              :columns="table.goTableColumns"
              enrichment-type="go"
              enrichment-subtype="cc"
              first-columns-header-color="primary"
              row-key="name"
              :is-downloadable="table.isDownloadable"
              tooltip-text="Results can be ordered by GO term, GO name, Gene name, or (adjusted) P-value. Click on the purple inscriptions to access external online resources."
            />

          </q-tab-panel>

          <q-tab-panel name="goMfTab">
            <p class="text-weight-light text-h6">Molecular Function (MF)</p>

            <snv-venn
              :snv-data="snvData.target_enrichment.go"
              :columns="table.goSubtableColumns"
              enrichment-type="go"
              enrichment-subtype="mf"
              wildtype-unique-title="Wild-type unique GO Terms"
              edited-unique-title="Edited unique GO Terms"
              intersection-title="Wild-type/Edited common GO Terms"
              badge-color="red"
              tooltip-wildtype-unique-text="List of putative GO terms regulated by the wild-type miRNA. Results can be ordered by GO term or name. Click on the purple inscriptions to access external online resources."
              tooltip-edited-unique-text="List of putative GO terms regulated by both miRNA versions. Results can be ordered by GO term or name. Click on the purple inscriptions to access external online resources."
              tooltip-intersection-text="List of putative GO terms regulated by both miRNA versions. Results can be ordered by GO term or name. Click on the purple inscriptions to access external online resources."
            />

            <enrichment-table-viewer
              :title="`${snvData.mirna} (wild-type) target enrichment`"
              :snv-data="snvData.target_enrichment.go.mf.wildtype"
              :columns="table.goTableColumns"
              enrichment-type="go"
              enrichment-subtype="mf"
              first-columns-header-color="primary"
              row-key="name"
              :is-downloadable="table.isDownloadable"
              tooltip-text="Results can be ordered by GO term, GO name, Gene name, or (adjusted) P-value. Click on the purple inscriptions to access external online resources."
            />

            <br>

            <enrichment-table-viewer
              :title="`${snvData.mirna} (${prettifySnvType(snvData.mod_type)}, position ${snvData.mirna_local_pos}) target enrichment`"
              :snv-data="snvData.target_enrichment.go.mf.edited"
              :columns="table.goTableColumns"
              enrichment-type="go"
              enrichment-subtype="mf"
              first-columns-header-color="primary"
              row-key="name"
              :is-downloadable="table.isDownloadable"
              tooltip-text="Results can be ordered by GO term, GO name, Gene name, or (adjusted) P-value. Click on the purple inscriptions to access external online resources."
            />

          </q-tab-panel>
        </q-tab-panels>
      </q-card-section>
    </q-card>

    <br>

    <q-card
      class="bg-grey-1"
      elevation
    >
      <q-card-section
        class="text-h5 text-weight-bold text-weight-light bg-deep-orange-7 text-white"
      >
        <div>
          <q-icon name="star" /> Pathways
        </div>
      </q-card-section>

      <q-card-section>
        <q-option-group
          v-model="pathwayTab"
          inline
          :options="[
            { label: 'KEGG', value: 'keggTab' },
            { label: 'Reactome', value: 'reactomeTab' },
          ]"
        />

        <q-tab-panels
          flat
          v-model="pathwayTab"
          class="bg-grey-1"
        >
          <q-tab-panel name="keggTab">
            <p class="text-weight-light  text-h6">KEGG</p>

            <snv-venn
              :snv-data="snvData.target_enrichment.kegg"
              :columns="table.pathwaySubtableColumns"
              enrichment-type="kegg"
              wildtype-unique-title="Wild-type unique Pathways"
              edited-unique-title="Edited unique Pathways"
              intersection-title="Wild-type/Edited common Pathways"
              badge-color="light-blue"
              tooltip-wildtype-unique-text="List of putative KEGG pathways regulated by the wild-type miRNA. Results can be ordered by the Pathway ID or name. Click on the purple inscriptions to access external online resources."
              tooltip-edited-unique-text="List of putative KEGG pathways regulated by both miRNA versions. Results can be ordered by the Pathway ID or name. Click on the purple inscriptions to access external online resources."
              tooltip-intersection-text="List of putative KEGG pathways regulated by the edited miRNA. Results can be ordered by the Pathway ID or name. Click on the purple inscriptions to access external online resources."
            />

            <enrichment-table-viewer
              :title="`${snvData.mirna} (wild-type) target enrichment`"
              :snv-data="snvData.target_enrichment.kegg.wildtype"
              :columns="table.pathwayTableColumns"
              enrichment-type="kegg"
              first-columns-header-color="primary"
              row-key="name"
              :is-downloadable="table.isDownloadable"
              tooltip-text="Results can be ordered by Pathway ID, Pathway name, Gene name, or (adjusted) P-value. Click on the purple inscriptions to access external online resources."
            />

            <br>

            <enrichment-table-viewer
              :title="`${snvData.mirna} (${prettifySnvType(snvData.mod_type)}, position ${snvData.mirna_local_pos}) target enrichment`"
              :snv-data="snvData.target_enrichment.kegg.edited"
              :columns="table.pathwayTableColumns"
              enrichment-type="kegg"
              first-columns-header-color="primary"
              row-key="name"
              :is-downloadable="table.isDownloadable"
              tooltip-text="Results can be ordered by Pathway ID, Pathway name, Gene name, or (adjusted) P-value. Click on the purple inscriptions to access external online resources."
            />

          </q-tab-panel>

          <q-tab-panel name="reactomeTab">
            <p class="text-weight-light  text-h6">Reactome</p>

            <snv-venn
              :snv-data="snvData.target_enrichment.reactome"
              :columns="table.pathwaySubtableColumns"
              enrichment-type="reactome"
              wildtype-unique-title="Wild-type unique Pathways"
              edited-unique-title="Edited unique Pathways"
              intersection-title="Wild-type/Edited common Pathways"
              badge-color="light-blue"
              tooltip-wildtype-unique-text="List of putative Reactome pathways regulated by the wild-type miRNA. Results can be ordered by the Pathway ID or name. Click on the purple inscriptions to access external online resources."
              tooltip-edited-unique-text="List of putative Reactome pathways regulated by both miRNA versions. Results can be ordered by the Pathway ID or name. Click on the purple inscriptions to access external online resources."
              tooltip-intersection-text="List of putative Reactome pathways regulated by the edited miRNA. Results can be ordered by the Pathway ID or name. Click on the purple inscriptions to access external online resources."
            />

            <enrichment-table-viewer
              :title="`${snvData.mirna} (wild-type) target enrichment`"
              :snv-data="snvData.target_enrichment.reactome.wildtype"
              :columns="table.pathwayTableColumns"
              enrichment-type="reactome"
              first-columns-header-color="primary"
              row-key="name"
              :is-downloadable="table.isDownloadable"
              tooltip-text="Results can be ordered by Pathway ID, Pathway name, Gene name, or (adjusted) P-value. Click on the purple inscriptions to access external online resources."
            />

            <br>

            <enrichment-table-viewer
              :title="`${snvData.mirna} (${prettifySnvType(snvData.mod_type)}, position ${snvData.mirna_local_pos}) target enrichment`"
              :snv-data="snvData.target_enrichment.reactome.edited"
              :columns="table.pathwayTableColumns"
              enrichment-type="reactome"
              first-columns-header-color="primary"
              row-key="name"
              :is-downloadable="table.isDownloadable"
              tooltip-text="Results can be ordered by Pathway ID, Pathway name, Gene name, or (adjusted) P-value. Click on the purple inscriptions to access external online resources."
            />

          </q-tab-panel>

        </q-tab-panels>
      </q-card-section>
    </q-card>
  </div>
</template>

<script>
import SnvVenn from 'components/SnvVenn'
import EnrichmentTableViewer from 'components/EnrichmentTableViewer'

export default {
  name: 'EnrichmentViewer',
  components: {
    SnvVenn,
    EnrichmentTableViewer
  },
  props: {
    snvData: {
      type: Object,
      required: true
    }
  },
  data () {
    return {
      goTermTab: 'goBpTab',
      pathwayTab: 'keggTab',
      table: {
        isDownloadable: true,
        goTableColumns: [
          {
            name: 'name',
            required: true,
            label: '',
            align: 'center',
            field: row => row.name,
            sortable: false,
            classes: 'bg-grey-2 ellipsis',
            format: val => `${val}`,
            headerClasses: 'text-white'
          },
          {
            name: 'goId',
            label: 'GO Term',
            field: 'go_id',
            sortable: true,
            align: 'center'
          },
          {
            name: 'goName',
            label: 'GO Name',
            field: 'go_name',
            sortable: true,
            align: 'left'
          },
          {
            name: 'pvalue',
            label: 'Pvalue',
            field: 'pvalue',
            sortable: true,
            align: 'center',
            format: val => `${val.toExponential()}`,
            sort: (a, b, rowA, rowB) => parseFloat(a) - parseFloat(b)
          },
          {
            name: 'adjpvalue',
            label: 'Adj-Pvalue (BH)',
            field: 'adj_pvalue',
            sortable: true,
            align: 'center',
            format: val => `${val.toExponential()}`,
            sort: (a, b, rowA, rowB) => parseFloat(a) - parseFloat(b)
          },
          {
            name: 'targetsList',
            label: 'Targets list',
            field: 'targets_list',
            sortable: true,
            align: 'left'
          }
        ],
        goSubtableColumns: [
          {
            name: 'name',
            required: true,
            label: '',
            align: 'center',
            field: row => row.name,
            sortable: false,
            classes: 'bg-grey-2 ellipsis',
            format: val => `${val}`,
            headerClasses: 'text-white'
          },
          {
            name: 'goId',
            label: 'GO Term',
            field: 'go_id',
            sortable: true,
            align: 'center'
          },
          {
            name: 'goName',
            label: 'GO Name',
            field: 'go_name',
            sortable: true,
            align: 'left'
          }
        ],
        pathwayTableColumns: [
          {
            name: 'name',
            required: true,
            label: '',
            align: 'center',
            field: row => row.name,
            sortable: false,
            classes: 'bg-grey-2 ellipsis',
            format: val => `${val}`,
            headerClasses: 'text-white'
          },
          {
            name: 'pathwayId',
            label: 'Pathway ID',
            field: 'pathway_id',
            sortable: true,
            align: 'center'
          },
          {
            name: 'pathwayName',
            label: 'Pathway Name',
            field: 'pathway_name',
            sortable: true,
            align: 'left'
          },
          {
            name: 'pvalue',
            label: 'Pvalue',
            field: 'pvalue',
            sortable: true,
            align: 'center',
            format: val => `${val.toExponential()}`,
            sort: (a, b, rowA, rowB) => parseFloat(a) - parseFloat(b)
          },
          {
            name: 'adjpvalue',
            label: 'Adj-Pvalue (BH)',
            field: 'adj_pvalue',
            sortable: true,
            align: 'center',
            format: val => `${val.toExponential()}`,
            sort: (a, b, rowA, rowB) => parseFloat(a) - parseFloat(b)
          },
          {
            name: 'targetsList',
            label: 'Targets list',
            field: 'targets_list',
            sortable: true,
            align: 'left'
          }
        ],
        pathwaySubtableColumns: [
          {
            name: 'name',
            required: true,
            label: '',
            align: 'center',
            field: row => row.name,
            sortable: false,
            classes: 'bg-grey-2 ellipsis',
            format: val => `${val}`,
            headerClasses: 'text-white'
          },
          {
            name: 'pathwayId',
            label: 'Pathway ID',
            field: 'pathway_id',
            sortable: true,
            align: 'center'
          },
          {
            name: 'pathwayName',
            label: 'Pathway Name',
            field: 'pathway_name',
            sortable: true,
            align: 'left'
          }
        ]
      }
    }
  },
  mounted () {},
  computed: {},
  methods: {

    isObjectNotEmpty (value) {
      return this.$utils.isObjectNotEmpty(value)
    },

    prettifySnvType (value) {
      return this.$utils.prettifySnvType(value)
    }

  }
}
</script>
