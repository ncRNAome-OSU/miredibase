import { exportFile } from 'quasar'

function _wrapCsvValue (val, formatFn) {
  let formatted = formatFn !== undefined
    ? formatFn(val)
    : val

  formatted = formatted === undefined || formatted === null
    ? ''
    : String(formatted)

  formatted = formatted.split('"').join('""')
  /**
   * Excel accepts \n and \r in strings, but some other CSV parsers do not
   * Uncomment the next two lines to escape new lines
   */
  // .split('\n').join('\\n')
  // .split('\r').join('\\r')

  return `"${formatted}"`
}

const exportDataTableAsCSV = function () {
  // naive encoding to csv format
  const content = [this.columns.map(col => _wrapCsvValue(col.label))].concat(
    this.data.map(row => this.columns.map(col => _wrapCsvValue(
      typeof col.field === 'function'
        ? col.field(row)
        : row[col.field === undefined ? col.name : col.field],
      col.format
    )).join(','))
  ).join('\r\n')

  const status = exportFile(
    'table-export.csv',
    content,
    'text/csv'
  )

  if (status !== true) {
    this.$q.notify({
      message: 'Browser denied file download...',
      color: 'negative',
      icon: 'warning'
    })
  }
}

export default exportDataTableAsCSV
