import sys

# The entries can look like this
#chr11 610084351 61008463 TMAGAPTVSLPELR -6.449607082775661 -6.594357132911682 2.4761785194277763 -6.903714265142169 3.635571431900774 -6.747785721506391 yes
#chr11 610086701 61008682 TMAGAPTVSLPELR -3.1567500233650208- 1.2344167158007622 -4.658666650454204 -0.09700000286102295 -5.706999897956848 -5.20116662979126 no
# We want to indicate for each peptide if it has predicted coding potential in at least one of its segments

any_coding = {}
peptides = set()

with open(sys.argv[1]) as iF:
    for line in iF:
        cols = line.strip().split()
        seq = cols[3]
        if(seq=="peptide_seq"): continue
        peptides.add(seq)
        pred = cols[10]
        if pred == 'yes': 
            any_coding[seq]=True
            
for p in sorted(peptides):
    if p in any_coding:
        print(p + '\tyes')
    else:
        print(p + '\tno')
