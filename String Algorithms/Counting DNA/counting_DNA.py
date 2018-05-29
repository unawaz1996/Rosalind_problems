
f = open("/Users/urwahnawaz/Desktop/rosalind_problems/rosalind_dna.txt", 'r')  # reads the file 
seq = f.readline().rstrip()  #reads individual lines 
f.close()

print seq.count("A"), #counts the number of A 
print seq.count("C"),  # counts the number of C 
print seq.count("G"), # counts the number of G
print seq.count("T")  # counts the number of T
