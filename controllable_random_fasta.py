import random

def generate_random_fasta_sequence(sequence_length, frequencies, max_repeat = 6):
    nucleotides = ['A', 'C', 'G', 'T']
    sequence = []

    while len(sequence) < sequence_length:
        nucleotide = random.choices(nucleotides, weights=frequencies, k=1)[0]
        sequence.append(nucleotide)

        # Check for consecutive repeats of size max_repeat
        if len(sequence) >= max_repeat:
            repeat_sequence = sequence[-max_repeat:]
            if all(n == repeat_sequence[0] for n in repeat_sequence):
                sequence.pop()  # Remove the last nucleotide to break the repeat

    sequence = ''.join(sequence)
    return sequence

# Specify the desired sequence length
sequence_length = 500  # Change this to your desired length
# Specify the desired frequencies for A, C, G, and T (sum of frequencies should be 1)
frequencies = [0.25, 0.25, 0.25, 0.25]

for i in range(1,11):
    # Generate the random FASTA sequence
    fasta_sequence = generate_random_fasta_sequence(sequence_length, frequencies)
    print(f">Random_Sequence_{i}\n{fasta_sequence}\n")

#References
#https://eu.idtdna.com/pages/support/faqs/what-types-of-sequence-motifs-should-be-avoided-when-ordering-gblocks-gene-fragments-
#low or high GC content (less than 25% and greater than 75%),
#10 or more As and Ts
#6 or more Gs and Cs
