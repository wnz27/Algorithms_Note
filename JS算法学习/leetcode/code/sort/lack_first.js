/*
给定一个未排序的整数数组，找出其中没有出现的最小的正整数。

示例 1:
输入: [1,2,0]
输出: 3
示例 2:
输入: [3,4,-1,1]
输出: 2
示例 3:
输入: [7,8,9,11,12]
输出: 1
说明:
你的算法的时间复杂度应为O(n)，并且只能使用常数级别的空间。
*/
// 利用选择排序特性
function lackFirst (nums) {
  let len = nums.length
  if (len === 1) {
    if (nums[0] > 1 || nums[0] <= 0) {
      return 1
    } else {
      return 2
    }
  }
  for (let i = 0; i < len; i++) {
    let min = nums[i]
    let index = i
    for (let j = i + 1; j < len; j++) {
      if (nums[j] < min) {
        min = nums[j]
        index = j
      }
    }
    nums[index] = nums[i]
    nums[i] = min
    if (i === 0) { // 起始边界处理
      if (nums[i] > 1) {
        return 1
      } else {
        continue
      }
    } else if (i >= 1) { // 中间处理
      if (nums[i] <= 0) {
        continue
      } else if (nums[i] > 0 && nums[i - 1] <= 0) {
        if (nums[i] > 1) {
          return 1
        } else {
          continue
        }
      } else {
        if (nums[i] - nums[i - 1] > 1) {
          return nums[i - 1] + 1
        } else {
          if (i === len - 1) { // 结尾边界处理
            return nums[i] + 1
          } else {
            continue
          }
        }
      }
    }
  }
}

export default lackFirst
