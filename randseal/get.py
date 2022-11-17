import discord, random
from importlib import resources

def seal():
	"""
	Returns a `discord.File()` of a seal!
	"""
	sealrand = f"{random.randrange(1, 82)}"
	if len(sealrand) == 1:
		sussy = sealrand
		sealrand = "0" + f"{sussy}"
	with resources.open_binary('randseal', f'00{sealrand}.jpg') as fp:
		img = fp.read()
	file = discord.File(fp=img, filename=f"{sealrand}.png")
	return file