f = open("/Users/urwahnawaz/Desktop/rosalind_problems/rosalind_dna.txt", 'r')

seq = f.readline().rstrip()  #reads individual lines 
f.close()


seq = seq.replace('T', 'U'),  # replaces all the R with U
print seq
