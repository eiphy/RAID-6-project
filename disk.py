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
        self.if_lost = False
        self.file = f'{disk_id}.txt'

        with open(f'{disk_id}.txt', 'w'):
            pass

    def write_to_file(self, data):
        '''Given a list of hexadecimal number, write it disk (file).
        
        The file is defined by disk_id.
        To be noticed, this should be finished by appending mode istead of 
        writing mode.
        Check and update the size.

        Returns:
            (start_pos, end_pos)
        '''
        assert len(data) > 0, "No data!"
        target_size = len(data) + self.size
        start = self.size

        content = []
        for d in data:
            assert d < 255, "Value is bigger than 255!"
            content.append("{:02x}".format(d))

        with open(self.file, 'a') as f:
            for c in content:
                f.write(c)
                self.size += 1

        assert self.size == target_size, "Lost data."

        end = self.size + 1

        return start, end

    def read_file(self, start, end):
        '''Read from file and return the hexadecimal number.
        Args:
            start: Start reading position.
            end: End reading position.

        Return:
            A tuple of reading hexadecimal numbers.
        '''
        with open(self.file, 'r') as f:
            f.seek(start)
            size = (end - start) * 2
            data_temp = f.read(size)

        data = []
        for i in range(len(data_temp)):
            if i % 2:
                temp = int(data_temp[i-1] + data_temp[i], 16)
                data.append(temp)

        return data

    def lost_data(self, n):
        '''Lost n bytes in the disk randomly.'''
        self.if_lost = True
    
    def recovered(self):
        self.if_lost = False
    
    def __repr__(self):
        return f'Disk {self.id} ({"lost" if self.if_lost else "normal"}), '    \
               f'used: {self.size}, '                                          \
               f'{self.size / self.capacity * 100}%'

if __name__ == "__main__":
    # a = 10
    # print(hex(a))
    # hex(a)

    d = Disk(0)
    print(d)

    data = [10, 20,3 ,4, 5, 46,23]

    start, end = d.write_to_file(data)

    print(d)

    a = d.read_file(start, end)
    print(a)