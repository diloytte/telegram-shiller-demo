import random

# Define shill functions as a dictionary
shill_functions = {
    0: lambda x: f"Looking at this \n\n{x}\n\nI think it is a good narative",
    1: lambda x: f"This \n\n{x}\n\nlooks like it should cook imo, but gamble still",
    2: lambda x: f"Saw some wallets aping this:\n\n{x}\n\ncould be something?",
    3: lambda x: f"Aped this\n\n{x}\n\ncould be a runner, gamble tho",
    4: lambda x: f"CTO on this it seems\n\n{x}\n\ni put some just in case",
    5: lambda x: f"Quant sent me this\n\n{x}\n\ndyor tho"
}

def get_shill_random(argument):
    """Choose a random shill function."""
    random_key = random.randint(0, len(shill_functions) - 1)
    return shill_functions[random_key](argument)

def get_shill_by_index(argument, index):
    """Choose a specific shill function by index."""
    if index in shill_functions:
        return shill_functions[index](argument)
    else:
        raise ValueError(f"Invalid index: {index}. Must be between 0 and {len(shill_functions) - 1}.")