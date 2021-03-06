import random
from pathlib import Path

import util as U


class Disk:
    def __init__(self, disk_id, capacity=102400, clear=False):
        """Initialize the Disk class.

        Create and maintain a ascii table as a dictionary.
        Store the disk_id which will associated a file to this disk. e.g.
        disk_id=10, then all data will write to file "10.txt" for this disk.
        """
        self.id = disk_id
        self.capacity = capacity
        self.if_lost = False
        self.file = f"disk/{disk_id}.txt"

        Path("disk").mkdir(parents=True, exist_ok=True)

        with open(self.file, "a+") as f:
            f.seek(0)
            self.size = int(len(f.read()) / 2)

        if clear:
            self.clear_disk()

    def write_to_file(self, data):
        """Given a list of hexadecimal number, write it disk (file).

        The file is defined by disk_id.
        To be noticed, this should be finished by appending mode istead of
        writing mode.
        Check and update the size.

        Returns:
            (start_pos, end_pos)
        """
        assert len(data) > 0, "No data!"
        target_size = len(data) + self.size
        start = self.size

        content = []
        for d in data:
            assert d <= 255, "Value is bigger than 255!"
            content.append("{:02x}".format(d))

        with open(self.file, "a") as f:
            for c in content:
                f.write(c)
                self.size += 1

        assert self.size == target_size, "Lost data."

        end = self.size + 1

        return start, end

    def read_file(self, start, end=-1):
        """Read from file and return the hexadecimal number.
        Args:
            start: Start reading position.
            end: End reading position.

        Return:
            A tuple of reading hexadecimal numbers.
        """
        if self.if_lost:
            return None

        size = self.size if end == -1 else start - end
        size *= 2

        with open(self.file, "r") as f:
            f.seek(start)
            data_temp = f.read(size)

        data = []
        for i in range(len(data_temp)):
            if i % 2:
                temp = int(data_temp[i - 1] + data_temp[i], 16)
                data.append(temp)

        return data

    def lost_data(self):
        """Lost n bytes in the disk randomly."""
        self.if_lost = True
        self.clear_disk()

    def clear_disk(self):
        with open(self.file, "w") as f:
            pass
        self.size = 0

    def recovered(self):
        self.if_lost = False

    def __repr__(self):
        return (
            f'Disk {self.id} ({"lost" if self.if_lost else "normal"}), '
            f"used: {self.size}, "
            f"{self.size / self.capacity * 100}%"
        )


if __name__ == "__main__":
    # a = 10
    # print(hex(a))
    # hex(a)

    d = Disk(0)
    print(d)

    data = [10, 20, 3, 4, 5, 46, 23]

    start, end = d.write_to_file(data)

    print(d)

    a = d.read_file(start, end)
    print(a)
