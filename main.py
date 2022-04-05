from core.MDDReducer import MDDReducer
from dto.Variable import Variable
from dto.Formula import Formula
from en.OutcomeType import OutcomeType


a1 = Variable(3, 0)
a1.set_dc(0, 4, "Domain")
a2 = Variable(2, 0)
a2.set_dc(0, 2, "Domain")
a3 = Variable(5, 0)
a3.set_dc(0, 3, "Domain")

example_formula: Formula = Formula([a1, a2, a3], OutcomeType.SMALLER_OR_EQUALS, 15)

r = MDDReducer()

MDD = r.MDDCreate(example_formula)

print("\n\n---\n\n")
for b_set in MDD:
	compound: str = "[ "
	for boundary in b_set:
		compound = compound + boundary.__str__()
	compound = compound + " ]"
	print(compound)
