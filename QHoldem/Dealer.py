from qiskit import Aer, execute
import random


class Dealer:
    """ Handles drawing a new 'card' and applying it to the circuit
        as well
    """
    def __init__(self, circ):
        self.circ = circ
        self.pool = 0
        self.current_qubit = 0

    def action(self, choice, player):
        if choice == 0:  # player "draws"
            player.bet(5)
            self.bet(5)
            roll = random.randint(0, 4) if (self.current_qubit > 0) else random.randint(0, 3)
            if roll == 0:
                outcome = "I"
            elif roll == 1:
                self.circ.x(self.current_qubit)
                outcome = "X"
            elif roll == 2:
                self.circ.h(self.current_qubit)
                outcome = "H"
            elif roll == 3:
                self.circ.z(self.current_qubit)
                outcome = "Z"
            elif roll == 4:
                self.circ.cx(self.current_qubit, self.current_qubit - 1)
                outcome = "C"
            else:
                outcome = "error"
            self.current_qubit += 1
            return outcome

        elif choice == 1:  # player "stands"
            player.bet(10)
            self.bet(10)
            self.current_qubit += 1
            return "I"
        else:
            return 0

    def bet(self, amount):
        self.pool += amount

    def finished(self):
        """useful for game loop"""
        return self.current_qubit > 4

    def evaluate(self):
        """for after the game is finished and it is time to measure and
            process the results
        """
        self.circ.measure(range(5),range(5))
        simulator = Aer.get_backend('qasm_simulator')
        job = execute(self.circ, simulator, shots=1)
        result = job.result()
        counts = result.get_counts(self.circ)
        return max(counts, key=counts.get)

    def reset(self, new_circ):
        self.current_qubit = 0
        self.circ = new_circ
