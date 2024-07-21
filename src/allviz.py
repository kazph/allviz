import uuid
import itertools
from typing import Type, TypeVar, Callable, ForwardRef

# The simulator is the core of the model
def create_simulator():
    return Simulator()


Simulator = ForwardRef("Simulator")
class Simulator:
    # A dictonary of componsnts and then actors
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

    def remove_actor(self, actor_id):
        for values in self.actors.values():
            values.pop(actor_id)

    def add_component(self, actor_id, component, component_instance = None):

        if component.__allviz_component_id__ not in self.actors:
            self.actors[component.__allviz_component_id__] = {}

        self.actors[component.__allviz_component_id__][actor_id] = component() if component_instance == None else component_instance
    
    def add_system(self, system):

        if hasattr(system, "__allviz_system__"):
            self.systems.append(system)
        else:
            print("ERROR: Added system does not have the @allviz.system decorator")
    
    def step(self):
        for system in self.systems:
            system(self)
    
    def run(self, max_steps = None, end_condition: Callable[[Simulator], bool] = lambda x: False):
        for i in range(0, min(max_steps, 1_000_000_000)): # Hand-coded max
            if end_condition(self) == True:
                break
            self.step()

    # This function retuns (actor, component) for all actors with component
    T = TypeVar('T')
    def quary_component(self, component: T) -> list[tuple[int, T]]:
        if not hasattr(component, "__allviz_component_id__"):
            print("ERROR: Passed argument is not an allviz component!")

        if component.__allviz_component_id__ not in self.actors:
            return []
        
        return list(self.actors[component.__allviz_component_id__].items())

    # This function return (actor, [components]) for all actors with at least one of the components
    def quary_components(self, components: list[Type[T]]) -> list[tuple[int, list[Type[T]]]]:
        pass

    # This function return (actor, [components]) for all actors with all components
    # TODO: High complexity
    def quary_components(self, components: list[Type[T]]) -> list[tuple[int, list[Type[T]]]]:
        def flatten(xss):
            return [x for xs in xss for x in xs]
        all_actors = set(flatten([[x[0] for x in self.quary_component(c)] for c in components]))
        
        full = []
        for c in components:
            c_list = []
            quary = self.quary_component(c)
            
            agent_components = self.actors[c.__allviz_component_id__]
            for a in all_actors:
                if a in agent_components:
                    c_list.append(agent_components[a])
                else:
                    c_list.append(None)
                
            full.append(c_list)
        
        complete_noned = list(zip(all_actors, list(zip(*full))))
        filtered_list = [
            element for element in complete_noned if all(item is not None for item in element[1])
        ]

        return filtered_list

# This decorator adds a uniqe int ID for each component
def component(cls):
    cls.__allviz_component_id__ = uuid.uuid4()
    return cls

# This decorator does add safety so only systems can be used in it
def system(func):
    func.__allviz_system__ = True
    return func