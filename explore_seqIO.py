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
