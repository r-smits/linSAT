from dto.Boundary import Boundary


class Variable:
	a: float
	var: int
	bc: Boundary = None
	dc: Boundary = None
	
	def __init__(self, a: float, var: int):
		self.a = a
		self.var = var
	
	def set_bc(self, lb: int, hb: int, name: str):
		self.bc = Boundary(lb, hb, name)
		
	def set_bc(self, bc: Boundary):
		self.bc = bc
		
	def set_dc(self, lb: int, hb: int, name: str):
		self.dc = Boundary(lb, hb, name)
	
	def get_bc(self) -> Boundary:
		return self.bc
	
	def get_dc(self) -> Boundary:
		return self.dc
