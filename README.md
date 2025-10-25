# QR Code Generator

Simple Python script to generate QR codes from URLs.

## Requirements

- Python 3.x
- Libraries listed in `requirements.txt`

## Installation
```bash
pip install -r requirements.txt
```

## Usage

**Interactive mode:**
```bash
python qr_generator.py
```

**With arguments:**
```bash
python qr_generator.py <URL> [filename.png]
```

## Examples
```bash
# Interactive mode
python qr_generator.py

# Generates qr_code.png by default
python qr_generator.py https://www.linkedin.com/in/tobias-david-veiga/

# Specify the filename
python qr_generator.py https://www.linkedin.com/in/tobias-david-veiga/ linkedin_qr.png
```

## Features

- Generates QR codes in PNG format
- Automatically adds .png extension if not specified
- Interactive mode or command-line arguments
