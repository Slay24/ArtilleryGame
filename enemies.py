

class Enemy():
	def __init__(self):
	    self.hp = 100
	    self.armour = 100
	    self.description = "An enemy of Canada that must not\
	    be allowed to live."
	    
	    
	
	def is_alive(self):
	    return self.hp > 0
    
    
class Armour(Enemy):
	
	def __init__(self):
		self.hp *= 1.25
		self.armour *= 1
		self.description = "The enemy apears to be hatches down in\
		some sort of armoured vehicle."
	
	def lose_armour(self, damage):
		self.armour -= damge
		return self.armour
			
class AntiAir(Enemy):
	def __init__(self):
		self.armour *= 0.5
		self.description = "It's a enemy air defence vehicle! This\
		should be top priority!"
		
    
		
        
class Dissmounts(Enemy):
	def __init__(self):
	    self.hp *= 0.5
	    self.armour = 0
	    self.description = "Enemy soldiers. Basic grunts."
	
	
        

class MBT(Armour):
    def __init__(self):
        pass

class Recce(Armour):
    def __init__(self):
        pass
