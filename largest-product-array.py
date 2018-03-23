def largest_product_array():
  product = 0
  array = [[1,2][3,4][5,6][7,8]]

  for i in len(array):
    if array[i][0] * array[i][0] > product:
      product = array[i][0] * array[i][0]
  return product
