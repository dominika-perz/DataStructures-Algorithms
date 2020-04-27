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


# Sentence reversal
def reverse_sentence(sentence):
    words = sentence.split()
    return ' '.join(reversed(words))


def reverse_sentence_basic(sentence):
    words = []
    new_word = True
    for letter in sentence:
        if letter not in '\n\r\t ':
            if new_word:
                words.append(letter)
                new_word = False
            else:
                words[-1] += letter
        else:
            new_word = True

    reversed_sentence = None
    for word in words:
        if reversed_sentence is None:
            reversed_sentence = word
        else:
            reversed_sentence = word + ' ' + reversed_sentence

    return reversed_sentence


# String compression
def string_compression(string):
    current_letter = ''
    count = 0
    compression = ''
    for letter in string:
        if letter == current_letter:
            count += 1
        else:
            if count > 0:
                compression += str(count)
            current_letter = letter
            count = 1
            compression += letter

    if count > 0:
        compression += str(count)

    return compression


# Unique character in string
def unique_char_in_str(string):
    unique_char = set(string)

    return len(unique_char) == len(string)


def unique_char_in_str2(string):
    seen = set()
    for char in string:
        if char in seen:
            return False
        else:
            seen.add(char)

    return True
