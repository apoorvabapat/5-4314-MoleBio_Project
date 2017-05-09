import dendropy
from dendropy.calculate import treecompare
taxa = dendropy.TaxonNamespace()



# bootstrapped_trees = dendropy.TreeList.get(file=open("./bootstrapping/data6/tree_data6_boot.txt"), schema="newick", taxon_namespace=taxa)
test_tree = dendropy.Tree.get(file=open("./benchmarking_data/data_4/last_tree_jc69.txt"), schema="newick", taxon_namespace=taxa)
reference_tree = dendropy.Tree.get(file=open("./benchmarking_data/data_4/data4.phy_phyml_tree_jc69.txt"), schema="newick", taxon_namespace=taxa)

bootstrapped_trees = [test_tree]

reference_tree_biparts = set(reference_tree.encode_bipartitions())
i = 0
true_positives = []
false_positives = []
for inference_tree in bootstrapped_trees:
    inference_tree_biparts = set(inference_tree.encode_bipartitions())
    tp = inference_tree_biparts.intersection(reference_tree_biparts)
    fp = inference_tree_biparts.difference(reference_tree_biparts)
    fn = reference_tree_biparts.difference(inference_tree_biparts)

    true_positives.append(float(len(tp)))
    false_positives.append(float(len(fp)))

tp_avg = reduce(lambda x, y: x + y, true_positives) / len(true_positives)
fp_avg = reduce(lambda x, y: x + y, false_positives) / len(false_positives)

print "tp avg: ", tp_avg
print "fp avg: ", fp_avg

precision = tp_avg/(tp_avg + fp_avg)
recall = tp_avg/(tp_avg + fp_avg)
accuracy =  (tp_avg)/(tp_avg + fp_avg + fp_avg)
fmeasure = 2*(precision*recall)/(precision+recall)

print "=="
print "precision ", precision
print "recall ", recall
print "accuracy ", accuracy
print "fmeasure ", fmeasure

# for tree in bootstrapped_trees:
#     tree.encode_bipartitions()
#     # print treecompare.false_positives_and_negatives(reference_tree, tree)
#     print treecompare.robinson_foulds_distance(reference_tree, tree)
