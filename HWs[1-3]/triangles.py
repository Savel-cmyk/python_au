import sys


class Triangle:
    def __init__(self, args):
        self.coords_of_sides = Point(args)
        self.areas = []
        self.finding_of_areas()
        self.maximums_of_areas = ''
        list_of_the_biggest_area = self.init_of_the_bigger()
        if list_of_the_biggest_area[0] != -1:
            for i in list_of_the_biggest_area:
                for side in self.coords_of_sides.lst[i]:
                    self.maximums_of_areas += str(side[0]) + ' ' + str(side[1]) + ' '
                self.maximums_of_areas += '\n'

    def finding_of_areas(self):
        for tri in self.coords_of_sides.lst:
            self.areas.append(abs(0.5 * (tri[0][0] * tri[1][1] + tri[1][0] * tri[2][1] + tri[2][0] * tri[0][1] -
                                         tri[1][0] * tri[0][1] - tri[2][0] * tri[1][1] - tri[0][0] * tri[2][1])))

    def init_of_the_bigger(self):
        if len(self.areas) > 0:
            maxi = [0]
            boole = True
            for i in range(1, len(self.areas)):
                if self.areas[maxi[0]] < self.areas[i]:
                    maxi.clear()
                    maxi.append(i)
                    boole = False
                elif self.areas[maxi[0]] == self.areas[i]:
                    maxi.append(i)
                elif self.areas[maxi[0]] > self.areas[i]:
                    boole = False
            if boole:
                return [-1]
        return maxi


class Point:
    def __init__(self, args):
        self.lst = []
        for arg in args:
            self.lst.append(arg.rstrip('\n').split())
        i = 0
        while i < len(self.lst):
            if len(self.lst[i]) != 6:
                del self.lst[i]
                continue
            self.init_of_the_coords(i)
            i += 1

    def init_of_the_coords(self, ind):
        prev = []
        i = 0
        while i <= len(self.lst[ind]):
            if len(prev) == 2:
                del self.lst[ind][i-2:i]
                i -= 1
                self.lst[ind].insert((i - 1), [])
                for j in prev:
                    self.lst[ind][i - 1] += [int(j)]
                prev.clear()
                continue
            if i != len(self.lst[ind]):
                prev.append(self.lst[ind][i])
            i += 1


def main(src, dst):
    with open(src, 'r') as inf:
        list_of_triangles = Triangle(inf.readlines())
    with open(dst, 'a') as inf:
        inf.write(list_of_triangles.maximums_of_areas)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])