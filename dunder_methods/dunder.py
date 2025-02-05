class DunderExample:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __str__(self):
        return f"DunderExample({self.name}, {self.value})"
    
    def __repr__(self):
        return f"DunderExample('{self.name}', {self.value})"
    
    def __len__(self):
        return len(self.name)
    
    def __call__(self, multiplier):
        return self.value * multiplier
    
    def __add__(self, other):
        if isinstance(other, DunderExample):
            return DunderExample(self.name + other.name, self.value + other.value)
        return NotImplemented
    
    def __eq__(self, other):
        if isinstance(other, DunderExample):
            return self.name == other.name and self.value == other.value
        return False
    
    def __getitem__(self, index):
        return self.name[index]
    
    def __setitem__(self, index, char):
        name_list = list(self.name)
        name_list[index] = char
        self.name = "".join(name_list)
    
    def __contains__(self, char):
        return char in self.name
    
    def __del__(self):
        print(f"Deleting {self}")

# Example usage
d1 = DunderExample("Hello", 10)
d2 = DunderExample("World", 20)

print(str(d1))         # __str__
print(repr(d1))        # __repr__
print(len(d1))         # __len__
print(d1(3))           # __call__
print(d1 + d2)         # __add__
print(d1 == d2)        # __eq__
print(d1[1])           # __getitem__
d1[1] = 'a'            # __setitem__
print(d1.name)         # Check modified name
print('a' in d1)       # __contains__
del d1                 # __del__
