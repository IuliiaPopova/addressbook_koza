from sys import maxsize

class Contact(object):
    def __init__(self, first_name=None, last_name=None, id=None):
        self.first_name = first_name
        self.last_name = last_name
        self.id = id

    def __repr__(self):
        """
        definition of format for id and name

        """
        return f"id = '{self.id}': first_name = '{self.first_name}': last_name'{self.last_name}'"

    def __eq__(self, other):
        """
        compare 2 objects - first:self, second:other

        """
        return (self.id is None or other.id is None or self.id == other.id) and self.first_name == other.first_name and \
               self.last_name ==other.last_name

    def id_or_max(self):

        if self.id:
            return int(self.id)
        else:
            return maxsize