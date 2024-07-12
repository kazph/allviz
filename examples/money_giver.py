import sys
sys.path.append("C:/Utvikling/Python/allviz")

import src.allviz as allviz
import statistics


def main():

    simulator = allviz.create_simulator()

    for i in range(0, 100):
        ac = simulator.create_actor()
        comp = MoneyAgent()
        comp.holdings = i
        simulator.add_component(ac, MoneyAgent, comp)
    
    simulator.add_system(distributer)
    simulator.add_system(printer)

    for step in range(0, 100):
        simulator.step()

@allviz.component
class MoneyAgent:
    holdings = 10

@allviz.system
def distributer(simultator: allviz.Simulator):
    res = simultator.quary_component(MoneyAgent)
    
    res.sort(key=lambda x: x[1].holdings)

    res[0][1].holdings += 1
    res[len(res) - 1][1].holdings -= 1

@allviz.system
def printer(simultator: allviz.Simulator):
    res = simultator.quary_component(MoneyAgent)
    holdnings = [x[1].holdings for x in res]
    print(f"max: {max(holdnings)} - min: {min(holdnings)}")

if __name__ == "__main__":
    main()