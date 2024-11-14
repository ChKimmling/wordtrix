
# WordTrix

WordTrix is a command-line tool and library for managing and checking anagrams. It provides both interactive and non-interactive modes for adding, checking, listing, and clearing anagram pairs in a JSON-based database.

## Features

- Check if two words are anagrams.
- List all stored anagram pairs.
- Find matching anagrams for a single word.
- Manage stored words with interactive and non-interactive command-line options.

## Requirements

- Python 3.12 or higher
- `setuptools` and `wheel` for building the package
- `twine` for uploading to PyPI (optional)

## Setting Up a Virtual Environment

It is recommended to use a virtual environment to keep dependencies isolated.

1. **Create a virtual environment:**

   ```bash
   python3 -m venv venv
   ```

2. **Activate the virtual environment:**

   - On Windows:
     ```bash
     .\venv\Scripts\activate
     ```
   - On macOS and Linux:
     ```bash
     source venv/bin/activate
     ```

3. **Install dependencies (if any):**

   If your package has dependencies listed in `requirements.txt`, install them with:
   
   ```bash
   pip install -r requirements.txt
   ```

## Building the Package

1. **Navigate to the project directory:**

   ```bash
   cd wordtrix
   ```

2. **Install `setuptools` and `wheel` (if not already installed):**

   ```bash
   pip install setuptools wheel
   ```

3. **Build the package:**

   Run the following command to create both `.whl` (wheel) and `.tar.gz` (source) distributions in the `dist` folder:

   ```bash
   python setup.py sdist bdist_wheel
   ```

   After building, you should see files in the `dist` directory, such as:
   
   - `wordtrix-0.1.0.tar.gz`
   - `wordtrix-0.1.0-py3-none-any.whl`

## Installing the Package

To install the package locally from the `dist` directory:

```bash
pip install dist/wordtrix-0.1.0-py3-none-any.whl
```

Or, to install it from the source:

```bash
pip install dist/wordtrix-0.1.0.tar.gz
```

## Using WordTrix

### Command-Line Options

The WordTrix CLI supports several command-line options:

- `--interactive`: Start the interactive mode.
- `--list`: List all stored anagram pairs.
- `--clear`: Clear all stored anagram pairs.
- `--check <subject1> <subject2>`: Check if `subject1` and `subject2` are anagrams.
- `--match <subject>`: Find if a stored pair matches the provided `subject`.

### Example Usage

1. **Check if two words are anagrams:**

   ```bash
   python -m wordtrix --check listen silent
   ```

2. **List all stored anagram pairs:**

   ```bash
   python -m wordtrix --list
   ```

3. **Start interactive mode:**

   ```bash
   python -m wordtrix --interactive
   ```

4. **Clear all anagram pairs:**

   ```bash
   python -m wordtrix --clear
   ```

## Uploading to PyPI (Optional)

If you want to make the package publicly available on PyPI, follow these steps:

1. **Install `twine`:**

   ```bash
   pip install twine
   ```

2. **Upload the package:**

   ```bash
   twine upload dist/*
   ```

   You will be prompted to enter your PyPI credentials. After a successful upload, the package will be available on PyPI and installable with:

   ```bash
   pip install wordtrix
   ```

## Testing the Installation

To verify that the package is installed correctly, try importing it in Python:

```python
import wordtrix
```

## License

Include the license information here, such as `MIT License`.

---