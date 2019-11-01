import cardGroup from '../../code/array/cardGroup'

test('let\'s cardGroup test, output bool', () => {
  expect(cardGroup([1, 2, 3, 4, 4, 3, 2, 1])).toEqual(true)
})
