import random
import matplotlib.pyplot as mat


def data_analysis():
    data = dict()
    curr_worker = dict()

    with open(r'C:\Users\savel\OneDrive\Рабочий стол\data.txt', 'r') as inf:
        k = inf.readlines()

        for j in range(len(k)):
            k[j] = k[j][0:-1]
        data.update({c: [] for c in k[0].split(', ')})

    for el in k[1:]:
        data['date'].append(el.split(', ')[0])

        if int(el.split(', ')[1]) not in data['resource']:
            data['resource'].append(int(el.split(', ')[1]))

        if int(el.split(', ')[2]) not in data['staff id']:
            data['staff id'].append(int(el.split(', ')[2]))

        data['count'].append(int(el.split(', ')[3]))

        if el.split(', ')[2] not in curr_worker.keys():
            curr_worker.update({el.split(', ')[2]: [[el.split(', ')[0], el.split(', ')[3]]]})
        else:
            curr_worker[el.split(', ')[2]].append([el.split(', ')[0], el.split(', ')[3]])
        '''
        matplotlib.pyplot.figure()
        matplotlib.pyplot.plot(data['date'], data['count'], 'r')
        matplotlib.pyplot.xlabel('x')
        matplotlib.pyplot.ylabel('y')
        matplotlib.pyplot.show()
        '''

    p = list()
    for key in curr_worker.keys():
        p.append(key)
    j = 0
    fig, axes = mat.subplots(nrows=1, ncols=len(p))
    print(curr_worker)
    for axe in axes:
        axe.set(title=p[j], xlabel='date', ylabel='count')
        axe.plot([curr_worker[p[j]][i][0] for i in range(len(curr_worker[p[j]]))],
                 [int(curr_worker[p[j]][n][1]) for n in range(len(curr_worker[p[j]]))], 'r')
        j += 1

    fig.tight_layout()
    mat.show()


def main():
    with open(r'C:\Users\savel\OneDrive\Рабочий стол\data.txt', 'w') as inf:
        inf.write("date, resource, staff id, count\n")

        for i in range(1, 13):
            inf.write("2021-{}, {}, {}, {}\n".format('0' + str(i) if i < 10 else str(i), random.randint(1, 10),
                                                     random.randint(20, 22), random.randint(0, 100)))
    data_analysis()


if __name__ == '__main__':
    main()
