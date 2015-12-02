

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
            {'num_enemies':10,'deploy_delay':10,'type':'BaseEnemy','speed':1,'health':25,'size':(20,20),
             'image_location':'Library\Assets\Enemies\BaseEnemy.png'},
            {'num_enemies':2,'deploy_delay':50,'type':'BaseEnemy','speed':1,'health':25,'size':(20,20),
             'image_location':'Library\Assets\Enemies\BaseEnemy.png'},
            {'num_enemies':10,'deploy_delay':10,'type':'BaseEnemy','speed':1,'health':25,'size':(20,20),
             'image_location':'Library\Assets\Enemies\BaseEnemy.png'}
        ]