class two_hundred_error(Exception):
	def __init__(self) -> None:
		super().__init__("The status wasn't 200")