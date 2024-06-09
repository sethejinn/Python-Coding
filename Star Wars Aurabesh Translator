def translate_to_aurebesh(text):
    aurebesh = {
        'a': 'Ⰰ', 'b': 'Ⰱ', 'c': 'Ⰲ', 'd': 'Ⰳ', 'e': 'Ⰴ',
        'f': 'Ⰵ', 'g': 'Ⰶ', 'h': 'Ⰷ', 'i': 'Ⰸ', 'j': 'Ⰹ',
        'k': 'Ⰺ', 'l': 'Ⰻ', 'm': 'Ⰼ', 'n': 'Ⰽ', 'o': 'Ⰾ',
        'p': 'Ⰿ', 'q': 'Ⱀ', 'r': 'Ⱁ', 's': 'Ⱂ', 't': 'Ⱃ',
        'u': 'Ⱄ', 'v': 'Ⱅ', 'w': 'Ⱆ', 'x': 'Ⱇ', 'y': 'Ⱈ',
        'z': 'Ⱉ', ' ': 'Ⱗ', '.': 'Ⱑ', ',': 'Ⱒ', '!': 'Ⱓ',
        '?': 'Ⱔ'
    }
    
    text = text.lower()
    result = ''
    for letter in text:
        if letter in aurebesh:
            result += aurebesh[letter]
        else:
            result += letter
    return result
