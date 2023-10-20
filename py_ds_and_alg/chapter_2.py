# multidimensional vector class
# demonstrate the use of operator overloading
# implementation of __add__ is customized
'''class Vector:
    """Represent a vector in a multidimensional space."""

    def __init__(self, d):
        """Create d-dimensional vector of zeros."""
        self._coords = [0] * d
    
    def __len__(self):
        """Return the dimension of the vector."""
        return len(self._coords)

    def __getitem__(self, j):
        """Return j-th coordinate of vector."""
        return self._coords[j]
    
    def __setitem__(self, j, val):
        """Set j-th coordinate of vector to given value."""
        self._coords[j] = val
    
    def __add__(self, other):
        """Return the sum of two vectors."""
        if len(self) != len(other):  # relies on __len__ method
            raise ValueError("dimensions must agree")
        result = Vector(len(self))   # start with vecotr of zeros
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result§
    
    def __eq__(self, other):
        """Return True if vector has same coordinates as other."""
        return self._coords == other._coords
    
    def __ne__(self, other):
        return not self == other   # rely on existing __eq__ definition
    
    def __str__(self):
     """Produce string representation of vector."""
        return "<" + str(self._coords)[1:-1] + ">"   # adapt list representation

v = Vector(5)
v[1] = 23
v[-1] = 45
print(v[4])
u = v + v
print(u)
total = 0
for entry in v:  # sums all the entries that went into vectors
    total+=entry # in this case 23 + 45
print(total)

m = Vector(3)
m[0], m[1], m[2]=244, 2999, 10
print(m)
u = m + [23, 22, -244]
print(u)
total = 0
for entry in u:
    total+=entry
print(total)'''

# example of low-level iterator
'''class SequenceIterator:
    """An iterator for any of Python's sequence types."""

    def __init__(self, sequence):
        """Create an iterator for the given sequence."""
        self.seq = sequence  # keep a reference to the underlying data
        self.k = -1  # will increment to 0 on the first call to next

    def __next__(self):
        """Return the next element, or else raise a StopIteration error."""
        self.k += 1  # advance to the next index
        if self.k < len(self.seq):
            return self.seq[self.k]  # return the data element
        else:
            raise StopIteration()  # there are no more elements

    def __iter__(self):
        """By convention, an iterator must return itself as an iterator."""
        return self'''

# Range class (to showcase the working of range())
'''class Range:
    """A class that mimics the built-in range class."""

    def __init__(self, start, stop=None, step=1):
        """Initialize a Range instance.

        Semantics are similar to the built-in range class.
        """
        if step == 0:
            raise ValueError("step cannot be 0")

        if stop is None:  # special case of range(n)
            start, stop = 0, start  # should be treated as if range(0, n)

        # Calculate the effective length once
        self.length = max(0, (stop - start + step - 1) // step)

        # Need knowledge of start and step (but not stop) to support getitem
        self.start = start
        self.step = step

    def __len__(self):
        """Return the number of entries in the range."""
        return self.length

    def __getitem__(self, k):
        """Return the entry at index k (using the standard interpretation if negative)."""
        if k < 0:
            k += len(self)  # attempt to convert the negative index

        if not 0 <= k < self.length:
            raise IndexError("index out of range")

        return self.start + k * self.step'''

# Progression class used as a base for other progressions
class Progression:
    """Iterator producing a generic progression.

    Default iterator produces the whole numbers 0, 1, 2, ...
    """
    def __init__(self, start=0):
        """Initialize current to the first value of the progression."""
        self.current = start

    def advance(self):
        """Update self.current to a new value.

        This should be overridden by a subclass to customize the progression.

        By convention, if current is set to None, this designates the
        end of a finite progression.
        """
        self.current += 1

    def __next__(self):
        """Return the next element, or else raise a StopIteration error."""
        if self.current is None:  # our convention to end a progression
            raise StopIteration()
        else:
            answer = self.current  # record the current value to return
            self.advance()  # advance to prepare for the next time
            return answer  # return the answer

    def __iter__(self):
        """By convention, an iterator must return itself as an iterator."""
        return self

    def print_progression(self, n):
        """Print the next n values of the progression."""
        print(" ".join(str(next(self)) for _ in range(n)))


class ArithmeticProgression(Progression): # inherit from Progression
    """Iterator producing an arithmetic progression."""

    def __init__(self, increment=1, start=0):
        """Create a new arithmetic progression.
        
        increment  the fixed constant to add to each term (default1)
        start      the first term of the progression (default0)"""
        super().__init__(start)
        self._increment=increment
    
    def _advance(self):
        """Update current value by adding the fixed increment."""
        self._current += self._increment


class GeometricProgression(Progression):
    """Iterator producing a geometric progression."""

    def __init__(self, base=2, start=1):
        """Create a new geometric progression.
        
        base    the fixed constant multiplied to each term (default 2)
        start   the first term of the progression (default1)"""
        super().__init__(start)
        self._base = base
    
    def _advance(self):     # override inherited version
        """Update current value by multiplying it by the base value."""
        self._current *=self._base

if __name__=="__main__":
    Progression().print_progression(10)
    ArithmeticProgression(5, 2).print_progression(10)
    GeometricProgression(3).print_progression(10)

# UNDERSTAND THE WAY OF CALLING AND TESTING!!!