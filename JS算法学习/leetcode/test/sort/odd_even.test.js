import oddEven from '../../code/sort/odd_even'

test('奇偶排序', () => {
  expect(oddEven([1, 8, 5, 3, 4, 6])).toEqual([6, 3, 4, 5, 8, 1])
})
