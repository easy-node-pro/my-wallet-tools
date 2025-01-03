import random

# Dictionary of animal names and their corresponding emojis
ANIMALS = {
    "monkey_face": "🐵",
    "monkey": "🐒",
    "gorilla": "🦍",
    "orangutan": "🦧",
    "dog": "🐶",
    "dog2": "🐕",
    "guide_dog": "🦮",
    "service_dog": "🐕‍🦺",
    "poodle": "🐩",
    "wolf": "🐺",
    "fox_face": "🦊",
    "raccoon": "🦝",
    "cat": "🐱",
    "cat2": "🐈",
    "black_cat": "🐈‍⬛",
    "lion": "🦁",
    "tiger": "🐯",
    "tiger2": "🐅",
    "leopard": "🐆",
    "horse": "🐴",
    "racehorse": "🐎",
    "unicorn": "🦄",
    "zebra": "🦓",
    "deer": "🦌",
    "bison": "🦬",
    "cow": "🐮",
    "ox": "🐂",
    "water_buffalo": "🐃",
    "cow2": "🐄",
    "pig": "🐷",
    "pig2": "🐖",
    "boar": "🐗",
    "pig_nose": "🐽",
    "ram": "🐏",
    "sheep": "🐑",
    "goat": "🐐",
    "dromedary_camel": "🐪",
    "camel": "🐫",
    "llama": "🦙",
    "giraffe": "🦒",
    "elephant": "🐘",
    "mammoth": "🦣",
    "rhinoceros": "🦏",
    "hippopotamus": "🦛",
    "mouse": "🐭",
    "mouse2": "🐁",
    "rat": "🐀",
    "hamster": "🐹",
    "rabbit": "🐰",
    "rabbit2": "🐇",
    "chipmunk": "🐿️",
    "beaver": "🦫",
    "hedgehog": "🦔",
    "bat": "🦇",
    "bear": "🐻",
    "polar_bear": "🐻‍❄️",
    "koala": "🐨",
    "panda_face": "🐼",
    "sloth": "🦥",
    "otter": "🦦",
    "skunk": "🦨",
    "kangaroo": "🦘",
    "badger": "🦡",
    "feet": "🐾",
    "turkey": "🦃",
    "chicken": "🐔",
    "rooster": "🐓",
    "hatching_chick": "🐣",
    "baby_chick": "🐤",
    "hatched_chick": "🐥",
    "bird": "🐦",
    "penguin": "🐧",
    "dove": "🕊️",
    "eagle": "🦅",
    "duck": "🦆",
    "swan": "🦢",
    "owl": "🦉",
    "dodo": "🦤",
    "feather": "🪶",
    "flamingo": "🦩",
    "peacock": "🦚",
    "parrot": "🦜",
    "frog": "🐸",
    "crocodile": "🐊",
    "turtle": "🐢",
    "lizard": "🦎",
    "snake": "🐍",
    "dragon_face": "🐲",
    "dragon": "🐉",
    "sauropod": "🦕",
    "t-rex": "🦖",
    "whale": "🐳",
    "whale2": "🐋",
    "dolphin": "🐬",
    "seal": "🦭",
    "fish": "🐟",
    "tropical_fish": "🐠",
    "blowfish": "🐡",
    "shark": "🦈",
    "octopus": "🐙"
}

def get_random_animal_emoji():
    """Returns a random animal emoji"""
    return random.choice(list(ANIMALS.values()))

def get_animal_emoji(animal_name):
    """Returns the emoji for a given animal name"""
    return ANIMALS.get(animal_name)