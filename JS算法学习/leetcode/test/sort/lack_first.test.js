import lackFirst from '../../code/sort/lack_first'

test('数组中的第K个最大元素', () => {
  expect(lackFirst([1, 2, 0])).toEqual(3)
  expect(lackFirst([3, 4, -1, 1])).toEqual(2)
  expect(lackFirst([7, 8, 9, 11, 12])).toEqual(1)
  expect(lackFirst([1, 2, 3, 4, 5, 5, 6, 7, 8])).toEqual(9)
})
