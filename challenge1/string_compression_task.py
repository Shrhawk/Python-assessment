"""
Time complexity: O(n)
Space complexity: O(n) / O(1)
"""


def gen_compressed_str(text: str) -> str:
    """
    Compresses a given string by counting repeated characters.

    Args:
        text (str): The input string to be compressed.

    Returns:
        str: The compressed string or the original string if the compressed version is longer.
    """
    if len(text) <= 1:
        return text

    count = 1
    comp_str = ""

    for char in range(len(text)):
        if char < len(text) - 1 and text[char] == text[char + 1]:
            count += 1
        else:
            comp_str += text[char]
            comp_str += str(count)
            count = 1

    return text if len(comp_str) >= len(text) else comp_str


if __name__ == '__main__':
    print("Testing string: bbcceeee")
    print("Expected compressed string: b2c2e4")
    print(f"Actual compressed string: {gen_compressed_str('bbcceeee')}")

# Test Cases
try:
    assert gen_compressed_str('bbcceeee') == 'b2c2e4'
    assert gen_compressed_str('aaabbbcccaaa') == 'a3b3c3a3'
    assert gen_compressed_str('a') == 'a'
except AssertionError:
    print("Assertion failed for test case")
