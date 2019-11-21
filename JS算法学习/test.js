function lackFirst (nums) {
  let len = nums.length
  // 特殊情况处理
  if (len === 0) { // 数组为空时
    return 1
  }
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
    console.log(nums)
    if (i === 0) { // 起始边界处理
      if (nums[i] > 1) {
        return 1
      } else {
        continue
      }
    } else if (i >= 1) { // 中间处理
      if (nums[i] <= 0) {
        if (i === len - 1) { // 结尾边界处理
          return 1
        } else {
          continue
        }
      } else if (nums[i] === 1) {
        if (i === len - 1) { // 结尾边界处理
          return 2
        } else {
          continue
        }
      } else if (nums[i] > 1 && nums[i - 1] <= 0) {
        return 1
      } else if (nums[i] > 1 && nums[i - 1] > 0) {
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
console.log(lackFirst([1000,-1]))
console.log('******************************')
console.log(lackFirst([-1,-2]))
console.log('******************************')
console.log(lackFirst([1, 2, 3, 4, 5, 5, 6, 7, 8]))
console.log('******************************')
console.log(lackFirst([1, 2, 0]))
console.log('******************************')
console.log(lackFirst([1, 1]))


// function maxLen (nums) {
//   let max = 0
//   let len = nums.length
//   if (nums.length < 2) {
//     return 0
//   } else {
//     for (let i = len - 1; i > 0; i--) {
//       for (let j = 0, temp; j < i; j++) {
//         if (nums[j] > nums[j + 1]) {
//           temp = nums[j]
//           nums[j] = nums[j + 1]
//           nums[j + 1] = temp
//         }
//       }
//       console.log(nums)
//       if (i < len - 1) {
//         let dif = Math.abs(nums[i + 1] - nums[i])
//         if (dif > max) {
//           max = dif
//         }
//       }
//       console.log(max)
//     }
//     let dif = Math.abs(nums[1] - nums[0])
//     if (dif > max) {
//       max = dif
//     }
//     console.log(max)
//     return max
//   }
// }
// maxLen([5,6,9,1])

// a = 'abababab'
// b = a.split('ab')
// c = [1, 8, 5, 3, 4, 6]
// let odd = []
// let even = []
// let result = []
// for (let i = 0; i < c.length; i++) {
//   if (c[i] % 2 === 0) {
//     even.push(c[i])
//   } else {
//     odd.push(c[i])
//   }
// }
// for (let j = 0; j < even.length; j++) {
//   result.splice(0, 0, even[j], odd[j])
// }
// console.log(odd)
// console.log(even)
// console.log(result)
// console.log(a)
// console.log(b)

// function repeatSubStr (str) {
//     var bitnumbers = []
//     for (var i = 1, len = str.length; i < len; i++) {
//       if (len % i === 0) {
//         bitnumbers.push(i.toString())
//       }
//     }
//     for (var j = 0, lon = bitnumbers.length; j < lon; j++) {
//       var result = new Set(str.split(str.slice(0, bitnumbers[j])))
//       if (result.size === 1) {
//         console.log(result)
//         return true
//       }
//     }
//     console.log(result)
//     return false
// }

// fzk = repeatSubStr("abcabcabcabc")
// console.log(fzk.size)
// console.log(fzk)
