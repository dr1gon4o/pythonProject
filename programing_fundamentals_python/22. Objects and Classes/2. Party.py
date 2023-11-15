class Party:
    def __init__(self):
        self.people = []


party = Party()
command = input()

while command != 'End':
    command = input()


    party.people.append(command)

print(f"Going: {party.people}")
print(f"Total: {len(party.people)}")
