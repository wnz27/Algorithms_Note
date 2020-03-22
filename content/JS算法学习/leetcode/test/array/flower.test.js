import flower from '../../code/array/flower'

test('let\'s flower test, output bool', () => {
  expect(flower([1, 0, 0, 0, 1], 1)).toEqual(true)
  expect(flower([1, 0, 0, 0, 1], 2)).toEqual(false)
})
