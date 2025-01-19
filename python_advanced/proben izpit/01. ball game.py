from collections import deque

# strengths = deque(map(int, input().split()))
# accuracies = deque(map(int, input().split()))
strengths = [int(element) for element in input().split(' ')]
accuracies = deque([int(element) for element in input().split(' ')])


goals_scored = 0

while strengths and accuracies:
    strength = strengths[-1]
    accuracy = accuracies[0]

    sum_value = strength + accuracy

    if sum_value == 100:
        strengths.pop()
        accuracies.popleft()
        goals_scored += 1
    elif sum_value < 100:
        if strength < accuracy:
            strengths.pop()
        elif strength > accuracy:
            accuracies.popleft()
        else:
            strengths[-1] = (strength + accuracy)
            # strengths.append(strength + accuracy)
            accuracies.popleft()
    else:
        strengths[-1] -= 10
        accuracies.append(accuracies.popleft())

if goals_scored == 3:
    print("Paul scored a hat-trick!")
elif goals_scored == 0:
    print("Paul failed to score a single goal.")
elif goals_scored > 3:
    print("Paul performed remarkably well!")
else:
    print("Paul failed to make a hat-trick.")

if goals_scored > 0:
    print(f"Goals scored: {goals_scored}")

if strengths:
    print(f"Strength values left: {', '.join(map(str, strengths))}")

if accuracies:
    print(f"Accuracy values left: {', '.join(map(str, accuracies))}")


