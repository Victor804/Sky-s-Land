class Character(object):
    def __init__(self, x, y, health, damage, speed, regeneration, mana):
        self.x = x
        self.y = y
        self.health = health
        self.damage = damage
        self.speed = speed
        self.regeneration = regeneration
        self.mana = mana
        self.object = {}
