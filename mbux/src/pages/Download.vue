<template>
  <q-page padding>
    <span class="text-h5 text-weight-light">Download</span>
    <q-separator spaced />
    <p class="text-weight-light">
      <q-btn dense no-caps type="a" color="primary" icon="cloud_download" label="Download" class="q-px-xs" href="db/MiREDiBase_v1.0.xlsx" target="_blank" />
      Here you can download the complete list of unique A-to-I and C-to-U miRNA modification sites (validated and putative) in human and primates included
      in the current version of the database (v1.0).
    </p>
  </q-page>
</template>

<script>
export default {
  name: 'Download',
  data () {
    return {}
  }
}
</script>
