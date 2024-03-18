class Player:
    # guild = False

    def __init__(self, name, hp, mp):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.skills = {}
        self.guild = "Unaffiliated"

    def add_skill(self, skill_name, mana_cost):
        if skill_name in self.skills.keys():
            return "Skill already added"
        self.skills[skill_name] = mana_cost
        return f"Skill {skill_name} added to the collection of the player {self.name}"

    def player_info(self):
        haha = "".join(f'{k} - {v}' for k, v in self.skills.items())
        return f"Name: {self.name}\n"\
               f"Guild: {self.guild}\n"\
               f"HP: {self.hp}\n"\
               f"MP: {self.mp}\n"\
               f"==={haha}"



# hoho = Player("bobo", 100, 50)
# Player.add_skill(hoho, 100, 50)
# print(Player.player_info(hoho))
# print(hoho.add_skill(100, 50))


# haha = "===".join(f'{k} - {v}' for k, v in self.skills.items())
# f"Guild: {self.name}\n" \