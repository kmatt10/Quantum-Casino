from qiskit import IBMQ
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
import random
import Dealer
import Player

def main():
    shots = 1
    max_credits = 3

    q = QuantumRegister(5,'q')
    circ = QuantumCircuit(q)
    backend = BasicAer.get_backend('qasm_simulator')
    
    state_position = []
    state_string = ["0","0","0","0","0"]
    random.seed(42)
    start_state.append(random.randint(0,4))
    start_state.append(random.randint(0,4))
    
    state_string[state_position[0]] = "1"
    state_string[state_position[1]] = "1"
    circ.x(q[start_state[0]])
    if (state_position[0] != state_position[1]):
        circ.x(q[state_position[1]])

    print("Your starting state is:")
    print(state_string)
    
if __name__ == '__main__':
    main()
