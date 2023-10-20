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
class Vector:
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
print(v3, -v3)