# -*- coding: utf-8 -*-
"""
Created on Wed Jan 13 20:42:38 2021

@author: zhang
"""

from pgmpy.models import BayesianModel
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination


bayesNet = BayesianModel()
bayesNet.add_node("S1")
bayesNet.add_node("S2")
bayesNet.add_node("S2")
bayesNet.add_node("S")

bayesNet.add_edge("S1", "S")
bayesNet.add_edge("S2", "S")
bayesNet.add_edge("S3", "S")


cpd_household = TabularCPD('S1', 3, values=[[.13], [.32], [.55]])
cpd_hdbcarp = TabularCPD('S2', 3, values=[[.25], [.28], [.46]])
cpd_publicarp = TabularCPD('S3', 3, values=[[.15], [.38], [.47]])


cpd_society = TabularCPD('S', 3,
                   values=[[1,0.99,0.95,0.8,0.54,0.56,0.7,0.6,0.52,0.7,0.45,0.1,0.1,0.1,0.12,0.19,0.12,0.18,0.4,0.22,0.12,0.1,0.02,0.02,0.03,0.01,0], 
                          [0,0.01,0.05,0.2,0.33,0.42,0.25,0.38,0.46,0.15,0.3,0.3,0.7,0.87,0.24,0.38,0.56,0.38,0.4,0.5,0.53,0.48,0.15,0.03,0.2,0.14,0.02],
                          [0,0,0,0,0.13,0.02,0.05,0.02,0.02,0.15,0.25,0.6,0.2,0.03,0.64,0.43,0.32,0.44,0.2,0.28,0.35,0.42,0.83,0.95,0.77,0.85,0.98]],
                   evidence=['S1', 'S2', 'S3'], 
                   evidence_card=[3, 3, 3]
                  )

bayesNet.add_cpds(cpd_household, cpd_hdbcarp,cpd_publicarp, cpd_society)

#bayesNet.check_model()
#print("Model is correct.")m



solver = VariableElimination(bayesNet)
#no evidence for S1
#result = solver.query(variables=['S','S1'],evidence={'S2':1,'S3':1}, joint=False)
#probability of R in 1 state
#print("R", result['R'].values[1])

result = solver.query(variables=['S'],evidence={'S1':1,'S2':1,'S3':1}, joint=False)#no evidence for S1
#print(result['S'])
print(result['S'].values[:])