class BWT(object):
    def __init__(self):
        return

    def encode(self,input):

        #cyclic shift matrix M
        matrix=[]
        for i in range(len(input)):
            cyclic=input[i:]+input[:i]
            matrix.append(cyclic)

        # lexical order sort
        matrix=sorted(matrix)

        # output : (last coulmn,row index of S)
        origin=matrix.index(input)
        lastString=""
        for s in matrix:
            lastString+=s[-1]
        self.lastString=lastString
        self.origin=origin
        return lastString, origin

    def decode(self,origin,lastString):
        n=len(lastString)
        X = sorted([(i, x) for i, x in enumerate(lastString)], key=itemgetter(1))

        T = [None for i in range(n)]
        for i, y in enumerate(X):
            j, _ = y
            T[j] = i

        Tx = [origin]
        for i in range(1, n):
            Tx.append(T[Tx[i - 1]])

        S = [lastString[i] for i in Tx]
        S.reverse()
        return ''.join(S)
