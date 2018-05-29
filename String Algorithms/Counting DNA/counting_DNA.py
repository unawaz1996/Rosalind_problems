
f = open("/Users/urwahnawaz/Desktop/rosalind_problems/rosalind_dna.txt", 'r')  # reads the file 
raw_seq = f.readline().rstrip()  #reads individual lines 
f.close()

print raw_seq.count("A"), #counts the number of A 
print raw_seq.count("C"),  # counts the number of C 
print raw_seq.count("G"), # counts the number of G
print raw_seq.count("T")  # counts the number of T
