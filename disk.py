import random
from pathlib import Path

import util as U

class Disk():
    def __init__(self, disk_id, disk_type="normal"):
        '''Initialize the Disk class.
        
        Create and maintain a ascii table as a dictionary.
        Store the disk_id which will associated a file to this disk. e.g. disk_id=10, then all data will write to file "10.txt" for this disk.
        '''
        assert disk_type in ["p", "q", "normal"], "Unknown disk type!"
        self.id = disk_id
        self.size = 0
        self.type = disk_type

    def write_to_file(self, data):
        '''Given a list of hexadecimal number, write it disk (file).
        
        The file is defined by disk_id.
        To be noticed, this should be finished by appending mode istead of writing mode.
        Update the 

        Returns:
            (start_pos, end_pos)
        '''

    def read_file(self, start, end):
        '''Read from file and return the hexadecimal number.
        Args:
            start: Start reading position.
            end: End reading position.

        Return:
            A tuple of reading hexadecimal numbers.
        '''

    def corrupt_data(self, n):
        '''Corrupt n bytes in the disk randomly.'''
    
    def __repr__(self):
        return f'Disk {self.id}, type: {self.type}'
