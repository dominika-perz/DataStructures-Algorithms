def insertion_sort(array, decresing=False):
    """
    :param decresing: optional parameter to sort in nonincreasing order, default is nondescreasing
    :param array: a list to be sorted in place
    :return:

    >>> a = [2, 9, 7, 3]
    >>> insertion_sort(a)
    >>> print(a)
    [2, 3, 7, 9]
    >>> a = [5, 1, 2, 9, 4, 6, 7, 3, 8]
    >>> insertion_sort(a)
    >>> print(a)
    [1, 2, 3, 4, 5, 6, 7, 8, 9]
    >>> a = [5, 1, 2, 9, 4, 6, 7, 3, 8]
    >>> insertion_sort(a, decresing=True)
    >>> print(a)
    [9, 8, 7, 6, 5, 4, 3, 2, 1]
    >>> b = []
    >>> insertion_sort(b)
    >>> print(b)
    []
    >>> c = [3]
    >>> insertion_sort(c)
    >>> print(c)
    [3]

    """
    for i in range(1, len(array)):
        key = array[i]
        j = i - 1
        while j >= 0 and (
                (not decresing and array[j] > key) or
                (decresing and array[j] < key)):
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key


def adding_bitwise(A, B):
    """
    :param A: first array to add
    :param B: second array to add
    :return C: an array resulted by adding A to B bitwise

    >>> A = [1, 1, 1, 0, 1]
    >>> B = [1, 1, 1, 0]
    >>> print(adding_bitwise(A, B))
    [1, 0, 1, 0, 1, 1]
    """
    C = []
    carry = 0
    for i in range(-1, -max(len(A), len(B))-1, -1):
        a = A[i] if -i-1 < len(A) else 0
        b = B[i] if -i-1 < len(B) else 0
        carry, c = divmod(a+b+carry, 2)
        C = [c] + C
    if carry == 1:
        C = [1] + C
    return C
