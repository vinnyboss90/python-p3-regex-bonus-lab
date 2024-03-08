import re

# Update the regular expression pattern to match the desired strings
my_pattern = r"It's such a lovely day today\.|Some weather we're having today, huh\?|Maybe today's just not my day\."
my_regex = re.compile(my_pattern)

# Test Cases
string1 = "It's such a lovely day today."
string2 = "Some weather we're having today, huh?"
string3 = "Maybe today's just not my day."

# Test 1
match1 = my_regex.fullmatch(string1)
assert match1 is not None, f"Failed to match: {string1}"

# Test 2
match2 = my_regex.fullmatch(string2)
assert match2 is not None, f"Failed to match: {string2}"

# Test 3
match3 = my_regex.fullmatch(string3)
assert match3 is not None, f"Failed to match: {string3}"

# Test 4
FINDALL_STRING = f"{string1} {string2} {string3}"
matches = my_regex.findall(FINDALL_STRING)
expected_matches = [
    "It's such a lovely day today.",
    "Some weather we're having today, huh?",
    "Maybe today's just not my day.",
]
assert matches == expected_matches, f"Unexpected matches: {matches}"