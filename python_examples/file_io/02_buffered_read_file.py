# read file function
def read_file():
    buffersize = 5  # declare buffer size
    file_data = open('./python_examples/file_io/input_file.txt')

    buffer = file_data.read(buffersize)  # loop over the chunks of buffer
    while len(buffer):
        print(buffer, end = '')
        buffer = file_data.read(buffersize)

if __name__ == "__main__":
    read_file()
