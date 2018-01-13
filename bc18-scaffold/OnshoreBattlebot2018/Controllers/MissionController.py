import random
import sys
import traceback

import battlecode as bc
from enum import Enum
from .StrategyController import *


class Missions(enum):
    Idle = 0 
    RandomMovement = 1 # Assign location to move to
    Mining = 2 # Assign location to mine
    FollowUnit = 3 # Assign Unit to follow
    Scout = 4 # Assign location to scout
    Patrol = 5 # Assign two locations to partrol 
    DestroyTarget = 6 # Assign unit to destroy
    DefendTarget = 7 # Assign unit to defend
    
class MissionTypes(enum):
    Worker = 0
    Healer = 1
    Combat = 2

# Controller that handles the creation and managment of missions
class MissionController:
    def __init__(self, gameController, strategyController):
        self.gameController = gameController
        self.strategyController = strategyController

        self.combatMissions = []
        self.healerMissions = []
        self.workerMissions = []

    # Adds a new mission created by outside source
    def AddMission(self,missionType,missionInfo):
        if missionType == MissionTypes.Worker.:
            self.workerMissions.append(mission)
        elif missionType == MissionTypes.Healer:
            self.healerMissions.append(mission)
        else:
            self.combatMissions.append(mission)

    #Pops the highest priority mission for the given unit off the queue and returns it
    def GetMission(self,unit):
        # Return a mission based on the type of unit
        # The mission will be based on the current strategy
        
        if unit.unit_type == bc.UnitType.Worker:
            if len(self.workerMissions) > 0:
                print("Worker mission assigned")
                return self.workerMissions.pop(0)
            else:
                return self.__CreateNewWorkerMission__()
        elif unit.unit_type == bc.UnitType.Healer:
            if len(self.healerMissions) > 0:
                print("Healer mission assigned")
                self.__CreateNewHealerMission__()
            else:
                return self.healerMissions.pop(0)
        else:
            if len(self.combatMissions) > 0:
                print("Combat mission assigned")
                return self.combatMissions.pop(0)
            else: 
                return __CreateNewCombatMission__(self)

    def __CreateNewWorkerMission__(self):
        #Determine what mission to assign based on the current strategy
        if self.strategyController.unitStrategy == self.strategyController.UnitStrategies.Default:
            chance = random.randint(0,100)
            if chance > 50:    
                return Missions.RandomMovement
            elif chance > 25:
                return Missions.Mining
            else:
                return Missions.Idle
    
    def __CreateNewHealerMission__(self):

        if self.strategyController.unitStrategy == self.strategyController.UnitStrategies.Default:
            chance = random.randint(0,100)
            if chance > 50:
                return Missions.FollowUnit
            else:
                return Missions.Idle
    
    def __CreateNewCombatMission__(self):

        if self.strategyController.unitStrategy == self.strategyController.UnitStrategies.Default:
            chance = random.randint(0,100)
            if chance > 50:
                return Missions.Scout
            elif chance > 25:
                return Missions.Patrol
            else:
                return Missions.Idle
