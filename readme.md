# Bounding Box Word Search

This project is a Python script that searches for words enclosed within a user-drawn rectangular bounding box on a document.

## Objective
Given a list of words and their bounding boxes (in scaled coordinates), find which words are contained within a specified bounding box on a document.

## Input
- `words_position_dict.txt`: A file containing a list of words and their bounding box positions.
- Document width: 1263 pixels
- Document height: 1644 pixels
- User-drawn bounding box: `[x1, y1, x3, y3]` in pixels

## Output
- A list of words within the bounding box.

## How to Run
1. Ensure `words_position_dict.txt` is in the same directory.
2. Run `main.py` to find words inside the bounding box.

```bash
python main.py
```
