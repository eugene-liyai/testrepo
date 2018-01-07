# read file function
def read_file():
    buffersize = 40000  # declare buffer size

    # the 'rb' represents a read binary directive
    file_data = open('./python_examples/file_io/sample.jpg', 'rb')

    # the 'wb' represents a write binary directive
    output_file = open('./python_examples/file_io/new.jpg', 'wb')

    buffer = file_data.read(buffersize)  # loop over the chunks of buffer
    while len(buffer):
        output_file.write(buffer)
        buffer = file_data.read(buffersize)

    print('Writing to file completed')


if __name__ == "__main__":
    read_file()
