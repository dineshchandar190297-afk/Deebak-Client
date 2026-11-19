import re

def fix_file(filepath):
    with open(filepath, 'rb') as f:
        content_bytes = f.read()

    # Convert bytes to string (Latin1 representation of UTF-8)
    text = content_bytes.decode('utf-8', errors='ignore')

    # Regex pattern to match Mojibake text containing 'à'
    def fix_mojibake(match):
        val = match.group(0)
        try:
            return val.encode('latin1').decode('utf-8')
        except Exception:
            return val

    # Match sequences starting with à or Ã or similar Mojibake prefix
    fixed_text = re.sub(r'à[®¤°´А-яA-Za-z0-9_~\^\%\$\#\@\!\&\*\(\)\-\+\=\[\]\{\}\|\\\;\:\'\"\,\<\.\>\/\?\s\¬\ˆ\‰\Š\Ž\‘\’\“\”\–\—\†\‡\•\…\™\¢\£\¤\¥\¦\§\¨\©\ª\«\¬\­\®\¯\°\±\²\³\´\µ\¶\·\¸\¹\º\»\¼\½\¾\¿]+', fix_mojibake, text)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(fixed_text)
    print(f"Fixed encoding for {filepath}")

fix_file(r"c:\Users\dines\Downloads\Deebak Client\utils\ai.ts")
