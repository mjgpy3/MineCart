#!/usr/bin/env python

# Created by Michael Gilliland
# Date: Tue Jan 15 22:36:35 EST 2013
# 
# 

class EmailFileWriter:
    def __init__(self, name):
        self.output_name = name

    def write(self, emails, output_file_name):
        raise NotImplementedError("Each writer must be able to write!")

class CsvWriter(EmailFileWriter):
    def __init__(self):
        EmailFileWriter.__init__(self, ".csv")

    def write(self, emails, output_file_name):
        with open(output_file_name + self.output_name, 'w') as f:
            for email in emails:
                f.write(email + ',\n')

class PlainTextWriter(EmailFileWriter):
    def __init__(self):
        EmailFileWriter.__init__(self, ".txt")

    def write(self, emails, output_file_name):
        with open(output_file_name + self.output_name, 'w') as f:
            for email in emails:
                f.write(email + '\n')
        

available_writers = {"CSV": CsvWriter, "Plaintext": PlainTextWriter}
