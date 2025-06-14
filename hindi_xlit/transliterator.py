"""
Hindi Transliterator
Using the original AI4Bharat model for Roman to Devanagari transliteration
"""

import os
from typing import List, Union
from .hindi_model import XlitPiston


class HindiTransliterator:
    """
    Hindi transliterator for Roman to Devanagari conversion (word-level only)
    """
    def __init__(self, model_dir=None, beam_size=4):
        current_dir = os.path.dirname(os.path.abspath(__file__))
        if model_dir is None:
            model_dir = os.path.join(current_dir, 'models', 'hindi')
        self.model_path = os.path.join(model_dir, 'hi_111_model.pth')
        self.vocab_path = os.path.join(model_dir, 'hi_words_a4b.json')
        self.script_path = os.path.join(model_dir, 'hi_scripts.json')
        self.beam_size = beam_size
        self.transliterator = XlitPiston(
            weight_path=self.model_path,
            tglyph_cfg_file=self.script_path,
            iglyph_cfg_file="en",
            vocab_file=self.vocab_path,
            device="cpu"
        )
        # Expose model for testing
        self.model = self.transliterator.model

    def transliterate(self, word: str, topk: int = 1) -> Union[str, List[str]]:
        """
        Transliterate a single Roman word to Devanagari (Hindi)
        Args:
            word: Input word (string)
            topk: Number of top transliterations to return (default: 1)
        Returns:
            If topk=1: Single transliterated word
            If topk>1: List of top-k transliterated words
        """
        if word is None:
            raise ValueError("Input must not be None")
        if not isinstance(word, str):
            raise ValueError("Input must be a string")
        if not word.strip():
            return "" if topk == 1 else [""]
            
        # Handle special characters
        special_chars = []
        word_chars = []
        for char in word:
            if char.isalpha():
                word_chars.append(char)
            else:
                special_chars.append(char)
        
        # Transliterate word
        if word_chars:
            transliterated = self.transliterator.inferencer(''.join(word_chars), beam_width=topk)
            results = transliterated[:topk]
        else:
            results = ['']
        
        # Add special characters
        results = [r + ''.join(special_chars) for r in results]
        
        return results[0] if topk == 1 else results

    def transliterate_batch(self, words: List[str], topk: int = 1) -> List[Union[str, List[str]]]:
        """Transliterate a batch of words"""
        if words is None:
            raise ValueError("Input must not be None")
        if not isinstance(words, list):
            raise ValueError("Input must be a list of strings")
        return [self.transliterate(w, topk) for w in words] 