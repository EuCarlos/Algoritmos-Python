# f) Ler três valores inteiros representados pelas variáveis A, B e C e apresentar os valores lidos dispostos em ordem crescente. Dica: utilizar tomada de decisão sequencial e as ideias trabalhadas nos exercícios "g" (propriedade distributiva) e "f' (troca de valores) do capítulo 3.
A = int(input('Informe valor de A: '))
B = int(input('Informe valor de B: '))
C = int(input('Informe valor de C: '))
if B > A and B > C:
  print(B, C, A)
else:
  if B >= A and B > C and A >= C:
    print(C, B, A)
  else:
    if B > A and B >= C and A <= C:
      print(A, C, B)
    else:
      if B > A and B <= C:
        print(A, B, C)
      else:
        if B < A and A < C:
          print(B, A, C)
        else: 
          if B < C and C <= A:
            print(B, C, A)
          else:
            print(A, B, C)