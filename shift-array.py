middle = len(array)/2
temp = array[middle]
temp2 = 0
array = [1,2,4,5]
value = 3

def shift_array(value):
  for i in range(middle, len(array)):
    temp2 = array[i + 1]
    array[i + 1] = temp
    temp = temp2
  return array
print (shift_array)
