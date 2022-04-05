# Python implementation of the following paper:
# https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.649.5035&rep=rep1&type=pdf
# Demonstrates the reduction of linear algebraic functions to DAGs.



from typing import List
from dto.Formula import Formula
from dto.Variable import Variable
from dto.Boundary import Boundary
import re


inf = 2 ** 31-1


class MDDReducer:
	
	b_sets: List[List[Boundary]] = []

	#	Calculates the boundaries for a given formula		
	#
	def MDDCreate(self, formula: Formula) -> List[List[Boundary]]:
		for i in range(0, formula.n()):
			self.b_sets.append([])
		self.b_sets.append([Boundary(0, inf, 'T'), Boundary(-inf, -1, 'F')])
		self._MDDConstruction(0, formula)
		return self.b_sets
	
	# Constructs a MDD, which is a DAG, e.g. Directional Acyclical Graph.
	# MDD stands for: 
	def _MDDConstruction(self, i: int, formula: Formula) -> Boundary:
		boundary: Boundary = self._search(i, formula.outcome)
		
		if boundary != []:
			return boundary
		else:
			parents: List[Boundary] = []
			for j in range(formula.vars[i].get_dc().lb, formula.vars[i].get_dc().hb+1):
				formula.outcome = formula.outcome - (j * formula.vars[i].a)
				boundary: Boundary = self._MDDConstruction(i + 1, formula)
				formula.outcome = formula.outcome + (j * formula.vars[i].a)
				parents.append(boundary)
			
			new_boundary = self._minmax(parents, formula.vars[i])
			formula.vars[i].set_bc(new_boundary)
			self._insert(i, new_boundary)
			return new_boundary
		
	def _search(self, i: int, outcome: int) -> Boundary:
		for boundary in self.b_sets[i]:
			if boundary.lb <= outcome and boundary.hb >= outcome:
				return boundary
		return []
	
	def _insert(self, i: int, boundary: Boundary):
		if len(self.b_sets[i]) == 0:
			self.b_sets[i] = [boundary]
			return
		
		for j in range(0, len(self.b_sets[i])):
			if boundary.lb >= self.b_sets[i][j].hb:
				self.b_sets[i].insert(j+1, boundary)
				return
			if boundary.hb <= self.b_sets[i][j].lb:
				self.b_sets[i].insert(j, boundary)
				return
		return
	
	def _minmax(self, boundaries: List[Boundary], domain: Variable) -> Boundary:
		min: List[int] = []
		max: List[int] = []
		
		for i in range(0, len(boundaries)):
			boundary: Boundary = boundaries[i]	
			ra = (domain.get_dc().lb + i) * domain.a
			min.append(-inf if boundary.lb == -inf else boundary.lb + ra)
			max.append(inf if boundary.hb == inf else boundary.hb + ra)
			
		min.sort(reverse=True)
		max.sort()
		return Boundary(min[0], max[0], f"{min[0]} - {max[0]}")
		

