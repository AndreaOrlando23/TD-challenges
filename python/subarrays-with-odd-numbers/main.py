
def all_sublists(data):
    sublists = [[]]
    for length in range(1, len(data) + 1):
        for i in range(0, len(data) - length + 1):
            sublists.append(data[i:i + length])
    print("len of sublists: ", len(sublists))
    # print(sublists)
    return sublists


def array_with_odd_numbers(arr):
    count = 0
    parse = all_sublists(arr)
    for arr_parsed in parse:
        if sum(arr_parsed) % 2 != 0:
            count += 1
    
    return count


print("A", array_with_odd_numbers([]))
print("B", array_with_odd_numbers([1]))
print("C", array_with_odd_numbers([1, 2]))
print("D", array_with_odd_numbers([1, 2, 3]))
print("E", array_with_odd_numbers([1, 2, 3, 4]))
print("F", array_with_odd_numbers([1, 2, 3, 4, 5]))
print("G", array_with_odd_numbers([1, 2, 3, 4, 5, 6]))
print("H", array_with_odd_numbers([1, 2, 3, 4, 5, 6, 7]))
print("I", array_with_odd_numbers([1, 2, 3, 4, 5, 6, 7, 8]))
print("J", array_with_odd_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9]))
print("K", array_with_odd_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print("L", array_with_odd_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]))
print("M", array_with_odd_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]))
print("N", array_with_odd_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]))
print("O", array_with_odd_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]))










"""
def countOddSum(ar, n):
    result = 0
 
    # Find sum of all subarrays and
    # increment result if sum is odd
    for i in range(n):
        val = 0
        for j in range(i, n ):
            val = val + ar[j]
            if (val % 2 != 0):
                result +=1
 
    return (result)
 
# Driver code
ar = [ 5, 4, 4, 5, 1, 3 ]
 
print("The Number of Subarrays" ,
            "with odd", end = "")
 
print(" sum is "+ str(countOddSum(ar, 6)))
 
# This code is contributed
# by ChitraNayal
"""