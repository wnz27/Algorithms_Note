/*

给定一个非负整数数组 A， A 中一半整数是奇数，一半整数是偶数。

对数组进行排序，以便当 A[i] 为奇数时，i 也是奇数；当 A[i] 为偶数时， i 也是偶数。

你可以返回任何满足上述条件的数组作为答案。

示例：

输入：[4,2,5,7]
输出：[4,5,2,7]
解释：[4,7,2,5]，[2,5,4,7]，[2,7,4,5] 也会被接受。

*/
// 自己的方法
function oddEven (arr) {
  let odd = []
  let even = []
  let result = []
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] % 2 === 0) {
      even.push(arr[i])
    } else {
      odd.push(arr[i])
    }
  }
  for (let j = 0; j < even.length; j++) {
    result.splice(0, 0, even[j], odd[j])
  }
  return result
}

export default oddEven
