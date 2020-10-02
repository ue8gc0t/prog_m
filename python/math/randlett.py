while True:	
	import random
	letters = ("Б В Д К Л М Н П Р С Т")
	letter = letters.split()
	i = random.randint(0,len(letter)-1)
	print(letter[i])
	input()