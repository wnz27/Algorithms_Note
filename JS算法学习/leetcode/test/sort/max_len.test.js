import maxLen from '../../code/sort/max_len'

test('数组中的第K个最大元素', () => {
  expect(maxLen([3, 6, 9, 1])).toEqual(3)
  expect(maxLen([10])).toEqual(0)
})
