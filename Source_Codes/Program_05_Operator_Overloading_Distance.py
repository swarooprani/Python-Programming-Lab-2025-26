class Distance:
    def __init__(self, f=0, i=0):
        self.feet = f
        self.inch = i

    def __add__(self, other):
        t = Distance()
        t.feet = self.feet + other.feet
        t.inch = self.inch + other.inch
        return t

    def __str__(self):
        self.feet = self.feet + (self.inch // 12)
        self.inch = self.inch % 12
        return f"{self.feet}:{self.inch}"


d1 = Distance(11, 16)
d2 = Distance(5, 8)

d3 = d1 + d2
print("Distance 1:",d1)
print("Distance 2:",d2)
print("Total Distance:")
print(d3)
