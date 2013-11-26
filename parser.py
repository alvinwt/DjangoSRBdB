import sys, re
import csv

class CommentedFile:
    def __init__(self, f, commentstring="#"):
        self.f = f
        self.commentstring = commentstring
    def next(self):
        line = self.f.next()
        while line.startswith(self.commentstring):
            line = self.f.next()
        return line
    def __iter__(self):
        return self

tsv_name = sys.argv[1]
    
tsv_file = csv.reader(CommentedFile(open(tsv_name, "rb")),
                      delimiter='\t')
for row in tsv_file:
    print row[2] # prints column 3 of each line
