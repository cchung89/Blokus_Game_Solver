import math

# Get the new x value of point pt (x, y) rotated about reference point
# refpt (x, y) by degrees clockwise
def rotatex(pt, refpt, deg):
   return (refpt[0] + (math.cos(math.radians(deg)) * (pt[0] - refpt[0]))
      + (math.sin(math.radians(deg)) * (pt[1] - refpt[1])))

# Get the new y value of point pt (x, y) rotated about reference point
# refpt (x, y) by degrees clockwise
def rotatey(pt, refpt, deg):
   return (refpt[1] + (-math.sin(math.radians(deg))*(pt[0] - refpt[0]))
      + (math.cos(math.radians(deg)) * (pt[1] - refpt[1])))

# Get the new point (x, y) rotated about the reference point refpt (x, y)
# by degrees clockwise
def rotatep(pt, refpt, deg):
   return (int(round(rotatex(pt, refpt, deg))),
      int(round(rotatey(pt, refpt, deg))))

# The Shape class
# Each difference game piece is a subclass of shape
# Each has a different id and specific total amount of block (size)
# points represent the shape of the pieces
# corners represent the corners to the piece
class Shape:
   def __init__(self):
      self.id = None
      self.size = 1
    
   # Set the shapes' point (x, y) locations on the board
   def set_points(self, x, y):
      self.points = []
      self.corners = []

   # Create the shapes on the board, num = square index of the piece
   # pt = reference point
   def create(self, num, pt):
      self.set_points(0, 0)
      pm = self.points
      self.pts_map = pm
        
      self.refpt = pt
      x = pt[0] - self.pts_map[num][0]
      y = pt[1] - self.pts_map[num][1]
      self.set_points(x, y)
   
   # Returns the points that would be covered by a
   # shape that is rotated 0, 90, 180, of 270 degrees
   # in a clockwise direction.
   def rotate(self, deg):
      self.points = [rotatep(pt, self.refpt, deg) for pt in self.points]
      self.corners = [rotatep(pt, self.refpt, deg) for pt in self.corners]
        
   # Returns the points that would be covered if the shape
   # was flipped horizontally or vertically.
   # orientation = 'h' (horizontal) or 'v' (vertical)
   # NOTE: For this project, vertical flip isn't needed
   def flip(self, orientation):
      # flip horizontally
      def flip_h(pt):
         x1 = self.refpt[0]
         x2 = pt[0]
         x1 = (x1 - (x2 - x1))
         return (x1, pt[1])
        
      # flip the piece horizontally
      if orientation == 'h':
         self.points = [flip_h(pt) for pt in self.points]
         self.corners = [flip_h(pt) for pt in self.corners]

# List of all the 21 Blokus shape objects
class I1(Shape):
   def __init__(self):
      self.id = 'I1'
      self.size = 1

   def set_points(self, x, y):
      self.points = [(x, y)]
      self.corners = [(x + 1, y + 1), (x - 1, y - 1), (x + 1, y - 1),
         (x - 1, y + 1)]

class I2(Shape):
   def __init__(self):
      self.id = 'I2'
      self.size = 2

   def set_points(self, x, y):
      self.points = [(x, y), (x, y + 1)]
      self.corners = [(x - 1, y - 1), (x + 1, y - 1), (x + 1, y + 2),
         (x - 1, y + 2)]

class I3(Shape):
   def __init__(self):
      self.id = 'I3'
      self.size = 3

   def set_points(self, x, y):
      self.points = [(x, y), (x, y + 1), (x, y + 2)]
      self.corners = [(x - 1, y - 1), (x + 1, y - 1), (x + 1, y + 3),
         (x - 1, y + 3)]

class I4(Shape):
   def __init__(self):
      self.id = 'I4'
      self.size = 4

   def set_points(self, x, y):
      self.points = [(x, y), (x, y + 1), (x, y + 2), (x, y + 3)]
      self.corners = [(x - 1, y - 1), (x + 1, y - 1), (x + 1, y + 4),
         (x - 1, y + 4)]

class I5(Shape):
   def __init__(self):
      self.id = 'I5'
      self.size = 5

   def set_points(self, x, y):
      self.points = [(x, y), (x, y + 1), (x, y + 2), (x, y + 3), (x, y + 4)]
      self.corners = [(x - 1, y - 1), (x + 1, y - 1), (x + 1, y + 5),
         (x - 1, y + 5)]

class V3(Shape):
   def __init__(self):
      self.id = 'V3'
      self.size = 3

   def set_points(self, x, y):
      self.points = [(x, y), (x, y + 1), (x + 1, y)]
      self.corners = [(x - 1, y - 1), (x + 2, y - 1), (x + 2, y + 1),
         (x + 1, y + 2), (x - 1, y + 2)]

class L4(Shape):
   def __init__(self):
      self.id = 'L4'
      self.size = 4

   def set_points(self, x, y):
      self.points = [(x, y), (x, y + 1), (x, y + 2), (x + 1, y)]
      self.corners = [(x - 1, y - 1), (x + 2, y - 1), (x + 2, y + 1),
         (x + 1, y + 3), (x - 1, y + 3)]

class Z4(Shape):
   def __init__(self):
      self.id = 'Z4'
      self.size = 4

   def set_points(self, x, y):
      self.points = [(x, y), (x, y + 1), (x + 1, y + 1), (x - 1, y)]
      self.corners = [(x - 2, y - 1), (x + 1, y - 1), (x + 2, y),
         (x + 2, y + 2), (x - 1, y + 2), (x - 2, y + 1)]

class O4(Shape):
   def __init__(self):
      self.id = 'O4'
      self.size = 4

   def set_points(self, x, y):
      self.points = [(x, y), (x, y + 1), (x + 1, y + 1), (x + 1, y)]
      self.corners = [(x - 1, y - 1), (x + 2, y - 1), (x + 2, y + 2),
         (x - 1, y + 2)]

class L5(Shape):
   def __init__(self):
      self.id = 'L5'
      self.size = 5

   def set_points(self, x, y):
      self.points = [(x, y), (x, y + 1), (x + 1, y), (x + 2, y), (x + 3, y)]
      self.corners = [(x - 1, y - 1), (x + 4, y - 1), (x + 4, y + 1),
         (x + 1, y + 2), (x - 1, y + 2)]

class T5(Shape):
   def __init__(self):
      self.id = 'T5'
      self.size = 5

   def set_points(self, x, y):
      self.points = [(x, y), (x, y + 1), (x, y + 2), (x - 1, y), (x + 1, y)]
      self.corners = [(x + 2, y - 1), (x + 2, y + 1), (x + 1, y + 3),
         (x - 1, y + 3), (x - 2, y + 1), (x - 2, y - 1)]

class V5(Shape):
   def __init__(self):
      self.id = 'V5'
      self.size = 5

   def set_points(self, x, y):
      self.points = [(x, y), (x, y + 1), (x, y + 2), (x + 1, y), (x + 2, y)]
      self.corners = [(x - 1, y - 1), (x + 3, y - 1), (x + 3, y + 1),
         (x + 1, y + 3), (x - 1, y + 3)]

class N(Shape):
   def __init__(self):
      self.id = 'N'
      self.size = 5

   def set_points(self, x, y):
      self.points = [(x, y), (x + 1, y), (x + 2, y), (x, y - 1), (x - 1, y - 1)]
      self.corners = [(x + 1, y - 2), (x + 3, y - 1), (x + 3, y + 1),
         (x - 1, y + 1), (x - 2, y), (x - 2, y - 2)]

class Z5(Shape):
   def __init__(self):
      self.id = 'Z5'
      self.size = 5

   def set_points(self, x, y):
      self.points = [(x, y), (x + 1, y), (x + 1, y + 1), (x - 1, y),
         (x - 1, y - 1)]
      self.corners = [(x + 2, y - 1), (x + 2, y + 2), (x, y + 2),
         (x - 2, y + 1), (x - 2, y - 2), (x, y - 2)]

class T4(Shape):
   def __init__(self):
      self.id = 'T4'
      self.size = 4

   def set_points(self, x, y):
      self.points = [(x, y), (x, y + 1), (x + 1, y), (x - 1, y)]
      self.corners = [(x + 2, y - 1), (x + 2, y + 1), (x + 1, y + 2),
         (x - 1, y + 2), (x - 2, y + 1), (x - 2, y - 1)]

class P(Shape):
   def __init__(self):
      self.id = 'P'
      self.size = 5

   def set_points(self, x, y):
      self.points = [(x, y), (x + 1, y), (x + 1, y - 1), (x, y - 1), (x, y - 2)]
      self.corners = [(x + 1, y - 3), (x + 2, y - 2), (x + 2, y + 1),
         (x - 1, y + 1), (x - 1, y - 3)]

class W(Shape):
   def __init__(self):
      self.id = 'W'
      self.size = 5

   def set_points(self, x, y):
      self.points = [(x, y), (x, y + 1), (x + 1, y + 1), (x - 1, y),
         (x - 1, y - 1)]
      self.corners = [(x + 1, y - 1), (x + 2, y), (x + 2, y + 2),
         (x - 1, y + 2), (x - 2, y + 1), (x - 2, y - 2), (x, y - 2)]

class U(Shape):
   def __init__(self):
      self.id = 'U'
      self.size = 5

   def set_points(self, x, y):
      self.points = [(x, y), (x, y + 1), (x + 1, y + 1), (x, y - 1),
         (x + 1, y - 1)]
      self.corners = [(x + 2, y - 2), (x + 2, y), (x + 2, y + 2),
         (x - 1, y + 2), (x - 1, y - 2)]

class F(Shape):
   def __init__(self):
      self.id = 'F'
      self.size = 5

   def set_points(self, x, y):
      self.points = [(x, y), (x, y + 1), (x + 1, y + 1), (x, y - 1), (x - 1, y)]
      self.corners = [(x + 1, y - 2), (x + 2, y), (x + 2, y + 2),
         (x - 1, y + 2), (x - 2, y + 1), (x - 2, y - 1), (x - 1, y - 2)]

class X(Shape):
   def __init__(self):
      self.id = 'X'
      self.size = 5

   def set_points(self, x, y):
      self.points = [(x, y), (x, y + 1), (x + 1, y), (x, y - 1), (x - 1, y)]
      self.corners = [(x + 1, y - 2), (x + 2, y - 1), (x + 2, y + 1),
         (x + 1, y + 2), (x - 1, y + 2), (x - 2, y + 1), (x - 2, y - 1),
         (x - 1, y - 2)]

class Y(Shape):
   def __init__(self):
      self.id = 'Y'
      self.size = 5

   def set_points(self, x, y):
      self.points = [(x, y), (x, y + 1), (x + 1, y), (x + 2, y), (x - 1, y)]
      self.corners = [(x + 3, y - 1), (x + 3, y + 1), (x + 1, y + 2),
         (x - 1, y + 2), (x - 2, y + 1), (x - 2, y - 1)]
