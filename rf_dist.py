import dendropy
from dendropy.calculate import treecompare

tns = dendropy.TaxonNamespace()
tree1 = dendropy.Tree.get_from_path(
        "./benchmarking_data/data_4/last_tree_jc69.txt",
        "newick",
        taxon_namespace=tns)
tree2 = dendropy.Tree.get_from_path(
        "./benchmarking_data/data_4/data4.phy_phyml_tree_jc69.txt",
        "newick",
        taxon_namespace=tns)
t1 = tree1.encode_bipartitions()
t2 = tree2.encode_bipartitions()
print len(t1)
print len(t2)
missing = treecompare.find_missing_bipartitions(tree1, tree2)
print(len(missing))