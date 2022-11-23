"""List implementation of a set."""

from typing import (
    Generic, Iterable, TypeVar
)

T = TypeVar('T')


class ListSet(Generic[T]):
    """A set of elements of type T."""

    data: list[T]

    def __init__(self, init: Iterable[T]) -> None:
        """Initialise set with init."""
        self.data = list(init)

    def __contains__(self, x: T) -> bool:
        """Test if x is in set."""
        bool=[]
        for i in x:
            if i in self.data:
                bool.append(True)
            else:
                bool.append(False)
        return bool

    def __bool__(self) -> bool:
        """
        Return truth value of the set.

        A set is True if it is non-empty and False
        otherwise
        """
        if self.data==None:
            return False
        elif self.data==[]:
            return False
        return True
    
    def add(self, x: T) -> None:
       """Add x to the set."""
       self.data.append(x)
       return self.data
    
    def remove(self,x:T)->None:
        """Remove x from the set."""
        if x not in self.data:
            return self.data
        while x in self.data:
            self.data.remove(x)
        return self.data



testname=ListSet([1,3,4,5,656,2,2,2,2,2])
print(testname.__bool__())
print(testname.__contains__([3,1,1]))
print(testname.add(1))
print(testname.remove(2))
