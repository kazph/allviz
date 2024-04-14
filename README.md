# Allviz
Allviz is a simple, modular and flexible framework for building agent-based models.

*Agent-based models* (ABM)  is a computer simulation that mimics the behavior of a system by simulating the actions and interactions of individual entities within that system. Therfore, the key concepts in ABM is the following:
- **Agents**: These are the building blocks of the model. They can represent real-world things like people, animals, cells, or even companies. Each agent is autonomous, meaning it can make its own decisions based on a set of rules.
- **Interactions** Agents interact with each other and their environment according to the rules programmed into the model. These interactions can be simple or complex, and they can have a big impact on the overall behavior of the system.

Using ABM you can often se that the complex behavior of the entire system arises from the simple interactions of the individual agents. ABMs are used to study all sorts of complex systems, from traffic flow to disease outbreaks to economic markets. They are a powerful tool for understanding how these systems work and for predicting how they might behave under different conditions.


## Modeling with Allviz
Then, we will go forward with explaining how you can models ABM's using Allviz.

Allviz is based on an Entity-Component-System (ECS), an software architectural pattern commonly used in video game development for representing game objects. It separates the data (entity and components) from the behavior (systems). If you are formiliar with these concepts then Allviz also should be easy to understand.

However, in the next section we will go trough how you can model ABM in allviz.

## Seperation of Agents, Components and Systems
In Allviz there is the seperation of Agents, Components and Systems. 

Firsly, an agent is an induvidal in the simulation and is represented by an integer. An agents has a set of components witch include the data of the agents. Therefore; an agent is a set of components. 

To model the interaction between the agents we use systems. You can register mulitple systems witch run at each step of the simulation. In the systems you can get all information about the envirement and make the agents take decitions. This is the place where you model the interaction.

This setup makes your projects more modular, seperating data and behavoiur, and also offers more flexibility where new components and systems dont affect old components and systems, and also can be more preforment then other methods. However, it can be a steeper learning curve and somewhat more difficult to debug. 


*Thanks for reading, and hope you enjoy!*