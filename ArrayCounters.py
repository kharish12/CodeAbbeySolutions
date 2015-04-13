#input
# 301 20
# 7 4 8 16 16 15 20 1 13 4 12 14 1 13 16 7 1 4 18 18 6 13 8 4 17 1 13 17 10 20 17 16 4 4 12 20 19 11 1 11 14 12 5 15 5 20 1 5 4 19 2 10 11 10 13 8 11 6 4 20 6 20 15 9 4 6 8 2 17 8 13 11 20 18 5 4 17 6 8 1 4 10 10 15 19 3 2 9 9 6 8 14 6 3 2 9 9 10 11 5 17 4 15 17 1 20 20 18 5 8 18 8 17 8 3 16 10 4 5 18 9 13 12 15 16 13 3 4 3 14 9 19 17 4 16 18 3 15 15 8 3 13 15 20 1 18 16 11 1 20 9 10 12 20 4 7 13 7 11 15 20 20 13 17 3 9 15 6 4 10 13 6 2 8 5 3 5 20 13 6 20 1 15 12 20 19 18 12 5 9 7 5 8 20 2 11 8 16 16 11 5 8 16 7 16 1 9 20 1 2 5 20 2 20 11 2 19 9 14 3 18 20 8 6 19 10 16 6 5 11 17 10 19 12 17 14 13 5 14 13 6 19 13 8 18 4 9 16 13 3 19 10 2 7 15 1 16 10 6 1 1 2 11 19 14 7 13 7 11 6 19 17 4 12 4 2 15 13 17 8 15 16 17 17 2 12 17 18 1 3 18 2 5 9 1 19 15 13 5 5 19

(m, n) = (input().split())

counters = {}

for x in input().split():
  if x in counters:
    counters[x] += 1
  else:
    counters[x] = 1
keys = sorted(counters)
for k in keys:
  print(counters[k], "", end="")

# (m, n) = (input().split())
#
# x = input().split()
#
# for i in range(0, int(n)):
#   print(x.count(str(i+1)), "", end="")