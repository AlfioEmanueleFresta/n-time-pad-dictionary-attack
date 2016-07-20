from itertools import combinations
from time import time


# Bitwise XOR two ASCII strings (results in an ASCII string)
def sxor(s1, s2):
    return ''.join(chr(ord(a) ^ ord(b)) for a, b in zip(s1, s2))


# Gets the binary equivalent of any ASCII string (i.e.: "mo" => "01101101 01101111")
def strbin(s):
    return " ".join("{:08b}".format(ord(x)) for x in s)


m1  = "makes"
m2  = "sense"
key = "#m$e%"

# Makes messages lowercase -- simply because our
#  dictionary is lowercase.
m1, m2 = m1.lower(), m2.lower()

c1 = sxor(m1, key)
c2 = sxor(m2, key)
cx = sxor(c1, c2)

# Prints messages and keys in binary
print(" ")
print("M1 : %s (%s)" % (m1, strbin(m1)))
print("Key: %s (%s)" % (key, strbin(key)))
print("---(XOR)-----%s" % ("-"*len(strbin(key))))
print("C1 : %s (%s)" % ("*" * len(m2), strbin(c1)))
print(" ")
print("M2 : %s (%s)" % (m2, strbin(m2)))
print("Key: %s (%s)" % (key, strbin(key)))
print("---(XOR)-----%s" % ("-"*len(strbin(key))))
print("C2 : %s (%s)" % ("*" * len(m2), strbin(c2)))
print(" ")


words_filename = "dictionary/words%d.txt" % len(cx)
with open(words_filename, 'r') as f:

    print("Searching word combinations in %s...\n" % words_filename)
    start_time = time()
    words_combinations = combinations(f, 2)

    found = 0
    for w1, w2 in words_combinations:
        w1, w2 = w1.rstrip('\n'), w2.strip('\n')
        wx = sxor(w1, w2)

        if cx == wx:
            found += 1
            print(" * Found possible combination (M1=%s, M2=%s)" % (w1, w2))
            print("   M1=%s, M2=%s\n" % (strbin(w1), strbin(w2)))


elapsed_time = time() - start_time
print("Found %d possible combination(s) in %f seconds." % (found, elapsed_time))
