#!environment/bin/python3
"""
Clean up weird entries on your form.
"""

# Major concern here is PERFORMANCE. Test, and measure.

# str.upper() and str.lower()

# str.replace() and re.sub()

# data.normalize() --> 2.9

# str.translate()

s = 'pýtĥöñ\fis\tawesome\r\n'

remap = { #translation table
    ord('\t'): ' ',
    ord('\f'): ' ',
    ord('\r'): None # Delete
}

a = s.translate(remap)
print(a) # pýtĥöñ is awesome

# Remove al combining characters
import unicodedata
import sys
cmb_chrs = dict.fromkeys(c for c in range(sys.maxunicode)
                            if unicodedata.combining(chr(c)))
    # Dictionary mapping every Unicode combining character to None
b = unicodedata.normalize('NFD',a) # normalize

fin = b.translate(cmb_chrs) # remove combined characters

print(fin) # python is awesome\n


# Map all Unicode decimal digits to their ASCII equivalent.

digitmap = {c: ord('0') + unicodedata.digit(chr(c))
            # position of 0 plus the number of steps to chr(c)
            for c in range(sys.maxunicode)
            if unicodedata.category(chr(c)) == 'Nd'
            # if number
            }

x = '\u0661\u0662\u0663'
print(x) # ١٢٣

print(x.translate(digitmap)) # 123


# Encode or Decode operations
print(a) #pýtĥöñ is awesome\n

d = unicodedata.normalize('NFD',a)
e = d.encode('ascii','ignore').decode('ascii')

print(e) # python is awesome\n
