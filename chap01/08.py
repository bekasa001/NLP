def _cipher_one_letter(c):
	c_ord = ord(c)
	if (ord('a') <= c_ord and c_ord <= ord('z')):
		return chr(219 - c_ord)
	return c

def cipher(string):
	return "".join(map(_cipher_one_letter, string))

print(cipher(input()))
