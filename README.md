# anonymous_chat
Анонимный чат, который работает на:  
Django, Aiogram, PythonTelegramBot.   

Суть бота в том, что это анонимный чат, где смс отправляется в телеграм бота, юзер шифруется через соль.   
Смс выводится в django приложении на главной странице.  
В файле bot.py(anonymous_chat/chat/management/commands/bot.py). 
Изменить констаны на ваши:   
TOKEN = 'YOU TOKEN'.  
SALT = 'YOU SALT'.  

<img width="961" alt="Снимок экрана 2022-04-09 в 23 06 36" src="https://user-images.githubusercontent.com/15955132/162589990-623f24ca-afe6-44e7-b697-4c1cd2405b1b.png">
