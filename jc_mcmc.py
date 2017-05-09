import math
import tree
# from ete3 import Tree

class JukesCantor():
	def __init__(self, mu=0.5):
		return 0

	def p_same(self, t):
		return 0.25 + 0.75*math.exp(-self.mu * t)

	def p_change(self):
		return 0.25 - 0.25*math.exp(-self.mu * t)



test_seq = [
	'T',
	'T',
	'G',
	'C'
]


tree = tree.Tree(test_seq, from_leaves=True)