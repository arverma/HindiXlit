"""
Hindi Transliteration Library
A lightweight CPU-only library for Roman to Devanagari (Hindi) transliteration.
"""

from .transliterator import HindiTransliterator
from .hindi_model import XlitPiston

__version__ = "1.0.0"
__all__ = ['HindiTransliterator', 'XlitPiston'] 