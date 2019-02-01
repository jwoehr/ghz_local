# ghz.py
# Greenberger, Horne, and Zeilinger
# Based on
# https://quantumexperience.ng.bluemix.net/qx/tutorial?sectionId=full-user-guide&page=003-Multiple_Qubits_Gates_and_Entangled_States~2F003-GHZ_States
# Copyright 2019 Jack Woehr jwoehr@softwoehr.com PO Box 51, Golden, CO 80402-0051
# BSD-3 license -- See LICENSE which you should have received with this code.
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# WITHOUT ANY EXPRESS OR IMPLIED WARRANTIES.

from qiskit.tools.monitor import job_monitor
from pylab import *
from qiskit import execute
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
import numpy as np
import argparse
import sys
import ghz_circuits as ghzc

explanation = """GHZ Local : Local Realism in Greenberger, Horne, and Zeilinger
Copyright 2019 Jack Woehr jwoehr@softwoehr.com PO Box 51, Golden, CO 80402-0051
BSD-3 license -- See LICENSE which you should have received with this code.
THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
WITHOUT ANY EXPRESS OR IMPLIED WARRANTIES.
"""

long_explan = """GHZ Local : Local Realism in Greenberger, Horne, and Zeilinger
Copyright 2019 Jack Woehr jwoehr@softwoehr.com PO Box 51, Golden, CO 80402-0051
BSD-3 license -- See LICENSE which you should have received with this code.
THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
WITHOUT ANY EXPRESS OR IMPLIED WARRANTIES.

Default is to run on genuine IBM Q quantum processor.

Type -h or --help for important options information
"""

parser = argparse.ArgumentParser(description=explanation)
group = parser.add_mutually_exclusive_group()
group.add_argument("-q", "--ibmq", action="store_true",
                   help="Use genuine IBMQ processor (default)")
group.add_argument("-s", "--sim", action="store_true",
                   help="Use IBMQ qasm simulator")
group.add_argument("-a", "--aer", action="store_true",
                   help="User QISKit aer simulator")
parser.add_argument("-u", "--usage", action="store_true",
                    help="Show long usage message and exit 0")
args = parser.parse_args()

if args.usage:
    print(long_explan)
    exit(0)

# exit()

# Choose backend
backend = None

if args.aer:
    # Import Aer
    from qiskit import BasicAer
    # Run the quantum circuit on a statevector simulator backend
    backend = BasicAer.get_backend('statevector_simulator')
else:
    from qiskit import IBMQ
    IBMQ.load_accounts()
    # Choose backend and connect
    if args.sim:
        backend = IBMQ.get_backend('ibmq_qasm_simulator')
    else:
        from qiskit.providers.ibmq import least_busy
        large_enough_devices = IBMQ.backends(filters=lambda x: x.configuration().n_qubits > 4 and
                                             not x.configuration().simulator)
        backend = least_busy(large_enough_devices)
        print("The best backend is " + backend.name())

print("Backend is", end=" ")
print(backend)

if backend == None:
    print("No backend available, quitting.")
    exit(100)

# Prepare job
# ###########

# Number of shots to run the program (experiment); maximum is 8192 shots.
shots = 1024
# Maximum number of credits to spend on executions.
max_credits = 3

# Create circuits
circuits = [ghzc.GHZState3Q(),ghzc.GHZ_YYX(),ghzc.GHZ_YXY(),ghzc.GHZ_XYY(),ghzc.GHZ_XXX(),ghzc.GHZ_XYX()]

def csv(circuit_name, sorted_keys, sorted_counts):
	print(circuit_name)
	for key in sorted_keys:
		print(key, end=';')
	print()
	for count in sorted_counts:                          
		print(count, end=';')
	print()

# Iterate executing
for i in circuits:
	circuit_name = type(i).__name__
	print(circuit_name)
	print(i.qc.draw())
	job_exp = execute(i.qc, backend=backend, shots=shots, max_credits=max_credits)
	job_monitor(job_exp)
	result_exp = job_exp.result()
	counts_exp = result_exp.get_counts(i.qc)
	print(counts_exp)
	sorted_keys = sorted(counts_exp.keys())
	sorted_counts = []
	for i in sorted_keys:
		sorted_counts.append(counts_exp.get(i))
	print(sorted_counts)
	csv(circuit_name, sorted_keys, sorted_counts)

print('Done!')

# End
