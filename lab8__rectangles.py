class Rectangle:
    def __init__(self, height, width):
        self.hei = height
        self.wid = width
    
    def area(self):
        return self.hei * self.wid
    
    def perimeter(self):
        return 2 * (self.hei + self.wid)

if __name__ == '__main__':
    h = float(input("enter the height: "))
    w = float(input("enter the width: "))
    r = Rectangle(h, w)
    print('Perimeter of rectangle  =', r.perimeter())
    print('Area of rectangle=', r.area())