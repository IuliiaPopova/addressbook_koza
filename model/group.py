from sys import maxsize


class Group(object):
    def __init__(self, name=None, header=None, footer=None, id=None):
        self.name = name
        self.header = header
        self.footer = footer
        self.id = id

    def __repr__(self):
        """
        definition of format for id and name

        """
        return f"id = '{self.id}': name = '{self.name}'"

    def __eq__(self, other):
        """
        compare 2 objects - first:self, second:other

        """
        return (self.id is None or other.id is None or self.id == other.id) and self.name == other.name

    def id_or_max(self):
        """
        checking object group has id, if yes - return id of object(group) of type int
        if no - return big number(maxsize)
        """
        if self.id:
            return int(self.id)
        else:
            return maxsize
