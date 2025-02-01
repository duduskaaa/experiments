from random import choice


width = 100
bank = ['y0', 'y1', 'y2', 'y3', 'y4', 'y5', 'y6', 'y7', 'y8', 'y9', 
				'b0', 'b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7', 'b8', 'b9', 
				'g0', 'g1', 'g2', 'g3', 'g4', 'g5', 'g6', 'g7', 'g8', 'g9', 
				'r0', 'r1', 'r2', 'r3', 'r4', 'r5', 'r6', 'r7', 'r8', 'r9',
							
							'y1', 'y2', 'y3', 'y4', 'y5', 'y6', 'y7', 'y8', 'y9', 
							'b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7', 'b8', 'b9', 
						  'g1', 'g2', 'g3', 'g4', 'g5', 'g6', 'g7', 'g8', 'g9', 
						  'r1', 'r2', 'r3', 'r4', 'r5', 'r6', 'r7', 'r8', 'r9',]
userCard = []
botCard = ['w1']

def CardSend(playerCard):
	randomCard = choice(bank)
	playerCard.append(randomCard)
	bank.remove(randomCard)

def CardCheck():
	while True:
		print(f"Ваши карты: {userCard}")
		userTurn = input("Выберите карту(Если у вас нет нужного, нажмите 0): ")
		if userTurn in userCard or userTurn == "0":
			return userTurn

def notBank():
	if not bank:
		print("Карты в банке кончились, все отбой!")

#Раздача карт
for _ in range(8):
	CardSend(userCard)
	CardSend(botCard)

#Границы
def border():
	print("=" * 80)

#Выбор первой случайной карты
gameCard = choice(bank)
print(f"Сейчас: {gameCard}")


while True:
	border()
	game = True

	
	##Проверка на отсутвие карт у игрока
	if not botCard:
		print("У Бота не осталось карт, он победил!")
		break

	botTurn = True
	while botTurn:
		notBank()
		for i in botCard:
			#Проверка на наличие карт
			if i[0] == gameCard[0] or i[1] == gameCard[1]:
				botCard.remove(i)
				gameCard = i
				botTurn = False
				print(f"Бот ходит: {i}")
				break
		#Если у Бота нет нужных карт
		if botTurn:
			CardSend(botCard)
			print(f"Бот берет карту")


	

	#Проверка на отсутвие карт у игрока
	if not userCard:
		print("Карты закончились \nТы победил!")
		border()
		break
	
	print(f"Сейчас: {gameCard}")
	
	notBank()
	#Выбор карты
	userTurn = CardCheck()
	#Проверка на пропуск хода
	if userTurn == "0":
		CardSend(userCard)
	
	#Проверка на правила игры и его описание
	if userTurn == "0":
		print("Добавление карты \r")
		continue
	elif userTurn[0] == gameCard[0] or userTurn[1] == gameCard[1]:
		userCard.remove(userTurn)
		print("Этот подходит, следующий ход")
	else:
		print("Выберите другую карту")
		continue
	
	#Смена карты
	gameCard = userTurn



