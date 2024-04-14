import allviz

def main():

    simulator = allviz.create_simulator()

    actor = simulator.create_actor()
    simulator.add_component(actor, TestComponent)
    simulator.add_component(actor, TestComponent2)
    simulator.add_component(actor, TestComponent3)
    simulator.add_component(actor, TestComponent4)

    actor1 = simulator.create_actor()
    simulator.add_component(actor1, TestComponent3)

    actor2 = simulator.create_actor()
    simulator.add_component(actor2, TestComponent)
    simulator.add_component(actor2, TestComponent3)

    simulator.add_system(printer)
    simulator.add_system(printer1)
    simulator.add_system(printer2)
    # simulator.add_system(printer3) # Should fail without decorator

    simulator.step()
    simulator.step()
    simulator.step()
    simulator.step()
    simulator.step()


@allviz.component
class TestComponent:
    number = 1

@allviz.component
class TestComponent2:
    number = 2

@allviz.component
class TestComponent3:
    number = 3

@allviz.component
class TestComponent4:
    number = 4

@allviz.system
def printer(simultator):
    print("WOW!")

@allviz.system
def printer1(simultator):
    print("Hallo")

@allviz.system
def printer2(simultator):
    print("Verden")
    

if __name__ == "__main__":
    main()