def get_ascii_raw(s):
    return [ord(c) for c in s]

def get_ascii(s):
    ascii_total = ""
    ascii_str = get_ascii_raw(s)
    for ascii_c in ascii_str:
        ascii_total += str(ascii_c) + "128"

    return int(ascii_total)
