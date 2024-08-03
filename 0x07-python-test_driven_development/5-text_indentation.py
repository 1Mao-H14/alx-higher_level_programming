#!/usr/bin/python3
"""Defines a text-indentation function."""

def text_indentation(text):
    """Print text with two new lines after each '.', '?', and ':'.

    Args:
        text (string): The text to print.
    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    
    result = []
    i = 0
    length = len(text)
    
    for char in text:
        result.append(char)
        
        if char in '.?':
            result.append('\n')
            result.append('\n')
            
            while i + 1 < length and text[i + 1] == ' ':
                i += 1
        elif char == ':':
            result.append('\n')
            
            while i + 1 < length and text[i + 1] == ' ':
                i += 1
        i += 1
    
    final_text = ''.join(result).strip()
    print(final_text)
