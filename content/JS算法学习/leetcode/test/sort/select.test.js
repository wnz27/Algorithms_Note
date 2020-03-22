import select from '../../code/sort/select'

test('选择排序', () => {
  expect(select([1, 9, 5, 3, 4])).toEqual([1, 3, 4, 5, 9])
})
