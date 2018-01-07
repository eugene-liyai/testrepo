# read file function
def read_file():
    buffersize = 5  # declare buffer size

    # the 'r' represents a read directive
    file_data = open('./python_examples/file_io/input_file.txt', 'r')

    # the 'w' represents a write directive
    output_file = open('./python_examples/file_io/output_file.txt', 'w')

    buffer = file_data.read(buffersize)  # loop over the chunks of buffer
    while len(buffer):
        output_file.write(buffer)
        buffer = file_data.read(buffersize)

    print('Writing to file completed')


if __name__ == "__main__":
    read_file()