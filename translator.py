from deep_translator import GoogleTranslator


def translate(st):
    translated = GoogleTranslator(source='auto', target='ru').translate(st)

    result = ''
    allowed = ' ,?!.'
    for char in translated:
        if 1040 <= ord(char) <= 1106 or char in allowed:
            result += char

    return ' '.join(result.split())
