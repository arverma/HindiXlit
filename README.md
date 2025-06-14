# Hindi Transliterator

A Python package for Roman to Devanagari (Hindi) transliteration using AI4Bharat's model.

## Features

- Word-level transliteration from Roman to Devanagari
- Support for multiple transliteration options (top-k)
- Interactive command-line interface
- Simple Python API
- CPU-only (no GPU required)

## Installation

```bash
pip install hindi-xlit
```

## Usage

### Command Line Interface

```bash
# Start interactive transliterator
hindi-xlit

# Set number of transliterations to show
topk 5

# Enter words to transliterate
namaste
bharat
hindi
```

### Python API

```python
from hindi_xlit import HindiTransliterator

# Initialize the transliterator
transliterator = HindiTransliterator()

# Single word transliteration
hindi = transliterator.transliterate("namaste")
print(hindi)  # नमस्ते

# Get multiple transliterations
hindi_options = transliterator.transliterate("bharat", topk=3)
print(hindi_options)  # ['भारत', 'भरत', 'भरट']

# Batch transliteration
words = ["namaste", "bharat", "hindi"]
results = transliterator.transliterate_batch(words)
print(results)  # ['नमस्ते', 'भारत', 'हिंदी']
```

## Model

This package uses AI4Bharat's Hindi transliteration model. The model files are automatically downloaded when the package is installed.

## Development

1. Clone the repository:
```bash
git clone https://github.com/yourusername/hindi_xlit.git
cd hindi_xlit
```

2. Install development dependencies:
```bash
pip install -e ".[dev]"
```

3. Run tests:
```bash
python -m pytest
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [AI4Bharat](https://ai4bharat.org/) for the original transliteration model
