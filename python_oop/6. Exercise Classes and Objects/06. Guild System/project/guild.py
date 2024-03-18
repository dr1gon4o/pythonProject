from typing import List

from project.player import Player


class Guild:

    def __init__(self, name):
        self.name = name
        self.players: List[Player] = []


    def assign_player(self, player: Player):
        if player not in self.players:
            player.guild = self.name
            self.players.append(player)
            return f"Welcome player {player.name} to the guild {self.name}"

        # player.guild = self.name
        if player in self.players and self.name != player.guild:
                return f"Player {player.name} is in another guild."
        return f"Player {player.name} is already in the guild."
        # player.guild = self.name
        # self.players.append(player)
        # return f"Welcome player {player} to the guild {self.name}"

    def kick_player(self, player_name: str):

        try:
            player = next(filter(lambda p: p.name == player_name, self.players))
        except StopIteration:
            return f"Player {player_name} is not in the guild."

        # if player_name == player.name and player in self.players:
        #     self.players.remove(player)
        #     Player.guild = "Unaffiliated"
        #     return f"Player {player_name} has been removed from the guild."
        # return f"Player {player_name} is not in the guild."
        self.players.remove(player)
        Player.guild = "Unaffiliated"
        return f"Player {player_name} has been removed from the guild."

    def guild_info(self):
        player_infoo = "\n".join(a.player_info() for a in self.players)
        return f"Guild: {guild.name}\n" \
               f"{player_infoo}"


player = Player("George", 50, 100)
print(player.add_skill("Shield Break", 20))
print(player.player_info())
guild = Guild("UGT")
print(guild.assign_player(player))
print(guild.guild_info())
# print(guild.kick_player("George"))
# print(guild.kick_player("George"))
# print(guild.kick_player("Georg"))
