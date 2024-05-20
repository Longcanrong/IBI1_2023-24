def find_repeat(seq, repeat_seq):
    count = 0
    for i in range(len(seq) - len(repeat_seq) + 1):  
        if repeat_seq == seq[i:i+len(repeat_seq)]:  
            count += 1
            i += 1 
    return count

count = 0
repeat_seqs = ['GTGTGT','GTCTGT']
seq = 'ATGCAATCGGTGTGTCTGTTCTGAGAGGGCCTAA'
for repeat_seq in repeat_seqs:
    count += find_repeat(seq, repeat_seq)
print(count)