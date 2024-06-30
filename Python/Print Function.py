if __name__ == '__main__':
    n = int(input())


s = ''
for i in range(n):
    if i > 0:
        if n > i:
            s = s + str(i)
s = s + str(n)
print(str(s))
