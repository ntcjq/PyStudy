x = int(input("请输入一个整数："))
if x < 10 and x % 2 == 0:
    print("小 偶")
elif x < 100 or x == 101:
    print("中")
else:
    print("大")

while x < 100:
    x += 1
    print(x)

l = ["a", "b", "c", "d"]

for index in range(len(l)):
    print("index=%d" % index)
    print("ele=%s" % l[index])

for index, ele in enumerate(l):
    print("index=%d" % index)
    print("ele=%s" % l[index])