# ghz_circuits.py
# Greenberger, Horne, and Zeilinger
# Based on
# https://quantumexperience.ng.bluemix.net/qx/tutorial?sectionId=full-user-guide&page=003-Multiple_Qubits_Gates_and_Entangled_States~2F003-GHZ_States

from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister

class GHZCircuit():
	# Original setup
	def __init__(self):
		self.q = QuantumRegister(3, 'q')
		self.circ = QuantumCircuit(self.q)
		self.circ.x(self.q[0])
		self.circ.h(self.q[1])
		self.circ.h(self.q[2])
		self.circ.cx(self.q[1],self.q[0])
		self.circ.cx(self.q[2],self.q[0])

class GHZState3Q(GHZCircuit):
	def __init__(self):
		super(GHZState3Q, self).__init__()
		self.c = ClassicalRegister(3, 'c')
		self.meas = QuantumCircuit(self.q, self.c)
		self.meas.barrier(self.q)
		self.circ.h(self.q[0])
		self.circ.h(self.q[1])
		self.circ.h(self.q[2])
		self.meas.measure(self.q, self.c)
		self.qc = self.circ + self.meas

class GHZ_YYX(GHZCircuit):
	def __init__(self):
		super(GHZ_YYX, self).__init__()
		self.c = ClassicalRegister(3, 'c')
		self.meas = QuantumCircuit(self.q, self.c)
		self.meas.barrier(self.q)
		self.circ.sdg(self.q[1])
		self.circ.sdg(self.q[2])
		self.circ.h(self.q[0])
		self.circ.h(self.q[1])
		self.circ.h(self.q[2])
		self.meas.measure(self.q, self.c)
		self.qc = self.circ + self.meas

class GHZ_YXY(GHZCircuit):
	def __init__(self):
		super(GHZ_YXY, self).__init__()
		self.c = ClassicalRegister(3, 'c')
		self.meas = QuantumCircuit(self.q, self.c)
		self.meas.barrier(self.q)
		self.circ.sdg(self.q[0])
		self.circ.sdg(self.q[2])
		self.circ.h(self.q[0])
		self.circ.h(self.q[1])
		self.circ.h(self.q[2])
		self.meas.measure(self.q, self.c)
		self.qc = self.circ + self.meas

class GHZ_XYY(GHZCircuit):
	def __init__(self):
		super(GHZ_XYY, self).__init__()
		self.c = ClassicalRegister(3, 'c')
		self.meas = QuantumCircuit(self.q, self.c)
		self.meas.barrier(self.q)
		self.circ.sdg(self.q[0])
		self.circ.sdg(self.q[1])
		self.circ.h(self.q[0])
		self.circ.h(self.q[1])
		self.circ.h(self.q[2])
		self.meas.measure(self.q, self.c)
		self.qc = self.circ + self.meas

class GHZ_XXX(GHZCircuit):
	def __init__(self):
		super(GHZ_XXX, self).__init__()
		self.c = ClassicalRegister(3, 'c')
		self.meas = QuantumCircuit(self.q, self.c)
		self.meas.barrier(self.q)
		self.circ.h(self.q[0])
		self.circ.h(self.q[1])
		self.circ.h(self.q[2])
		self.meas.measure(self.q, self.c)
		self.qc = self.circ + self.meas

class GHZ_XYX(GHZCircuit):
	def __init__(self):
		super(GHZ_XYX, self).__init__()
		self.c = ClassicalRegister(3, 'c')
		self.meas = QuantumCircuit(self.q, self.c)
		self.meas.barrier(self.q)
		self.circ.sdg(self.q[1])
		self.circ.h(self.q[0])
		self.circ.h(self.q[1])
		self.circ.h(self.q[2])
		self.meas.measure(self.q, self.c)
		self.qc = self.circ + self.meas

# End