import pyautogui as pg
from time import sleep


message_box = pg.alert(text='Дарова, уважаемый клиент компании "NE NAEBALOVO & GAYS" ' , title='Не придумал', button='Я подпишу на вас имущество')

while True:
	user_box = pg.prompt(text='Твое имя?', title='lol', default='Еблан')
	if user_box:
		break
	else:
		message_box_danger = pg.alert(text='Нет нет, вам придется ответить ^-^' , title='УГРОЗА', button='Хорошо')

user_password = pg.password(text='Пароль какой-то напиши:', title='Окошко еблана', mask='*')
message_box = pg.alert(text='Все, дальше не придумал, иди на' , title='ЗА ГИ', button='Щя скину 1000тг')