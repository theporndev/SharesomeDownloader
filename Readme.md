# ssdownload

**ssdownload** is a Python-based command-line tool to download videos from **[Sharesome](https://sharesome.net)**.

## Features

- Downloads videos from Sharesome post URLs.
- Asynchronous behavior powered by `aiohttp` and `aiofiles`.
- Automatically retries when failures occur.
- Simple console-based execution.

## Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Install the tool:
   ```bash
   pip install .
   ```

## Usage

Run the `ssdownload` command in the terminal:

- **Passing URLs as arguments**:
   ```bash
   ssdownload <url1> <url2> <url3>
   ```
  Replace `<url1>`, `<url2>`, etc., with valid Sharesome post URLs.

- **Interactive mode**:
  Run the tool without arguments to input a Sharesome post URL manually.
   ```bash
   ssdownload
   Enter post URL: https://sharesome.net/post/<post_id>
   ```

## Requirements

- `aiohttp~=3.11.10`
- `aiofiles~=24.1.0`
- `beautifulsoup4~=4.10.0`
- `setuptools~=59.6.0`

Install using:

```bash
pip install -r requirements.txt
```

## Notes

- The tool only supports downloading posts from [Sharesome](https://sharesome.net).
- Videos are saved to the current working directory.

## License

This project is open-source and licensed under the MIT License.

Enjoy downloading! 🎥