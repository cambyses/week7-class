class Player:

  def __init__(self, name, jersey_number):
    self.name = name
    self.number = jersey_number



class Team:

  def __init__(self, team_name):
    self.name = team_name
    self.players = []

  def add_player(self, player):
    self.players.append(player)

  def display():
    print(self.name)
    print("-------------------------")
    for player in self.players:
      print("{0:<4} {1}".format(player.number, player.name))


player1 = Player("Jeff", 21)
player2 = Player("Hannah", 44)
player3 = Player("Nick", 16)
player4 = Player("Philip", 16)
player5 = Player("Christoper", 22)
player6 = Player("David", 10)

home_team = Team("Chicago")
away_team = Team("New York")

# TO DO: Add players to each team
# then display each team's roster

