#!/usr/bin/env python3
"""
Interactive Hindi Transliteration Script
Takes English input and shows Hindi output in a readable format
"""

import os
from .transliterator import HindiTransliterator

def print_hindi(text, is_list=False):
    """Print Hindi text with a clear label"""
    print("\nHindi Output:")
    print("=" * 50)
    if is_list:
        for i, t in enumerate(text, 1):
            print(f"{i}. {t}")
    else:
        print(text)
    print("=" * 50)

def main():
    # Initialize the transliterator
    transliterator = HindiTransliterator()
    
    print("\nWelcome to Hindi Transliterator!")
    print("Type 'quit' or 'exit' to end the program")
    print("Type 'help' to see example words")
    print("Type 'topk N' to set number of transliterations (e.g., 'topk 5')")
    print("\nEnter English words to transliterate to Hindi:")
    
    examples = [
        "namaste",
        "bharat",
        "hindi",
        "swagat",
        "dhanyavaad"
    ]
    
    topk = 1  # Default to single output
    
    while True:
        try:
            # Get input
            english = input("\nEnglish > ").strip()
            
            # Check for exit commands
            if english.lower() in ['quit', 'exit']:
                print("\nGoodbye!")
                break
                
            # Show help
            if english.lower() == 'help':
                print("\nExample words:")
                for word in examples:
                    hindi = transliterator.transliterate(word, topk)
                    if isinstance(hindi, list):
                        print(f"\n{word}:")
                        for i, h in enumerate(hindi, 1):
                            print(f"  {i}. {h}")
                    else:
                        print(f"{word:15} → {hindi}")
                continue
            
            # Set topk
            if english.lower().startswith('topk '):
                try:
                    new_topk = int(english.split()[1])
                    if new_topk > 0:
                        topk = new_topk
                        print(f"\nNow showing top {topk} transliterations")
                    else:
                        print("\nPlease enter a positive number")
                except (IndexError, ValueError):
                    print("\nPlease use format: topk N (e.g., topk 5)")
                continue
            
            # Skip empty input
            if not english:
                continue
                
            # Transliterate
            hindi = transliterator.transliterate(english, topk)
            print_hindi(hindi, isinstance(hindi, list))
            
        except KeyboardInterrupt:
            print("\n\nGoodbye!")
            break
        except Exception as e:
            print(f"\nError: {str(e)}")

if __name__ == "__main__":
    main() 