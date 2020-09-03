const loadApiData = function (url, func, payload = null) {
  let ax = this.$axios
  if (payload !== null) {
    ax = ax.post(url, payload)
  } else {
    ax = ax.get(url)
  }

  ax.then((response) => {
    func(response.data)
    if (!this.$utils.isObjectNotEmpty(response.data)) {
      this.$q.notify({
        color: 'negative',
        position: 'top',
        message: 'No data available for you request.',
        icon: 'grading'
      })
    }
  }).catch(() => {
    this.$q.notify({
      color: 'negative',
      position: 'top',
      message: 'Loading failed. API: ' + url,
      icon: 'report_problem'
    })
  })
}

export default loadApiData
