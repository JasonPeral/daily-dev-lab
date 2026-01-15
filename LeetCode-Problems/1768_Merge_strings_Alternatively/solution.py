# Create an empty result string
# Initialize index i = 0

# While i is less than the length of word1 OR word2:
#     If i is less than length of word1:
#         append word1[i] to result
#     If i is less than length of word2:
#         append word2[i] to result
#     Increment i

# Return result

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = []
        i = 0

        while i < len(word1) or i < len(word2):
            if i < len(word1):
                result.append(word1[i])
            if i < len(word2):
                result.append(word2[i])

            i += 1
    
        return "".join(result)
    
def run_tests():
    solution = Solution()

    test_cases = [
        ("ab", "pqrs", "apbqrs"),
        ("abcd", "pq", "apbqcd"),
        ("", "xyz", "xyz"),
        ("hello", "", "hello"),
        ("a", "b", "ab"),
        ("ace", "bdf", "abcdef"),
    ]

    print("Running test cases...\n")

    for i, (word1, word2, expected) in enumerate(test_cases, start=1):
        result = solution.mergeAlternately(word1, word2)
        status = "PASS" if result == expected else "FAIL"

        print(f"Test {i}:")
        print(f"  Input:    word1='{word1}', word2='{word2}'")
        print(f"  Output:   '{result}'")
        print(f"  Expected: '{expected}'")
        print(f"  Result:   {status}\n")


if __name__ == "__main__":
    run_tests()
                
        