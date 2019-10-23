# Quantum-Casino
God does not play dice with the universe... but we do

A collection of games (text-based or not) inspired by quantum mechanics and utilizing the Qiskit library. More will be added over time

# Quantum Hold 'em

A quantum inspired version of Texas Hold 'em. In this game you're given 5 qubits initialized in a state containing no more than 2 1s. Then for each qubit you can either "Hit" or "Stand". A "Hit" will randomly select a gate from [I,X,H,Z,CNOT] and apply it to the current qubit. In the case of CNOT it will be tied between the current qubit and the previous qubit. "Stand" will take no action (applying an I gate with 100% chance). Finally after all 5 qubits have been acted upon, the system is measured and your resulting string is scored!

Scoring is as such:
  20 -- all 1s
  15 -- all 0s
  10 -- palindrome string
  or a point for each 1 in the result.
  
Still to come:
  Several more 'draws'; try to get the best points/$ ratio possible!
