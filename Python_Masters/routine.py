from routine_base import SecurityBase


class Security(SecurityBase):
    """
        Implement all the necessary methods here
    """


if __name__ == '__main__':

    """
        !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        REMOVE THE MAIN FUNCTION BEFORE SUBMITTING TO THE AUTOGRADER 
        !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

        The following main function is provided for simple debugging only
    """

    g = Security()
    terminalZ = g.insert_area(g.AreaBase("Z"))
    terminalA = g.insert_area(g.AreaBase("A"))
    terminalB = g.insert_area(g.AreaBase("B"))
    terminalC = g.insert_area(g.AreaBase("C"))

    g.add_order(terminalZ, terminalA)
    g.add_order(terminalA, terminalB)
    g.add_order(terminalB, terminalC)
    g.add_order(terminalA, terminalC)
    t = g.calculate_total_order()
    assert [el.id for el in t] == ['Z', 'A', 'B', 'C']