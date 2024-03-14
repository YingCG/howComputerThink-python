import random


def band_notice(member, band_name):
    text = f"""
    Kia Ora,
    Greeting to you all,
    we will annouce our band {band_name}, our performer are: {member}
    We will have a performance coming in next month
    """
    return text


performer = ["Graham", "Alex", "Melenie"]

for member in performer:
    print(band_notice(member, band_name="Hello Rock"))
