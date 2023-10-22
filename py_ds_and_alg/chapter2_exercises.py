#R-2.1
# insulin pumps, self-driving cars, hr monitoring machines
#R-2.2
# Software that estimates market demand -> you don't overproduce etc.
#R-2.3
# saving a file...
#R-2.4
'''class Flower:
    def __init__(self, name, n_petals, price):
        self.name = str(name)
        self.n_petals = int(n_petals)
        self.price = float(price)
    
    def set_name(self, new_name):
        self.name = new_name
    def set_n_petals(self, new_n_petals):
        self.n_petals = new_n_petals
    def set_price(self, new_price):
        self.price = new_price
    
    def get_name(self):
        return self.name
    def get_n_petals(self):
        return self.n_petals
    def get_price(self):
        return self.price
    
    def get_info(self):
        """made for easier checking of the values :)"""
        print(self.name, self.n_petals, self.price)

f1 = Flower("dandy", 36, 9.99)
f1.get_info()
f1.set_price(23.97)
f1.get_info()
f1.set_name("Dandelion?")
f1.get_info()'''
# a solution where we can assign those values and check for errors!:
'''
class Flower():
    def __init__(self, name = None, petals = None, price = None):
        self._name = self._petals = self._price = None
               
        self.set_name(name)
        self.set_petals(petals)
        self.set_price(price)
        
    def set_name(self, name):
        try:
            self._name = str(name)
        except:
            print ('Invalid input for a name, it must be a string')
            
    def set_petals(self, petals):
        try:
            self._petals = petals
        except:
            print ('Invalid input')
            
    def set_price(self, price):
        if price is not None: 
            try:
                self._price = float(price)
            except:
                print ('Invalid price, must be a number (no dollar sign)')
            
    def get_name(self):
        if self._name is None: return ('Attribute has not been set')
        else: return self._name
    
    def get_price(self):
        if self._price is None: return ('Attribute has not been set')
        else: return self._price
    
    def get_petals(self):
        if self._petals is None: return ('Attribute has not been set')
        else: return self._petals
    
    
    
Dand = Flower('Dandelion', 5, '$10.32')
print(Dand.get_name(), Dand.get_petals(), Dand.get_price())


print ('\n')
Rose = Flower()
print(Rose.get_name(), Rose.get_petals(), Rose.get_price())

Rose.set_name('Rose')
Rose.set_price(20)
Rose.set_petals(30)
print(Rose.get_name(), Rose.get_petals(), Rose.get_price())'''
#R-2.5
'''class CreditCard():
    def __init__(self, customer, bank, acnt, limit):
        self._customer = customer
        self._bank = bank
        self._account = acnt
        self._limit = limit
        self._balance = 0  #Start with a balance of zero
        
    def get_customer(self):
        return self._customer
    def get_bank(self):
        return self._bank
    def get_account(self):
        return self._account
    def get_limit(self):
        return self._limit
    def get_balance(self):
        return self._balance
    
    def set_balance(self, value):
        self._balance = value
          
    def charge(self, price):
        try:
            price = float(price)  #This will accept an int, float or string that can be converted to a float
        except:
            print ('Invalid input')
            return False       
        if price+self._balance >self._limit:
            print(f'Your deposit of {price} exceeds your remainder of {self.get_limit()-self.get_balance()}')
            return False #You are going over your limit
        else:
            self._balance += price
            return True
        
    def make_payment(self, amount):
        try:
            amount = float(amount)  #This will accept an int, float or string that can be converted to a float
        except:
            print ('Invalid input')
            return False 
        self._balance -= amount
        return True
                
cc1 = CreditCard('Andrew', 'ABC', '1234567890', 1000)
cc1.make_payment(100); print(cc1.get_balance())
cc1.charge(100); print(cc1.get_balance()) 
cc1.charge(500); print(cc1.get_balance()) 
cc1.charge(200); print(cc1.get_balance()) 
cc1.charge(100); print(cc1.get_balance()) 
cc1.charge(500); print(cc1.get_balance()) 
cc1.charge("Hello"); print(cc1.get_balance())
cc1.charge("20"); print(cc1.get_balance())
cc1.charge("453.4"); print(cc1.get_balance())'''
#R-2.6
'''class CreditCard():
    def __init__(self, customer, bank, acnt, limit):
        self._customer = customer
        self._bank = bank
        self._account = acnt
        self._limit = limit
        self._balance = 0  #Start with a balance of zero
        
    def get_customer(self):
        return self._customer
    def get_bank(self):
        return self._bank
    def get_account(self):
        return self._account
    def get_limit(self):
        return self._limit
    def get_balance(self):
        return self._balance
    
    def set_balance(self, value):
        self._balance = value
          
    def charge(self, price):
        try:
            price = float(price)  #This will accept an int, float or string that can be converted to a float
        except:
            print ('Invalid input')
            return False       
        if price+self._balance >self._limit:
            print(f'Your deposit of {price} exceeds your remainder of {self.get_limit()-self.get_balance()}')
            return False #You are going over your limit
        else:
            self._balance += price
            return True
        
    def make_payment(self, amount):
        try:
            amount = float(amount)  #This will accept an int, float or string that can be converted to a float
        except:
            print ('Invalid input')
            return False
        if amount <= 0:
            raise ValueError(("cannot pay a negative amount"))
        self._balance -= amount
        return True
        
cc1 = CreditCard('Andrew', 'ABC', '1234567890', 1000)
print(cc1.get_balance())
cc1.make_payment(-100)
print(cc1.get_balance())
# cc1.charge(100); print(cc1.get_balance()) '''
#R-2.7
"""def __init__(self, customer, bank, acnt, limit, balance=0):...
remove the self.balance=0 from the definitions"""
#R-2.8
'''class CreditCard():
    def __init__(self, customer, bank, acnt, limit):
        self._customer = customer
        self._bank = bank
        self._account = acnt
        self._limit = limit
        self._balance = 0  #Start with a balance of zero
        
    def get_customer(self):
        return self._customer
    def get_bank(self):
        return self._bank
    def get_account(self):
        return self._account
    def get_limit(self):
        return self._limit
    def get_balance(self):
        return self._balance
    
    def set_balance(self, value):
        self._balance = value
          
    def charge(self, price):
        try:
            price = float(price)  #This will accept an int, float or string that can be converted to a float
        except:
            print ('Invalid input')
            return False       
        if price+self._balance >self._limit:
            print(f'Your deposit of {price} exceeds your remainder of {self.get_limit()-self.get_balance()}')
            return False #You are going over your limit
        else:
            self._balance += price
            return True    
    def make_payment(self, amount):
        try:
            amount = float(amount)  #This will accept an int, float or string that can be converted to a float
        except:
            print ('Invalid input')
            return False
        if amount <= 0:
            raise ValueError(("cannot pay a negative amount"))
        self._balance -= amount
        return True

class CreditCardSelfReport(CreditCard):
    def special_charge(self, amount):
        if super().charge(amount): return True
        else:
            print("Credit card has failed:", self.get_bank())


if __name__ == "__main__":
    wallet = []
    wallet.append(CreditCardSelfReport("John Bowman", "California Savings", "5391 0375 9387 5309", 2500))
    wallet.append(CreditCardSelfReport("John Bowman", "California Federal", "3485 0399 3395 1954", 3500))
    wallet.append(CreditCardSelfReport("John Bowman", "California Finance", "5391 0375 9387 5309", 5000))
    
    for val in range(1, 100):
        wallet[0].special_charge(val)
        wallet[1].special_charge(2 * val)
        wallet[2].special_charge(3 * val)

    for c in range(3):
        print("Customer =", wallet[c].get_customer())
        print("Bank =", wallet[c].get_bank())
        print("Account =", wallet[c].get_account())
        print("Limit =", wallet[c].get_limit())
        print("Balance =", wallet[c].get_balance())
        
        while wallet[c].get_balance() > 100:
            wallet[c].make_payment(100)
        print("New balance =", wallet[c].get_balance())
        print()'''
#R-2.9 and R-2.10
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
        return result
    # R-2.9
    def __sub__(self, other):
        """Return the difference of two vectors."""
        if len(self) != len(other):
            raise ValueError("dimensions must agree")
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] - other[j]
        return result
    
    # R-2.10
    def __neg__(self):
        """Return negated values of the coordinates"""
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] * -1
        return result
    
    def __eq__(self, other):
        """Return True if vector has same coordinates as other."""
        return self._coords == other._coords
    
    def __ne__(self, other):
        return not self == other   # rely on existing __eq__ definition
    
    def __str__(self):
        """Produce string representation of vector."""
        return "<" + str(self._coords)[1:-1] + ">"   # adapt list representation
#R-2.9 testing
v1 = Vector(5)
v2 = Vector(5)
for i in range(5):
    v1[i] = 5
    v2[i] = i
print(v1+v2)
print(v1-v2)
print(v2-v1)
#R-2.10 testing
import random
v3 = Vector(5)
for i in range(5):
    v3[i] = random.randrange(0, 50)
print(v3, -v3)'''
#R2.11
"""
If the method list.add fails, the method in Vector.radd will be checked instead.
Adding a def __radd__(self, other): would allow you to solve that problem
One option would be to use an iterator to go through each of the components and add them 
(since __len__ and __getitem__ should be defined for each class) 

"""

#R2.12
''''class Vector:
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
        return result
    # R-2.9
    def __sub__(self, other):
        """Return the difference of two vectors."""
        if len(self) != len(other):
            raise ValueError("dimensions must agree")
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] - other[j]
        return result
    
    # R-2.10
    def __neg__(self):
        """Return negated values of the coordinates"""
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] * -1
        return result
    
    # R-2.12
    def __mul__(self, val):
        """Return vector with coordinates multiplied"""
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] * val
        return result
    # R-2.13
    def __rmul__(self, val):
        return (self*val)
    
    def __eq__(self, other):
        """Return True if vector has same coordinates as other."""
        return self._coords == other._coords
    
    def __ne__(self, other):
        return not self == other   # rely on existing __eq__ definition
    
    def __str__(self):
        """Produce string representation of vector."""
        return "<" + str(self._coords)[1:-1] + ">"  '''

# R2-12 testing
'''v1 = Vector(5)
for i in range(5):
    v1[i] = 5
print(v1*6)
print(7*v1)'''

# R-2.14
'''class VectorVectorDot(Vector):
    def __mul__(self, other):
        if type(other) == int or type(other) == float:
            result = Vector(len(self))
            for i in range(len(self)):
                result[i] = self[i]*other
            return result
        else:
            len(other)
            print(len(other), len(self))
            if len(other)!=len(self):
                raise ValueError("Vector lengths do not match")
            sum = 0
            for i in range(len(self)):
                sum+= self[i]*other[i]
            return sum

vvd = VectorVectorDot

"""v2 = vvd(5)
v3 = vvd(5)
import random
for i in range(5):
    v2[i], v3[i] = 5, i
print(v2*v3)
try:
    print (v1*vvd(7))
except Exception as e:
    print(e)
print (v1*3.3)"""'''

# R-2.15
'''class VectorwListInit(VectorVectorDot):
    def __init__(self, param): # Override the original constructor
        if type(param) == int:
            super().__init__(param)
        else:
            # if the parameter is a list, the values are set as vector coord.
            self._coords = param

"""vv = VectorwListInit
print(vv([1, 2, 3]), vv(3))"""'''

# R-2.16
'''# self.length = max(0, (stop - start + step - 1) // step)
# eg. stop = 20, start = 10, step=2
# (20 - 10 + 2 - 1 )//2 = 10
# stop - start -> calculates the number of v. in range
# step - 1 -> used to account for inclusive range behavior (stop v. included in range)
# // step -> determines how many times step size must be added
# max() -> makes sure the result of the division is never negative
# --> ensures that the minimum value is 0
# --> prevents negative values from indicating that the range is non-empty when it's not
'''
# R-2.17 --> picture
# R-2.18
'''class Progression:
    """Iterator producing a generic progression."""

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
        for _ in range(n):
            print(next(self), end=' ')
        print()  # Print a new line at the end of the sequence
class FibonacciProgression(Progression):
    """Iterator producing a generalized Fibonacci progression."""
    
    def __init__(self, first=0, second=1):
        """Create a new fibonacci progression.
        first   the first term of the progression (default 0)
        second  the second term of the progression (default 1)"""
        
        super().__init__(first)
        self._prev = second

    def advance(self):
        """Update current value by taking the sum of the previous two."""
        self.current, self._prev = self.current + self._prev, self.current

fp = FibonacciProgression(2, 2)
fp.print_progression(7)
# 8th value = 42'''

#R-2.19
'''class ArithmeticProgression(Progression):
    def __init__(self, start=0, step = 1):
        self._current = start
        self._step = step
        
    def __next__(self):
        answer = self._current
        self._current = self._current + self._step
        return answer
    
    def __getitem__(self, index):
        current = self._current
        for i in range(index + 1):
            answer = next(self)
        self._current = current
        return (answer)
    
    
p = Progression()
p.print_progression(10)

a = ArithmeticProgression(1,1)
for i in range (8):
    print (f'Value Number {i+1} is {a[i]}')
a.print_progression(8)

#The answer is 2**63//128, which is 7.2e16 calls

b = ArithmeticProgression(0, 128)
i = 0
goal = 2**63
value = 0
while value < goal:
    i+=1
    value = next(b)'''

#R-2.20
"""
If behaviour changes in A without D knowing, can be difficult
to troubleshoot

Great chance of namespace conflicts you might not even be aware of."""
#R-2.21
"""
If any of the classes change, it will mess up the entire Z subclass
Namespace conflicts might be more difficult to resolve."""
#R-2.22 & R-2.23
'''from abc import ABCMeta, abstractmethod

class Sequence(metaclass=ABCMeta):
    """Our own version of collections.Sequence abstract base class."""
    
    @abstractmethod
    def __len__(self):
        """Return the length of the sequence."""
    
    @abstractmethod
    def __getitem__(self, j):
        """Return the element at index j of the sequence."""
    
    def contains(self, val):
        """Return True if val is found in the sequence; False otherwise."""
        for j in range(len(self)):
            if self[j] == val:  # found a match
                return True
        return False
    
    def index(self, val):
        """Return the leftmost index at which val is found (or raise ValueError)."""
        for j in range(len(self)):
            if self[j] == val:  # leftmost match
                return j
        raise ValueError("value not in sequence")  # never found a match
    
    def count(self, val):
        """Return the number of elements equal to the given value."""
        k = 0
        for j in range(len(self)):
            if self[j] == val:  # found a match
                k += 1
        return k
    # R-2.22
    def __eq__(seq1, seq2):
        if len(seq1) != len(seq2):
            raise ValueError("sequences not of same length")
        else:
            for i in range(len(seq1)):
                if seq1[i] != seq2[i]:
                    return False
            return True
    #R-2.23
    def __lt__(self, other):
        """
This loop iterates through the indices from 0 up to the minimum length of self and other.
It ensures that the loop won't go out of bounds if one sequence is shorter than the other.
This is important to avoid IndexError exceptions when comparing sequences of different lengths.

Inside the loop, it compares elements at the same index in self and other.
If it finds a pair of elements that are not equal, it immediately returns False.
This means that the sequences are not equal at this point in the lexicographic order,
and no further comparisons are needed.

If the loop completes without returning False, it means that all elements up to
the length of the shorter sequence have been found to be equal.
In this case, the function returns True, indicating that self is less than other
in the lexicographic order.
"""

        for i in range(min(len(self), len(other))):
            if self[i] != other[i]: return False
        return True'''
        

#C-2.24
"""
Methods:
purchase_books()
view_purchased()
read_purchased

Class Hierarchy:
E-book Class
Class for a specific book"""

#C-2.25
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
        return result
    def __mul__(self, other):
        if type(other) == int or type(other) == float:
            result = Vector(len(self))
            for i in range(len(self)):
                result[i] = self[i]*other
            return result
        else:
            len(other)
            print(len(other), len(self))
            if len(other)!=len(self):
                raise ValueError("Vector lengths do not match")
            sum = 0
            for i in range(len(self)):
                sum+= self[i]*other[i]
            return sum'''

#C-2.26
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
        return self
class ReverseSequenceIterator():
    def __init__(self, sequence):
        self.seq = sequence
        self.k = len(self.seq)
    
    def __next__(self):
        self.k -=1
        if self.k>=0:
            return self.seq[self.k]
        else:
            raise StopIteration()
    def __iter__(self):
        return self

s = ReverseSequenceIterator([1, 2, 3 ,4, 5, 6, 7, 8])
s1 = ReverseSequenceIterator([1, 2, 3, "m", 35, 23.49])
print([x for x in s])
print([y for y in s1])'''

#C-2.27
"""class Range():
    def __init__(self, start, stop = None, step = 1):
        if step == 0: raise ValueError('step cannot be 0')
        if stop is None:    #This is more robust than if stop == None, since it's ambiguous sometimes (ex. custom classes)
            start, stop = 0, start
            
        self._length = max(0, (stop-start + step -1)//step)
        
        self._start = start
        self._step = step
        
    def __len__(self):
        return self._length
    
    def __getitem__(self, k):
        if k<0:
            k+= len(self)
        if not 0<=k<self._length:
            raise IndexError('index out of range')
            
        return self._start + k*self._step
    
    def __contains__(self, value):
        # The number will be in the sequence if (value - start)% step == 0
        factor, remainder = divmod((value-self._start), self._step)
        
        if remainder == 0:    #It is a part of the infinite range in either directiom
            #Now we just need to check if it's within the defined range...
            if factor < len(self) and factor >=0: return True
            else: return False
        else:
            return False
r = Range(1,100,2)
print (len(r), r[3], 4 in r, 5 in r)

r = Range(-100, step = -1)
print (len(r), r[3], 4 in r, 5 in r)
"""

#C-2.28 & C-2.29
'''class CreditCard:
    """A consumer credit card."""
    
    def __init__(self, customer, bank, acnt, limit):
        """
        Create a new credit card instance.

        The initial balance is zero.

        customer: the name of the customer (e.g., John Bowman)
        bank: the name of the bank (e.g., California Savings)
        acnt: the account identifier (e.g., 5391 0375 9387 5309)
        limit: credit limit (measured in dollars)
        """
        self.customer = customer
        self.bank = bank
        self.account = acnt
        self.limit = limit
        self.balance = 0

    def get_customer(self):
        """Return the name of the customer."""
        return self.customer

    def get_bank(self):
        """Return the bank's name."""
        return self.bank

    def get_account(self):
        """Return the card identifying number (typically stored as a string)."""
        return self.account

    def get_limit(self):
        """Return the current credit limit."""
        return self.limit

    def get_balance(self):
        """Return the current balance."""
        return self.balance

    def charge(self, price):
        """Charge the given price to the card, assuming sufficient credit limit.

        Return True if the charge was processed; False if the charge was denied.
        """
        if price + self.balance > self.limit:  # if the charge would exceed the limit,
            return False  # cannot accept the charge
        else:
            self.balance += price
            return True

    def make_payment(self, amount):
        """Process a customer payment that reduces the balance."""
        self.balance -= amount

class PredatoryCreditCard(CreditCard):
    """An extension to CreditCard that compounds interest and fees."""
    MAX_CHARGES = 10 # C-2.28
    def __init__(self, customer, bank, acnt, limit, apr):
        """
        Create a new predatory credit card instance.

        The initial balance is zero.

        customer: the name of the customer (e.g., John Bowman)
        bank: the name of the bank (e.g., California Savings)
        acnt: the account identifier (e.g., 5391 0375 9387 5309)
        limit: credit limit (measured in dollars)
        apr: annual percentage rate (e.g., 0.0825 for 8.25% APR)
        """
        super().__init__(customer, bank, acnt, limit)  # call super constructor
        self.apr = apr
        self.charge_count=0
        self.month_paid = False

    def charge(self, price):
        """Charge the given price to the card, assuming sufficient credit limit.

        Return True if the charge was processed.
        Return False and assess a $5 fee if the charge is denied.
        """
        success = super().charge(price)  # call inherited method
        if not success:
            self.balance += 5  # assess a penalty
        else:
            self.charge_count+=1
            if self.charge_count > self.MAX_CHARGES: # C-2.28
                self.balance+=1
        return success  # caller expects a return value
    def monthly_charge(self):
        self.m_fee = self.balance*(0.022) # 2.2%
        self.balance+=self.m_fee
        self.month_paid = True
        
    def process_month(self):
        """Assess monthly interest on the outstanding balance."""
        if self.balance > 0:
            if not self.month_paid:
                self.late_fee = self.balance*(0.1) # 10.0%ˇ
                self.balance += self.late_fee
            self.month_paid = False
            # if a positive balance, convert APR to a monthly multiplicative factor
            monthly_factor = pow(1 + self.apr, 1/12)
            self.balance *= monthly_factor'''

#C-2.31
'''class Progression:
    """Iterator producing a generic progression."""

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
        for _ in range(n):
            print(next(self), end=' ')
        print()  # Print a new line at the end of the sequence

class AbsProgression(Progression):
    def __init__(self, first=2, second=200):
        self.current = first
        self.prev1 = 202
    def advance(self):
        self.current
        self.current, self.prev1 = abs(self.current-self.prev1), self.current

AbsProgression().print_progression(10)
AbsProgression(2334, 39).print_progression(10)

from math import sqrt
class SqrtProgression(Progression):
    def __init__(self, start=65536):
        self.current = start
    def advance(self):
        self.current = sqrt(self.current)

SqrtProgression().print_progression(10)'''

#P-2.33
'''class Polynomial():
    # Constructor: Initializes a polynomial with specified length
    def __init__(self, length=4):
        self._coords = [0] * length  # Coefficients of the polynomial

    # Get the length of the polynomial
    def __len__(self):
        return len(self._coords)

    # Get the coefficient at a specific power
    def __getitem__(self, index):
        return self._coords[index]

    # Representation of the polynomial as a string
    def __repr__(self):
        # Each term represented as "ax^b"
        return " + ".join([f"{self[i]}x^{i}" for i in range(len(self))])

    # Set the coefficient at a specific power
    def __setitem__(self, index, value):
        self._coords[index] = value

    # Calculate and return the derivative of the polynomial
    def derivative(self):
        result = Polynomial(len(self) - 1)
        for i in range(1, len(self)):
            result[i - 1] = self[i] * i
        return result
    
p = Polynomial(10)
for i in range(len(p)):
    p[i] = i
print(p)
print(p.derivative())
f = Polynomial(4)
f[0] = 7
f[1] = -5
f[2] = 2
f[3] = 3
print(f)
print(f.derivative())'''

#P-2.34
class BarChart():
    ALPHABET = "abcdefghijklmnopqrstuvwxyz"
    def __init__(self, filename):
        self.count = 0
        self.text = ""
        self.filename = filename
        
    
    def _reader(self):
        with open(fr"C:\Users\tomas\Desktop\code\all-code\py_ds_and_alg\{self.filename}", "r") as file:
            for line in file:
                line = line.strip()
                line = line.lower()
                self.text+=str(line)
    def _counter(self):
        # self.count = self.text.count()
        for i in range(len(self.ALPHABET)):
            pass
    def _chart_maker(self, letter, count):
        # making the count display thousands of occurances (one # -> 1K)
        print()
        
    
        
            

