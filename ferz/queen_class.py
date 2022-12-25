class Queen:
    def __init__(self, N=8):
        self.N = N
        self.board = [[0 for i in range(N)] for j in range(N)]
        self.x = [[0 for i in range(N)] for j in range(N)]
        self.count = 0
        
    def check(self,i, j):
        for x in range(self.N):
            if self.board[x][j] == 1:
                return False
        for x,y in zip(range(i,-1,-1), range(j,-1,-1)):
            if self.board[x][y] == 1:
                return False
        for x,y in zip(range(i, -1, -1), range(j, self.N)):
            if self.board[x][y] == 1:
                return False
        return True

    def find_solution(self, col):
        if col>=self.N:
            self.count+=1
            if self.count == 1:
                for i in range(self.N):
                    for j in range(self.N):
                        if self.board[i][j] == 1:
                            self.x[i][j]=1
                for q in self.board:
                    print(q)
                print()
        for i in range(self.N):
            if self.check(col,i):
                self.board[col][i] = 1
                self.find_solution(col+1)
                self.board[col][i] = 0


    def getRes(self):
        return self.x
