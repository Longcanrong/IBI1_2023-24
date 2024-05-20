def parse_fasta_file(fasta_file):
    sequences = []
    current_sequence = None
    file =  open(fasta_file, 'r')
    for line in file:
        line = line.strip()
        if line.startswith('>'):
            if current_sequence:
                sequences.append(current_sequence)
            current_sequence = {'header': line, 'sequence': ''}
        else:
            if current_sequence:
                current_sequence['sequence'] += line
    if current_sequence:
        sequences.append(current_sequence)
    return sequences

def find_repeat(seq, repeat_seq):
    count = 0
    for i in range(len(seq) - len(repeat_seq) + 1):  
        if repeat_seq == seq[i:i+len(repeat_seq)]:  
            count += 1
            i += 1
    return count

def count_repeats(sequences, repeat):
    resulting_sequences = []
    for seq in sequences:
        if 'duplication' in seq['header'] and repeat in seq['sequence']:
            count = find_repeat(seq['sequence'],repeat)
            gene_name = seq['header'].split()[0]
            resulting_sequences.append({'header': gene_name, 'count': count, 'sequence': seq['sequence']})
    return resulting_sequences, count

def write_fasta_file(sequences, count, output_file,):
    file = open(output_file, 'w')
    for seq in sequences:
        file.write(seq['header'] + f" repeat count is {seq['count']}" + '\n')
        file.write(seq['sequence'] + '\n')


repeat = input("Please enter one of the repetitive sequences: ").strip()

fasta_file = 'Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa'
output_file = f"{repeat}_duplicate_genes.fa"
# output_file = f"F:\Desktop\IBI\Practical8\{repeat}_duplicate_genes.fa"
# fasta_file = 'F:\Desktop\IBI\Practical8\Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa'

sequences = parse_fasta_file(fasta_file)
resulting_sequences, count = count_repeats(sequences, repeat)
write_fasta_file(resulting_sequences, count, output_file)