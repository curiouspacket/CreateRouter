
"""
Start of project to Instantiate a router creation, goal is from CSV or source of truth
"""
#class router(object):
    
    #def __init__(self, name, vendor):
     #   self.name = name
      #  self.vendor = vendor
      
my_int={'Loopback': {'Loop1': '10.20.30.1', 'Loop2': '10.20.30.2'}, 'Gigabit' :{'Giga1': '10.10.10.1', 'Giga2': '10.10.20.1'}}  

 
def interfaces(intConfig):
    for interType, interNum in intConfig.items():
        print('\n - Interfaces: ')
        for key in interNum:
            #print('\n' + key + ':', interNum[key])
            interName = key
            interIP = interNum[key]
            print(interName)
            print(interIP)

      
interfaces(my_int)
