import random
import itertools

# The simulator is the core of the model
def create_simulator():
    return Simulator()


class Simulator:
    # A dictonary of actorIDs and their components
    actors = {}

    # A list of systems to run in a simulation step.
    systems = []
    
    # A counter to ensure uniqe IDs to actors
    id_counter = itertools.count()

    # Returns a uniqe number of the actor and registers it in
    # the 'actors' dictonary
    def create_actor(self):
        id = next(self.id_counter)
        return id

    def add_component(self, actor_id, component):

        if component.__allviz_component_id__ not in self.actors:
            self.actors[component.__allviz_component_id__] = {}

        self.actors[component.__allviz_component_id__][actor_id] = component()

        print(self.actors)
    
    def add_system(self, system):

        if hasattr(system, "__allviz_system__"):
            self.systems.append(system)
        else:
            print("ERROR: Added system does not have the @allviz.system decorator")
    
    def step(self):
        for system in self.systems:
            system(None)

# This decorator adds a uniqe int ID for each component
def component(cls):
    cls.__allviz_component_id__ = random.randint(0, 4_294_967_295)
    return cls

# This decorator does add safety so only systems can be used in it
def system(func):
    func.__allviz_system__ = True
    return func