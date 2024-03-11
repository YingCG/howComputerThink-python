# to generate an email using function and loop:
import random


def generate_band_name():
    adjectives = ["Electric", "Mystic", "Groovy", "Dazzling", "Epic"]
    genres = ["Rock", "Funk", "Pop", "Jazz", "Blues"]
    return f"The {random.choice(adjectives)} {random.choice(genres)}"


def band_notice(member, band_name):
    BLUE = "\033[34m"
    RESET = "\033[0m"
    text = f"""Dear {BLUE}{member}{RESET},

We are thrilled to announce that our band, "{band_name}," 
will be performing live on {BLUE}Saturday, 15 October 2023{RESET}, 
at the Grand Music Hall (123 Main Street, Your City). 
The show will start at {BLUE}8:00 PM{RESET}. 

Don't miss the chance to experience an unforgettable night of music and entertainment. 
Invite your friends and family for an incredible musical journey!

See you at the show!

Best regards,
{band_name}
"""

    return text


guest_list = [
    "Graham",
    "Alex",
    "Karen",
    "Van",
]

for member in guest_list:
    current_band_name = generate_band_name()
    print(band_notice(member, current_band_name))
