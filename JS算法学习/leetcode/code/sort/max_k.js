/*
在未排序的数组中找到第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。

示例 1:
输入: [3,2,1,5,6,4] 和 k = 2
输出: 5

示例 2:
输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
输出: 4
*/

// 最简单的方法
// function maxK (arr, k) {
//   // function compare (a, b) {
//   //   return b - a
//   // }
//   // let res = arr.sort(compare)
//   let res = arr.sort((a, b) => b - a)
//   return res[k - 1]
// }

// 性能更高的方法，冒泡排序，每一次都找出一个最大值，那么我找k轮不就是我们需要的第k个最大值吗
// function maxK (arr, k) {
//   let res = []
//   for (let i = arr.length - 1, temp; i > arr.length - 1 - k; i--) {
//     for (let j = 0; j < i; j++) {
//       if (temp > arr[j + 1]) {
//         temp = arr[j]
//         arr[j] = arr[j + 1]
//         arr[j + 1] = temp
//       }
//     }
//     res = arr[i]
//   }
//   return res
// }

function maxK (arr, k) {
  for (let i = arr.length - 1, temp; i > arr.length - 1 - k; i--) {
    for (let j = 0; j < i; j++) {
      if (arr[j] > arr[j + 1]) {
        temp = arr[j]
        arr[j] = arr[j + 1]
        arr[j + 1] = temp
      }
    }
  }
  return arr[arr.length - k]
}

export default maxK
