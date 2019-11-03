function grayCode (n) {
  function binayCode (n) {
    if (n === 0) {
      return [0]
    } else if (n === 1) {
      return [0, 1]
    } else {
      let prev = grayCode(n - 1)
      let result = []
      let max = Math.pow(2, n) - 1
      for (let i = 0, len = prev.length; i < len; i++) {
        result[i] = `0${prev[i]}`
        result[max - i] = `1${prev[i]}`
      }
      return result
    }
  }
  let grayResult = binayCode(n).map((item) => {
    return parseInt(item.toString(), 2)
  })
  return grayResult
}

export default grayCode
