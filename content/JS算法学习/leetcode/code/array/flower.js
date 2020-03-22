function flower (arr, n) {
  var count = 0
  for (var i = 1; i < arr.length - 1; i++) {
    if (arr[i - 1] === 0 && arr[i + 1] === 0) {
      count += 1
      arr[i] = 1
    }
    if (count === n) {
      return true
    }
  }
  return false
}

export default flower
