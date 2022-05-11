#!/usr/bin/env python

'''
Testing for genomic sequences and analysis
'''

import numpy as np
import re
import random

from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder


# create a label encoder with 'acgtz' alphabet
label_encoder = LabelEncoder()
# label_encoder.fit(np.array(['a','c','g','t','z']))
label_encoder.fit(np.array(['a','c','g','t']))


# one-hot encode a DNA sequence string
def one_hot_encoder(my_array):
    integer_encoded = label_encoder.transform(my_array)
    categories = [range(5)] * 1
    onehot_encoder = OneHotEncoder(sparse=False, dtype=int, categories=categories, handle_unknown='ignore')
    integer_encoded = integer_encoded.reshape(len(integer_encoded), 1)
    onehot_encoded = onehot_encoder.fit_transform(integer_encoded)
    onehot_encoded = np.delete(onehot_encoded, -1, 1)

    return onehot_encoded


# seq to vec
def seq_to_vec(sequence):
    seq_arr = np.array(list(sequence.lower()))
    seq_integer_encoded = label_encoder.transform(seq_arr)
    seq_onehot = one_hot_encoder(seq_arr)
    seq_vec = seq_onehot.flatten()

    return seq_vec


# generate random DNA sequence
def generate_test_seq(seqlen_init=10):
    bases = 'ACGT'
    sequence = ''.join(random.choice(bases) for i in range(seqlen_init))

    return sequence


def main():
    # DNA sequence length
    seq_len = 10

    test_sequence = generate_test_seq(seq_len)
    print(f'random DNA sequence of length {seq_len}: {test_sequence}')

    test_seq_vec = seq_to_vec(test_sequence)
    print(f'DNA sequence vector encoded: {test_seq_vec}')


if __name__ == '__main__':
    main()
