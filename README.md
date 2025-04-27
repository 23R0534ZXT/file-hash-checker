# File Hash Checker

A simple Python tool to calculate file hashes (MD5, SHA256) and check if they match. Made by 23R.

I built this for a school project to learn about file integrity in cybersecurity. It uses Tkinter for a basic GUI and saves results to a JSON file.

## Features

- Pick a file and choose MD5 or SHA256.
- See the hash and compare it to one you have.
- Saves everything to `hashes.json`.
- Easy to use with a simple window.

## Requirements

- Python 3.8 or higher
- No extra libraries (just uses tkinter and hashlib, which come with Python)

## How to Install

1. Clone the repo:
   ```bash
   git clone https://github.com/yourusername/file-hash-checker.git
   ```
2. Run the script:
   ```bash
   python hash_checker.py
   ```

## How to Use

1. Open the program, it’ll show a small window.
2. Click "Browse" to pick a file (like a .txt or .jpg).
3. Choose MD5 or SHA256 from the dropdown.
4. If you have a hash to compare, type it in the "Expected hash" box.
5. Click "Calculate" to get the hash and see if it matches.
6. Results are saved in `hashes.json` in the same folder.

## Notes

- This is just a school project, so it’s pretty basic.
- Use it to check if files are safe, like when you download something.
- If it crashes, make sure you picked a real file!

## License

MIT License. Check out [LICENSE](LICENSE) for more info.

## Author

23R 
