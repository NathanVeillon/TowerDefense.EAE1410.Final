

class Level02:

    def __init__(self):
        self.letter_map=[
        ['  ','SD','  ','  ','  ','  ','  ','  ','  ','  '],
        ['  ','PD','  ','PR','PR','PR','PR','PR','PR','PD'],
        ['  ','PD','  ','PU','  ','  ','  ','  ','  ','PD'],
        ['  ','PD','  ','PU','  ','PD','PL','PL','PL','PL'],
        ['  ','PD','  ','PU','  ','PD','  ','  ','  ','  '],
        ['  ','PD','  ','PU','  ','PD','  ','PR','PR','PD'],
        ['  ','PD','  ','PU','  ','PD','  ','PU','  ','PD'],
        ['  ','PD','  ','PU','  ','PD','  ','PU','  ','PD'],
        ['  ','PD','  ','PU','  ','PR','PR','PU','  ','PD'],
        ['  ','PR','PR','PU','  ','  ','  ','  ','  ','ED']
         ]

        self.enemy_waves = [
            {'num_enemies':10,'deploy_delay':100,'type':'BaseEnemy'},
            {'num_enemies':5,'deploy_delay':50,'type':'StrongEnemy'},
            {'num_enemies':4,'deploy_delay':50,'type':'QuickEnemy'}
        ]