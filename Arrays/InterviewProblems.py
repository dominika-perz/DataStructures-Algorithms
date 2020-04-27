# Anagram

def is_anagram(a_str, b_str):
    A = a_str.lower().replace(" ", "")
    B = b_str.lower().replace(" ", "")

    return sorted(A) == sorted(B)


def is_anagram2(a_str, b_str):
    A = a_str.lower().replace(" ", "")
    B = b_str.lower().replace(" ", "")

    if len(A) != len(B):
        return False

    set_char = {a for a in A}

    for char in set_char:
        if A.count(char) != B.count(char):
            return False

    return True


def is_anagram3(a_str, b_str):
    A = a_str.lower().replace(" ", "")
    B = b_str.lower().replace(" ", "")

    if len(A) != len(B):
        return False

    count = {}

    for a in A:
        if a in count:
            count[a] += 1
        else:
            count[a] = 1

    for b in B:
        if b in count:
            count[b] -= 1
        else:
            return False

    return sum(count.values()) == 0


# Array Pair Sum
def array_pair_sum(array, result):
    pairs = set()
    seen = set()

    for a in array:
        if result - a not in seen:
            seen.add(a)
        else:
            pairs.add((min(a, result - a), max(a, result - a)))

    return len(pairs)


# Finding the missing element
def find_missing_sum(full, missing):
    return sum(full) - sum(missing)


def find_missing_xor(full, missing):
    result = 0
    for num in full+missing:
        result ^= num
    return result


# Largest continuous sum
def large_cont_sum(array):
    current_start = array[0]
    max_sum = 0
    current_sum = 0
    start, stop = current_start, 0
    change = False
    for num in array:
        if num > current_sum + num:
            change = True
            current_start = num
            current_sum = num
        else:
            current_sum += num
        if current_sum > max_sum:
            if change:
                start = current_start
                change = False
            stop = num
            max_sum = current_sum

    return max_sum, start, stop
