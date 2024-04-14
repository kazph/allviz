import allviz

def main():

    simulator = allviz.create_simulator()

    actor = simulator.create_actor()
    actor.add_component(Wealth)
    actor.add_component(ProductionCapability)

    simulator.add_actor(actor)
    
    simulator.add_system(negotiate)
    simulator.add_system(bankruptize)
    
    simulator.run(steps = 100)


@allviz.component
class Wealth:
    wealth = 0

@allviz.component
class ProductionCapability:
    marginal_cost = 0.5
    fixed_cost = 200

@allviz.component
class ConsumptionCapability:
    value = 0.4

@allviz.system
def negotiate(env):
    for actor, (prod, cons) in env.get_components(ProductionCapability, ConsumptionCapability):
        print("HALLA!")

@allviz.system
def bankruptize(env):
    for actor, (prod) in env.get_components(ProductionCapability):
        if prod.marginal_cost * prod.q - prod.fixed_cost < 0:
            allviz.delete_actor(actor)