import sys
sys.path.append("C:/Utvikling/Python/allviz")

import src.allviz as allviz
import random as rand
from itertools import combinations
from enum import Enum


def main():

    simulator = allviz.create_simulator()

    for i in range(0, 1000):
        ac = simulator.create_actor()
        comp = RockPaperSizzorAgent()
        comp.mode = i % 3
        simulator.add_component(ac, RockPaperSizzorAgent, comp)
    
    simulator.add_system(matchmake)
    simulator.add_system(analyze)
    simulator.add_system(reproduce)

    for step in range(0, 5000):
        simulator.step()

class Mode(Enum):
    ROCK = 0
    PAPER = 1
    SIZZOR = 2

class MatchResult(Enum):
    TIDE = 0
    WIN = 1
    LOSS = 2

    NOT_PLAYED = 100

@allviz.component
class RockPaperSizzorAgent:
    mode: Mode
    result : MatchResult = MatchResult.NOT_PLAYED


@allviz.system
def matchmake(simultator: allviz.Simulator):
    res = simultator.quary_component(RockPaperSizzorAgent)

    competitors = [x[1] for x in res]
    indexes = list(range(0, len(competitors)))
    half = len(indexes)//2

    rand.shuffle(indexes)

    for p1, p2 in zip(indexes[:half], indexes[half:]):
        strategy1 = res[p1][1].mode
        strategy2 = res[p2][1].mode
        
        if strategy1 == strategy2:
            res[p1][1].result = MatchResult.TIDE
            res[p2][1].result = MatchResult.TIDE
        else:
            win_lookup = { 0: Mode.SIZZOR, 1: Mode.ROCK, 2: Mode.PAPER }

            if win_lookup[strategy1] == strategy2:
                res[p1][1].result = MatchResult.WIN
                res[p2][1].result = MatchResult.LOSS
            else:
                res[p1][1].result = MatchResult.LOSS
                res[p2][1].result = MatchResult.WIN


@allviz.system
def reproduce(simultator: allviz.Simulator):
    res = simultator.quary_component(RockPaperSizzorAgent)

    # Remove all who has lost
    # Double all who has won
    # Leave tide alone

    for actor_id, comp in res:

        if comp.result == MatchResult.WIN:
            ac = simultator.create_actor()
            new = RockPaperSizzorAgent()
            new.mode = comp.mode
            simultator.add_component(ac, RockPaperSizzorAgent, new)

        elif comp.result == MatchResult.LOSS:
            simultator.remove_actor(actor_id)  
    

@allviz.system
def analyze(simultator: allviz.Simulator):
    res = simultator.quary_component(RockPaperSizzorAgent)
    types = [x[1].mode for x in res]

    num_0 = types.count(0)
    num_1 = types.count(1)
    num_2 = types.count(2)

    print(f"Rock: {num_0} - Paper: {num_1} - Sizzor: {num_2}")

    

if __name__ == "__main__":
    main()