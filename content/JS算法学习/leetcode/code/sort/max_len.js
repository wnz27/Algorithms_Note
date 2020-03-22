/*
给定一个无序的数组，找出数组在排序之后，相邻元素之间最大的差值。
如果数组元素个数小于 2，则返回 0。

示例 1:
输入: [3,6,9,1]
输出: 3
解释: 排序后的数组是 [1,3,6,9], 其中相邻元素 (3,6) 和 (6,9) 之间都存在最大差值 3。
示例 2:
输入: [10]
输出: 0
解释: 数组元素个数小于 2，因此返回 0。
*/

// 自己的方法
// function maxLen (nums) {
//   if (nums.length < 2) {
//     return 0
//   } else {
//     let res = 0
//     nums.sort((a, b) => a - b)
//     for (let i = 0; i < nums.length - 1; i++) {
//       let dif = Math.abs(nums[i] - nums[i + 1])
//       if (dif > res) {
//         res = dif
//       }
//     }
//     return res
//   }
// }

// 性能更好的方法，依然利用冒泡排序，从第二次遍历开始，就已经能拿到相邻差值了
function maxLen (nums) {
  let max = 0
  let len = nums.length
  if (nums.length < 2) {
    return 0
  } else {
    for (let i = len - 1; i > 0; i--) {
      for (let j = 0, temp; j < i; j++) {
        if (nums[j] > nums[j + 1]) {
          temp = nums[j]
          nums[j] = nums[j + 1]
          nums[j + 1] = temp
        }
      }
      if (i < len - 1) {
        let dif = Math.abs(nums[i + 1] - nums[i])
        if (dif > max) {
          max = dif
        }
      }
    }
    // 循环里没有最前面两个数的差值
    let dif = Math.abs(nums[1] - nums[0])
    if (dif > max) {
      max = dif
    }
    return max
  }
}

// 此题还可以做隔一个数差值最大变种

export default maxLen
