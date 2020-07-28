#Анаграммы
import sys

s1 = list(sys.stdin.readline().strip())
s2 = list(sys.stdin.readline().strip())

C = {}
D = {}
a = 1

if len(s1) == len(s2):
  for i in range(0, len(s1)):
    C[s1[i]] = 0
    D[s2[i]] = 0

  for i in range(0, len(s1)):
    C[s1[i]] += 1
    D[s2[i]] += 1

  if len(s1) == len(s2):
    for i in range(0, len(s1)):
      if C[s1[i]] != D[s1[i]]:
        a = 0
else:
  a = 0

print(a)