# -*- coding: utf-8 -*-
"""OlimpUSE.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1BPcyUMyjzajLOBiRkX_k_sde1u9P3P8f

ДЗ от 25 октября: ЕГЭ-17: 186, 216, 220, 228, 240, 258, 284, 285, 289;  
ЕГЭ-26: 2-6, 21, 225
"""

with open('17-5.txt') as ff:
    s = ff.read().split()
    a = [int(x) for x in s]

cnt = 0
m = []

for i in range(len(a)-1):
  if ((a[i]%10 == 5) and (a[i+1]%10 == 5)):
    cnt+=1
    m.append(a[i]+a[i+1])

print(cnt, max(m))

a = []
sum = 0
with open('17-1.txt') as ff:
    s = ff.read().split()
    for x in s:
      a.append(int(x))
      sum += int(x)

armean = sum/len(a)
cnt = 0
m = []

for i in range(len(a)-1):
  if ((a[i] > armean or a[i+1] > armean) and (abs(a[i]) % 10 == 3 or abs(a[i+1]) % 10 == 3)):
    cnt+=1
    m.append(a[i]+a[i+1])

print(cnt, max(m))

a = []
sum = 0
with open('17-1.txt') as ff:
    s = ff.read().split()
    for x in s:
      a.append(int(x))
      sum += int(x)

armean = sum/len(a)
cnt = 0
m = []

for i in range(len(a)-1):
  if ((a[i] > armean and a[i+1] < armean) or (a[i] < armean and a[i+1] > armean)):
    cnt+=1
    m.append(a[i]+a[i+1])

print(cnt, max(m))

a = []
sum = 0
with open('17-1.txt') as ff:
    s = ff.read().split()
    for x in s:
      a.append(int(x))
      sum += int(x)

armean = sum/len(a)
cnt = 0
m = []

for i in range(len(a)-2):
  if ((min(a[i], min(a[i+1], a[i+2])) < armean) and (abs(a[i]) % 3 == 0 or abs(a[i+1]) % 3 == 0 or abs(a[i+2] % 3 == 0))):
    cnt+=1
    m.append(a[i]+a[i+1]+a[i+2])

print(cnt, max(m))

a = []
sum = 0
with open('17-1.txt') as ff:
    s = ff.read().split()
    for x in s:
      a.append(int(x))
      sum += int(x)

armean = sum/len(a)
cnt = 0
m = []
helpar = []

for i in range(len(a)-2):
  helpar = [a[i], a[i+1], a[i+2]]
  helpar.sort()
  if ((helpar[0] < armean and helpar[1] < armean) and (('6' in str(a[i])) or ('6' in str(a[i+1])) or ('6' in str(a[i+2])))):
    cnt+=1
    m.append(a[i]+a[i+1]+a[i+2])

print(cnt, max(m))

cnteven = 0
cntodd = 0

maxeven = -1
mineven = 10001

maxodd = -1
minodd = 10001

with open('17-257.txt') as ff:
    s = ff.read().split()
    for x in s:
      if int(x) % 2 == 0:
        maxeven = max(maxeven, int(x))
        mineven = min(mineven, int(x))
        cnteven += 1
      if int(x) % 2 == 1:
        maxodd = max(maxodd, int(x))
        minodd = min(minodd, int(x))
        cntodd += 1

if (maxeven > maxodd):
  print(cnteven, mineven)
else:
  print(cntodd, minodd)

a = []
maxel = -1
with open('17-282.txt') as ff:
    s = ff.read().split()
    for x in s:
      a.append(int(x))
      if int(x) % 41 == 0:
        maxel = max(maxel, int(x))


cnt = 0
m = []

for i in range(len(a)-1):
  if (a[i]+a[i+1] < maxel):
    cnt+=1
    m.append(a[i]+a[i+1])

print(cnt, max(m))

a = []
minel = 10001
with open('17-282.txt') as ff:
    s = ff.read().split()
    for x in s:
      a.append(int(x))
      if int(x) % 37 == 0:
        minel = min(minel, int(x))


cnt = 0
m = []

for i in range(len(a)-1):
  num1 = 0
  num2 = 0
  nummin = 0

  for x in str(a[i]):
    num1 += int(x)

  for x in str(a[i+1]):
    num2 += int(x)

  for x in str(minel):
    nummin += int(x)

  if ((num1 == nummin) or (num2 == nummin)):
    cnt+=1
    m.append(a[i]+a[i+1])

print(cnt, min(m))

def functrans(num, k):
  final = ''
  if (num == 0): final = '0'
  #print(num)
  while (num > 0):
    #print("swag")
    final = str(num%k) + final
    num = num // k

  #print("endswag")

  return int(final)

def func1(helpar):
  flag = False
  for x in helpar:
    if (abs(x) % 10 == 3):
      flag = True

  return flag

def func2(helpar):
  flag = True
  for x in helpar:
    n = functrans(abs(int(x)), 7)
    if (n % 10 == 3):
      flag = False

  return flag

a = []
with open('17-288.txt') as ff:
    s = ff.read().split()
    for x in s:
      a.append(int(x))

cnt = 0
m = []
helpar = []

for i in range(len(a)-3):
  helpar = [a[i], a[i+1], a[i+2], a[i+3]]
  helpar.sort()
  if (func1(helpar) and func2(helpar)):
    cnt+=1
    m.append(helpar[3] - helpar[0])

print(cnt, min(m))

def functrans(num, k):
  final = ''

  while (num != 0):
    final = str(num%k) + final
    num = num // k

  return int(final)

x = input()
print(functrans(int(x), 7) % 10)

a = []
n = 0
k = 0
with open('26-k1.txt') as ff:
    s = ff.read().split()
    n = int(s[0])
    k = int(s[1])
    a = [int(s[x]) for x in range(2, n)]

a.sort(reverse=True)

sum = 0
for x in range(k):
  sum += a[x]
print(a[k], int(sum*0.2))

a = [1, 6, 7, 5]
a.sort(reverse=True)
a