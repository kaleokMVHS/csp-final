
class GridHelper:
    def __init__(self):
        self.side_buffer = 200

    def pos_to_coord(self, xy_tuple): # top left of 800*800 grid in center
        x, y = xy_tuple
        return(self.side_buffer + x*50, y*50)

    def left_of(self, xy_tuple):
        x, y = xy_tuple
        return(self.side_buffer + (x-1)*50, y*50)

    def right_of(self, xy_tuple):
        x, y = xy_tuple
        return(self.side_buffer + (x+1)*50, y*50)

    def up_of(self, xy_tuple):
        x, y = xy_tuple
        return(self.side_buffer + x*50, (y+1)*50)

    def down_of(self, xy_tuple):
        x, y = xy_tuple
        return(self.side_buffer + x*50, (y+1)*50)