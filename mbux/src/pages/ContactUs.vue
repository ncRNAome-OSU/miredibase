<template>
  <q-page padding>
    <span class="text-h5 text-weight-light">Contact Us</span>
    <q-separator spaced />
    <div class="row">
      <div class="col-xs-12 col-sm-12 col-md-3 col-lg-3 q-pa-xs">
        <p class="text-weight-light text-justify">
          Equal contributors <q-icon color="deep-orange-9" name="handyman" /> <q-icon color="light-blue-9" name="star" />
        </p>
        <q-card>
          <q-card-section class="text-weight-light text-h6">
            Institutions involved in MiREDiBase.
          </q-card-section>

          <q-separator />

          <q-card-section class="flex flex-center">
            <q-btn flat dense type="a" href="https://www.osu.edu" target="_blank">
              <q-img
                class="q-ma-xs"
                src="logos/the-ohio-state-university.png"
                style="width: 90px"
              />
            </q-btn>
            <q-btn flat dense type="a" href="https://icahn.mssm.edu" target="_blank">
              <q-img
                class="q-ma-xs"
                src="logos/msmc-icahn.png"
                style="width: 58px"
              />
            </q-btn>
            <q-btn flat dense type="a" href="https://www.cpr.ku.dk" target="_blank">
              <q-img
                class="q-ma-xs"
                src="logos/novo-nordisk-foundation.png"
                style="width: 113px"
              />
            </q-btn>
            <q-btn flat dense type="a" href="https://www.istitutotumori.mi.it" target="_blank">
              <q-img
                class="q-ma-xs"
                src="logos/national-cancer-institute-of-italy.png"
                style="width: 203px"
              />
            </q-btn>
            <q-btn flat dense type="a" href="https://www.newcastle.edu.au" target="_blank">
              <q-img
                class="q-ma-xs"
                src="logos/university-of-newcastle.png"
                style="width: 80px"
              />
            </q-btn>
            <q-btn flat dense type="a" href="https://www.unict.it/en" target="_blank">
              <q-img
                class="q-ma-xs"
                src="logos/university-of-catania.png"
                style="width: 53px"
              />
            </q-btn>
            <q-btn flat dense type="a" href="https://www.vcu.edu" target="_blank">
              <q-img
                class="q-ma-xs"
                src="logos/vcu.png"
                style="width: 80px"
              />
            </q-btn>
          </q-card-section>
        </q-card>
      </div>

      <div class="col-xs-12 col-sm-12 col-md-9 col-lg-9 q-pa-xs">
        <template  v-for="item in authorsList">
          <div :key="item.name">
            <contact-item
              :bio="item.bio"
              :icon="item.icon"
              :name="item.name"
              :role="item.role"
              :department="item.department"
              :division="item.division"
              :institution="item.institution"
              :institution2="item.institution2"
              :picture="item.picture"
              :email="item.email"
            />
          </div>
        </template>

      </div>
    </div>
  </q-page>
</template>

<script>
import ContactItem from 'components/ContactItem'

export default {
  name: 'ContactUs',
  components: {
    ContactItem
  },
  data () {
    return {
      authorsList: [
        {
          name: 'Gioacchino P. Marceca, Ph.D.',
          role: '',
          department: 'Department of Clinical and Experimental Medicine',
          division: '',
          institution: 'University of Catania, Italy',
          institution2: '',
          icon: 'handyman',
          bio: 'Data collection (manual curation)',
          picture: 'contactus/gioacchino-paolo-marceca.jpg',
          email: 'gioacchinopaolo.marceca@unict.it'
        },
        {
          name: 'Rosario Distefano, Ph.D.',
          role: '',
          department: 'Department of Cancer Biology and Genetics and Comprehensive Cancer Center',
          division: 'College of Medicine',
          institution: 'The Ohio State University, Columbus, OH, USA',
          institution2: '',
          icon: 'handyman',
          bio: 'Platform design and development',
          picture: 'contactus/rosario-distefano.png',
          email: 'rosario.distefano@osumc.edu'
        },
        {
          name: 'Luisa Tomasello, Ph.D.',
          role: '',
          department: 'Department of Cancer Biology and Genetics and Comprehensive Cancer Center',
          division: 'College of Medicine',
          institution: 'The Ohio State University, Columbus, OH, USA',
          institution2: '',
          icon: '',
          bio: '',
          picture: 'contactus/luisa-tomasello.jpg',
          email: 'luisa.tomasello@osumc.edu'
        },
        {
          name: 'Alessandro Lagana\', Ph.D.',
          role: '',
          department: 'Department of Genetics and Genomic Sciences',
          division: '',
          institution: 'Icahn School of Medicine at Mount Sinai, New York, NY, USA',
          institution2: '',
          icon: '',
          bio: '',
          picture: '',
          email: 'alessandro.lagana@mssm.edu'
        },
        {
          name: 'Francesco Russo, Ph.D.',
          role: '',
          department: 'Disease Systems Biology, Novo Nordisk Foundation Center for Protein Research, Faculty of Health and Medical Sciences',
          division: '',
          institution: 'University of Copenhagen, Copenhagen, Denmark',
          institution2: '',
          icon: '',
          bio: '',
          picture: '',
          email: 'francesco.russo@cpr.ku.dk'
        },
        {
          name: 'Federica Calore, Ph.D.',
          role: '',
          department: 'Department of Cancer Biology and Genetics and Comprehensive Cancer Center',
          division: '',
          institution: 'The Ohio State University, Columbus, OH, USA',
          institution2: '',
          icon: '',
          bio: '',
          picture: '',
          email: 'federica.calore@osumc.edu'
        },
        {
          name: 'Giulia Romano, Ph.D.',
          role: '',
          department: 'Division of Pulmonary Diseases and Critical Care Medicine',
          division: '',
          institution: 'Virginia Commonwealth University, Richmond, VA, USA',
          institution2: '',
          icon: '',
          bio: '',
          picture: '',
          email: 'giulia.romano@vcuhealth.org'
        },
        {
          name: 'Marina Bagnoli, Ph.D.',
          role: '',
          department: '',
          division: '',
          institution: 'Fondazione IRCCS Istituto Nazionale dei Tumori (INT), Milan, Italy',
          institution2: '',
          icon: '',
          bio: '',
          picture: '',
          email: 'marina.bagnoli@istitutotumori.mi.it'
        },
        {
          name: 'Pierluigi Gasparini, Ph.D.',
          role: '',
          department: 'Department of Cancer Biology and Genetics and Comprehensive Cancer Center',
          division: '',
          institution: 'The Ohio State University, Columbus, OH, USA',
          institution2: 'University of Newcastle, Newcastle, New South Wales, Australia',
          icon: '',
          bio: '',
          picture: '',
          email: 'pierluigi.gasparini@osumc.edu'
        },
        {
          name: 'Alfredo Ferro, Ph.D.',
          role: '',
          department: 'Department of Clinical and Experimental Medicine',
          division: '',
          institution: 'University of Catania, Catania, Italy',
          institution2: '',
          icon: '',
          bio: '',
          picture: '',
          email: 'ferro@dmi.unict.it'
        },
        {
          name: 'Mario Acunzo, Ph.D.',
          role: '',
          department: 'Division of Pulmonary Diseases and Critical Care Medicine',
          division: '',
          institution: 'Virginia Commonwealth University, Richmond, VA, USA',
          institution2: '',
          icon: '',
          bio: '',
          picture: '',
          email: 'mario.acunzo@vcuhealth.org'
        },
        {
          name: 'Qin Ma, Ph.D.',
          role: '',
          department: 'Department of Biomedical Informatics, College of Medicine',
          division: '',
          institution: 'The Ohio State University, Columbus, OH, USA',
          institution2: '',
          icon: '',
          bio: '',
          picture: '',
          email: 'qin.ma@osumc.edu'
        },
        {
          name: 'Carlo Maria Croce, M.D.',
          role: '',
          department: 'Department of Cancer Biology and Genetics and Comprehensive Cancer Center',
          division: 'College of Medicine',
          institution: 'The Ohio State University, Columbus, OH, USA',
          institution2: '',
          icon: 'star',
          bio: 'Project leader - Corresponding author',
          picture: 'contactus/carlo-maria-croce.png',
          email: 'carlo.croce@osumc.edu'
        },
        {
          name: 'Giovanni Nigita, Ph.D.',
          role: '',
          department: 'Department of Cancer Biology and Genetics and Comprehensive Cancer Center',
          division: 'College of Medicine',
          institution: 'The Ohio State University, Columbus, OH, USA',
          institution2: '',
          icon: 'star',
          bio: 'Project leader - Corresponding author',
          picture: 'contactus/giovanni-nigita.jpg',
          email: 'giovanni.nigita@osumc.edu'
        }
      ]
    }
  }
}
</script>
