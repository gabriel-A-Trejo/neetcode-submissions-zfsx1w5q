class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # First we need to process each string in the list
        # We create a key for the anagrams based on a character count tuple
        # Then we store the grouped strings in the container dictionary

        container = defaultdict(list)  # Initialize the defaultdict

        for string in strs:  # Iterate through each string
            counter = [0] * 26  # Create a counter for the 26 lowercase English letters
            for char in string:  # Count each character in the string
                counter[ord(char) - ord("a")] += 1

            container[tuple(counter)].append(string)  # Use the tuple of counts as the key

        return list(container.values())  # Return the grouped anagrams as a list of lists

