# read file function
def read_file():
    file_data = open('./python_examples/file_io/input_file.txt')
    for single_line in file_data:
        print(single_line, end='')

if __name__ == "__main__":
    read_file()
