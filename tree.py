import random

class Tree():
	def __init__(self, values=[], from_leaves=False, randomize=False):
		if from_leaves:
			self.root = self.build_from_leaves(values, randomize).root
		else:
			self.root = self.build_tree(values)
		self.values = values

	def build_from_leaves(self, leaf_values, randomize, internal_value='*'):
		n_internal = [i for i in range(0, len(leaf_values) - 1)]
		labels = [i for i in range(0, len(leaf_values))]


		t = Tree()
		t.root = self.build_tree(n_internal, randomize)
		leaves = t.get_leaf_nodes()

		i = 0
		l = 0
		while i < len(leaves):
			new_node_1 = TreeNode(leaf_values[l])
			new_node_1.name = labels[l]
			new_node_1.parent = leaves[i]
			leaves[i].first_child = new_node_1

			if len(leaf_values) - l != 1: # edge case - uneven number of input leaves
				new_node_2 = TreeNode(leaf_values[l+1])
				new_node_2.name = labels[l+1]
				new_node_2.parent = leaves[i]
				leaves[i].second_child = new_node_2

			i += 1
			l += 2

		return t

	def get_edges(self):
		edges = []
		nodes = self.get_nodes()

		for node in nodes:
			if node.parent != None:
				if node.parent.value != "ROOT":
					edges.append(str(node.value) + str(node.parent.value))
			else: # special case, only root node
				edges.append(str(node.first_child.value) + str(node.second_child.value))
				

		return edges

	def randomize(self):
		self.root = self.build_tree(self.values, randomize=True)

	def build_tree(self, values, randomize=False):
		root = TreeNode("ROOT")
		for value in values:
			root.add_child(TreeNode(value), randomize)
		return root

	def get_nodes(self):
		return self.root.get_child_nodes()

	def get_leaf_nodes(self):
		leaves = []
		for node in self.get_nodes():
			if node.first_child == None and node.second_child == None:
				leaves.append(node)

		return leaves

	def print_internal_nodes(self):
		all_nodes = self.root.get_child_nodes()
		internal_nodes = []
		for node in all_nodes:
			if node.parent != None and node.first_child != None:
				internal_nodes.append(node)
		print internal_nodes

	def print_tree(self):
		print "(%s, %s)" % (self.root.first_child.print_value(), self.root.second_child.print_value())

	def get_newick(self):
		return "(%s, %s)" % (self.root.first_child.print_value(newick=True), self.root.second_child.print_value(newick=True))

class TreeNode():
	def __init__(self, value, parent=None, depth=0):
		self.parent = parent
		self.value = value
		self.depth = depth
		self.first_child = None
		self.second_child = None
		self.name = None

	def get_path_to_parent(self):
		next_node = self

		path = []
		while(next_node.parent != None):
			path.append(next_node.parent)
			next_node = next_node.parent

		return path

	def is_leaf(self):
		return self.first_child == None and self.second_child == None

	def add_child(self, child, randomize=False):
		child.parent = self
		
		if randomize and self.parent != None:
			if self.first_child != None and self.second_child != None:
				if random.random() >= 0.5:
					self.first_child.add_child(child, randomize)
				else:
					self.second_child.add_child(child, randomize)
			else:
				if self.first_child == None:
					self.first_child = child
				else:
					self.second_child = child
		else:

			if self.first_child == None:
				self.first_child = child
			elif self.second_child == None: 
				self.second_child = child
			else:
				self.first_child.add_child(child, randomize)

	def get_child_nodes(self):
		nodes = [self]
		if self.first_child != None:
			nodes += self.first_child.get_child_nodes()
		if self.second_child != None:
			nodes += self.second_child.get_child_nodes()
		return nodes

	def print_value(self, newick=False):
		if self.first_child != None and self.second_child != None:
			return "(" + self.first_child.print_value(newick) + ", " + self.second_child.print_value(newick) + ")"
		elif self.first_child != None and self.second_child == None:
			return "" + self.first_child.print_value(newick) + ""
		elif self.second_child != None:
			return "" + self.second_child.print_value(newick) + ""
		else:
			if newick:
				return str(self.name)
			else:
				return str(self.value)
			
		
	def __str__(self):
		return self.value

if __name__ == '__main__':
	test_tree = Tree(['A', 'B', 'C', 'D', 'E'], from_leaves=True)
	test_tree.print_tree()
	print test_tree.get_edges()