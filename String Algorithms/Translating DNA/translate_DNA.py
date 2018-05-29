#translate the DNA sequences to proteins 

from Bio.Seq import Seq

f = open("/Users/urwahnawaz/Desktop/rosalind_problems/rosalind_prot.txt", 'r')  # reads the file 
seq = f.readline().rstrip()
f.close()

seq= Seq(seq)
print seq.translate()
