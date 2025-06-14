import unittest
import os
import torch
from hindi_xlit.transliterator import HindiTransliterator
from hindi_xlit.hindi_model import XlitPiston

def format_hindi(text):
    """Convert Hindi text to a readable format showing Unicode escape sequences"""
    return ''.join(f'\\u{ord(c):04x}' for c in text)

class TestHindiTransliterator(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Set up test fixtures before running tests."""
        cls.model_path = os.path.join(os.path.dirname(__file__), "models", "hindi", "hi_111_model.pth")
        cls.transliterator = HindiTransliterator()

    def test_model_initialization(self):
        """Test if the model initializes correctly."""
        self.assertIsNotNone(self.transliterator.model)
        self.assertIsInstance(self.transliterator.transliterator, XlitPiston)

    def test_basic_transliteration(self):
        """Test basic transliteration functionality."""
        test_cases = [
            ("namaste", "नमस्ते"),
            ("bharat", "भारत"),
            ("hindi", "हिंदी"),
            ("swagat", "स्वागत"),
        ]
        
        for roman, expected in test_cases:
            result = self.transliterator.transliterate(roman)
            if result != expected:
                print(f"\nFailed transliteration for '{roman}':")
                print(f"Expected: {expected} ({format_hindi(expected)})")
                print(f"Got:      {result} ({format_hindi(result)})")
            self.assertEqual(result, expected, f"Failed to transliterate '{roman}'")

    def test_empty_input(self):
        """Test handling of empty input."""
        result = self.transliterator.transliterate("")
        self.assertEqual(result, "")

    def test_special_characters(self):
        """Test handling of special characters."""
        test_cases = [
            ("hello!", "हेलो!"),
            ("test123", "टेस्ट123"),
        ]
        
        for roman, expected in test_cases:
            result = self.transliterator.transliterate(roman)
            if result != expected:
                print(f"\nFailed transliteration for '{roman}':")
                print(f"Expected: {expected} ({format_hindi(expected)})")
                print(f"Got:      {result} ({format_hindi(result)})")
            self.assertEqual(result, expected, f"Failed to transliterate '{roman}'")

    def test_model_save_load(self):
        """Test if the model can be saved and loaded correctly."""
        # Save the model
        torch.save(self.transliterator.model.state_dict(), self.model_path)
        
        # Create a new instance and load the model
        new_transliterator = HindiTransliterator()
        
        # Test if both instances produce the same output
        test_word = "namaste"
        result1 = self.transliterator.transliterate(test_word)
        result2 = new_transliterator.transliterate(test_word)
        if result1 != result2:
            print(f"\nFailed model save/load test:")
            print(f"Original: {result1} ({format_hindi(result1)})")
            print(f"Loaded:   {result2} ({format_hindi(result2)})")
        self.assertEqual(result1, result2)

    def test_batch_transliteration(self):
        """Test batch transliteration functionality."""
        test_words = ["namaste", "bharat", "hindi"]
        expected = ["नमस्ते", "भारत", "हिंदी"]
        results = self.transliterator.transliterate_batch(test_words)
        if results != expected:
            print("\nFailed batch transliteration:")
            for i, (word, exp, res) in enumerate(zip(test_words, expected, results)):
                if exp != res:
                    print(f"\nWord {i+1} ('{word}'):")
                    print(f"Expected: {exp} ({format_hindi(exp)})")
                    print(f"Got:      {res} ({format_hindi(res)})")
        self.assertEqual(results, expected)

    def test_invalid_input(self):
        """Test handling of invalid input."""
        with self.assertRaises(ValueError):
            self.transliterator.transliterate(None)
        
        with self.assertRaises(ValueError):
            self.transliterator.transliterate_batch(None)
            
        with self.assertRaises(ValueError):
            self.transliterator.transliterate(123)  # Non-string input
            
        with self.assertRaises(ValueError):
            self.transliterator.transliterate_batch("not a list")  # Non-list input

if __name__ == '__main__':
    unittest.main() 