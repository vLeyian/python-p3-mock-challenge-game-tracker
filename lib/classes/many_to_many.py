class Game:
    def __init__(self, title):
        self.title = title
        
        self._players = []
        self._results = []

    @property
    def title(self):
        return self._title 
    
    @title.setter
    def title(self, title):
        if isinstance(title, str) and len(title) and not hasattr(self, 'title'):
            self._title = title

    def results(self):
        return self._results

    def players(self):
        return list(set(self._players))

    def average_score(self, player):
        total = 0
        num_plays = 0

        for result in self.results():
            if result.player is player:
                total += result.score
                num_plays += 1

        return total/num_plays

class Player:
    def __init__(self, username):
        self.username = username

        self._games = []
        self._results = []

    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self, username):
        if isinstance(username, str) and 2 <= len(username) <= 16:
            self._username = username

    def results(self):
        return self._results

    def games_played(self):
        return list(set(self._games))

    def played_game(self, game):
        return game in self.games_played()
        
    def num_times_played(self, game):
        games_played = [result.game for result in self.results()]
        return games_played.count(game)

class Result:
    all = []

    def __init__(self, player, game, score):
        self.player = player
        self.game = game
        self.score = score

        self.game._players.append(self.player)
        self.game._results.append(self)

        self.player._games.append(self.game)
        self.player._results.append(self)

        Result.all.append(self)

    @property
    def score(self):
        return self._score
    
    @score.setter
    def score(self, score):
        if isinstance(score, int) and 1 <= score <= 5000 and not hasattr(self, 'score'):
            self._score = score

    @property
    def player(self):
        return self._player 
    
    @player.setter
    def player(self, player):
        if isinstance(player, Player):
            self._player = player

    @property
    def game(self):
        return self._game
    
    @game.setter
    def game(self, game):
        if isinstance(game, Game):
            self._game = game

    
    