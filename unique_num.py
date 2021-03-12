""" There is an array with some numbers. All numbers are equal except for one. Try to find it!
   It’s guaranteed that array contains at least 3 numbers.
   The tests contain some very huge arrays, so think about performance. """

def find_uniq(arr):
    arr.sort()
    if arr[0] == arr[1]:
        return arr[-1]
    else:
        return arr[0]
