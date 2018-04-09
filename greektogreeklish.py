import os, argparse
from os import walk

class GreekToGreeklish(object):
    def __init__(self):
        parser = argparse.ArgumentParser(
            description = "Description for my parser"
            )
        parser.add_argument(
            "-I",
            "--Input",
            help = "When we need to add specific input location",
            required = False,
            default = os.getcwd()
        )
        parser.add_argument(
            "-O",
            "--Output",
            help = "When we need to add specific output location",
            required = False,
            default = os.getcwd()
        )
        argument = parser.parse_args()
        self.input = argument.Input
        self.output = argument.Output
        self.f = [] # empty list of filenames
        for (dirpath, dirnames, filenames) in walk(self.input):
            self.f.extend(filenames)
            break
    def printfilenames(self):
        print(self.f)


if __name__ == '__main__':
    app = GreekToGreeklish()
    app.printfilenames()
