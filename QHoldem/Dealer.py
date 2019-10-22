from qiskit import IBMQ
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
import random

class Dealer:
    """ Handles drawing a new 'card' and applying it to the circuit
        as well
    """
    def __init__(self, circ, qreg, creg):
        self.circ = circ
        self.qreg = qreg
        self.pool = 0
        self.creg = creg
        #self.spent_qubits = []
        #self.current_qubit = random.randint(0,4)
        #for potentially using random qubit registers depending on how it plays
        self.current_qubit = 0

    def action(self, choice, player):
        if (choice == "0"): #player "draws"
            player.bet(5)
            self.bet(5)
            roll = random.randint(0,4) if (current_qubit > 0) else random.randint(0,3)
            if (roll == 0):
                outcome = "I"
            elif (roll == 1):
                self.circ.x(qreg[current_qubit])
                outcome = "X"
            elif (roll == 2):
                self.circ.h(qreg[current_qubit])
                outcome = "H"
            elif (roll == 3):
                self.circ.z(qreg[current_qubit])
                outcome = "Z"
            elif (roll == 4):
                self.circ.cx(self.qreg[current_qubit],self.qreg[current_qubit-1])
                outcome = "C"
            self.current_qubit += 1
            return outcome
            
        elif (choice == "1"): #player "stands"
            player.bet(10)
            self.bet(10)
            self.current_qubit += 1
            return 1
        else return 0
            
    def bet(self,amount):
        self.pool += amount

    def finished(self):
        """useful for game loop"""
        return self.current_qubit > 4

    def evaluate(self):
        """for after the game is finished and it is time to measure and
            process the results
        """
        pass
