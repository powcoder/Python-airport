
class SecurityBase:
    """
    A Security class contains a collection of areas that need to be checked by a security team.
    """
    def __init__(self):
        """
        Creates a new SecurityBase instance.
        """

    class AreaBase:
        """
        Represents an area to be checked in the security routine.
        """
        def __init__(self, id: str):
            """
            Creates a new AreaBase instance with the given ID
            :param id: area ID (str)
            """
            self.id = id

    def insert_area(self, area):
        """
        Adds the given area to the SecurityBase, and returns the added area.

        :param area: area to add
        :return: area that was added
        """
        raise NotImplementedError('must be implemented')

    def add_order(self, area_1, area_2):
        """
        Adds the order between two areas, where area_1 should be checked before area_2.

        :param area_1: area that should be checked before
        :param area_2: area that should be checked after
        """
        raise NotImplementedError('must be implemented')

    def calculate_total_order(self):
        """
        Calculate and returns the order in which the areas must be checked by the
        security team.

        :return: the list of AreaBase instances
                 or
                 None if it is not possible to define the order
        """
        raise NotImplementedError('must be implemented')
