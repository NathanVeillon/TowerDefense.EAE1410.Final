

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
            {'num_enemies':10,'deploy_delay':100,'type':'BaseEnemy','speed':2,'health':15,'size':(20,20),
             'image_location':'Library\Assets\Enemies\BaseEnemy.png'},
            {'num_enemies':5,'deploy_delay':50,'type':'BaseEnemy','speed':1,'health':25,'size':(20,20),
             'image_location':'Library\Assets\Enemies\BaseEnemy.png'},
            {'num_enemies':4,'deploy_delay':50,'type':'BaseEnemy','speed':5,'health':2,'size':(20,20),
             'image_location':'Library\Assets\Enemies\BaseEnemy.png'}
        ]