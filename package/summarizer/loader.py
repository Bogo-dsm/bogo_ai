import re

def pdf_load(text : str) -> str:
    roman_numerals = {'Ⅰ': '1', 'Ⅱ': '2', 'Ⅲ': '3', 'Ⅳ': '4', 'Ⅴ': '5'}

    text = text.replace('\n\n', '[[NEWLINE]]')
    text = re.sub(r'\n\s*-\s*\d+\s*-\s*\n', '\n', text)
    text = re.sub(r'(?<![.!?])\n', ' ', text)
    text = text.replace('[[NEWLINE]]', '\n\n')
    text = re.sub(r' +', ' ', text)
    for roman_numeral in roman_numerals: text = text.replace(roman_numeral, roman_numerals[roman_numeral])
    re_text = text.strip()

    return re_text