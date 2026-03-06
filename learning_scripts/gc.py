import sys 
import gc 

gc.disable() 

class garbage_collector:
    def __init__(self):
        self.data = [i for i in range(100000)]
      #  print(self.data)
    def __del__(self):
        print("Instance is being destroyed (sys.getrefcount() reached zero).")
        del self.data

if __name__ == "__main__":
    obj1 = garbage_collector()
    print("Reference count of obj1:", sys.getrefcount(obj1)) 

    obj2 = obj1 
    print("Reference count of obj1 after creating obj2:", sys.getrefcount(obj1)) 

    del obj2 
    print("Reference count of obj1 after deleting obj2:", sys.getrefcount(obj1)) 

    del obj1 
    try:
        print("Reference count of obj1 after deleting obj1:", sys.getrefcount(obj1))
    except NameError as e:
        print("obj1 is no longer defined because it was deleted and the object destroyed.")

    gc.collect() 
