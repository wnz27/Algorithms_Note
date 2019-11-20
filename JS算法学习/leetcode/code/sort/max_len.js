// 自己的方法
function maxLen (nums) {
  if (nums.length < 2) {
    return 0
  } else {
    let res = 0
    nums.sort((a, b) => a - b)
    for (let i = 0; i < nums.length - 1; i++) {
      let dif = Math.abs(nums[i] - nums[i + 1])
      if (dif > res) {
        res = dif
      }
    }
    return res
  }
}

export default maxLen
