#Founder of Intel - Gordan Moor and Andrew Grove
#Threads Demo
#Thread is the smallest unit of processors
from threading import *
from time import sleep
class Hello(Thread):
    def run(self):
        for i in range(5):
            print("Hello")
            sleep(1)



class Hi(Thread):
    def run(self):
        for i in range(5):
            print("\nHi")
            sleep(1)

obj1 = Hello() # Hello thread created
obj2 = Hi() # Hi thread created

print("Welcome to the session")
print("We are learning threads")
x = 9

obj1.start() # Hello thread to start
sleep(1)
obj2.start()

#Join joins to the parrent threads
obj1.join()
obj2.join()

#sleep(10) # The use of sleep() is inefficient here as we don't know when the process ends

print("\nBye\n")

# mutation - Change
# thread

# mutation + thread = Corrupt
# Deadlock

# Sirsha - resourse
# Tisu and Hellocc
# 2 resourses A B
# 2 threads T1 T2

# Mutex - Mutual Exclusion

