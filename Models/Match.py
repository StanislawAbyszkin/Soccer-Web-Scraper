class Match(object):
    def __init__(self, **kwargs):
        self.date = kwargs.get('date')
        self.home_team = kwargs.get('home_team')
        self.away_team = kwargs.get('away_team')
        self.result = kwargs.get('result')
        self.player_list = kwargs.get('player_list')
        self.match_events_list = kwargs.get('match_events_list')
        self.gameType = kwargs.get('gameType')
