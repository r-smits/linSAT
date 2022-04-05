class Boundary:
	
	name: str
	lb: int
	hb: int
	
	def __init__(self, lb, hb, name: str):
		self.lb = lb
		self.hb = hb
		self.name = name
	
	def __str__(self):
		return f"({self.name}, lb: {self.lb}, hb: {self.hb})"
