# Assignment Explanation:
# Imagine you have a rectangular document where words are placed inside rectangles. Each rectangle's position and size are scaled between 0 and 1, meaning the values for width, height, left, and top are fractions of the document's full size.
# The goal is to check if a user-drawn box on the document (given with real pixel coordinates) contains any words from the predefined list of words and their scaled bounding boxes.

# Steps to solve this:
# 1. Convert the scaled bounding box coordinates into actual pixel coordinates using the given width and height of the document.
# 2. Check if each word's bounding box lies inside the user-drawn box.
# 3. Return the words that are fully or partially enclosed.

import json

# Load the words position dictionary from a file
def load_words_position_dict(filename):
    with open(filename, 'r') as file:
        words_position = json.load(file)
    return words_position

# Convert scaled coordinates to pixel coordinates
def scale_to_pixel_coordinates(word_box, doc_width, doc_height):
    left = word_box[2] * doc_width
    top = word_box[3] * doc_height
    width = word_box[0] * doc_width
    height = word_box[1] * doc_height
    right = left + width
    bottom = top + height
    return left, top, right, bottom

# Check if a word box is inside or overlaps the user-drawn box
def is_within_user_box(word_box_pixel, user_box):
    word_left, word_top, word_right, word_bottom = word_box_pixel
    user_left, user_top, user_right, user_bottom = user_box

    # Check if there is any overlap
    return not (word_right < user_left or word_left > user_right or
                word_bottom < user_top or word_top > user_bottom)

# Main function to find words inside user-drawn bounding box
def find_words_in_bounding_box(words_position, doc_width, doc_height, user_box):
    enclosed_words = []
    for entry in words_position:  # Loop through each dictionary in the list
        word = entry["word"]
        word_box = entry["bounding_box"]
        word_pixel_box = scale_to_pixel_coordinates(word_box, doc_width, doc_height)
        print(f"Checking word: {word}, pixel box: {word_pixel_box}")  # Debugging line
        if is_within_user_box(word_pixel_box, user_box):
            enclosed_words.append(word)
    return enclosed_words

if __name__ == "__main__":
    # Inputs
    filename = 'words_position_dict.txt'  # Replace with the correct file path
    document_width = 1263
    document_height = 1644
    user_box = [358, 140, 498, 171]  # [x1, y1, x3, y3]

    # Load data and find enclosed words
    words_position = load_words_position_dict(filename)
    result = find_words_in_bounding_box(words_position, document_width, document_height, user_box)

    # Output result
    print("Words enclosed within the bounding box:", result)
