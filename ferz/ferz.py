import queen_class as q
import Board as db

queen = q.Queen()
pole = db.Board()

queen.find_solution(0)
res = queen.getRes()

for j in range(pole.getN()):
    for k in range(pole.getN()):
        z=0
        x=j*pole.getSize()-4*pole.getSize()
        y=k*pole.getSize()-4*pole.getSize()
        z=j+k
        pole.square(x,y,z)
        if res[j][k] == 1:
            pole.ferz(j,k)
