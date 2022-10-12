
# Get user input
# age = input('How old are you? ')
# # print(age)

#File management

file = open("test.txt", "r")

# Open, read and navigate in file
# print(file.read(16))
# print(file.tell())
# file.seek(27)
# print(file.tell())
# file.close()

# Read line by line
# for line in file:
#     print(line)
# file.close()

# Check state and info on file
# print('File Name: ' + file.name)
# print('is closed: ' + str(file.closed))
# print('Mode ' + file.mode)
file.close()

# print('File Name: ' + file.name)
# print('is closed: ' + str(file.closed))
# print('Mode ' + file.mode)

# Writing to file
file = open("write.txt", "w+")
file.write('Hello, this is some coole text i can write in my new file')
file.seek(0)
print(file.read())
file.close()
