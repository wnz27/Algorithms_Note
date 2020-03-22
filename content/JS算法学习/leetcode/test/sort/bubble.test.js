import bubble from '../../code/sort/bubble'

test('冒泡排序', () => {
  expect(bubble([1, 9, 5, 3, 4])).toEqual([1, 3, 4, 5, 9])
})
