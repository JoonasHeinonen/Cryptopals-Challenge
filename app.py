string = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"

def compare_2_strings(hex1, hex2):
    if (hex1 == hex2 and hex2 == hex1):
	return true
    return false

def hex_to_base64(string):
    encoded = string.decode("hex").encode("base64")
    return encoded

if __name__ == '__main__':
    string = hex_to_base64(string)
    print(string)
