"""
Hindi Transliteration Library
============================

A Python library for transliterating English text to Hindi using AI4Bharat's model.
"""

try:
    from importlib.metadata import version
    __version__ = version("hindi_xlit")
except ImportError:
    __version__ = "unknown"

from .transliterator import HindiTransliterator

__all__ = ["HindiTransliterator"]
