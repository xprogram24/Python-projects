class Environment:
    def __init__(self):
        self.locations = {"A":"Dirty", "B":"Dirty"}
        self.vacuum_position = "A"

    def is_dirty(self):
        return self.locations[self.vacuum_position] == "Dirty"
    
    def clean(self):
        self.locations[self.vacuum_position] = "Clean"

    def move(self):
        if self.vacuum_position == "A":
            self.vacuum_position = "B"
        else:
            self.vacuum_position = "A"

class SimpleReflexAgent:
    def choose_action(self, env):
        if env.is_dirty():
            return "Suck"
        else :
            return "Move"
    
#simulation
env = Environment()
agent = SimpleReflexAgent()

for step in range(6):
    action = agent.choose_action(env)

    if action == "Suck":
        env.clean()
        print(f"step {step + 1}: Sucked dirt at {env.vacuum_position}")
    else:
        env.move()
        print(f"Step {step + 1} Moved to {env.vacuum_position}" )

    print("Current Enviroment:" , env.locations)
    print()