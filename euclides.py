def euclides (a, b):
    if b==0: return a
    else: return euclides(b, a % b)
