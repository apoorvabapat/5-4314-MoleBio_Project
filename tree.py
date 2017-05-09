import random

class Tree():
	def __init__(self, values=[], from_leaves=False):
		if from_leaves:
			self.root = self.build_from_leaves(values).root
		else:
			self.root = self.build_tree(values)
		self.values = values

	def build_from_leaves(self, leaf_values):
		n_internal = [i for i in range(0, len(leaf_values) - 1)]

		t = Tree()
		t.root = self.build_tree(n_internal)
		leaves = t.get_leaf_nodes()

		i = 0
		l = 0
		while i < len(leaves):
			print l, len(leaf_values)
			leaves[i].first_child = TreeNode(leaf_values[l])

			if len(leaf_values) - l != 1:
				leaves[i].second_child = TreeNode(leaf_values[l+1])

			i += 1
			l += 2

		return t

	def randomize(self):
		self.root = self.build_tree(self.values, randomize=True)

	def build_tree(self, values, randomize=False):
		root = TreeNode("ROOT")
		for value in values:
			print "added %s" % value
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
		# print self.root.first_child, self.root.second_child
		print "root: (%s, %s)" % (self.root.first_child.print_value(), self.root.second_child.print_value())

class TreeNode():
	def __init__(self, value, parent=None, depth=0):
		self.parent = parent
		self.value = value
		self.depth = depth
		self.first_child = None
		self.second_child = None

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

	def print_value(self):
		if self.first_child != None and self.second_child != None:
			return "(" + self.first_child.print_value() + ", " + self.second_child.print_value() + ")"
		elif self.first_child != None and self.second_child == None:
			return "(" + self.first_child.print_value() + ")"
		elif self.second_child != None:
			return "(" + self.second_child.print_value() + ")"
		else:
			return str(self.value)
		
	def __str__(self):
		return self.value

if __name__ == '__main__':
	test_tree = Tree(['A', 'B', 'C', 'D', 'E'], from_leaves=True)
	test_tree.print_tree()
