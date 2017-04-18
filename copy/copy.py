# This should be the basic replica of the 'cp' command
# If ran from the command line without arguments
# It should print out the usage:
# copy [source] [destination]
# When just one argument is provided print out
# No destination provided
# When both arguments provided and the source is a file
# Read all contents from it and write it to the destination
import sys

class Copy(object):
    def __init__(self):
        self.controller()

    def controller(self):
        if len(sys.argv) == 1:
            print("copy [source] [destination]")
        if len(sys.argv) == 2:
            print("No destination provided")
        if len(sys.argv) == 3:
            self.destination = sys.argv[2]
            self.data_reader(sys.argv[1])

    def data_reader(self, source):
        while True:
            try:
                self.raw_data = open(source, "r")
                self.data = self.raw_data.read()
                self.raw_data.close()
                self.data_writer(self.data)
                break
            except:
                print("Couldn't open source file.")
                break

    def data_writer(self, meta):
        self.data_write = open(self.destination, "w")
        self.data_write.write(meta)
        self.data_write.close()

start = Copy()
