# Algorithm: Sorting the Letters of a Full Name (Insertion Sort)

**Name:** Jonhlen Mart F. Amaro

## Part 1: Build the unsorted array
1. START
2. Store the full name in `FULL_NAME`.
3. Create an empty list `letters`.
4. For each character `ch` in `FULL_NAME`:
   1. If `ch` is not a letter (space or symbol such as "."), skip it.
   2. Convert `ch` to lowercase.
   3. If `ch` is not yet in `letters`, add it (duplicates are discarded).
5. `letters` is now the **unsorted array**.

## Part 2: Insertion Sort (ascending)
1. Copy the unsorted array into `result`.
2. For `i` from 1 to the last index of `result`:
   1. Set `key = result[i]` and `j = i - 1`.
   2. While `j >= 0` and `result[j] > key`:
      - Move `result[j]` one position to the right (`result[j+1] = result[j]`).
      - Decrease `j` by 1.
   3. Place `key` at `result[j+1]`.
3. `result` is now the **sorted array**.

## Part 3: Output
1. Print the unsorted array.
2. Print the sorted array.
3. END

## Result
- Unsorted: `['j', 'o', 'n', 'h', 'l', 'e', 'm', 'a', 'r', 't', 'f']`
- Sorted:   `['a', 'e', 'f', 'h', 'j', 'l', 'm', 'n', 'o', 'r', 't']`

## Complexity
Insertion Sort: O(n^2) worst/average case, O(n) best case, O(1) extra space.
