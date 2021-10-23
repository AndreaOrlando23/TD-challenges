## Task

Implement a function which takes an array of nonnegative integers and returns the number of subarrays with an odd number of odd numbers. Note, a subarray is a contiguous subsequence.
Example

Consider an input:

```Python
[1, 2, 3, 4, 5]
```

The subarrays containing an odd number of odd numbers are the following:

```Python
[1, 2, 3, 4, 5], [2, 3, 4], [1, 2], [2, 3], [3, 4], [4, 5], [1], [3], [5]
```

The expected output is therefore 9.
Test suite

The expected output for an empty array is 0, otherwise the content of the arrays are always integers k such that 0 <= k <= 10000.

Expected time complexity is O(n)
