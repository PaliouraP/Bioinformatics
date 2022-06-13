"""
Bioinformatics Thema 3
An Introduction to Bioinformatics Algorithms ex. 6.14
Team:
Palioura Paraskevi P19129,
Petropoulou Maria P19140,
Myrto Spatha P19156
"""

from Bio import SeqIO
import random

nucleotides = {}


def get_fasta(name, file):
    seq = SeqIO.parse(open(file), 'fasta')
    for fasta in seq:
        nucleotides[name] = len(str(fasta.seq))


get_fasta("pygb", "pygb.fasta")
get_fasta("pygl", "pygl.fasta")
get_fasta("pygm", "pygm.fasta")

print(nucleotides)

n = random.choice(list(nucleotides.items()))
m = n
while n == m:
    m = random.choice(list(nucleotides.items()))


def strategy(a, b):
    if a[1] >= b[1] and a[1] % 3 == 0:
        print("This is a losing position because " + a[0] +
              "'s number of nucleotides is a multiple of 3 and is larger than the number of nucleotides of " + b[0] +
              ". You should play second.")
    elif a[1] <= b[1] and b[1] % 3 == 0:
        print("This is a losing position because " + b[0] +
              "'s number of nucleotides is a multiple of 3 and is larger than the number of nucleotides of " + a[0] +
              ". You should play second.")
    elif a[1] == b[1] and (a[1] - 1) % 3 == 0:
        print("This is a losing position because the two isoenzymes have the same number of nucleotides which, "
              "if subtracted by 1, is a multiple of 3. (The number is: " + a[1] + "). You should play second.")
    else:
        print("This is a winning position.")
        if (n[1] >= m[1] and (n[1] - 2) % 3 == 0) or (n[1] <= m[1] and (m[1] - 1) % 3 == 0):
            print("You should play first and remove 2 nucleotides from " + str(n[0]) + " and 1 nucleotide from " + str(
                m[0]))
        elif (n[1] >= m[1] and (n[1] - 1) % 3 == 0) or (n[1] <= m[1] and (m[1] - 2) % 3 == 0):
            print("You should play first and remove 1 nucleotide from " + str(n[0]) + " and 2 nucleotide from " + str(
                m[0]))


print("The first isoenzym is: " + str(n[0]) + " and consists of " + str(n[1]) +
      " nucleotides.\nThe second isoenzym is: " + str(m[0]) + " and consists of " + str(m[1]) +
      " nucleotides.\n")
strategy(n, m)

