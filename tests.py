
def nand(a: bool, b: bool) -> bool:
    """
    >>> nand(False, False)
    True
    >>> nand(True, False)
    True
    >>> nand(False, True)
    True
    >>> nand(True, True)
    False
    """
    return not (a and b)


def not_(a: bool) -> bool:
    """
    >>> not_(False)
    True
    >>> not_(True)
    False
    """
    return nand(a, a)


def and_(a: bool, b: bool) -> bool:
    """
    >>> and_(False, False)
    False
    >>> and_(True, False)
    False
    >>> and_(False, True)
    False
    >>> and_(True, True)
    True
    """
    return not_(nand(a, b))


def or_(a: bool, b: bool) -> bool:
    """
    >>> or_(False, False)
    False
    >>> or_(True, False)
    True
    >>> or_(False, True)
    True
    >>> or_(True, True)
    True
    """
    return nand(not_(a), not_(b))


def xor(a: bool, b: bool) -> bool:
    """
    >>> xor(False, False)
    False
    >>> xor(True, False)
    True
    >>> xor(False, True)
    True
    >>> xor(True, True)
    False
    """
    return and_(or_(a, b), nand(a, b))
