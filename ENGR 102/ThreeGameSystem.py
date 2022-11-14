
import time

class gameInstance:
    
    def __init__(self, userName):
        self.userName = userName
        self.startTime = time.time()
        
    
    
    
gInstance = gameInstance("hudson")

print(gInstance.userName,"spun up a game instance at second time", g.startTime)
        
        




