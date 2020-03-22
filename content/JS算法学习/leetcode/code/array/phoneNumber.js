/**
 * 给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。
 * 给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。
 * 示例:
 * 输入："23"
 * 输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
 * 说明:
 * 尽管上面的答案是按字典序排列的，但是你可以任意选择答案输出的顺序。
 */

function lettersByNumstr (str) {
  const letterMap = {
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz'
  }
  var letters = str.split('')
  var calculateArray = letters.map((item) => {
    return letterMap[item].split('')
  })
  var result = []
  function Foo (arr) {
    for (var i = 0; i < arr[0].length; i++) {
      for (var j = 0; j < arr[1].length; j++) {
        result.push(arr[0][i] + arr[1][j])
      }
    }
    arr.splice(0, 2, result)
    if (arr.length > 1) {
      Foo(arr)
    } else {
      return result
    }
    return arr[0]
  }
  return Foo(calculateArray)
}

export default lettersByNumstr
