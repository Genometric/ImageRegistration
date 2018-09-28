"""
TODO
"""


class Vertex(object):
    def __init__(self, x, y, z=None):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        z=""
        if self.z:
            z=", {}".format(self.z)
        return "<V: {}, {}{} >".format(self.x, self.y, z)
