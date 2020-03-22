function select (arr) {
  for (let i = 0, min, index, len = arr.length; i < len; i++) {
    min = arr[i]
    index = i // 避免遍历内循环没有小于min的情况
    for (let j = i + 1; j < len; j++) {
      if (arr[j] < min) {
        min = arr[j]
        index = j
      }
    }
    arr[index] = arr[i]
    arr[i] = min
  }
  return arr
}

export default select
