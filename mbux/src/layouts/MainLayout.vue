<template>
  <q-layout
    view="hHh Lpr lFf"
    class="bg-grey-1"
  >
    <q-header
      class="text-grey-10"
    >
      <!--style="background: radial-gradient(circle, #35a2ff 0%, #014a88 100%)"-->
      <q-toolbar
        class="text-grey-10 shadow-2 bg-grey-3"
      >
        <q-btn
          flat
          dense
          round
          icon="menu"
          aria-label="Menu"
          @click="leftDrawerOpen = !leftDrawerOpen"
          color="grey-10"
        />

        <q-toolbar-title
          class="text-weight-light"
        >
          <q-btn
            no-caps
            flat
            type="a"
            href="/miredibase"
            size="md"
            class="q-ma-xs text-weight-light"
          >
            MiREDiBase
            <q-badge color="red" dense floating>1.0</q-badge>
          </q-btn>
        </q-toolbar-title>
        <q-btn
          flat
          dense
          no-caps
          type="a"
          href="https://www.osu.edu"
          target="_blank"
          class="text-weight-light"
        >
          &copy; The Ohio State University - {{ getCurrentYear() }}
        </q-btn>
      </q-toolbar>
    </q-header>

    <q-drawer
      v-model="leftDrawerOpen"
      show-if-above

      :mini="miniState"
      @mouseover="miniState = false"
      @mouseout="miniState = true"

      :width="350"
      bordered
      content-class="bg-white"
    >
      <q-list
        padding
      >
        <internal-link
          v-for="link in mainMenuLinks"
          :key="link.title"
          v-bind="link"
        />

         <essential-link
          v-for="link in externalLinks"
          :key="link.title"
          v-bind="link"
        />
      </q-list>
    </q-drawer>

    <q-page-container>
      <router-view />
    </q-page-container>
    <q-page-scroller position="bottom-right" :scroll-offset="150" :offset="[18, 18]">
      <q-btn fab icon="keyboard_arrow_up" color="primary" />
    </q-page-scroller>
  </q-layout>
</template>

<script>
import InternalLink from 'components/InternalLink'
import EssentialLink from 'components/EssentialLink'

// import { format } from 'quasar'
// Destructuring to keep only what is needed
// const { capitalize } = format

export default {
  name: 'MainLayout',
  components: {
    InternalLink,
    EssentialLink
  },
  data () {
    return {
      leftDrawerOpen: false,
      miniState: true,
      mainMenuLinks: [
        {
          title: 'Homepage',
          caption: 'Go to the homepage',
          icon: 'home',
          link: '/'
        },
        {
          title: 'Search',
          caption: 'Search for RNA Editing Sites in microRNAs',
          icon: 'search',
          link: '/search'
        },
        {
          title: 'Compare',
          caption: 'Case versus Control',
          icon: 'timeline',
          link: '/compare'
        },
        {
          title: 'Statistics',
          caption: 'MiREDiBase data statistics',
          icon: 'insert_chart',
          link: '/stats'
        },
        {
          title: 'Download',
          caption: 'Get the latest dataset',
          icon: 'cloud_download',
          link: '/download'
        },
        {
          title: 'Help',
          caption: 'MiREDiBase documentation',
          icon: 'help',
          link: '/help'
        },
        {
          title: 'Changelog',
          caption: 'System updates',
          icon: 'build',
          link: '/changelog'
        },
        {
          title: 'Contact Us',
          caption: 'Who we are',
          icon: 'email',
          link: '/contactus'
        }
      ],
      externalLinks: [
        {
          title: 'MiREDiBase APIs',
          caption: 'Go to the APIs for data retrieving',
          icon: 'call_split',
          link: 'https://ncrnaome.osumc.edu/miredibaseapi/docs'
        }
      ]
    }
  },
  methods: {
    getCurrentYear () {
      return new Date().getFullYear()
    }
  }

}
</script>
