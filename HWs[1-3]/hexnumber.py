class HexNumber:

    def __init__(self, string=''):
        if len(string) != 0:
            if string[-1] in '0123456789ABCDEF':
                if string[-1].isalpha():
                    if string[-1].isupper():
                        self.val = string[-1]
                        if len(string[:(len(string) - 1)]) != 0:
                            self.next = HexNumber(string[:(len(string) - 1)])
                        else:
                            self.next = None
                else:
                    self.val = string[-1]
                    if len(string[:(len(string) - 1)]) != 0:
                        self.next = HexNumber(string[:(len(string) - 1)])
                    else:
                        self.next = None
            else:
                self.val = '-1'
                self.next = None
        else:
            self.val = '-1'
            self.next = None

    def add(self, num):
        dct1 = {'0000': '0', '0001': '1', '0010': '2', '0011': '3', '0100': '4', '0101': '5', '0110': '6', '0111': '7',
                '1000': '8', '1001': '9', '1010': 'A', '1011': 'B', '1100': 'C', '1101': 'D', '1110': 'E', '1111': 'F'}
        dct2 = {'0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101', '6': '0110', '7': '0111',
                '8': '1000', '9': '1001', 'A': '1010', 'B': '1011', 'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'}
        numb1 = self
        numb2 = num

        while numb1.next or numb2.next:
            if numb1.next:
                numb1 = numb1.next
            if numb2.next:
                numb2 = numb2.next

        if numb1 and (numb1.val != '-1') and numb2 and (numb2.val != '-1'):
            numb1 = self
            numb2 = num
            lst = ['0']
            while numb1 or numb2:
                i = -1

                if numb1:
                    for it in dct2[numb1.val][::-1]:
                        if numb2:
                            lst.insert(0, str((int(it) + int(dct2[numb2.val][i]) + int(lst[0])) // 2))
                            lst[1] = str((int(it) + int(dct2[numb2.val][i]) + int(lst[1])) % 2)
                        else:
                            lst.insert(0, str((int(it) + int(lst[0])) // 2))
                            lst[1] = str((int(it) + int(lst[1])) % 2)
                        i -= 1
                lst.insert(1, ' ')
                if numb1:
                    numb1 = numb1.next
                if numb2:
                    numb2 = numb2.next

                if numb2 and (numb1 is None):
                    for it in dct2[numb2.val][::-1]:
                        lst.insert(0, str((int(it) + int(lst[0])) // 2))
                        lst[1] = str((int(it) + int(lst[1])) % 2)

            lst = (''.join(lst)).split()
            if len(lst[0]) < 4:
                lst[0] = ('0' * (4 - len(lst[0]))) + lst[0]

            for i, string in enumerate(lst):
                lst[i] = dct1[string]
            if int(lst[0]) == 0:
                del lst[0]
            return ''.join(lst)


num1 = HexNumber('BE37A8')
num2 = HexNumber('61AF790')
num3 = num1.add(num2)
print(num3)