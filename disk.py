import random
from pathlib import Path

import util as U
import convert as C

class Disk():
    def __init__(self, disk_id, capacity=102400):
        '''Initialize the Disk class.
        
        Create and maintain a ascii table as a dictionary.
        Store the disk_id which will associated a file to this disk. e.g. 
        disk_id=10, then all data will write to file "10.txt" for this disk.
        '''
        self.id = disk_id
        self.size = 0
        self.capacity = capacity

    def write_to_file(self, data):
        '''Given a list of hexadecimal number, write it disk (file).
        
        The file is defined by disk_id.
        To be noticed, this should be finished by appending mode istead of 
        writing mode.
        Check and update the size.

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

    def lost_data(self, n):
        '''Lost n bytes in the disk randomly.'''
    
    def __repr__(self):
        return f'Disk {self.id}, used: {self.size}, '                          \
               f'{self.size / self.capacity * 100}%'
