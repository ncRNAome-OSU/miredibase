<template>
  <q-page padding>
    <!-- content -->
    <span class="text-h5 text-weight-light">Changelog</span>
    <q-separator spaced />

    <q-timeline layout="comfortable" side="right" color="secondary">
      <q-timeline-entry heading>Timeline</q-timeline-entry>

      <q-timeline-entry heading>September, 2020</q-timeline-entry>

      <q-timeline-entry
        title="MiREDiBase v1.0"
        subtitle="September 1, 2020"
        side="left"
        color="orange"
        icon="done_all"
      >
        <div>
          First release.
        </div>
      </q-timeline-entry>

    </q-timeline>
  </q-page>
</template>

<script>
export default {
  // name: 'PageName',
  data () {
    return {
      layout: 'dense',
      side: 'right'
    }
  }
}
</script>
