class Player(object):
    def __init__(self, **kwargs):
        self.name = kwargs.get('name')
        self.surname = kwargs.get('surname')
        self.date_of_birth = kwargs.get('date_of_birth')
        self.current_team = kwargs.get('current_team')