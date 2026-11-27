"""
Assessment 3.7: Sorting Algorithms
Name: Jonhlen Mart F. Amaro
Sorting method: Insertion Sort

Rules followed:
  * Two arrays are created: unsorted and sorted.
  * Duplicate letters are discarded (case-insensitive, first occurrence is kept).
  * Symbols (the "." in "F.") and spaces are excluded.
"""

FULL_NAME = "Jonhlen Mart F. Amaro"


def build_unsorted_array(name):
    """Return a list of unique letters from the name, in original order."""
    letters = []
    for ch in name:
        if not ch.isalpha():          # exclude symbols (".") and spaces
            continue
        ch = ch.lower()               # so 'A' and 'a' count as the same letter
        if ch not in letters:         # discard duplicate letters
            letters.append(ch)
    return letters


def insertion_sort(arr):
    """Sort a list in ascending order using Insertion Sort.
    Works on a copy so the unsorted array stays untouched."""
    result = arr[:]
    for i in range(1, len(result)):
        key = result[i]
        j = i - 1
        while j >= 0 and result[j] > key:
            result[j + 1] = result[j]  # shift larger element to the right
            j -= 1
        result[j + 1] = key            # insert key in its correct position
    return result


def main():
    unsorted_array = build_unsorted_array(FULL_NAME)
    sorted_array = insertion_sort(unsorted_array)

    print("Full Name      :", FULL_NAME)
    print("Unsorted array :", unsorted_array)
    print("Sorted array   :", sorted_array)


if __name__ == "__main__":
    main()
