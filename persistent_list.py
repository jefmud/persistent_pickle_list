import pickle
import os

def store_data(filename, data):
    # simple save of the data as a pickle serialization
    with open(filename, 'wb') as foutput:
        pickle.dump(data, foutput)

def load_data(filename): 
    # load data as a pickle serialized file
    with open(filename, 'rb') as finput:
        data = pickle.load(finput)
    return data

class PersistentList(list):
    import os, pickle
    def __init__(self, filename, *args, **kwargs):
        # overide the __init__ method of list
        self.filename = filename
        if os.path.exists(filename):
            data = self._load_data()
        else:
            data = list()
        super().__init__(data)
            
    def append(self, *args, **kwargs):
        # override the append method.
        # first call the list's append in the superclass
        super().append(*args, **kwargs)
        # store the data!
        self._store_data()

    def save(self, filename=None):
        # PUBLIC save, can override the filename
        self._store_data(filename)
        
    def delete(self):
        # PUBLIC clear/delete persistent storage, but not existing data
        if os.path.exists(self.filename):
            os.remove(self.filename)
        
    def _store_data(self, filename=None):
        # PRIVATE save as a pickle list serialization
        # Note, you can override the filename if needed
        if filename is None:
            filename = self.filename
        data = list(self)
        with open(filename, 'wb') as foutput:
            pickle.dump(data, foutput)

    def _load_data(self, filename=None):
        # load the data, you can override the filename of the class
        if filename is None:
            filename = self.filename
        # PRIVATE load data from pickle serialized file
        with open(filename, 'rb') as finput:
            data = pickle.load(finput)
        return data
    

filename = 'mydata.pkl'
fn1 = 'x.pkl'
fn2 = 'y.pk1'

list1 = [1,2,3,4,5]

store_data(filename,list1)

list2 = load_data(filename)

print(list1)
print(list2)

x = PersistentList(fn1)
print(x)
x.append('Hi there')

y = PersistentList(fn2)
y.append(list1)
print(y)
y.delete()

z = PersistentList('my_persistent_list.pkl')
z.append('I am a persistent list')
z.append({'name':'Guido Van Rostrum','age':55})
print(z)
