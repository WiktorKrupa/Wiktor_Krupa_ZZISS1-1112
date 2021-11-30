import re
mes = "To be, or not to be, that is the question"
v = re.findall("[aeiouy]",mes)
print (len(v))