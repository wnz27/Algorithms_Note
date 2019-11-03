import grayCode from '../../code/array/grayCode'

test('let\'s grayCode test, output array', () => {
  expect(grayCode(2)).toEqual([0, 1, 3, 2])
  expect(grayCode(0)).toEqual([0])
  expect(grayCode(1)).toEqual([0, 1])
})
