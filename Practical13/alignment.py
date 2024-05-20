import numpy as np

def read_sequence(file_path):
    seq=''
    file=open(file_path, 'r')
    for line in file:
        if line.startswith('>'):
            continue
        else:
            seq+=line
    return seq

def calculate_score(seq1, seq2):
    hamming_distance=0			
    for	i in range(len(seq1)):
        if	seq1[i]!=seq2[i]:				
            hamming_distance+=1
    return hamming_distance

def calculate_identity(seq1, seq2):
    identical = sum(1 for a, b in zip(seq1, seq2) if a == b)
    return (identical / len(seq1)) * 100

seq1 = read_sequence('SLC6A4_HUMAN.fa')
seq2 = read_sequence('SLC6A4_MOUSE.fa')

score = calculate_score(seq1, seq2)
identity = calculate_identity(seq1, seq2)

print(f"Alignment Score (hamming distance): {score}")
print(f"Percentage of Identity: {identity}%")