import random

def get_kiss():
    """Return a randomly selected cute kiss emoticon or phrase.

    Used to add a playful, affectionate touch in CLI output.

    Returns:
        str: A randomly chosen kiss representation from a predefined list.
    """
    arts = [
        "😘 xoxo",
        "💋 <3",
        "❤️ Mwah!"
    ]
    return random.choice(arts)