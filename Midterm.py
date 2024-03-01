def find_pattern_occurrences(text):
    # Initialize a count variable to keep track of pattern matches
    count = 0

    # Split the text into words
    words = text.split()

    # Iterate through each word in the text
    for word in words:
        # Check if the word starts with "un" and ends with "an"
        if word.startswith("un") and word.endswith("an"):
            count += 1  # Increment the count if the condition is met

    # Return the total count of matches
    return count


# Example usage:
text = "This function finds an unknown number of patterns like unclean or unkind man but not an unrelated or an umbrella."
print(find_pattern_occurrences(text))