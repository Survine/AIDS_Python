import array

# Create an array of integers
arr = array.array('i', [1, 2, 3, 4, 5])

# Insertion: Append an element to the array
arr.append(6)

# Deletion: Remove an element from the array
arr.remove(3)

# Updating: Update an element in the array
arr[1] = 10

# Print the updated array
for num in arr:
    print(num)