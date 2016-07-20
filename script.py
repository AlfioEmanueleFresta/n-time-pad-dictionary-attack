from itertools import combinations


# Bitwise XOR two ASCII strings (results in an ASCII string)
def sxor(s1, s2):
    return ''.join(chr(ord(a) ^ ord(b)) for a, b in zip(s1, s2))


# Gets the binary equivalent of any ASCII string (i.e.: "mo" => "01101101 01101111")
def strbin(s):
    return " ".join("{:08b}".format(ord(x)) for x in s)


m1  = "yelling"
m2  = "monster"
key = "1234567"

m1, m2, key = m1.lower(), m2.lower(), key.lower()

c1 = sxor(m1, key)
c2 = sxor(m2, key)
cx = sxor(c1, c2)

print(" ")
print("Key: %s (%s)" % (key, strbin(key)))
print("M1 : %s (%s)" % (m1, strbin(m1)))
print("C1 : %s (%s)" % ("X" * len(m2), strbin(c1)))
print(" ")
print("Key: %s (%s)" % (key, strbin(key)))
print("M2 : %s (%s)" % (m2, strbin(m2)))
print("C2 : %s (%s)" % ("X" * len(m2), strbin(c2)))
print(" ")


words_filename = "dictionary/words%d.txt" % len(cx)
with open(words_filename, 'r') as f:

    print("Searching word combinations in %s..." % words_filename)
    words_combinations = combinations(f, 2)

    for w1, w2 in words_combinations:
        w1, w2 = w1.rstrip('\n'), w2.strip('\n')
        wx = sxor(w1, w2)

        if cx == wx:
            print(" * Found possible combination (M1=%s, M2=%s)" % (w1, w2))

print(" ")
print("End.")
