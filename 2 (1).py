class Zherebez(object):
    def __init__(self,ar,point):
        from datetime import datetime

        start_time = datetime.now()


        a = [[0 for j in range(ar)] for i in range(ar)]
        matriza = [[0 for j in range(ar * ar)] for i in range(ar * ar)]

        k = 1
        for i in range(ar):
            for j in range(ar):
                a[i][j] = k
                k += 1



        def isNormal(i, j):
            if i >= 0 and j >= 0 and i < ar and j < ar:
                return True
            else:
                return False

        s = []

        for i in range(0, ar):
            for j in range(0, ar):
                if isNormal(i + 1, j + 2):
                    matriza[i * ar + j][(i + 1) * ar + (j + 2)] = 1
                if isNormal(i - 1, j - 2):
                    matriza[i * ar + j][(i - 1) * ar + (j - 2)] = 1
                if isNormal(i + 1, j - 2):
                    matriza[i * ar + j][(i + 1) * ar + (j - 2)] = 1
                if isNormal(i - 1, j + 2):
                    matriza[i * ar + j][(i - 1) * ar + (j + 2)] = 1
                if isNormal(i + 2, j + 1):
                    matriza[i * ar + j][(i + 2) * ar + (j + 1)] = 1
                if isNormal(i - 2, j - 1):
                    matriza[i * ar + j][(i - 2) * ar + (j - 1)] = 1
                if isNormal(i + 2, j - 1):
                    matriza[i * ar + j][(i + 2) * ar + (j - 1)] = 1
                if isNormal(i - 2, j + 1):
                    matriza[i * ar + j][(i - 2) * ar + (j + 1)] = 1


        visited = []

        voavrat = 0

        def Sosedi(point):
            t = matriza[point - 1]

            sosediu = []
            for i in range(0, ar * ar):
                if t[i] == 1:
                    sosediu.append(i + 1)

            return sosediu

        def isStoped(vist):
            for i in range(0, ar * ar):
                if (i + 1) not in vist:
                    s = Sosedi(i + 1)

                    Flag = True
                    for x in Sosedi(i + 1):
                        if x not in vist:
                            Flag = False

                            break
                    if Flag and ((i + 1) not in Sosedi(vist[len(vist) - 1])):
                        return True
            return False

        def chngnei(point, visit):
            sosedi = Sosedi(point)
            a = [[] for i in range(len(sosedi))]
            for i in range(len(sosedi)):
                a[i].append(sosedi[i])
                newsosedi = Sosedi(sosedi[i])
                k = len(newsosedi)
                for j in newsosedi:
                    if j in visit:
                        k = k - 1
                a[i].append(k)
            a.sort(key=lambda x: x[1])
            res = []
            for x in a:
                res.append(x[0])
            return res

        visited.append(point)
        bad = [[] for i in range(ar * ar + 1)]

        while True:
            if len(visited) == ar * ar:


                self.hody= visited
                break
            Flag = True
            for x in chngnei(point, visited):
                if (x not in visited) and (x not in bad[point]):
                    visited.append(x)
                    Flag = False
                    break
            # isStoped(visited)

            if False:
                print('Чупапи муняня')
                bad[visited[len(visited) - 2]].append(visited[len(visited) - 1])
                bad[visited[len(visited) - 1]].clear()
                del visited[len(visited) - 1]
                voavrat = voavrat + 1
            else:
                if Flag:
                    bad[visited[len(visited) - 2]].append(point)
                    del visited[len(visited) - 1]
                    voavrat = voavrat + 1
                    bad[point].clear()

                    try:
                        point = visited[len(visited) - 1]
                    except:
                        print(visited)
                        exit()

                else:
                    point = visited[len(visited) - 1]


        print(datetime.now() - start_time)

        """Constructor"""
    def getLoshadinyaSila(self):
        return self.hody



#Создаем элемент класса Жеребец первый параметр длина доски второй коорда
mikroLoshad = Zherebez(8,63)
#получить от коня ходы функцией лошадиная сила
print(mikroLoshad.getLoshadinyaSila())
