import re

cp1252_map = {
    '\u20AC': 0x80, '\u201A': 0x82, '\u0192': 0x83, '\u201E': 0x84,
    '\u2026': 0x85, '\u2020': 0x86, '\u2021': 0x87, '\u02C6': 0x88,
    '\u2030': 0x89, '\u0160': 0x8A, '\u2039': 0x8B, '\u0152': 0x8C,
    '\u017D': 0x8E, '\u2018': 0x91, '\u2019': 0x92, '\u201C': 0x93,
    '\u201D': 0x94, '\u2022': 0x95, '\u2013': 0x96, '\u2014': 0x97,
    '\u02DC': 0x98, '\u2122': 0x99, '\u0161': 0x9A, '\u203A': 0x9B,
    '\u0153': 0x9C, '\u017E': 0x9E, '\u0178': 0x9F
}

def decode_token(token):
    b = bytearray()
    for ch in token:
        if ch in cp1252_map:
            b.append(cp1252_map[ch])
        elif ord(ch) <= 255:
            b.append(ord(ch))
        else:
            return token
    try:
        return b.decode('utf-8')
    except Exception:
        return token

def fix_mojibake_file(path):
    with open(path, 'r', encoding='utf-8', errors='ignore') as f:
        text = f.read()

    # Pattern for Mojibake sequences starting with à or Ã or Â
    def replacer(m):
        return decode_token(m.group(0))

    fixed = re.sub(r'[àÃÂ][^\s\'\",;:\{\}\[\]\(\)]+', replacer, text)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(fixed)
    print(f"Fixed Mojibake in {path}")

fix_mojibake_file(r"c:\Users\dines\Downloads\Deebak Client\constants\translations.ts")
fix_mojibake_file(r"c:\Users\dines\Downloads\Deebak Client\utils\ai.ts")
