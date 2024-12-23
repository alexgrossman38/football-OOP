# Model football stats / team

# Domain Analysis:
"""
- players
- equipment
- fans
- stadium
- field
- team
- coaches
- ref
- game
- stats

"""


# Which on these things should be classes, which of these things should be properties?

# can you represent the object with one value, or do you need multiple
#-> What are the data types?

"""
- players : class
    - Player(number, name, position, age, height, weight, number) : Player class
- equipment
    - helmets , shoulder pads clietes : list of strings
- fans : int
- stadium : str
- field : str
- team : class
- coaches : class
    - ccooach(pos, name, age )
- ref : str
- game : str
- stats : class

"""

# Functionality
"""
- add and remove players from teams
- add and remove coaches from teams
- calculate the stats
- get field, ref, stats info

"""

# Make Classes: player , Coach, Stats


class Stats():

    def __init__(self,points, catches, touchdowns, fumbles, interceptions, sacks):
        self.points = points
        self.catches = catches
        self.touchdowns = touchdowns
        self.fumbles = fumbles
        self.interceptions = interceptions
        self.sacks = sacks

    def __str__(self):
        return f"Stats(points={self.points}, catches={self.catches}, touchdowns={self.touchdowns}, fumbles={self.fumbles}, interceptions={self.interceptions}, sacks={self.sacks})"

    def set_points(self, points):
        """
        sets points
        """
        self.points = points

    def get_points(self):
        """
        gets points
        """
        return self.points

    def set_catches(self, catches):
        """
        sets catches
        """
        self.catches = catches

    def get_catches(self):
        """
        gets catches
        """
        return self.catches

    def set_touchdowns(self, touchdowns):
        """
        sets touchdowns
        """
        self.touchdowns = touchdowns

    def get_touchdowns(self):
        """
        gets touchdowns
        """
        return self.touchdowns

    def set_fumbles(self, fumbles):
        """
        sets fumbles
        """
        self.fumbles = fumbles

    def get_fumbles(self):
        """
        gets fumbles
        """
        return self.fumbles

    def set_interceptions(self, interceptions):
        """
        sets interceptions
        """
        self.interceptions = interceptions

    def get_interceptions(self):
        """
        gets interceptions
        """
        return self.interceptions

    def set_sacks(self, sacks):
        """
        sets sacks
        """
        self.sacks = sacks

    def get_sacks(self):
        """
        gets sacks
        """
        return self.sacks



class Player():
    def __init__ (self, number, name, position, age, height, weight):
        self.number = number
        self.name = name
        self.position = position
        self.age = age
        self.height = height
        self.weight = weight

    def __str__ (self):
        return f"Player(number={self.number}, name={self.name})"

    def set_number(self, number):
        """
        sets the number of the player
        """
        self.number = number

    def get_number(self):
        """
        gets the number of the player
        """
        return self.number

    def set_name(self, name):
        """
        sets the name of the player
        """
        self.name = name

    def get_name(self):
        """
        gets the name of the player
        """
        return self.name

    def set_position(self, position):
        """
        sets the position of the player
        """
        self.position = position

    def get_position(self):
        """
        gets the position of the player
        """
        return self.position

    def set_age(self, age):
        """
        sets the age of the player
        """
        self.age = age

    def get_age(self):
        """
        gets the age of the player
        """
        return self.age

    def set_height(self, height):
        """
        sets the height of the player
        """
        self.height = height

    def get_height(self):
        """
        gets the height of the player
        """
        return self.height

    def  set_weight(self, weight):
        """
        sets the weight of the player
        """
        self.weight = weight

    def get_weight(self):
        """
        gets the weight of the player
        """
        return self.weight


class Coach():
    def __init__ (self, position, name, age):
        self.position = position
        self.name = name
        self.age = age
    def __str__ (self):
        return f"Coach(position={self.position}, name={self.name})"
    def set_position(self, position):
        """
        sets the position of the coach
        """
        self.position = position
    def get_position(self):
        """
        gets the position of the coach
        """
        return self.position
    def set_name(self, name):
        """
        sets the name of the coach
        """
        self.name = name
    def get_name(self):
        """
        gets the name of the coach
        """
        return self.name
    def set_age(self, age):
        """
        sets the age of the coach
        """
        self.age = age
    def get_age(self):
        """
        gets the age of the coach
        """
        return self.age


class Team():

    def __init__ (self, name, players, coaches, stats):
        self.name = name
        self.players = players
        self.coaches = coaches
        self.stats = stats

    def __str__ (self):

        return f"Team(name={self.name})"

    def set_name(self, name):
        """
        sets the name of the team
        """
        self.name = name

    def get_name(self):
        """
        gets the name of the team
        """
        return self.name

    def set_players(self, players):
        """
        sets the players of the team
        """
        self.players = players

    def get_players(self):
        """
        gets the players of the team
        """
        return self.players

    def set_coaches(self, coaches):
        """
        sets the coaches of the team
        """
        self.coaches = coaches

    def get_coaches(self):
        """
        gets the coaches of the team
        """
        return self.coaches

    def set_stats(self, stats):
        """
        sets the stats of the team
        """
        self.stats = stats

    def get_stats(self):
        """
        gets the stats of the team
        """
        return self.stats


coach1 = Coach("Head Coach", "Dino", 40)
coach2 = Coach("Assistant Coach", "Sean", 35)

print(coach1)
print(coach2)



player1 = Player(10, "Manning", "quaterback", 34, 76, 210,)
player2 = Player(88, "Nicks", "receiver", 32, 77, 190)


# add stats
stats1 = Stats(10,1,1,1,1,1)

print(stats1)

print(player1)
print(player2)


# instantiate team
# team HAS players
# team has coaches
# team has tats
team1 = Team("Giants", [player1, player2], [coach1, coach2], stats1)

# what kind of functionality would be useful to have for team

print(team1)

