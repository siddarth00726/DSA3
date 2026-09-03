# =====================================================
# NAIVE PATTERN MATCHING AND KMP ALGORITHM
# =====================================================


# NAIVE PATTERN MATCHING

def naive_search(text, pattern):

    print("Naive Pattern Matching:")

    n = len(text)
    m = len(pattern)

    for i in range(n - m + 1):

        j = 0

        while j < m:

            if text[i + j] != pattern[j]:
                break

            j += 1

        if j == m:
            print("Pattern found at index:", i)


# KMP PATTERN MATCHING

def kmp_search(text, pattern):

    print("KMP Pattern Matching:")

    n = len(text)
    m = len(pattern)

    # Create LPS array
    lps = [0] * m

    compute_lps(pattern, lps)

    i = 0
    j = 0

    while i < n:

        # Characters match
        if text[i] == pattern[j]:

            i += 1
            j += 1

        # Complete pattern found
        if j == m:

            print("Pattern found at index:", i - j)

            j = lps[j - 1]

        # Characters do not match
        elif i < n and text[i] != pattern[j]:

            if j != 0:

                j = lps[j - 1]

            else:

                i += 1


# FUNCTION TO CREATE LPS ARRAY

def compute_lps(pattern, lps):

    length = 0
    i = 1

    while i < len(pattern):

        if pattern[i] == pattern[length]:

            length += 1
            lps[i] = length

            i += 1

        else:

            if length != 0:

                length = lps[length - 1]

            else:

                lps[i] = 0

                i += 1


# MAIN PROGRAM

text = "ABABDABACDABABCABAB"

pattern = "ABABCABAB"

naive_search(text, pattern)

print()

kmp_search(text, pattern)