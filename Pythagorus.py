import math
inputs = input().split()
opp = float(inputs[0])
adj = float(inputs[1])



expOpp = opp * opp
expAdj = adj * adj
hyp = math.sqrt(expOpp + expAdj)

print ("{:.6f}".format(hyp))