from p4 import *
import dendropy

# tree = dendropy.Tree.get(path="test.fasta", schema="fasta")
# print tree.as_string(schema="newick")

read ('benchmarking_data/data4.phy')

d = Data()
t = func.randomTree(taxNames=d.taxNames)
t.data = d

#jukes-cantor
t.newComp(free=0, spec='equal')
t.newRMatrix(free=0, spec='ones')
t.setNGammaCat(nGammaCat=1)
# t.newGdasrv(free=1, val=0.5)
t.setPInvar(free=0, val=0)

m = Mcmc(t, nChains=1, runNum=0, sampleInterval=500, checkPointInterval=10000)
m.autoTune()

# m.prob.polytomy = 1.0       # Default is zero
# m.prob.brLen = 0.001        # Default is zero
# m.tunings.chainTemp = 0.12  # Default is 0.15, this week

m.run(10000)