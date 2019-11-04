
a = 'abababab'
b = a.split('ab')

console.log(a)
console.log(b)

function repeatSubStr (str) {
    var bitnumbers = []
    for (var i = 1, len = str.length; i < len; i++) {
      if (len % i === 0) {
        bitnumbers.push(i.toString())
      }
    }
    for (var j = 0, lon = bitnumbers.length; j < lon; j++) {
      var result = new Set(str.split(str.slice(0, bitnumbers[j])))
      if (result.size === 1) {
        console.log(result)
        return true
      }
    }
    console.log(result)
    return false
}

fzk = repeatSubStr("abcabcabcabc")
console.log(fzk.size)
console.log(fzk)
