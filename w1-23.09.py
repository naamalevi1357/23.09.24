# start
import statistics

high: list[float] = []
mona: int = 0
two: float = 0
while True:
    highes: float = float(input("what is high? "))
    mona += 1
    if highes == -999:
        break
    if highes < 1.60 or highes > 3:
        continue
    high.append(highes)
    if highes > 2:
        two +=1

print(high)
print(f"amount of players {mona}")
if high:
    print(f"max players {max(high)} ")
    print(f" min players {min(high)} ")
    print(f"agv {statistics.mean(high)}")
    print(F" high frm two {two}")
    agv_high: float = statistics.mean(high)
    count = 0
    for i in range(len(high)):
        print(high[i])
        if high[i] > agv_high:
            count += 1
    print(f"  count {count}")

# stop
