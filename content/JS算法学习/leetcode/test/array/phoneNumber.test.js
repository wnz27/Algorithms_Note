import phoneNumber from '../../code/array/phoneNumber'

test('let\'s phoneNumber test, output letters By Numstr', () => {
  expect(phoneNumber('23')).toEqual(['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf'])
})
