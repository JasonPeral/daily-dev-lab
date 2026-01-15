## Pseudocode / Approach

**Goal:**  
Merge two strings by alternating characters, starting with the first string.  
If one string is longer, append the remaining characters at the end.

### Steps
1. Create an empty result container to store the merged characters.
2. Initialize an index `i = 0`.
3. Loop while `i` is less than the length of **either** string:
   - If `i` is within bounds of `word1`, append `word1[i]` to the result.
   - If `i` is within bounds of `word2`, append `word2[i]` to the result.
   - Increment `i` by 1.
4. Join the result container into a single string.
5. Return the merged string.

### Notes
- This uses a **two-pointer (parallel traversal)** pattern.
- Bounds checking prevents out-of-range errors.
- Each character is processed once.
