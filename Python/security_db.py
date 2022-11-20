
from security_db_base import HashTableBase
import sys


class HashTable(HashTableBase):
    """
        Implement all the necessary methods here
    """


if __name__ == "__main__":
    """
        !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        REMOVE THE MAIN FUNCTION BEFORE SUBMITTING TO THE AUTOGRADER 
        !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

        The following main function is provided for simple debugging only
    """

    ht = HashTable(3, 2)
    # add
    ht.add_passenger("Rob Bekker", "Asb23f")
    ht.add_passenger("Kira Adams", "MKSD23")
    ht.add_passenger("Kira Adams", "MKSD24")
    assert "Asb23f" in ht

    # count
    assert ht.count() == 3

    # del
    del ht["MKSD23"]
    assert "MKSD23" not in ht
    assert "Asb23f" in ht

    # hashcodes
    assert ht.hash_codes("Asb23f") == 1717

    # suspicious
    ht = HashTable(3, 2)
    ht.add_passenger("Rob Bekker", "Asb23f")
    ht.add_passenger("Robert Bekker", "Asb23f")
    # Should raise a warning
    # sys.stderr.write("Suspicious behaviour")
