#!/usr/bin/env python

'''
biopython SeqIO of DNA sequences

'''

import numpy as np
import re

from Bio import SeqIO


# for record in SeqIO.parse('fasta/NC_000011.10.fasta', "fasta"):
#     print(record.id)
#     print(record.seq[:10])
#     print(len(record.seq))
#     # seq_id = record.id
#     # seq = record.seq

record = SeqIO.read('fasta/NC_000011.10.fasta', "fasta")
print(record.id)
print(len(record))

# get seq as a string and convert to lower
one_seq = str(record.seq.lower())
# print(one_seq[:10])

# convert to array
seq_arr = np.array(list(one_seq))
print(seq_arr[:10])


# ----------------

seq1 = SeqIO.read('fasta/NC_000011.10.fasta', "fasta")
seq2 = SeqIO.read('fasta/NC_000012.12.fasta', "fasta")

from Bio import pairwise2
from Bio.pairwise2 import format_alignment

alignments = pairwise2.align.globalxx(seq1, seq2)
for alignment in alignments:
    print(alignment)
    print(format_alignment(*alignment))
