code = "SYNTFjmtkOWFNZdjkkNH"


def _rot13(c):
    if 'A' <= c <= 'Z':
        # 13 文字分ずらす
        return chr((ord(c) - ord('A') + 13) % 26 + ord('A'))

    if 'a' <= c <= 'z':
        # 13 文字分ずらす
        return chr((ord(c) - ord('a') + 13) % 26 + ord('a'))

    # その他の文字は対象外
    return c


result = ""

for ch in code:
    result += _rot13(ch)

print(result)

