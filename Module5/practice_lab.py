'''
Write code that does the following:  

Create an an output file with the filename list.txt that uses a loop to write numbers 1 through 20 to the file, then closes the file.  

Then have your code open the list.txt file and then read all of the numbers from the file to then display each number one line at a time to the console then closes the file.  

Use exception handling where applicable. 
'''

def create_file():
    with open("list.txt", "w") as file:
        for i in range(1, 21):
            file.write(f"{i}\n")

def read_file():
    with open("list.txt", "r") as file:
        for line in file:
            print(line.strip())

create_file()
read_file()