import { format } from 'quasar'
const { capitalize } = format

const utils = {
  scrollToElement (elementId, scrollType = 'top', duration = 100) {
    const el = document.getElementById(elementId)
    if (this.isNotNull(el)) {
      window.scrollTo(0, el.offsetTop)
    }
  },
  sanitizeEmail (value) {
    return value.replace(/@/g, ' [ AT ] ')
  },
  objectHasPropery (object, property) {
    return Object.prototype.hasOwnProperty.call(object, property)
  },
  isObjectNotEmpty (object) {
    return (object !== null && Object.keys(object).length)
  },
  isNotNull (object) {
    return (object !== null)
  },
  capitalize: function (e) {
    return capitalize(e)
  },
  toLowerCase (value) {
    return String.prototype.toLowerCase(value)
  },
  prettifySnvType: function (e) {
    return capitalize(e.charAt(0)) +
      '-to-' +
      capitalize(e.charAt(1))
  },
  selectOpt: function (data, ref = '') {
    const target = []
    data.forEach((e) => {
      switch (ref) {
        case 'organism':
          target.push({ label: capitalize(e), value: e })
          break
        case 'editing':
          target.push({ label: this.prettifySnvType(e), value: e })
          break
        default:
          target.push(e)
          break
      }
    })
    return target
  },
  setSnvDetailsList (data, labelsList) {
    const response = []
    if (this.isObjectNotEmpty(data)) {
      labelsList.forEach((key) => {
        if (this.objectHasPropery(data, key)) {
          let label = null
          let value = null
          let link = null
          switch (key) {
            case 'organism':
            case 'chromosome':
            case 'strand':
              label = this.capitalize(key)
              value = this.capitalize(data[key])
              break
            case 'mod_type':
              label = 'Modification type'
              value = this.prettifySnvType(data[key])
              break
            case 'genomic_position':
              label = 'Genomic position'
              value = data[key]
              link = data.uri.ucsc
              break
            case 'stemloop':
              label = 'Stem-loop'
              value = data[key]
              link = `http://www.mirbase.org/cgi-bin/mirna_entry.pl?acc=${data.stemloop_acc_number}`
              break
            case 'stemloop_local_pos':
              if (data[key] !== null) {
                label = 'Stem-loop local position'
                value = data[key]
              }
              break
            case 'stemloop_region_involved':
              if (data[key] !== null) {
                label = 'Stem-loop region involved'
                value = data[key]
              }
              break
            case 'mirna':
              if (data[key] !== null) {
                label = 'miRNA'
                value = data[key]
                link = `http://www.mirbase.org/cgi-bin/mirna_entry.pl?acc=${data.mirna_acc_number}`
              }
              break
            case 'mirna_local_pos':
              if (data[key] !== null) {
                label = 'miRNA local position'
                value = data[key]
              }
              break
            default:
              break
          }

          if (label !== null && value !== null) {
            response.push({ key: key, label: label, value: value, link: link })
          }
        }
      })
    }
    return response
  },
  setSnvDetailstableRow (data, labelsList) {
    const response = { name: 0 }
    if (this.isObjectNotEmpty(data)) {
      labelsList.forEach((key) => {
        if (this.objectHasPropery(data, key)) {
          switch (key) {
            case 'organism':
            case 'chromosome':
              response[key] = this.capitalize(data[key])
              break
            case 'mod_type':
              response[key] = this.prettifySnvType(data[key])
              break
            case 'transcript_region':
            case 'strand':
            case 'is_putative':
              response[key] = data[key]
              break
            case 'genomic_position':
              response[key] = {
                value: data[key],
                link: data.uri.ucsc
              }
              break
            case 'conservation':
              response[key] = data[key]
              break
            case 'stemloop':
              response[key] = {
                value: data[key],
                mirbaseLink: this.isNotNull(data.stemloop_acc_number) ? `http://www.mirbase.org/cgi-bin/mirna_entry.pl?acc=${data.stemloop_acc_number}` : null,
                rnacentralLink: this.isNotNull(data.stemloop_rnacentral_acc_number) ? `https://rnacentral.org/rna/${data.stemloop_rnacentral_acc_number}/${data.organism_id}` : null
              }
              break
            case 'stemloop_local_pos':
              if (data[key] !== null) {
                response[key] = data[key]
              }
              break
            case 'stemloop_region_involved':
              if (data[key] !== null) {
                response[key] = data[key]
              }
              break
            case 'mirna':
              if (data[key] !== null) {
                response[key] = {
                  value: data[key],
                  mirbaseLink: this.isNotNull(data.mirna_acc_number) ? `http://www.mirbase.org/cgi-bin/mirna_entry.pl?acc=${data.mirna_acc_number}` : null,
                  rnacentralLink: this.isNotNull(data.mirna_rnacentral_acc_number) ? `https://rnacentral.org/rna/${data.mirna_rnacentral_acc_number}/${data.organism_id}` : null
                }
              }
              break
            case 'mirna_local_pos':
              if (data[key] !== null) {
                response[key] = data[key]
              }
              break
            case 'uri':
              if (data[key].darned !== null) {
                response.darned = {
                  value: 'Darned',
                  link: data.uri.darned
                }
              }
              if (data[key].radar !== null) {
                response.radar = {
                  value: 'Radar',
                  link: data.uri.radar
                }
              }
              if (data[key].rediportal !== null) {
                response.rediportal = {
                  value: 'REDIportal',
                  link: data.uri.rediportal
                }
              }
              if (data[key].ucsc !== null) {
                response.ucsc = {
                  value: 'UCSC',
                  link: data.uri.ucsc
                }
              }
              break
            default:
              break
          }
        }
      })
    }
    return response
  }
}

export default utils
