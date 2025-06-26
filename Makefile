# HindiXlit Makefile - pyproject.toml based build and deployment
# Uses modern Python packaging standards with pyproject.toml

.PHONY: help install-dev clean build publish clean-all setup-venv

# Default target
help:
	@echo "HindiXlit - pyproject.toml based build system"
	@echo ""
	@echo "Setup & Installation:"
	@echo "  setup-venv     Create virtual environment"
	@echo "  install-dev    Install development dependencies"
	@echo ""
	@echo "Building & Distribution:"
	@echo "  build          Build package using pyproject.toml"
	@echo "  publish        Publish to PyPI"
	@echo ""
	@echo "Development:"
	@echo "  format         Format code"
	@echo ""
	@echo "Cleaning:"
	@echo "  clean          Clean build artifacts"
	@echo "  clean-all      Clean everything including venv"

# Virtual environment setup
setup-venv:
	@echo "Creating virtual environment..."
	python3 -m venv venv
	@echo "Virtual environment created. Activate with:"
	@echo "source venv/bin/activate  # macOS/Linux"
	@echo "venv\\Scripts\\activate     # Windows"

# Installation development dependencies
install-dev:
	@echo "Installing development dependencies..."
	pip install build twine black flake8 pytest pytest-cov

# Building using pyproject.toml
build:
	@echo "Building package using pyproject.toml and creating distribution files..."
	python -m build --sdist --wheel

publish: build
	@echo "Publishing to PyPI..."
	@echo "Note: This requires PyPI credentials"
	@echo "Run: twine upload dist/*"
	@echo "Or for test PyPI: twine upload --repository testpypi dist/*"

# Development tasks
format:
	@echo "Formatting code with black..."
	@if command -v black >/dev/null 2>&1; then \
		black hindi_xlit/ playground.py; \
	else \
		echo "black not found. Install with: make install-dev"; \
	fi

# Cleaning tasks
clean:
	@echo "Cleaning build artifacts..."
	rm -rf build/ dist/ *.egg-info/ 2>/dev/null || true
	find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	find . -type f -name "*.pyc" -delete 2>/dev/null || true
	find . -type d -name "*.egg-info" -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name ".pytest_cache" -exec rm -rf {} + 2>/dev/null || true


clean-all: clean
	@echo "Cleaning virtual environment..."
	rm -rf venv/ 2>/dev/null || true