# synthetic IVT for NGS
We were interested in creating a totally randomic ivt to use in NGS runs as positive control.

We designed a scritp following some general recommendations od IDT for oligo synthesis: https://eu.idtdna.com/pages/support/faqs/what-types-of-sequence-motifs-should-be-avoided-when-ordering-gblocks-gene-fragments-

Briefly, the script avoids low or high GC content (less than 25% and greater than 75%) and 6 or more repeated nucleotides.

## Execution

'''{bash}
python3 controllable_random_fasta.py > set1.fasta
'''

## Blast
No hit was returned with blast using NCBI's nucleotide database ant the methods blastn, blastx, tblastx.

## Folding structure
We ran rna Folding prediction just in case it is desired to have in amplification of our ivt.

we used the RNAfold WebServer http://rna.tbi.univie.ac.at/cgi-bin/RNAWebSuite/RNAfold.cgi,
which runs the equivalent RNAfold commnad

'''{bash}
RNAfold -p -d2 --noLP < Random_Seque.fa > Random_Seque.out
'''

Based on the RNAfold results, the sequences with probable less 2D structures would be 3, 5 and 8.
Above is shown the vienna representation of the centroids of their thermodynamic ensemble prediction.

>Random_Sequence_3
CTCTGGCCTGGTAAATACGTATCGGCTAGCTGCACTATAGCTATCCACACGCAAATATGGAACTAGTACCGAAGATATCACCGATCTTCAAACTACCATCGTCCCCGTCGGGCGACCTCCCTACTATCACCAATAGGAACCCGCCTACCCGCGTTCGTTCCGTAATTGCTATGGGCGCAGCGCGACCGACAGTATGTAATGGTTGACATCATACCGGCTAGTGCTCCGGTCCCATATGCACATATAAATAGTGTGAGATAGCGGCTGGATCGGTTAAGCATGACCAAATAATACCCCCAGCATCTTGAGCTATATTCACGGACACTGAGAAGGACGTATTTCGTCGCTGGGAGAGGGTATCGCGCCTCTCTGCCGCTATGAACGCTAGATTGAGGTTTACCACCAATGCTGGGTGGTCGATGCAGGTGGCTACTGTTCCTGAAAACTTCTCGCTATGAACTACTGGGGGATGTTCTTTACTAGCGGGAAACCATCTGTTT
.........................................(((((((((((((.((((((((((((...((((((.......))))))..))))...((((((.....))))))........((((.....))))((((............)))))))))))).))))((((((((.(((((..(((...(((((..(((.....)))))))))))...))))).))..))))))..............))))).))))...........(((((....)))))....................(((.......)))..............((((.....))))......................................................(((((.......))))).................................................................................... (-77.90)

>Random_Sequence_5
CTAAAACGATCAAAAGCGACACAAGCAGGTGTAGCCTACGCTTAGGGATACCGAGTCGATCTGTCCATCTGCTAAGGATGACGACCCTTTGTAAAACAGTGCAGCTCTTTATGCGCTTCACCTTGCAGTAGTCTGTGGGTTCACTTCTGTCCATTAACCCACACCAATGAAATATTGTACGACATGGGTCAAGAATATAGACCGGAACGTTCATGATTAGCGCATTTTGACCAGTAAAATACGAAATGTTGGCTCCCTATAAATACACTCTGCCTCTATCCGCACCGGTTCATGTTACTCCTGTAACCTAAGCGGAGAGCCAATCTGGCCGAGTTTCACTGTAAGTAACTACACAACGAATTGTCCCCAACGACACACGTGGTTCCGTGCGCAAGTCGTAGTTAGGCGGACTCGTGGCCTTGATGCTTTACGTGGGTCTTTTCTACCAGCACCTGAGGTACGGAATTGGGAGCAAGATAGTCGACGATTAGCGGCTGCGA
...............((.......))....((((((...(((..((....))..(((((.(((((.....(((((..(((.((..((..........((((((........))))))................((((((((..............)))))))).......................((((.........))))))..))..)))..)))))((((((((............))))))))..((((((......................(((..............................))).........................((........)).........((((......))))........................................................(((((.....))))).....................))))))..))))))))))....))))))))).. (-75.90)

>Random_Sequence_8
GGTCGCTCCCTAAGTTGGTGGGCTATGACGAAGACTCAGGATCAACACCAATTTTGCCTGCCCGTAAGAATGATCGCGTATGTACAGTGACGTTCCTTGAAGAATTAATAACGCCTGCAACTACAAGACTGGGTTGCGGCCCGTGACGTGATGTGCCCCCTATTACCAGGTCTGGGTTAATTCTAAGCCTGGCCTTCACTGGCCATAAAGACTAACTCGATGTGGTTCGTACTTCACCAGCGTGTATAGAAACCCGGCCATGCCCTGCAAAGGTCACCGTCATAAGTGCGTAGCCAGTGGCACTTAGGTCGCGGACTCGTTGTCAGACCCTCATGTGGACCATGGGCGTACACTCAGCTTTCTATCGCTATGACGATCTCTTACCCTCCGCAAGCATTGGACCCCGATACCGGAACTTGGTTAATGTGCGGTTCGCGCTGGCGGGGGCTCTACGTCCGTACATGCACTGTTCGGTGGCCTTTAATATCATGAAGCAACAA
...................................................................(((((.((((.........))))))))).................(...(((((...........)))))..)..((((((.(((((((((((....((((.(((.((((((..(((.....(((((......)))))...))).))))))))).))))..........((((((((.................((...)).......................................(((...(((.....))).)))............................((........))...................((((...((((..((((((....))).....))).)))).))))..)))))))).))))))...)))))))).)))..................................... (-83.50)

Probably, the most suitable sequence would be the 8, given it has overall less probable base pairings.

T7 promoter sequence
https://international.neb.com/faqs/2015/01/30/what-is-the-promoter-sequence-of-t7-rna-polymerase

T7 Promoter
5′ TAATACGACTCACTATAG 3′

T7 RNA polymerase starts transcription at the underlined G in the promoter sequence. The polymerase then transcribes using the opposite strand as a template from 5’->3’. The first base in the transcript will be a G.
