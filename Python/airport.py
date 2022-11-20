
from priority_queue import AdaptableHeapPriorityQueue
from airport_base import AirportBase


class Airport(AirportBase):

    """
        Implement all the necessary methods of the Airport here
    """

    class Shuttle(AirportBase.ShuttleBase):
        """
            Implement all the necessary methods of the Shuttle here
        """
    class Terminal(AirportBase.TerminalBase):
        """
            Implement all the necessary methods of the Terminal here
        """


if __name__ == "__main__":

    """
        !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        REMOVE THE MAIN FUNCTION BEFORE SUBMITTING TO THE AUTOGRADER 
        !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

        The following main function is provided for simple debugging only
    """

    g = Airport(capacity=3)
    terminalA = g.insert_terminal(g.Terminal("A", 1))
    terminalB = g.insert_terminal(g.Terminal("B", 3))
    terminalC = g.insert_terminal(g.Terminal("C", 4))
    terminalD = g.insert_terminal(g.Terminal("D", 2))

    shuttle1 = g.insert_shuttle(terminalA, terminalB, 2)
    shuttle2 = g.insert_shuttle(terminalA, terminalC, 5)
    shuttle3 = g.insert_shuttle(terminalA, terminalD, 18)
    shuttle4 = g.insert_shuttle(terminalB, terminalD, 8)
    shuttle5 = g.insert_shuttle(terminalC, terminalD, 15)

    # Opposite
    assert g.opposite(shuttle1, terminalA).id == 'B'

    # Outgoing Shuttles
    assert [s.time for s in g.outgoing_shuttles(terminalA)] == [2, 5, 18]

    # Remove Terminal
    g.remove_terminal(terminalC)
    assert [s.time for s in g.outgoing_shuttles(terminalA)] == [2, 18]

    # Shortest path
    shortest_path, distance = g.find_shortest_path(terminalA, terminalD)
    assert [t.id for t in shortest_path] == ['A', 'D']
    assert distance == 19

    # Fastest path
    fastest_path, distance = g.find_fastest_path(terminalA, terminalD)
    assert [t.id for t in fastest_path] == ['A', 'B', 'D']
    assert distance == 14