from qiskit import IBMQ, BasicAer
from qiskit import QuantumCircuit, ClassicalRegister, QuantumRegister
import random
from Dealer import Dealer
from Player import Player
import time


def mark_qubit(state, active):
    return '*' + state[active]


def score(win_string):
    if win_string.count('1') == 5:
        method = "Straight 1s!"
        points = 20
    elif win_string.count('0') == 5:
        method = "Straight 0s!"
        points = 15
    elif win_string[::-1] == win_string:
        method = "Palindrome string!"
        points = 10
    else:
        method = "count of 1s"
        points = win_string.count('1')
    return method, points


def main():
    # start while loop conditioned on player still has money (initialize the stuff)
    q = QuantumRegister(5, 'q')
    c = ClassicalRegister(5, 'c')
    circ = QuantumCircuit(5, 5)
    backend = BasicAer.get_backend('qasm_simulator')

    game = Dealer(circ)
    player = Player()

    state_position = []
    state_string = ["0", "0", "0", "0", "0"]
    random.seed(42)
    state_position.append(random.randint(0, 4))
    state_position.append(random.randint(0, 4))

    state_string[state_position[0]] = "1"
    state_string[state_position[1]] = "1"
    circ.x(q[state_position[0]])
    if state_position[0] != state_position[1]:
        circ.x(q[state_position[1]])

    print("Your starting state is:")
    print(state_string)

    while not game.finished():
        state_string[game.current_qubit] = mark_qubit(state_string, game.current_qubit)

        print("--" * 30)
        print("Total Points: %d" % player.points)
        print("Round: %d/5" % (game.current_qubit + 1))
        print("Cash: %d" % player.wallet)
        print("Currently status of qubits:")
        print(state_string)

        choice = input("'0': Hit($5)  '1': Stand($10)?")
        while choice not in ["0", "1"]:
            choice = input("Please input '0'(Hit) or '1'(Stand)")
        if player.wallet < 10:
            print("insufficient funds... proceeding with draw (this is on the house!)")
            choice = "0"

        new_gate = game.action(int(choice), player)
        state_string[game.current_qubit - 1] = new_gate + state_string[game.current_qubit - 1][1]
        if new_gate == "C":
            state_string[game.current_qubit - 1] = "N" + state_string[game.current_qubit - 1]
            new_gate = "CNOT"
        print("You drew %s!" % new_gate)

    # outside of loop; run the finished circuit
    print("--" * 30)
    print("Your final state is:")
    time.sleep(1)
    print(state_string)
    print("Time for measurement!")
    time.sleep(1)
    final_string = game.evaluate()
    method, points = score(final_string)
    player.win(points)
    print("The result:")
    print(final_string[::-1])
    print("You won %d points by means of %s" % (points, method))


if __name__ == '__main__':
    main()
