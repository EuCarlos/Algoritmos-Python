A = []
B = []
C = []
D = []
for i in range(0, 5):
  A.append(int(input('Digite {}° valor de A: '.format(i + 1))))
for i in range(0, 5):
  B.append(int(input('Digite {}° valor de B: '.format(i + 1))))
for i in range(0, 5):
  C.append(int(input('Digite {}° valor de C: '.format(i + 1))))
D = A + B + C
for x in range(0, 15):
  print('D[{}] = {}'.format(x+1, D[x]))