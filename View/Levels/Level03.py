

class Level03:

    def __init__(self):
        self.letter_map=[
        ['SR','PR','PR','PR','PR','PR','PR','PR','PR','PD'],
        ['  ','  ','  ','  ','  ','  ','  ','  ','  ','PD'],
        ['  ','PR','PR','PR','PR','PR','PR','PD','  ','PD'],
        ['  ','PU','  ','  ','  ','  ','  ','PD','  ','PD'],
        ['  ','PU','  ','PR','PR','PD','  ','PD','  ','PD'],
        ['  ','PU','  ','PU','  ','ED','  ','PD','  ','PD'],
        ['  ','PU','  ','PU','  ','  ','  ','PD','  ','PD'],
        ['  ','PU','  ','PU','PL','PL','PL','PL','  ','PD'],
        ['  ','PU','  ','  ','  ','  ','  ','  ','  ','PD'],
        ['  ','PU','PL','PL','PL','PL','PL','PL','PL','PL']
         ]

        self.enemy_waves = [
            {'num_enemies':10,'deploy_delay':50,'type':'BaseEnemy','speed':1,'health':40,'size':(30,30),
             'image_location':'Library\Assets\Enemies\BaseEnemy.png'},
            {'num_enemies':20,'deploy_delay':25,'type':'BaseEnemy','speed':2,'health':30,'size':(20,20),
             'image_location':'Library\Assets\Enemies\BaseEnemy.png'},
            {'num_enemies':30,'deploy_delay':30,'type':'BaseEnemy','speed':2.5,'health':20,'size':(40,40),
             'image_location':'Library\Assets\Enemies\BaseEnemy.png'},
            {'num_enemies':1,'deploy_delay':50,'type':'BaseEnemy','speed':1,'health':500,'size':(60,60),
             'image_location':'Library\Assets\Enemies\BaseEnemy.png'}

        ]