from Bio.Seq import Seq


f = open("/Users/urwahnawaz/Desktop/rosalind_problems/rosalind_revc.txt", 'r')  # reads the file 
seq = f.readline().rstrip()  #reads individual lines 

seq = Seq(seq)

print seq.reverse_complement()
