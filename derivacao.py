fatores = []
def derivacao (n,p):
  if n > 1:
    if n % p == 0:
      fatores.append(p)
      return derivacao(n/p, p)
    else: return derivacao(n, p+1)
  print(fatores)

if __name__ == '__main__':
    derivacao(300,2)