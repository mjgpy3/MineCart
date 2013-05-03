#!/usr/bin/env python

# Created by Michael Gilliland
# Date: Tue Jan 15 22:36:35 EST 2013
# 
# 

"""
    Contains writer classes for different outputs
"""

class EmailFileWriter:
    """
        The "interface" for a writer object
    """
    def __init__(self, name):
        self.output_name = name

    def write(self, emails, output_file_name):
        """
            A function to write out emails in various formats
        """
        raise NotImplementedError("Each writer must be able to write!")

class CsvWriter(EmailFileWriter):
    """
        Used to write out a simple CSV list
    """
    def __init__(self):
        EmailFileWriter.__init__(self, ".csv")

    def write(self, emails, output_file_name):
        """
            Writes the emails out emails separated by commas and newlines
        """
        with open(output_file_name + self.output_name, 'w') as f:
            for email in emails:
                f.write(email + ',\n')

class PlainTextWriter(EmailFileWriter):
    """
        Writes out emails to a plain text file
    """
    def __init__(self):
        EmailFileWriter.__init__(self, ".txt")

    def write(self, emails, output_file_name):
        """
            Writes out emails on newlines
        """
        with open(output_file_name + self.output_name, 'w') as f:
            for email in emails:
                f.write(email + '\n')
        
available_writers = {"CSV": CsvWriter, "Plaintext": PlainTextWriter}
