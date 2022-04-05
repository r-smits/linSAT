from typing import List
from dto.Variable import Variable
from en.OutcomeType import OutcomeType


class Formula:
	vars: List[Variable]
	type: OutcomeType
	outcome: float
	
	def __init__(self, vars: List[Variable], type: OutcomeType, outcome: float):
		self.vars = vars
		self.type = type
		self.outcome = outcome
	
	def n(self) -> int:
		return len(self.vars)
	
	def __str__():
		return f"-Formula-\nvars: {self.vars}\ntype: {self.type} \noutcome: ={self.outcome}"
