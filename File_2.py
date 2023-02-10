''' f = open('test.txt', 'w')
f.write("Be a good listener") #It will be printed on our file
f.close() '''

# This one automatic closes
with open('test.txt', 'w') as f:
    f.write("Be a good listener ")
