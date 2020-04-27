import re

sentence = "Stephen William Hawking CH CBE FRS FRSA (08-02-1942 – 14 March 2018) was an English theoretical physicist, cosmologist, and author who was director of research at the Centre for Theoretical Cosmology at the University of Cambridge at the time of his death"

pattern1 = "\d{2}-\d{2}-\d{4}"
pattern2 = "\d{2} \w+ \d{4}"
pattern3 = "-"

matchEn = re.findall(pattern1, sentence)
matchEn2 = re.findall(pattern2, sentence)
matchEn3 = re.findall(pattern3, sentence)
print(matchEn+matchEn2)

"""Substituir algo"""

newSetence = re.sub(pattern3, "/", sentence)

print(re.findall("\d{2}/\d{2}/\d{4}", newSetence))