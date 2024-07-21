import allviz

def main():

    simulator = allviz.create_simulator()

    c = TestComponent()
    c.number = 3

    actor0 = simulator.create_actor()
    simulator.add_component(actor0, TestComponent, c)
    # simulator.add_component(actor0, IdentificationComponent)

    actor1 = simulator.create_actor()
    simulator.add_component(actor1, TestComponent)
    simulator.add_component(actor1, IdentificationComponent)

    actor2 = simulator.create_actor()
    simulator.add_component(actor2, IdentificationComponent)

    simulator.add_system(printer)
    
    simulator.step()
    simulator.step()
    simulator.step()
    simulator.step()


@allviz.component
class TestComponent:
    number = 1

@allviz.component
class IdentificationComponent:
    pass


@allviz.system
def printer(simultator: allviz.Simulator):

    res = simultator.quary_components([TestComponent, IdentificationComponent])

    for a, (c, i) in res:
        print(f"Agent: {a}, number: {c.number}")
        c.number += 1

if __name__ == "__main__":
    main()