import math

'''
	This holds all of the things that can be permuted by the guess step of the metropolis algorithm
'''
class Model():
	def __init__(self, sequences, evolution_parameters=None):
		self.sequences = sequences
		self.evolution_parameters = evolution_parameters

	def get_transition_probability(self, i, j, t=1):
		P_trans = self.evolution_parameters.transitions
		rates = self.evolution_parameters.rates

		if i == 'A' or i == 'G':
			lambda_j = P_trans['A'] + P_trans['G']
		else: 
			lambda_j = P_trans['T'] + P_trans['C']

		gamma_j = 1 + (rates['kappa'] - 1) * lambda_j

		if i == j:
			return P_trans[i] + P_trans[i] * ( (1/lambda_j) - 1 ) * math.pow(math.e, -rates['alpha'] * t) + ((lambda_j - P_trans[j]) / lambda_j) * math.pow(math.e, -rates['alpha'] * gamma_j * t)
		else:
			if (i == 'A' or i == 'G') and (j == 'C' or j == 'T'): #transition event
				return P_trans[j] + P_trans[j] * ( (1/lambda_j) - 1 ) * math.pow(math.e, -rates['alpha'] * t) + (P_trans[j] / lambda_j) * math.pow(math.e, -rates['alpha'] * gamma_j * t)
			else: #transversion event
				return P_trans[j] * (1 - math.pow(math.e, -rates['alpha'] * t))

	def get_t_probability(self):
		n = len(self.sequences)
		return reduce(lambda x, y: x * (n + 1), range(2, n-1)) / math.pow(self.get_total_topologies(), n - 2)

	def get_total_topologies(self):
		n = len(self.sequences)
		return reduce(lambda x, y: x * (2 * y - 1), range(1, n - 1))

	def get_node_transition_probability(self, t, n1, n2):
		m = 1 # number of sites with nucleotide i in n1 and nucleotide j in n2
			  # literally how

		result = 1
		for i in ['A', 'G', 'C', 'T']:
			for j in ['A', 'G', 'C', 'T']:
				result =  result * (self.get_transition_probability(i, j, t) ** m)

		return result

# using jukes-cantor assumption for now
class EvolutionParameters():
	def __init__(self):
		self.transitions = {
			'A': .25,
			'G': .25,
			'T': .25,
			'C': .25,
		}
		self.rates = {
			'alpha': 1, #transversion
			'kappa': 1 	#transition
		}

if __name__ == '__main__':
	test_sequences = [
		'AAAA',
		'AAGA',
		'ACAC',
		'AGAG',
		'TTAG',
		# 'GGAG'
	]

	evolution_parameters = EvolutionParameters()
	model = Model(test_sequences, evolution_parameters=evolution_parameters)

	print model.get_total_topologies()