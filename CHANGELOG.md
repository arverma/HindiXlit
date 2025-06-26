# Changelog

All notable changes to this project will be documented in this file.

## [1.0.1] - 2024-06-26
### Added
- Command line interface (CLI) support with `hindi-xlit <word> [topk]` command
- `pyproject.toml` configuration for modern Python packaging
- `__init__.py` files for proper package structure
- Simple playground demo script

### Changed
- Migrated from `setup.py` to `pyproject.toml` for modern Python packaging standards
- Updated README.md with accurate CLI documentation and PyPI-ready content
- Improved package structure and organization
- Updated dependencies to use more restrictive version constraints

### Removed
- `download_model.py` - model files are now included in the package
- `interactive_transliterate.py` - replaced with simple CLI interface
- `test_hindi_xlit.py` - test files removed from main package
- `MANIFEST.in` - no longer needed with pyproject.toml
- `requirements.txt` - dependencies now managed in pyproject.toml

### Fixed
- Fixed packaging logic to properly include model files
- Resolved .DS_Store tracking issues in git
- Improved error handling in transliterator

## [1.0.0] - 2024-06-09
### Added
- Initial release of HindiXlit on PyPI.
- Hindi to Devanagari transliteration using AI4Bharat's model.
- Python API: `HindiTransliterator` class with `transliterate` and `transliterate_batch`.
- Command line interface: `hindi-xlit <word> [topk]`.
- Model and data files included in the package.
