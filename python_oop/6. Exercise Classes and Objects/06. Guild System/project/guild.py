from typing import List

from project.player import Player


class Guild:

    def __init__(self, name):
        self.name = name
        self.players: List[Player] = []


    def assign_player(self, player: Player):
        if player.name not in self.players:
            player.guild = self.name
            self.players.append(player.name)
            return f"Welcome player {player.name} to the guild {self.name}"

        # player.guild = self.name
        if player.name in self.players and self.name != player.guild:
                return f"Player {player.name} is in another guild."
        return f"Player {player.name} is already in the guild."
        # player.guild = self.name
        # self.players.append(player)
        # return f"Welcome player {player} to the guild {self.name}"

    def kick_player(self, player_name: str):
        if player_name in self.players:
            self.players.remove(player_name)
            Player.guild = "Unaffiliated"
            return f"Player {player_name} has been removed from the guild."
        return f"Player {player_name} is not in the guild."

    def guild_info(self):
        return f"Guild: {guild.name}\n" \
               f"{player.player_info()}"


player = Player("George", 50, 100)
print(player.add_skill("Shield Break", 20))
print(player.player_info())
guild = Guild("UGT")
print(guild.assign_player(player))
print(guild.guild_info())


