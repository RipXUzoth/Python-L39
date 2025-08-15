import numpy as np
arr = np.arange(1, 11)
print("Original array: ", arr)
print("Shape: ", arr.shape)
print("Size: ",arr.size)
reshaped = arr.reshape(2, 5)
print("Reshaped array (2x5):\n", reshaped[-1, -1])
print("Elements from index 2 to 7: ", arr[2:8])
print("Array + 5", arr + 5)
print("Array * 2", arr * 2)
print("Max Value: ", arr.max())
print("Min value: ", arr.min())
print("Mean value: ", arr.mean())
print("Squared Elements: ", np.square(arr))
mask = arr > 5
print("Boolean Mask: ", mask)
print("Values > 5: ", arr[mask])
sorted_desc = np.sort(arr)[::-1]
print("Sorted in descending order: ", sorted_desc)