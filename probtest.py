from tree import *
from model import *

def calculate_probability(tree, model):
	return 0

test_seq = [
	'AAA',
	'AGA',
	'AAG',
	'AGG',
	'AGA',
	'CTC',
	'CTA'
]
test_model = Model(test_seq, EvolutionParameters())
test_tree = Tree(['A', 'B', 'C', 'D', 'E', 'F'])

print "==rand=="
test_tree.randomize()
test_tree.print_tree()

leaves = test_tree.get_leaf_nodes()
print "leaves: %s" % [str(l) for l in leaves]

test_leaf = leaves[0]

possible = ['A', 'C', 'T', 'G']
probabilities = []
for node in test_leaf.get_path_to_parent():
	temp_prob = 0
	for n1 in possible:
		for n2 in possible:
			prob = test_model.get_transition_probability(n1, n2)
			print "possibility of %s to %s mutation: %s" % (n1, n2, prob)

	probabilities.append(temp_prob)

print probabilities