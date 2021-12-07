import matplotlib.pyplot as plt
from math import log

"""
Graph.py
Creates a .png  matplotlib graph of the called in array from QauntumCircuit.py class method "graph(self)"
"""

class Graph:
    def __init__(self, qubits):
        # array of values of the qubits to be placed on the x axis of the bar graph.
        self._qubitValues = []
        # array of values that have converted the 2D array that was called into the constructor into a 1D array to be plotted on the bar graph as valeus.
        self._percents = []
        # stores the called paramaters in the constructor for further use.
        self._qubits = []
        # stores the size of the qubits array being called in for other functions usage.
        self._size = len(qubits)
        self._qubits = qubits

        self.getQubitValues()
        self.getPercents()

    def getQubitValues(self):
        """
        Get Qubit Values to Turn Into String of Values for x axis.
        Params:
            None
        Returns:
            None
        """
        if (self._size % 2 != 0 and self._size != 1):
            print("QCpy: A critical error has occured and the occuring size of final qubit is: " + str(self._size))
            exit(1)
        val = 1
        for i in range(self._size):
            if self._size < 3:
                val = 0
            placeBin = str(bin(i))
            placeBin = placeBin[2:]
            placeBin = (round((log(self._size)) + val - len(placeBin)) * '0') + placeBin
            self._qubitValues.append(placeBin)      

    def getPercents(self):
        """
        Get percents in from the called in array in the constructor and compares all the valeus that they are equal to one.
        Params:
            None
        Returns:
            None
        """
        total = 0
        for i in range(self._size):
            self._percents.append(100 * self._qubits[i][0])
            total += self._qubits[i][0]
        if 1 < total:
            print("QCpy: A critical error has occured and the calculation is above 100%")
            exit(1)
        
    def makeGraph(self):
        """
        Makes bar graph and creates an image from above class methods.
        Params:
            None
        Returns:
            None
        """
        plt.figure(figsize=(self._size + 3,5)) 
        ax = plt.axes()
        ax.bar(self._qubitValues, self._percents, align='center', color='#34b4fc')
        ax.set_ylim(0, 100)
        ax.grid(True)
        ax.xaxis.grid()
        plt.xlabel('Computational basis states')
        plt.ylabel('Probability (%)')
        plt.title('Probabilities')
        plt.savefig('probability.png')


    