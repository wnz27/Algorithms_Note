import repeatSubStr from '../../code/RegExp/repeatSubStr'

test('let\'s repeatSubStr test, output bool', () => {
  expect(repeatSubStr('abcabcabcabc')).toEqual(true)
  expect(repeatSubStr('aba')).toEqual(false)
  expect(repeatSubStr('abab')).toEqual(true)
})
