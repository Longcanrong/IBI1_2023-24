import numpy as np
import pandas as pd

def read_sequence(file_path):
    seq=''
    file=open(file_path, 'r')
    for line in file:
        if line.startswith('>'):
            continue
        else:
            seq+=line.strip()
    return seq

df = pd.read_csv('BLOSUM62.csv', index_col=0, header=0)

blosum62_matrix = df.to_dict('index')

# def calculate_score(seq1, seq2, blosum62_matrix):
#     score = 0
#     min_len = min(len(seq1), len(seq2))
#     # Ensure the two sequences are in the same length
#     for i in range(min_len):
#         aa1, aa2 = seq1[i], seq2[i]
#         score += blosum62_matrix.get(aa1, {}).get(aa2, 0)
#     # Define the calculate measures
#     return score

def calculate_score(seq1, seq2, blosum62_matrix):
    score = 0
    for aa1, aa2 in zip(seq1, seq2):
        score += blosum62_matrix[aa1][aa2]
    return score

def calculate_identity(seq1, seq2):
    identical = sum(1 for a, b in zip(seq1, seq2) if a == b)
    return (identical / len(seq1)) * 100

seq1 = read_sequence('SLC6A4_HUMAN.fa')
seq2 = read_sequence('SLC6A4_MOUSE.fa')

score = calculate_score(seq1, seq2, blosum62_matrix)
identity = calculate_identity(seq1, seq2)

print(f"Alignment Score: {score}")
print(f"Percentage of Identity: {identity}%")