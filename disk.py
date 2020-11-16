from pathlib import Path

class Disk():
    def __init__(self, disk_id):
        '''Create a dictionary contains the ascii table.'''

    def write_to_file(self, s):
        '''Given a string, write its hexadecimal representation to disk (file).'''

    def decode_string(self, s):
        '''Decode a given string to hexadecimal number.

        For instance, "start" will be a list of [0x73, 0x74, 0x61, 0x72, 0x74].

        Args:
            s, Input string.
        
        Returns:
            A list of hexadecimal number.
        '''
