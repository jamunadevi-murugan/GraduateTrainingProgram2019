def PyramidI(size):
    m=size
    for i in range(1,size+1):
        for j in range(0,m):
            print(end=" ")
        print(i*"**",end="")
        print(" ")
        m = m - 1
def PyramidR(n,intend=0):
    if n>0:
        PyramidR(n-1,intend+1)
        print(' '*intend,'**'*n)
PyramidR(7)
PyramidI(7)