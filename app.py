teht1_a = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
teht1_vastaus = "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"

teht2_a = "1c0111001f010100061a024b53535009181c"
teht2_b = "686974207468652062756c6c277320657965"
teht2_vastaus = "746865206b696420646f6e277420706c6179"

def xor_two_str(hex_a,hex_b):
    xored = int(hex_a, 16) ^ int(hex_b, 16)
    return '{:x}'.format(xored)

def hex_to_base64(string):
    encoded = string.decode("hex").encode("base64")
    return encoded

if __name__ == '__main__':
    teht1_a = hex_to_base64(teht1_a)
    print("Exercise 1: ")
    print(teht1_vastaus)
    print(teht1_a)

    teht2 = xor_two_str(teht2_a, teht2_b)
    print("Exercise 2: ")
    print(teht2)
    print(teht2_vastaus)
