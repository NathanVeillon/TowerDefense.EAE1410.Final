

class Level01:

    def __init__(self):
        self.letter_map=[
        ['SR','PR','PR','PD','  ','  ','  ','  ','  ','  '],
        ['  ','  ','  ','PR','PR','PR','PR','PR','PD','  '],
        ['  ','  ','  ','  ','  ','  ','  ','  ','PD','  '],
        ['EL','PL','PL','PL','  ','  ','  ','  ','PD','  '],
        ['  ','  ','  ','PU','  ','  ','  ','  ','PD','  '],
        ['  ','  ','  ','PU','  ','  ','  ','  ','PD','  '],
        ['  ','  ','  ','PU','  ','  ','  ','  ','PD','  '],
        ['  ','PR','PR','PU','  ','  ','  ','  ','PD','  '],
        ['  ','PU','  ','  ','  ','PD','PL','PL','PL','  '],
        ['  ','PU','PL','PL','PL','PL','  ','  ','  ','  ']
         ]

        self.enemy_waves = [
            {'BaseEnemy':25},
            {'BaseEnemy':25},
            {'BaseEnemy':25},
            {'BaseEnemy':25}
        ]
