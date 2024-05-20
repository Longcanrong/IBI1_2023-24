def parse_fasta_file(fasta_file):
    file= open(fasta_file, 'r')
    sequences = []
    current_sequence = None
    for line in file:
        line = line.strip()
        if line.startswith('>'):
            if current_sequence:
                sequences.append(current_sequence)
            current_sequence = {'header': line, 'sequence': ''}
        else:
            current_sequence['sequence'] += line
    if current_sequence:
        sequences.append(current_sequence)
    return sequences

def find_sequences(sequences):
    resulting_sequences = []
    for seq in sequences:
        if 'duplication' in seq['header']:
            gene_name = seq['header'].split()[0]
            resulting_sequences.append({'header': gene_name, 'sequence': seq['sequence']})
    return resulting_sequences

def write_fasta_file(sequences, output_file):
    file = open(output_file, 'w')
    for seq in sequences:
        file.write(seq['header'] + '\n')
        file.write(seq['sequence'] + '\n')

fasta_file = 'Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa' 
#Maybe there is something wrong, when I used F:\*******\file_name, it worked correctly. But when I just used file_name, it showed Error no such file.
output_file = 'duplicate_genes.fa'
keyword = 'duplication'
sequences = parse_fasta_file(fasta_file)
resulting_sequences = find_sequences(sequences)
write_fasta_file(resulting_sequences, output_file)