import math
import tree
import random

class JukesCantor():
	def __init__(self, mu=0.5):
		self.mu = mu

	def p_same(self, t):
		return 0.25 + 0.75*math.exp(-self.mu * t)

	def p_change(self, t):
		return 0.25 - 0.25*math.exp(-self.mu * t)

	def find_likelihood(self, tree, seq):
		p = 0
		t = 1.0
		for edge in tree.get_edges():
			if edge[0] == edge[1]:
				p += math.log(model.p_same(t))
			else:
				p += math.log(model.p_change(t))

		return p



def assign_internal_nodes(in_tree):
	edges = in_tree.get_edges()

	nucleotides = ['A','C','T','G']
	attempt_map = {}
	for edge in edges:
		e1 = edge[0]
		e2 = edge[1]

		if e1 not in nucleotides and e1 not in attempt_map:
			attempt_map[e1] = nucleotides[random.randrange(0,4)]

		if e2 not in nucleotides and e2 not in attempt_map:
			attempt_map[e2] = nucleotides[random.randrange(0,4)]

	return attempt_map

def get_tree_likelihood(in_tree, model, attempt_map):
	edges = in_tree.get_edges()

	p = 0
	t = 1.0
	for edge in edges:
		edge_1 = edge[0]
		edge_2 = edge[1]

		if edge_1 in attempt_map:
			edge_1 = attempt_map[edge_1]
		if edge_2 in attempt_map:
			edge_2 = attempt_map[edge_2]

		if edge_1 == edge_2:
			p += math.log(model.p_same(t))
		else:
			p += math.log(model.p_change(t))

	return p

def random_tree_likelihood(seq, model):
	t = tree.Tree(seq, from_leaves=True, randomize=True)
	edges = t.get_edges()

	# randomize internal nodes
	attempt_map = assign_internal_nodes(t)

	# apply model to each nucleotide transition
	p = get_tree_likelihood(t, model, attempt_map)

	return (p, t)

if __name__ == "__main__":
	test_seq = [
		'TT',
		'TT',
		'GC',
		'CA',
		'TG',
		'GT',
		'GG',
		'AA',
		'AT',
		'TA',
		'TC'
	]


	model = JukesCantor()

	site_one = [e[1] for e in test_seq]
	init_t = tree.Tree(site_one, from_leaves=True)
	init_internals = assign_internal_nodes(init_t)
	
	t = init_t
	p = get_tree_likelihood(t, model, init_internals)
	for i in range(0, 100):
		p_0, t_0 = random_tree_likelihood(site_one, model)

		q = p_0 / p

		if q > 1:
			t = t_0
			p = p_0

	print "most likely tree: ", t.print_tree()
	print "with likelihood: ", p


	# edges = tree.get_edges()
	# print "edges: ", edges

	# nucleotides = ['A','C','T','G']

	# attempt_map = {}
	# for edge in edges:
	# 	e1 = edge[0]
	# 	e2 = edge[1]

	# 	if e1 not in nucleotides and e1 not in attempt_map:
	# 		attempt_map[e1] = nucleotides[random.randrange(0,4)]

	# 	if e2 not in nucleotides and e2 not in attempt_map:
	# 		attempt_map[e2] = nucleotides[random.randrange(0,4)]
	
	# p = 0
	# t = 1.0
	# for edge in edges:
	# 	edge_1 = edge[0]
	# 	edge_2 = edge[1]

	# 	if edge_1 in attempt_map:
	# 		edge_1 = attempt_map[edge_1]
	# 	if edge_2 in attempt_map:
	# 		edge_2 = attempt_map[edge_2]

	# 	if edge_1 == edge_2:
	# 		p += math.log(model.p_same(t))
	# 	else:
	# 		p += math.log(model.p_change(t))

	# print "Likelihood: ", p