from pathlib import Path

import util as U

class Disk():
    def __init__(self, disk_id):
        '''Initialize the Disk class.
        
        Create and maintain a ascii table as a dictionary.
        Store the disk_id which will associated a file to this disk. e.g. disk_id=10, then all data will write to file "10.txt" for this disk.
        '''

    def write_to_file(self, s):
        '''Given a string, write its hexadecimal representation to disk (file).
        
        To be noticed, this should be finished by appending mode istead of writing mode.

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
    
    def encode_string(self, s):
        '''Decode a given string to hexadecimal number.

        For instance, "start" will be a list of [0x73, 0x74, 0x61, 0x72, 0x74].

        Args:
            s, Input string.
        
        Returns:
            A list of hexadecimal number.
        '''
