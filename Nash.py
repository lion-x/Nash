import nashpy as nash
import numpy as np

#Creating a game
A = np.array([[0, -1, 1], [1, 0, -1], [-1, 1, 0]])
rps = nash.Game(A)
rps
#Calculating the utility of a pair of strategies
sigma_r = [0, 0, 1]
sigma_c = [0, 1, 0]
print(rps[sigma_r, sigma_c])
sigma_c = [1/2, 1/2, 0]
print(rps[sigma_r, sigma_c])
sigma_r = [0, 1/2, 1/2]

#Computing Nash equilibria
#Solve with support enumeration
eqs = rps.support_enumeration()
print(list(eqs))
#Solve with vertex enumeration
eqs = rps.vertex_enumeration()
print(list(eqs))
#Solve with Lemke Howson enumeration
eqs = rps.lemke_howson_enumeration()
print(list(eqs))
#Learning in games


iterations = 100
np.random.seed(0)
play_counts = rps.fictitious_play(iterations=iterations)
for row_play_count, column_play_count in play_counts:
    print(row_play_count, column_play_count)