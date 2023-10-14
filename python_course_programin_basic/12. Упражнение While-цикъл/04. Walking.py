goal = 10000

all_steps = 0
#steps = input()
while True:
    steps = input()

    if steps == 'Going home':
        steps = int(input())
        all_steps += steps
        if all_steps >= goal:
            print(f"Goal reached! Good job!\n{all_steps - goal} steps over the goal!")
        break

    steps = int(steps)

    all_steps += steps

    if all_steps >= goal:
        print(f"Goal reached! Good job!\n{all_steps - goal} steps over the goal!")
        break

if all_steps < goal:
    print(f"{goal - all_steps} more steps to reach goal.")
# else:
#     print(f"Goal reached! Good job!\n{all_steps - goal} steps over the goal!")
