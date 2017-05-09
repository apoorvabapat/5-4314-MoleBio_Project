import random
import math

def generate_observations(length, probability=0.5):
	sequence = ""
	
	for i in range(0, length): 
		prob = random.random()
		if prob >= probability:
			sequence += "H"
		else:
			sequence += "T"

	return sequence

class Model():
	def __init__(self, observed, initial_prob=0):
		self.observed = observed
		self.probability = initial_prob

	def calculate_likelihood(self):
		n = len(self.observed)
		k = self.observed.count("H")
		p = self.probability

		coeff = (math.factorial(n) / (math.factorial(k) * math.factorial(n - k)))
		return coeff * (p ** k) * ((1-p) ** (n-k))

def run_mcmc():
	# test_obs = "HHTTHTHHTTT"
	test_obs = generate_observations(100)
	print "observations: ", test_obs
	model = Model(test_obs, 0.5)

	iterations = 10000
	current_guess = 0.7
	for i in range(0, iterations):
		model.probability = current_guess
		prev_likelihood = model.calculate_likelihood()

		new_guess = max(min(random.random() + random.uniform(-.5, .5), 1.0), 0.0)
		model.probability = new_guess
		new_likelihood = model.calculate_likelihood()

		# print "comparing (%s, %s) to (%s, %s)" % (current_guess, prev_likelihood, new_guess, new_likelihood)

		ratio = new_likelihood / prev_likelihood
		if(ratio > 1):
			# print "found better guess: ", new_guess
			current_guess = new_guess


	print "i think that the most likely probability is: ", current_guess
	return current_guess

mcmc_things = [run_mcmc() for i in range(0,10)]
av = reduce(lambda x,y: x + (y/2), mcmc_things)
print "average guess: ", av