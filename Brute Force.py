def find_max(arr):
  max_num = arr[0]
  for num in arr[1:]:
    if num > max_num:
      max_num = num
  return max_num

# Contoh penggunaan
numbers = [3, 7, 2, 9, 5]
result = find_max(numbers)
print("Nilai maksimum:", result)