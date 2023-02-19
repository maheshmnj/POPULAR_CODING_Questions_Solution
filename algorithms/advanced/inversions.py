# Description: Counting Inversions and Significant Inversions in an array.
# See Readme.md for more details.

class Inversions():
  def __init__(self , array):
    self.array = array
    self.length = len(array)
    self.inversions = 0
    self.significantInversions = 0

  def countInversions(self):
    length = len(self.array)
    start = 0
    end = length - 1
    sorted_array = self.sortAndCount(self.array, start, end)
    print("Sorted Array = {}".format(sorted_array))
    print("Inversions = {}, Significant Inversions = {}".format(self.inversions, self.significantInversions))

  def sortAndCount(self, arr, s, e):
    size = e - s + 1
    if(size == 1):
        return [arr[s]]
    else:
      start = s
      end = e
      mid = start + (end - start) // 2
      sortedLeftHalf = self.sortAndCount(arr, start, mid)
      sortedRightHalf = self.sortAndCount(arr, mid + 1, end)
      sorted_array = self.mergeAndCountInversions(sortedLeftHalf,sortedRightHalf)
    return sorted_array

  def mergeAndCountInversions(self, array1, array2):
    len1 = len(array1)
    len2 = len(array2)
    i = 0
    j = 0
    sorted_array = []
    count = 0
    sigCount = 0
    while(i < len1 and j < len2):
      if(array1[i] > array2[j]):
        count += (len1 - i)
        if(array1[i] > 2*array2[j]):
          sigCount += 1
        sorted_array.append(array2[j])
        j+=1
      else:
        sorted_array.append(array1[i])
        i+=1
    if(i < len1):
        while(i < len1):
          sorted_array.append(array1[i])
          i+=1
    if(j < len2):
      while(j < len2):
          sorted_array.append(array2[j])
          j+=1
    self.inversions += count
    self.significantInversions += sigCount
    return sorted_array

if __name__ == '__main__':
  print("enter elements of array:")
  array = [int(x) for x in input().split()]
  # inversions = Inversions([5, 4, 3, 2, 1]) # 10
  # inversions = Inversions([2, 4, 1, 3, 5]) # 3
  # inversions = Inversions([1, 20, 6, 4, 5]) # 5
  # inversions = Inversions([4, 1, 5, 2, 3, 7, 6, 8]) # 6
  inversions = Inversions(array)
  inversions.countInversions()

# Output:
# enter elements of array:
# 4 1 5 2 3 7 6 8
# Sorted Array = [1, 2, 3, 4, 5, 6, 7, 8]
# Inversions = 6, Significant Inversions = 2



# Pseudocode:
# let Numbers be an array of n integers.
# let length = Numbers.size()
# let start = 0, end = length - 1;
# mid  = end + start / 2
# count = 0

# function sortAndCount(Numbers, start, end):
#  if(length of Numbers is 1):
#    return Numbers