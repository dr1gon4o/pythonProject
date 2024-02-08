from collections import deque

food = int(input())
# line = [int(el) for el in input().split(" ")]
queue = deque([int(el) for el in input().split(" ")])
print(max(queue))

for i in queue.copy():
    if food >= i:
        queue.popleft()
        food -= i
    else:
        print(f"Orders left:", *queue)
        break

# print(queue)
# print(line)
# print(max(queue))
if len(queue) == 0:
    print("Orders complete")
# print(f"Orders left: {queue}")
