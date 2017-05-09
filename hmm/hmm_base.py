import math
'''
todo:
- emission probabilities
- transition probabilities


'''

class Node():
    def __init__(self, state, p, nextNode=None):
        self.state = state
        self.p = p
        self.nextNode = nextNode



# n2 = Node('Y', 0.5)
# n1 = Node('X', 0.5, n1)

test_observations = "AA"

# P(X | X_t-1)
transition_probabilities = {
    'X': {
        'X': 0.5,
        'Y': 0.5,
        # 'Z': 0.2
    },
    'Y': {
        'X': 0.4,
        'Y': 0.6,
        # 'Z': 0.4
    },
    # 'Z': {
    #     'X': 0.2,
    #     'Y': 0.2,
    #     'Z': 0.6
    # }
}

# P(Y | X)
# rain = x
# umbrella = a
emission_probabilities = {
    'X': {
        'A': 0.2,
        'B': 0.3,
        'C': 0.3,
        'D': 0.2
    },
    'Y': {
        'A': 0.3,
        'B': 0.2,
        'C': 0.2,
        'D': 0.3
    },
    # 'Z': {
    #     'A': 0.1,
    #     'B': 0.4,
    #     'C': 0.3,
    #     'D': 0.2
    # }
}

def forward_step(observation, prev_state, prev_vals):
    total = 0
    i = 0
    for state in transition_probabilities.keys():
        total += transition_probabilities[state][prev_state] * prev_vals[i]
        i += 1

    return total * emission_probabilities[prev_state][observation]


initial = [
    0.15,
    0.1
] # x, y ,z
a1 = forward_step('C', 'X', initial)
b1 = forward_step('C', 'Y', initial)
v1 = [a1, b1]
print v1

a2 = forward_step('C', 'X', v1)
b2 = forward_step('C', 'Y', v1)
v2 = [a2, b2]
print v2

a3 = forward_step('B', 'X', v2)
b3 = forward_step('B', 'Y', v2)
v3 = [a3, b3]
print v3

a4 = forward_step('A', 'X', v3)
b4 = forward_step('A', 'Y', v3)
v4 = [a4, b4]
print v4

# a = viterbi_step(test_observations[0], 0.5)
# b = viterbi_step(test_observations[1], step1[0])
# c = viterbi_step(test_observations[1], step1[1])



# def get_next_probability(observation, previous):
#     next_prob = 1

#     for state in transition_probabilities.keys():

#         trans_prob = transition_probabilities[state]
#         emiss_prob = emission_probabilities[state][observation]

#         # next_prob *= emiss_prob * trans_prob

#     return next_prob

# p1 = get_next_probability(test_observations[0], 0.5)
# print p1
# p2 = get_next_probability(test_observations[1], p1)
# print p2
