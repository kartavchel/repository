import pygame
from time import sleep
from random import*
#Імпортування бібліотек
pygame.init()

w = pygame.display.set_mode((1300, 700))#створення об'єкту екрану
w.fill((0, 230, 250))
clock = pygame.time.Clock()#створення годинника



class Area():#створення класу Area
    def __init__(self, x=0, y=0, width=10, height=10, color=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.fill_color = (30, 144, 255)
        if color:
            self.fill_color = color

    def color(self, new_color):
        self.fill_color = new_color

    def fill(self):
        pygame.draw.rect(w, self.fill_color, self.rect)


class Picture(Area):#створення підкласу Picture
    def __init__(self, filename, x=0, y=0, width=10, height=10, color=None):
        Area.__init__(self, x, y, width, height, color)
        self.image = pygame.image.load(filename)

    def draw_picture(self):
        w.blit(self.image, (self.rect.x, self.rect.y))


class Label(Area):#створення підкласу Label
    def set_text(self, text, fsize=12, text_color=(255, 255, 255)):
        self.text = text
        self.image = pygame.font.SysFont('verdana', fsize).render(text, True, text_color)

    def draw_text(self, shift_x=0, shift_y=0):
        w.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))
        
        

menu_background = Picture('pics/city1.png',0,0,0,0)
# створення об'єктів для екрану меню
menu_start = Picture('pics/button_play.PNG', 567, 300, 166, 66)
menu_settings = Picture('pics/button_settings.png', 504, 400, 292, 66)
menu_exit=Picture('pics/button_exit.PNG', 568, 500, 164, 66)
napys = Picture('pics/напис.png',250,-250,800,100)

# створення об'єктів для екрану налаштування
sett_guide = Picture('pics/guide.png', 568, 117.2, 164, 66)
sett_plot = Picture('pics/plot.png', 568, 250.4, 164, 66)
sett_back = Picture('pics/button_back.png',565, 516.8, 164, 66)
change_controls=Picture('pics/controls.png',568,383.6,164,66)

#Створення об'єктів для екрану сюжету
plot_back = Picture('pics/button_back.png',565, 400, 164, 66)


plot_text1 = Label(360,170,180,40)
plot_text2 = Label(360,200,180,40)
plot_text3 = Label(360,230,180,40)
plot_text4 = Label(360,260,180,40)
plot_text5 = Label(360,290,180,40)



plot_text1.set_text("В 2100 році на землю напали інопланетяни. Україна",20)
plot_text2.set_text("стала першою країною , яка розробила зброю для",20)
plot_text3.set_text("протидії інопланетянам. Багато міст було зруйновано,",20)
plot_text4.set_text("і вам треба застосувати нову зброю для захисту",20)
plot_text5.set_text("Землі та заробітку грошей для відновлення України.",20)

#Створеня об'єктів для еркану гайду
guide_back = Picture('pics/button_back.png',565, 400, 164, 66)


guide_text1 = Label(360,70,180,40)
guide_text2 = Label(360,100,180,40)
guide_text3 = Label(360,130,180,40)
guide_text4 = Label(360,160,180,40)
guide_text5 = Label(360,190,180,40)
guide_text6 = Label(360,220,180,40)
guide_text7 = Label(360,250,180,40)
guide_text8 = Label(360,280,180,40)

guide_text1.set_text("Щоб почати грати зайдіть в меню рівнів",20)
guide_text2.set_text("та виберіть рівень. На рівнях будуть різні круги,",20)
guide_text3.set_text("які збільшуються з часом. Треба наводити курсор миші ",20)
guide_text4.set_text("і натискати кнопку для того щоб круг зменшмвся і перемістився",20)
guide_text5.set_text("якщо ви не встигаєте цього зробити то вам віднімають очко.",20)
guide_text6.set_text("Пропускаєте п'ять і більше кругів - програєте.",20)
guide_text7.set_text("При навеленні на червоний круг натискайте q або 1,",20)
guide_text8.set_text("на зелений w або 2, на синій e або 3(в залежності від керування.)",20)
#Створення об'єктів для екрану зміни керування
change_controls_text=Label(550,220,0,0)
change_controls_text.set_text('Змінити керування',20)
change_controls_back=Picture('button_back.png',567,450,166,66)
change_controls_button=Picture("controls1.PNG",567,350,166,66)
#Створення об'єктів для екрану після натискання "Грати"
play_contgame = Picture("pics/contgame.png",502, 300, 296, 56)
play_newgame = Picture("pics/newgame.png",568, 400, 166, 66)
play_back = Picture("pics/button_back.png",568, 500, 164, 66)

#створення об'єктів для екрану перевірки створення нової гри
sure_check_yes = Picture('pics/yes.png', 450, 400, 106, 66)
sure_check_no = Picture('pics/no.png', 700, 400, 106, 66)

sure_check_text = Label(375,170,180,40)
sure_check_text.set_text('Ви дійсно хочете почати спочатку?',30)

#створення об'єктів для меню вибора рівнів
level1=Picture('pics/level1.png',550,150,50,50)
level2=Picture('pics/level2.png',675,150,50,50)
level3=Picture('pics/level3.png',550,275,50,50)
level4=Picture('pics/level4.png',675,275,50,50)
level5=Picture('pics/level5.png',550,400,50,50)
level6=Picture('pics/level6.png',675,400,50,50)

levels_to_menu = Picture('pics/to_menu.png', 450, 600, 166, 66)
levels_to_city = Picture('pics/to_city.png', 666, 600, 166, 66)

#створення об'єктів для екрану міста
city_back = Picture("pics/button_back.png",450, 500, 164, 66)
city_background = Picture("pics/city1.png",0,0,0,0)
dump_money = Picture('pics/dump.png', 700, 500, 166, 66)
dumped_money_text = Label(750,450,0,0)

#Створення об'єктів для першого рівня
lvl1_score=-2
lvl1_counter=0

#Створення об'єктів для другого рівня
lvl2_score=-3
lvl2_counter=0

#Створення об'єктів для третього рівня
lvl3_score=-3
lvl3_counter=0

#Створення об'єктів для четвертого рівня
lvl4_score=-4
lvl4_counter=0

#Створення об'єктів для п'ятого рівня
lvl5_score=-5
lvl5_counter=0

#Створення об'єктів для шостого рівня
lvl6_score=-6
lvl6_counter=0

#Створення об'єктів для рівнів 
level_background = Picture("pics/level_background.png",0,0,300,200)
to_levels=Picture("pics/button_back.png",500,350,164,66)

#Створення об'єктів для екрану програшу
losing_text=Label(550,250,0,0)
losing_text.set_text("Ви програли!",40)
lose_restart=Picture('pics/pause_restart.png',620,325,50,50)
lose_to_levels=Picture('pics/pause_to_levels.png',702,325,50,50)

#Створення об'єктів для екрану перемоги
winning_text=Label(550,250,0,0)
winning_text.set_text("Ви перемогли!",40)
win_restart=Picture('pics/pause_restart.png',620,325,50,50)
win_to_levels=Picture('pics/pause_to_levels.png',702,325,50,50)



#Створення ворогів та їх анімацій
red_enemy1=Picture("pics/enemy_red1.png", randint(0,1250),randint(0,650),50,50)
red_enemy_counter1 = 0
def red_enemy_func1(red_enemy_counter1):
    if red_enemy_counter1==0:
        red_enemy1.image = pygame.image.load('pics/enemy_red1.png')
    elif red_enemy_counter1==24:
        red_enemy1.image = pygame.image.load('pics/enemy_red2.png')    
    elif red_enemy_counter1==48:
        red_enemy1.image = pygame.image.load('pics/enemy_red3.png')
    elif red_enemy_counter1==72:
        red_enemy1.image = pygame.image.load('pics/enemy_red4.png')
    elif red_enemy_counter1==96:
        red_enemy1.image = pygame.image.load('pics/enemy_red5.png')
        
    if red_enemy_counter1==120:
        return 0
    else:
        return red_enemy_counter1+1

red_enemy2=Picture("pics/enemy_red1.png", randint(0,1250),randint(0,650),50,50)
red_enemy_counter2 = 0
def red_enemy_func2(red_enemy_counter2):
    if red_enemy_counter2==0:
        red_enemy2.image = pygame.image.load('pics/enemy_red1.png')
    elif red_enemy_counter2==24:
        red_enemy2.image = pygame.image.load('pics/enemy_red2.png')    
    elif red_enemy_counter2==48:
        red_enemy2.image = pygame.image.load('pics/enemy_red3.png')
    elif red_enemy_counter2==72:
        red_enemy2.image = pygame.image.load('pics/enemy_red4.png')
    elif red_enemy_counter2==96:
        red_enemy2.image = pygame.image.load('pics/enemy_red5.png')
        
    if red_enemy_counter2==120:
        return 0
    else:
        return red_enemy_counter2+1
        
red_enemy3=Picture("pics/enemy_red1.png", randint(0,1250),randint(0,650),50,50)
red_enemy_counter3 = 0
def red_enemy_func3(red_enemy_counter3):
    if red_enemy_counter3==0:
        red_enemy3.image = pygame.image.load('pics/enemy_red1.png')
    elif red_enemy_counter3==24:
        red_enemy3.image = pygame.image.load('pics/enemy_red2.png')    
    elif red_enemy_counter3==48:
        red_enemy3.image = pygame.image.load('pics/enemy_red3.png')
    elif red_enemy_counter3==72:
        red_enemy3.image = pygame.image.load('pics/enemy_red4.png')
    elif red_enemy_counter3==96:
        red_enemy3.image = pygame.image.load('pics/enemy_red5.png')
        
    if red_enemy_counter3==120:
        return 0
    else:
        return red_enemy_counter3+1
        
green_enemy1=Picture("pics/enemy_green1.png", randint(0,1250),randint(0,650),50,50)
green_enemy_counter1 = 0
def green_enemy_func1(green_enemy_counter1):
    if green_enemy_counter1==0:
        green_enemy1.image = pygame.image.load('pics/enemy_green1.png')
    elif green_enemy_counter1==24:
        green_enemy1.image = pygame.image.load('pics/enemy_green2.png')    
    elif green_enemy_counter1==48:
        green_enemy1.image = pygame.image.load('pics/enemy_green3.png')
    elif green_enemy_counter1==72:
        green_enemy1.image = pygame.image.load('pics/enemy_green4.png')
    elif green_enemy_counter1==96:
        green_enemy1.image = pygame.image.load('pics/enemy_green5.png')
        
    if green_enemy_counter1==120:
        return 0
    else:
        return green_enemy_counter1+1
        
green_enemy2=Picture("pics/enemy_green1.png", randint(0,1250),randint(0,650),50,50)
green_enemy_counter2 = 0
def green_enemy_func2(green_enemy_counter2):
    if green_enemy_counter2==0:
        green_enemy2.image = pygame.image.load('pics/enemy_green1.png')
    elif green_enemy_counter2==24:
        green_enemy2.image = pygame.image.load('pics/enemy_green2.png')    
    elif green_enemy_counter2==48:
        green_enemy2.image = pygame.image.load('pics/enemy_green3.png')
    elif green_enemy_counter2==72:
        green_enemy2.image = pygame.image.load('pics/enemy_green4.png')
    elif green_enemy_counter2==96:
        green_enemy2.image = pygame.image.load('pics/enemy_green5.png')
        
    if green_enemy_counter2==120:
        return 0
    else:
        return green_enemy_counter2+1
        
blue_enemy1=Picture("pics/enemy_blue1.png", randint(0,1250),randint(0,650),50,50)
blue_enemy_counter1 = 0
def blue_enemy_func1(blue_enemy_counter1):
    if blue_enemy_counter1==0:
        blue_enemy1.image = pygame.image.load('pics/enemy_blue1.png')
    elif blue_enemy_counter1==24:
        blue_enemy1.image = pygame.image.load('pics/enemy_blue2.png')    
    elif blue_enemy_counter1==48:
        blue_enemy1.image = pygame.image.load('pics/enemy_blue3.png')
    elif blue_enemy_counter1==72:
        blue_enemy1.image = pygame.image.load('pics/enemy_blue4.png')
    elif blue_enemy_counter1==96:
        blue_enemy1.image = pygame.image.load('pics/enemy_blue5.png')
        
    if blue_enemy_counter1==120:
        return 0
    else:
        return blue_enemy_counter1+1
    
blue_enemy2=Picture("pics/enemy_blue1.png", randint(0,1250),randint(0,650),50,50)
blue_enemy_counter2 = 0
def blue_enemy_func2(blue_enemy_counter2):
    if blue_enemy_counter2==0:
        blue_enemy2.image = pygame.image.load('pics/enemy_blue1.png')
    elif blue_enemy_counter2==24:
        blue_enemy2.image = pygame.image.load('pics/enemy_blue2.png')    
    elif blue_enemy_counter2==48:
        blue_enemy2.image = pygame.image.load('pics/enemy_blue3.png')
    elif blue_enemy_counter2==72:
        blue_enemy2.image = pygame.image.load('pics/enemy_blue4.png')
    elif blue_enemy_counter2==96:
        blue_enemy2.image = pygame.image.load('pics/enemy_blue5.png')
        
    if blue_enemy_counter2==120:
        return 0
    else:
        return blue_enemy_counter2+1

#Створення об'єктів для паузи
pause_cont=Picture('pics/pause_cont.png',537.5,325,50,50)
pause_restart=Picture('pics/pause_restart.png',620,325,50,50)
pause_to_levels=Picture('pics/pause_to_levels.png',702,325,50,50)
        
#змінна яка зберігає у собі керування 
controls=1 #1-q,w,e. 2-1,2,3.
#змінні для створеня ворогів на рівнях
wait1=0
wait2=0
wait3=0
wait4=0
wait5=0
wait6=0

#змінна для запуску екрану програшу
lost=False

#змінна для екрану перемоги
win=False

#змінна для екарну паузи
pause=False

#змінна для переходу між екранами
screen = 'menu'

#ігровий цико
while True:
    #відмальовування фону
    menu_background.draw_picture()
    
    #відкриття тестового файлу який зберігає керування та вигруження інформації з нього
    f = open('controls_save.txt', 'r')
    controls = f.read() #1-q,w,e. 2-1,2,3.
    f.close()
    controls = int(controls)
    
    
    #відкриття тестового файлу який зберігає кількість грошей та вигруження інформації з нього
    f = open('money_save.txt','r')
    money = f.read()
    f.close()
    money=int(money)
    
    #відкриття тестового файлу який зберігає кількість вкладених грошей та вигруження інформації з нього
    f = open('dump_money_save.txt','r')
    dumped_money = f.read()
    f.close()
    dumped_money = int(dumped_money)
    
    #встановлення тексту для екрану міста
    dumped_money_text.set_text(str(dumped_money)+'/1000',20)
    
    #встановлення фону в залежності від кількості вкладених грошей
    if dumped_money<500:
        city_background = Picture("pics/city1.png",0,0,0,0)
        menu_background = Picture("pics/city1.png",0,0,0,0)
    elif dumped_money>500 and dumped_money<1000:
        city_background = Picture("pics/city2.png",0,0,0,0)
        menu_background = Picture("pics/city2.png",0,0,0,0)
    elif dumped_money>1000:
        city_background = Picture("pics/city3.png",0,0,0,0)
        menu_background = Picture("pics/city3.png",0,0,0,0)
    

    if screen == 'menu':
        #відмальовування спрайтів для екрану меню
        menu_background.draw_picture()
        menu_start.draw_picture()
        menu_settings.draw_picture()
        menu_exit.draw_picture()
        napys.draw_picture() 
        

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:#перевірка на те куди натиснуто
                x, y = event.pos
                if menu_start.rect.collidepoint(x, y):#якщо натиснуто в області кнопки грати перекадаї на екран game_start
                    screen = 'game_start'
                elif menu_settings.rect.collidepoint(x, y):#якщо натиснуто в області кнопки грати перекадаї на екран налаштувань
                    screen = 'settings'            
                
                elif menu_exit.rect.collidepoint(x, y):#якщо натиснуто в області кнопки вихід виход із гри
                    pygame.quit()

            if event.type == pygame.QUIT:#виходить із гри якщо натиснуто хрестик на вікні гри
                pygame.quit()
                
            
            if event.type == pygame.MOUSEMOTION:#перевіряє рух миші і якщо попадає на кнопку то робить її світлішою
                x, y = event.pos
                if menu_start.rect.collidepoint(x, y):
                    menu_start = Picture('pics/button_play_light.PNG', 567, 300, 166, 66)
                elif not menu_start.rect.collidepoint(x, y):
                    menu_start = Picture('pics/button_play.PNG', 567, 300, 166, 66)
                
                if menu_exit.rect.collidepoint(x, y):
                    menu_exit=Picture('pics/button_exit_light.PNG', 568, 500, 164, 66)
                elif not menu_start.rect.collidepoint(x, y):
                    menu_exit=Picture('pics/button_exit.PNG', 568, 500, 164, 66)
                    
                if menu_settings.rect.collidepoint(x,y):
                    menu_settings = Picture('pics/button_settings_light.png', 504, 400, 292, 66)
                elif not menu_exit.rect.collidepoint(x,y):
                    menu_settings = Picture('pics/button_settings.png', 504, 400, 292, 66)
                         
    elif screen == 'settings':
        #відмальовування спрайтів для екрану налаштувань
        menu_background.draw_picture()
        sett_plot.draw_picture()
        sett_guide.draw_picture()
        sett_back.draw_picture()
        change_controls.draw_picture()

        for event in pygame.event.get():#перевіряю куди натиснуто
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if sett_back.rect.collidepoint(x, y):#при натискані на кнопку назад перекидає на екран меню
                    screen = 'menu'

                    
                elif sett_plot.rect.collidepoint(x,y):#при натискані перекидає на екран сюжету
                    screen = "plot"
                    
                elif sett_guide.rect.collidepoint(x,y):#при натисканні перекидає на екран гайду
                    screen = "guide"
                    
                elif change_controls.rect.collidepoint(x,y):#при натискані перекидає на екран вибору керування
                    screen = "controls"
                    
            if event.type == pygame.MOUSEMOTION:#перевіряє на рух миші і якщо миша попадає на будь-яку кнопку то кнопка стає світлішою
                x, y = event.pos
                if sett_plot.rect.collidepoint(x,y):
                    sett_plot=Picture('pics/plot_light.png', 568, 250.4, 164, 66)
                elif not sett_plot.rect.collidepoint(x,y):
                    sett_plot=Picture('pics/plot.png', 568, 250.4, 164, 66)

                if sett_guide.rect.collidepoint(x,y):
                    sett_guide = Picture('pics/guide_light.png', 568, 117.2, 164, 66)
                elif not sett_guide.rect.collidepoint(x,y):
                    sett_guide = Picture('pics/guide.png', 568, 117.2, 164, 66)

                if change_controls.rect.collidepoint(x,y):
                    change_controls=Picture('pics/controls_light.png',568,383.6,164,66)
                elif not change_controls.rect.collidepoint(x,y):
                    change_controls=Picture('pics/controls.png',568,383.6,164,66)
                    
                if sett_back.rect.collidepoint(x,y):
                    sett_back = Picture('pics/button_back_light.png',565, 516.8, 164, 66)
                elif not change_controls.rect.collidepoint(x,y):
                    sett_back = Picture('pics/button_back.png',565, 516.8, 164, 66)
                    
            if event.type == pygame.QUIT:#виходить із гри при натисканні хрестика на вікні гри
                pygame.quit()
    
    elif screen == 'plot':
        #відмальовує об'єкти екрану сюжету
        menu_background.draw_picture()
        plot_back.draw_picture()
        plot_text1.draw_text()
        plot_text2.draw_text()
        plot_text3.draw_text()
        plot_text4.draw_text()
        plot_text5.draw_text()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:# перевіряє чи натиснуто кнопку назад і якщо натиснуто то перекидає в меню налаштувань
                x, y = event.pos
                if plot_back.rect.collidepoint(x, y):
                    screen = 'settings'
                    
            if event.type == pygame.QUIT:#виходить із гри при натисканні хрестика на вікні гри
                pygame.quit()
                
            if event.type == pygame.MOUSEMOTION:#перевіряє чи попадає курсор по кнопці назад і якщо так то робить її світлішою
                x,y=event.pos
                if plot_back.rect.collidepoint(x,y):
                    plot_back = Picture('pics/button_back_light.png',565, 400, 164, 66)
                elif not plot_back.rect.collidepoint(x,y):
                    plot_back = Picture('pics/button_back.png',565, 400, 164, 66)
                
    elif screen == 'guide':
        #відмальовує об'єкти екрану гайду
        menu_background.draw_picture()
        guide_back.draw_picture()
        guide_text1.draw_text()
        guide_text2.draw_text()
        guide_text3.draw_text()
        guide_text4.draw_text()
        guide_text5.draw_text()
        guide_text6.draw_text()
        guide_text7.draw_text()
        guide_text8.draw_text()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:# перевіряє чи натиснуто кнопку назад і якщо натиснуто то перекидає в меню налаштувань
                x, y = event.pos
                if guide_back.rect.collidepoint(x, y):
                    screen = 'settings'
                    
            if event.type == pygame.QUIT:#виходить із гри при натисканні хрестика на вікні гри
                pygame.quit()
                
            if event.type == pygame.MOUSEMOTION:#перевіряє чи попадає курсор по кнопці назад і якщо так то робить її світлішою
                x,y=event.pos
                if guide_back.rect.collidepoint(x,y):
                    guide_back = Picture('pics/button_back_light.png',565, 400, 164, 66)
                elif not guide_back.rect.collidepoint(x,y):
                    guide_back = Picture('pics/button_back.png',565, 400, 164, 66)
    
    elif screen == "controls":
        #відмальовування об'єктів екрану керування
        menu_background.draw_picture()   
        change_controls_back.draw_picture()
        change_controls_button.draw_picture()
        change_controls_text.draw_text()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:#виходить із гри при натисканні хрестика на вікні гри
                pygame.quit()
                
            if event.type == pygame.MOUSEBUTTONDOWN:# перевіряє чи натиснуто кнопку назад і якщо натиснуто то перекидає в меню налаштувань
                if change_controls_back.rect.collidepoint(x, y):
                    screen = 'settings'
                    
                elif change_controls_button.rect.collidepoint(x,y):#міняє керування 
                    if controls==1:
                        f = open('controls_save.txt', 'w')
                        f.write('2')
                        f.close()
                    else:
                        f = open('controls_save.txt', 'w')
                        f.write('1')
                        f.close()
                        
            if event.type == pygame.MOUSEMOTION:#перевіряє чи попадає курсор по кнопці  і якщо так то робить її світлішою
                x,y=event.pos
                
                if change_controls_back.rect.collidepoint(x,y):
                    change_controls_back=Picture('pics/button_back_light.png',567,450,166,66)
                elif not change_controls_back.rect.collidepoint(x,y):
                    change_controls_back=Picture('pics/button_back.png',567,450,166,66)
                    
                if controls==1:
                    if change_controls_button.rect.collidepoint(x,y):
                        change_controls_button=Picture("pics/controls2_light.png",567,350,166,66)
                    
                    elif not change_controls_button.rect.collidepoint(x,y):
                        change_controls_button=Picture("pics/controls2.png",567,350,166,66)
                        
                elif controls==2:
                    if change_controls_button.rect.collidepoint(x,y):
                        change_controls_button=Picture("pics/controls1_light.png",567,350,166,66)
                    
                    elif not change_controls_button.rect.collidepoint(x,y):
                        change_controls_button=Picture("pics/controls1.png",567,350,166,66)
                      
    elif screen == 'game_start':
        #відмальовування спрайтів для екрану початку гри
        menu_background.draw_picture()
        play_back.draw_picture()
        play_newgame.draw_picture()
        play_contgame.draw_picture()
        napys.draw_picture()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:#виходить із гри при натисканні хрестика на вікні гри
                pygame.quit()
                
            if event.type == pygame.MOUSEBUTTONDOWN:#перевіряє чи натиснуто якусь кнопку
                x, y = event.pos
                if play_back.rect.collidepoint(x, y):#якщо натиснуто кнопку назад перекидає на екран меню
                    screen = 'menu'
                elif play_contgame.rect.collidepoint(x,y):#якщо натиснуто кнопку продовжити то перекидає на екран вибору рівнів
                    screen = 'levels'
                elif play_newgame.rect.collidepoint(x,y):#якщо натиснуто кнопку нова гра то перекидає на екран перевірки       
                    screen = 'sure_check'
                    
            if event.type == pygame.MOUSEMOTION:#перевіряє чи попадає курсор миші на якусь і кнопку і якщо попадає то робить її світлішою
                x,y=event.pos
                if play_contgame.rect.collidepoint(x,y):
                    play_contgame = Picture("pics/contgame_light.png",502, 300, 296, 56)
                elif not play_contgame.rect.collidepoint(x,y):
                    play_contgame = Picture("pics/contgame.png",502, 300, 296, 56)
                    
                if play_newgame.rect.collidepoint(x,y):
                    play_newgame = Picture("pics/newgame_light.png",568, 400, 166, 66)
                elif not play_newgame.rect.collidepoint(x,y):
                    play_newgame = Picture("pics/newgame.png",568, 400, 166, 66)
                    
                if play_back.rect.collidepoint(x,y):
                    play_back = Picture("pics/button_back_light.png",568, 500, 164, 66)
                elif not play_back.rect.collidepoint(x,y):
                    play_back = Picture("pics/button_back.png",568, 500, 164, 66)
                      
    elif screen == 'levels':
        #відмальовування спрайтів для екрану вибору рівнів
        menu_background.draw_picture()
        level1.draw_picture()
        level2.draw_picture()
        level3.draw_picture()
        level4.draw_picture()
        level5.draw_picture()
        level6.draw_picture()
        
        levels_to_menu.draw_picture()
        levels_to_city.draw_picture()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:#виходить із гри при натисканні хрестика на вікні гри
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:#перевіряє чи натиснуто якусь кнопку
                x,y = event.pos
                if levels_to_menu.rect.collidepoint(x,y):#якщо натиснуто то перекидає на екран меню
                    screen = 'menu'
                    
                if levels_to_city.rect.collidepoint(x,y):#якщо натиснуто то перекидає на екран міста
                    screen = 'city'
                    
                if level1.rect.collidepoint(x,y):#якщо натиснуто то перекидає на екран першого рівня
                    screen = 'level1'
                    
                if level2.rect.collidepoint(x,y):#якщо натиснуто то перекидає на екран другого рівня
                    screen = 'level2'
                    
                if level3.rect.collidepoint(x,y):#якщо натиснуто то перекидає на екран третього рівня
                    screen = 'level3'
                    
                if level4.rect.collidepoint(x,y):#якщо натиснуто то перекидає на екран четвертого рівня
                    screen = 'level4'
                    
                if level5.rect.collidepoint(x,y):#якщо натиснуто то перекидає на екран п'ятого рівня
                    screen = 'level5'
                    
                if level6.rect.collidepoint(x,y):#якщо натиснуто то перекидає на екран шостого рівня
                    screen = 'level6'
                    
                    
                    
                    
                    
                    
            if event.type == pygame.MOUSEMOTION:#перевіряє рух курсора миші і якщо він попадає на якусь кнопку то вона стає світлішою
                x,y = event.pos
                if levels_to_menu.rect.collidepoint(x,y):
                    levels_to_menu = Picture('pics/to_menu_light.png', 450, 600, 166, 66)
                elif not levels_to_menu.rect.collidepoint(x,y):
                    levels_to_menu = Picture('pics/to_menu.png', 450, 600, 166, 66)
                    
                if levels_to_city.rect.collidepoint(x,y):
                    levels_to_city = Picture('pics/to_city_light.png', 666, 600, 166, 66)
                elif not levels_to_city.rect.collidepoint(x,y):
                    levels_to_city = Picture('pics/to_city.png', 666, 600, 166, 66)
                    
                    
                if level1.rect.collidepoint(x,y):
                    level1=Picture('pics/level1_light.png',550,150,50,50)
                elif not level1.rect.collidepoint(x,y):
                    level1=Picture('pics/level1.png',550,150,50,50)
                    
                if level2.rect.collidepoint(x,y):
                    level2=Picture('pics/level2_light.png',675,150,50,50)
                elif not level2.rect.collidepoint(x,y):
                    level2=Picture('pics/level2.png',675,150,50,50)
                    
                if level3.rect.collidepoint(x,y):
                    level3=Picture('pics/level3_light.png',550,275,50,50)
                elif not level3.rect.collidepoint(x,y):
                    level3=Picture('pics/level3.png',550,275,50,50)
                    
                if level4.rect.collidepoint(x,y):
                    level4=Picture('pics/level4_light.png',675,275,50,50)
                elif not level4.rect.collidepoint(x,y):
                    level4=Picture('pics/level4.png',675,275,50,50)
                    
                if level5.rect.collidepoint(x,y):
                    level5=Picture('pics/level5_light.png',550,400,50,50)
                elif not level5.rect.collidepoint(x,y):
                    level5=Picture('pics/level5.png',550,400,50,50)
                    
                if level6.rect.collidepoint(x,y):
                    level6=Picture('pics/level6_light.png',675,400,50,50)
                elif not level6.rect.collidepoint(x,y):
                    level6=Picture('pics/level6.png',675,400,50,50)  
                
    elif screen == 'sure_check':
        #відмальовування об'єктів для екрану перевірки
        menu_background.draw_picture()
        sure_check_yes.draw_picture()
        sure_check_no.draw_picture()
        sure_check_text.draw_text()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:#виходить із гри при натисканні хрестика на вікні гри
                pygame.quit()
                
            if event.type == pygame.MOUSEBUTTONDOWN:#перевіряє чи натиснуто якусь кнопку
                x,y = event.pos
                if sure_check_yes.rect.collidepoint(x,y):# якщо натиснуто на кнопку так то скидається прогрес та перекидає на екран вибору рівнів
                    f = open('money_save.txt','w')
                    f.write('0')
                    f.close()
                    
                    f = open('dump_money_save.txt','w')
                    f.write('0')
                    f.close()
                    
                    f = open('city_level_save.txt','w')
                    f.write('0')
                    f.close()
                    
                    menu_background = Picture('pics/city1.png',0,0,0,0)
                    
                    screen='levels'
                elif sure_check_no.rect.collidepoint(x,y):#якщо натиснуто ні то перекидає назад на екран game_start
                    screen='game_start'
                    
            if event.type == pygame.MOUSEMOTION:#вже було описане багато разів тому буду позначити такі фрагменти як "зміна кнопок на світліші"
                x,y=event.pos
                if sure_check_yes.rect.collidepoint(x,y):
                    sure_check_yes = Picture('pics/yes_light.png', 450, 400, 106, 66)
                elif not sure_check_yes.rect.collidepoint(x,y):
                    sure_check_yes = Picture('pics/yes.png', 450, 400, 106, 66)
                        
                if sure_check_no.rect.collidepoint(x,y):
                    sure_check_no = Picture('pics/no_light.png', 700, 400, 106, 66)
                elif not sure_check_no.rect.collidepoint(x,y):
                    sure_check_no = Picture('pics/no.png', 700, 400, 106, 66)
                      
    elif screen == 'city':
        #відмальовування об'єктів для екрану міста
        city_background.draw_picture()
        city_back.draw_picture()
        dump_money.draw_picture()
        dumped_money_text.draw_text()
        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:#виходить із гри при натисканні хрестика на вікні гри
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:#перевірка на натискання на кнопки
                x,y = event.pos
                if city_back.rect.collidepoint(x,y):#при натисканні перекидає на екран меню
                    screen = 'levels'
                if dump_money.rect.collidepoint(x,y):
                    f = open('dump_money_save.txt', 'r')
                    dumped_money = f.read()
                    f.close()
                    dumped_money = int(dumped_money)
                    
                    f = open('money_save.txt','r')
                    money = f.read()
                    f.close()
                    money=int(money)
                    
                    dumped_money = dumped_money + money
                    
                    f = open('dump_money_save.txt', 'w')
                    f.write(str(dumped_money))
                    f.close()
                    
                    f = open('money_save.txt','w')
                    f.write('0')
                    f.close()
                    
                    
                    
                    
            if event.type == pygame.MOUSEMOTION:#змінює кнопки на світліші
                x,y = event.pos
                if city_back.rect.collidepoint(x,y):
                    city_back = Picture("pics/button_back_light.png",450, 500, 164, 66)
                elif not city_back.rect.collidepoint(x,y):
                    city_back = Picture("pics/button_back.png",450, 500, 164, 66)
                    
                if dump_money.rect.collidepoint(x,y):
                    dump_money = Picture('pics/dump_light.png', 700, 500, 166, 66)
                elif not dump_money.rect.collidepoint(x,y):
                    dump_money = Picture('pics/dump.png', 700, 500, 166, 66)

    elif screen == 'level1':
        #відмальовування фону та ворогів для першого рівня
        level_background.draw_picture()
        
        red_enemy_counter1 = red_enemy_func1(red_enemy_counter1)
        red_enemy_counter2 = red_enemy_func2(red_enemy_counter2)
          
        if wait1==0:
            wait1=120
            red_enemy1=Picture('pics/enemy_red1.png', randint(0,1250),randint(0,650),50,50)  
            lvl1_score = lvl1_score + 1
            red_enemy_counter1=0
        else:
            red_enemy1.draw_picture()
            wait1 = wait1 - 1
            
        if wait2==0:
            wait2=120
            red_enemy2=Picture('pics/enemy_red1.png', randint(0,1250),randint(0,650),50,50)  
            lvl1_score = lvl1_score + 1
            red_enemy_counter2=0  
        else:
            red_enemy2.draw_picture()
            wait2 = wait2 - 1
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q and controls==1 or event.key == pygame.K_1 and controls==2:#перевіряє чи натиснуто на клавішу і чи попадає в це місце ворог
                    if red_enemy1.rect.collidepoint(pygame.mouse.get_pos()):   
                        money = money+1
                        f = open('money_save.txt','w')
                        f.write(str(money))
                        f.close()
                        wait1=0
                        lvl1_score = lvl1_score - 1
                        red_enemy_counter1=0
                        
                    if red_enemy2.rect.collidepoint(pygame.mouse.get_pos()):   
                        money = money+1
                        f = open('money_save.txt','w')
                        f.write(str(money))
                        f.close()
                        wait2=0
                        lvl1_score = lvl1_score - 1
                        red_enemy_counter2=0
                
                if event.key == pygame.K_ESCAPE:#пауза
                    pause=True
                    while pause==True:  
                        pause_cont.draw_picture()
                        pause_restart.draw_picture()
                        pause_to_levels.draw_picture()
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT:
                                pygame.quit()
                        
                            if event.type == pygame.MOUSEBUTTONDOWN:#перевіряє чи натиснуто кнопки
                                x,y = event.pos
                                if pause_cont.rect.collidepoint(x,y):#при натисканні продовжує рівень
                                    pause=False
                                
                                if pause_restart.rect.collidepoint(x,y):#при натисканні перезапускає рівень
                                    pause=False
                                    lvl1_score=-2
                                    lvl1_counter=0
                                    wait1=0
                                    wait2=0
                                 
                                if pause_to_levels.rect.collidepoint(x,y):#при натисканні перекидає на екран вибору рівнів
                                    pause=False
                                    lvl1_score=-2
                                    lvl1_counter=0
                                    wait1=0
                                    wait2=0
                                    screen="levels"
                                    
                            if event.type == pygame.MOUSEMOTION:#робить кнопки світліше
                                x,y = event.pos
                                if pause_restart.rect.collidepoint(x,y):
                                    pause_restart=Picture('pics/pause_restart_light.png',620,325,50,50)
                                elif not pause_restart.rect.collidepoint(x,y):
                                    pause_restart=Picture('pics/pause_restart.png',620,325,50,50)
                                    
                                if pause_to_levels.rect.collidepoint(x,y):
                                    pause_to_levels=Picture('pics/pause_to_levels_light.png',702,325,50,50)
                                elif not pause_to_levels.rect.collidepoint(x,y):
                                    pause_to_levels=Picture('pics/pause_to_levels.png',702,325,50,50)
                                    
                                if pause_cont.rect.collidepoint(x,y):
                                    pause_cont=Picture('pics/pause_cont_light.png',537.5,325,50,50)
                                elif not pause_cont.rect.collidepoint(x,y):
                                    pause_cont=Picture('pics/pause_cont.png',537.5,325,50,50)
                                
                        clock.tick(40)
                        pygame.display.update()




        lvl1_counter=lvl1_counter+1
        if lvl1_counter>600 and lvl1_score>5:#екран перемоги
            lost=True
            while lost==True:
                losing_text.draw_text()
                lose_restart.draw_picture()
                lose_to_levels.draw_picture()
                                        
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        
                    if event.type == pygame.MOUSEBUTTONDOWN:#перевіряє чи натиснуто якусь кнопку
                        x,y = event.pos
                        if lose_restart.rect.collidepoint(x,y):#при натисканні заново запускає перший рівень
                            lost=False
                            lvl1_score=-2
                            lvl1_counter=0
                            wait1=0
                            wait2=0
                            screen='level1'
                        
                        if lose_to_levels.rect.collidepoint(x,y):#при натисканні перекидає на екран вибору рівнів
                            lost=False
                            lvl1_score=-2
                            lvl1_counter=0
                            wait1=0
                            wait2=0
                            screen='levels'

                    if event.type == pygame.MOUSEMOTION:#зміна кнопок на світліші
                        x,y = event.pos
                        if lose_restart.rect.collidepoint(x,y):
                            lose_restart=Picture('pics/pause_restart_light.png',620,325,50,50)
                        elif not lose_restart.rect.collidepoint(x,y):
                            lose_restart=Picture('pics/pause_restart.png',620,325,50,50)
                                    
                        if lose_to_levels.rect.collidepoint(x,y):
                            lose_to_levels=Picture('pics/pause_to_levels_light.png',702,325,50,50)
                        elif not lose_to_levels.rect.collidepoint(x,y):
                            lose_to_levels=Picture('pics/pause_to_levels.png',702,325,50,50)
                                    
                clock.tick(40)
                pygame.display.update()
                            
        if lvl1_counter>600 and lvl1_score<=5:#екран програшу
            win=True
            while win==True:
                winning_text.draw_text()
                win_restart.draw_picture()
                win_to_levels.draw_picture()
                                        
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        
                    if event.type == pygame.MOUSEBUTTONDOWN:#перевірка чи натиснуто якусь клавішу
                        x,y = event.pos
                        if win_restart.rect.collidepoint(x,y):#при натисканні перезапускає перший рівень
                            win=False
                            lvl1_score=-2
                            lvl1_counter=0
                            wait1=0
                            wait2=0
                            money = money+5
                            f = open('money_save.txt','w')
                            f.write(str(money))
                            f.close()
                            screen='level1'
                        
                        if win_to_levels.rect.collidepoint(x,y):#при натисканні перекидає на екран вибору рівнів
                            win=False
                            lvl1_score=-2
                            lvl1_counter=0
                            wait1=0
                            wait2=0
                            screen='levels'
                            money = money+5
                            f = open('money_save.txt','w')
                            f.write(str(money))
                            f.close()
                            
                    if event.type == pygame.MOUSEMOTION:#робить кнопки світлішими
                        x,y = event.pos
                        if win_restart.rect.collidepoint(x,y):
                            win_restart=Picture('pics/pause_restart_light.png',620,325,50,50)
                        elif not win_restart.rect.collidepoint(x,y):
                            win_restart=Picture('pics/pause_restart.png',620,325,50,50)
                                    
                        if win_to_levels.rect.collidepoint(x,y):
                            win_to_levels=Picture('pics/pause_to_levels_light.png',702,325,50,50)
                        elif not pause_to_levels.rect.collidepoint(x,y):
                            win_to_levels=Picture('pics/pause_to_levels.png',702,325,50,50)
                            
                            
                            
                clock.tick(40)
                pygame.display.update()
                
    elif screen=='level2':
        #відмальовування ворогів та фону для другого рівня
        level_background.draw_picture()
        
        red_enemy_counter1 = red_enemy_func1(red_enemy_counter1)
        red_enemy_counter2 = red_enemy_func2(red_enemy_counter2)
        red_enemy_counter3 = red_enemy_func3(red_enemy_counter3)
        
        if wait1==0:
            wait1=120
            red_enemy1=Picture('pics/enemy_red1.png', randint(0,1250),randint(0,650),50,50)  
            lvl2_score = lvl2_score + 1
            red_enemy_counter1=0
        else:
            red_enemy1.draw_picture()
            wait1 = wait1 - 1
            
        if wait2==0:
            wait2=120
            red_enemy2=Picture('pics/enemy_red1.png', randint(0,1250),randint(0,650),50,50)  
            lvl2_score = lvl2_score + 1
            red_enemy_counter2=0  
        else:
            red_enemy2.draw_picture()
            wait2 = wait2 - 1
            
        if wait3==0:
            wait3=120
            red_enemy3=Picture('pics/enemy_red1.png', randint(0,1250),randint(0,650),50,50)  
            lvl2_score = lvl2_score + 1
            red_enemy_counter3=0
        else:
            red_enemy3.draw_picture()
            wait3 = wait3 - 1
        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q and controls==1 or event.key == pygame.K_1 and controls==2:#принцип такий самий як і раніше
                    if red_enemy1.rect.collidepoint(pygame.mouse.get_pos()):   
                        money = money+1
                        f = open('money_save.txt','w')
                        f.write(str(money))
                        f.close()
                        wait1=0
                        lvl2_score = lvl2_score - 1
                        red_enemy_counter1=0
                        
                    if red_enemy2.rect.collidepoint(pygame.mouse.get_pos()):   
                        money = money+1
                        f = open('money_save.txt','w')
                        f.write(str(money))
                        f.close()
                        wait2=0
                        lvl2_score = lvl2_score - 1
                        red_enemy_counter2=0
                        
                    if red_enemy3.rect.collidepoint(pygame.mouse.get_pos()):
                        money = money+1
                        f = open('money_save.txt','w')
                        f.write(str(money))
                        f.close()
                        wait3=0
                        lvl2_score = lvl2_score - 1
                        red_enemy_counter3=0
            
                if event.key == pygame.K_ESCAPE:#пауза була описанна вище
                        pause=True
                        while pause==True:  
                            pause_cont.draw_picture()
                            pause_restart.draw_picture()
                            pause_to_levels.draw_picture()
                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                    pygame.quit()
                            
                                if event.type == pygame.MOUSEBUTTONDOWN:
                                    x,y = event.pos
                                    if pause_cont.rect.collidepoint(x,y):
                                        pause=False
                                    
                                    if pause_restart.rect.collidepoint(x,y):
                                        pause=False
                                        lvl2_score=-3
                                        lvl2_counter=0
                                        wait1=0
                                        wait2=0
                                        wait3=0
                                    
                                    if pause_to_levels.rect.collidepoint(x,y):
                                        pause=False
                                        lvl2_score=-3
                                        lvl2_counter=0
                                        wait1=0
                                        wait2=0
                                        wait3=0
                                        screen="levels"
                                        
                                if event.type == pygame.MOUSEMOTION:
                                    x,y = event.pos
                                    if pause_restart.rect.collidepoint(x,y):
                                        pause_restart=Picture('pics/pause_restart_light.png',620,325,50,50)
                                    elif not pause_restart.rect.collidepoint(x,y):
                                        pause_restart=Picture('pics/pause_restart.png',620,325,50,50)
                                        
                                    if pause_to_levels.rect.collidepoint(x,y):
                                        pause_to_levels=Picture('pics/pause_to_levels_light.png',702,325,50,50)
                                    elif not pause_to_levels.rect.collidepoint(x,y):
                                        pause_to_levels=Picture('pics/pause_to_levels.png',702,325,50,50)
                                        
                                    if pause_cont.rect.collidepoint(x,y):
                                        pause_cont=Picture('pics/pause_cont_light.png',537.5,325,50,50)
                                    elif not pause_cont.rect.collidepoint(x,y):
                                        pause_cont=Picture('pics/pause_cont.png',537.5,325,50,50)
                                    
                            clock.tick(40)
                            pygame.display.update()     

        lvl2_counter=lvl2_counter+1
        if lvl2_counter>600 and lvl2_score>5:#екран програшу був описаний на першому рівні
            lost=True
            while lost==True:
                losing_text.draw_text()
                lose_restart.draw_picture()
                lose_to_levels.draw_picture()
                                        
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        x,y = event.pos
                        if lose_restart.rect.collidepoint(x,y):
                            lost=False
                            lvl2_score=-3
                            lvl2_counter=0
                            wait1=0
                            wait2=0
                            wait3=0
                            screen='level2'
                        
                        if lose_to_levels.rect.collidepoint(x,y):
                            lost=False
                            lvl2_score=-3
                            lvl2_counter=0
                            wait1=0
                            wait2=0
                            wait3=0
                            screen='levels'
                            
                    if event.type == pygame.MOUSEMOTION:
                        x,y = event.pos
                        if lose_restart.rect.collidepoint(x,y):
                            lose_restart=Picture('pics/pause_restart_light.png',620,325,50,50)
                        elif not lose_restart.rect.collidepoint(x,y):
                            lose_restart=Picture('pics/pause_restart.png',620,325,50,50)
                                    
                        if lose_to_levels.rect.collidepoint(x,y):
                            lose_to_levels=Picture('pics/pause_to_levels_light.png',702,325,50,50)
                        elif not lose_to_levels.rect.collidepoint(x,y):
                            lose_to_levels=Picture('pics/pause_to_levels.png',702,325,50,50)
                            
                clock.tick(40)
                pygame.display.update()

        if lvl2_counter>600 and lvl2_score<=5:#екран перемоги був описаний раніше
            win=True
            while win==True:
                winning_text.draw_text()
                win_restart.draw_picture()
                win_to_levels.draw_picture()
                                        
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        x,y = event.pos
                        if win_restart.rect.collidepoint(x,y):
                            win=False
                            lvl2_score=-3
                            lvl2_counter=0
                            wait1=0
                            wait2=0
                            wait3=0
                            
                            
                            money = money+10
                            f = open('money_save.txt','w')
                            f.write(str(money))
                            f.close()
                            screen='level2'
                        
                        if win_to_levels.rect.collidepoint(x,y):
                            win=False
                            lvl2_score=-3
                            lvl2_counter=0
                            wait1=0
                            wait2=0
                            wait3=0
                            money = money+10
                            f = open('money_save.txt','w')
                            f.write(str(money))
                            f.close()
                            screen='levels'
                            
                    if event.type == pygame.MOUSEMOTION:
                        x,y = event.pos
                        if win_restart.rect.collidepoint(x,y):
                            win_restart=Picture('pics/pause_restart_light.png',620,325,50,50)
                        elif not win_restart.rect.collidepoint(x,y):
                            win_restart=Picture('pics/pause_restart.png',620,325,50,50)
                                        
                        if win_to_levels.rect.collidepoint(x,y):
                            win_to_levels=Picture('pics/pause_to_levels_light.png',702,325,50,50)
                        elif not pause_to_levels.rect.collidepoint(x,y):
                            win_to_levels=Picture('pics/pause_to_levels.png',702,325,50,50)

                clock.tick(40)
                pygame.display.update()

    elif screen == 'level3':
        #відмальвування ворогів та фону третього рівня
        level_background.draw_picture()
        
        red_enemy_counter1 = red_enemy_func1(red_enemy_counter1)
        red_enemy_counter2 = red_enemy_func2(red_enemy_counter2)
        green_enemy_counter1 = green_enemy_func1(green_enemy_counter1)
        
        if wait1==0:
            wait1=120
            red_enemy1=Picture('pics/enemy_red1.png', randint(0,1250),randint(0,650),50,50)  
            lvl3_score = lvl3_score + 1
            red_enemy_counter1=0
        else:
            red_enemy1.draw_picture()
            wait1 = wait1 - 1
            
        if wait2==0:
            wait2=120
            red_enemy2=Picture('pics/enemy_red1.png', randint(0,1250),randint(0,650),50,50)  
            lvl3_score = lvl3_score + 1
            red_enemy_counter2=0  
        else:
            red_enemy2.draw_picture()
            wait2 = wait2 - 1
            
        if wait3==0:
            wait3=120
            green_enemy1=Picture('pics/enemy_green1.png', randint(0,1250),randint(0,650),50,50)  
            lvl3_score = lvl3_score + 1
            green_enemy_counter1=0
        else:
            green_enemy1.draw_picture()
            wait3 = wait3 - 1
        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q and controls==1 or event.key == pygame.K_1 and controls==2:#було описане вище
                    if red_enemy1.rect.collidepoint(pygame.mouse.get_pos()):   
                        money = money+1
                        f = open('money_save.txt','w')
                        f.write(str(money))
                        f.close()
                        wait1=0
                        lvl3_score = lvl3_score - 1
                        red_enemy_counter1=0
                        
                    if red_enemy2.rect.collidepoint(pygame.mouse.get_pos()):   
                        money = money+1
                        f = open('money_save.txt','w')
                        f.write(str(money))
                        f.close()
                        wait2=0
                        lvl3_score = lvl3_score - 1
                        red_enemy_counter2=0
                        
                if event.key == pygame.K_w and controls==1 or event.key == pygame.K_2 and controls==2:
                    
                    if green_enemy1.rect.collidepoint(pygame.mouse.get_pos()):
                        money = money+2
                        f = open('money_save.txt','w')
                        f.write(str(money))
                        f.close()
                        wait3=0
                        lvl3_score = lvl3_score - 1
                        green_enemy_counter1=0
            
                if event.key == pygame.K_ESCAPE:#пауза була описанна вище
                        pause=True
                        while pause==True:  
                            pause_cont.draw_picture()
                            pause_restart.draw_picture()
                            pause_to_levels.draw_picture()
                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                    pygame.quit()
                            
                                if event.type == pygame.MOUSEBUTTONDOWN:
                                    x,y = event.pos
                                    if pause_cont.rect.collidepoint(x,y):
                                        pause=False
                                    
                                    if pause_restart.rect.collidepoint(x,y):
                                        pause=False
                                        lvl3_score=-3
                                        lvl3_counter=0
                                        wait1=0
                                        wait2=0
                                        wait3=0
                                    
                                    if pause_to_levels.rect.collidepoint(x,y):
                                        pause=False
                                        lvl3_score=-3
                                        lvl3_counter=0
                                        wait1=0
                                        wait2=0
                                        wait3=0
                                        screen="levels"
                                        
                                if event.type == pygame.MOUSEMOTION:
                                    x,y = event.pos
                                    if pause_restart.rect.collidepoint(x,y):
                                        pause_restart=Picture('pics/pause_restart_light.png',620,325,50,50)
                                    elif not pause_restart.rect.collidepoint(x,y):
                                        pause_restart=Picture('pics/pause_restart.png',620,325,50,50)
                                        
                                    if pause_to_levels.rect.collidepoint(x,y):
                                        pause_to_levels=Picture('pics/pause_to_levels_light.png',702,325,50,50)
                                    elif not pause_to_levels.rect.collidepoint(x,y):
                                        pause_to_levels=Picture('pics/pause_to_levels.png',702,325,50,50)
                                        
                                    if pause_cont.rect.collidepoint(x,y):
                                        pause_cont=Picture('pics/pause_cont_light.png',537.5,325,50,50)
                                    elif not pause_cont.rect.collidepoint(x,y):
                                        pause_cont=Picture('pics/pause_cont.png',537.5,325,50,50)
                                    
                            clock.tick(40)
                            pygame.display.update()     

        lvl3_counter=lvl3_counter+1
        if lvl3_counter>600 and lvl3_score>5:#екран поразки був описаний вище
            lost=True
            while lost==True:
                losing_text.draw_text()
                lose_restart.draw_picture()
                lose_to_levels.draw_picture()
                                        
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        x,y = event.pos
                        if lose_restart.rect.collidepoint(x,y):
                            lost=False
                            lvl3_score=-3
                            lvl3_counter=0
                            wait1=0
                            wait2=0
                            wait3=0
                            screen='level3'
                        
                        if lose_to_levels.rect.collidepoint(x,y):
                            lost=False
                            lvl3_score=-3
                            lvl3_counter=0
                            wait1=0
                            wait2=0
                            wait3=0
                            screen='levels'
                            
                    if event.type == pygame.MOUSEMOTION:
                        x,y = event.pos
                        if lose_restart.rect.collidepoint(x,y):
                            lose_restart=Picture('pics/pause_restart_light.png',620,325,50,50)
                        elif not lose_restart.rect.collidepoint(x,y):
                            lose_restart=Picture('pics/pause_restart.png',620,325,50,50)
                                    
                        if lose_to_levels.rect.collidepoint(x,y):
                            lose_to_levels=Picture('pics/pause_to_levels_light.png',702,325,50,50)
                        elif not lose_to_levels.rect.collidepoint(x,y):
                            lose_to_levels=Picture('pics/pause_to_levels.png',702,325,50,50)
                            
                clock.tick(40)
                pygame.display.update()

        if lvl3_counter>600 and lvl3_score<=5:#екран перемоги був описаний вище
            win=True
            while win==True:
                winning_text.draw_text()
                win_restart.draw_picture()
                win_to_levels.draw_picture()
                                        
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        x,y = event.pos
                        if win_restart.rect.collidepoint(x,y):
                            win=False
                            lvl3_score=-3
                            lvl3_counter=0
                            wait1=0
                            wait2=0
                            wait3=0
                            
                            
                            money = money+20
                            f = open('money_save.txt','w')
                            f.write(str(money))
                            f.close()
                            screen='level3'
                        
                        if win_to_levels.rect.collidepoint(x,y):
                            win=False
                            lvl3_score=-3
                            lvl3_counter=0
                            wait1=0
                            wait2=0
                            wait3=0
                            money = money+20
                            f = open('money_save.txt','w')
                            f.write(str(money))
                            f.close()
                            screen='levels'
                            
                    if event.type == pygame.MOUSEMOTION:
                        x,y = event.pos
                        if win_restart.rect.collidepoint(x,y):
                            win_restart=Picture('pics/pause_restart_light.png',620,325,50,50)
                        elif not win_restart.rect.collidepoint(x,y):
                            win_restart=Picture('pics/pause_restart.png',620,325,50,50)
                                        
                        if win_to_levels.rect.collidepoint(x,y):
                            win_to_levels=Picture('pics/pause_to_levels_light.png',702,325,50,50)
                        elif not pause_to_levels.rect.collidepoint(x,y):
                            win_to_levels=Picture('pics/pause_to_levels.png',702,325,50,50)

                clock.tick(40)
                pygame.display.update()

    elif screen=="level4":
        #відмальовування ворогів та фону для четвертого рівня
        level_background.draw_picture()
        red_enemy_counter1 = red_enemy_func1(red_enemy_counter1)
        red_enemy_counter2 = red_enemy_func2(red_enemy_counter2)
        green_enemy_counter1 = green_enemy_func1(green_enemy_counter1)
        green_enemy_counter2 = green_enemy_func2(green_enemy_counter2)
        
        if wait1==0:
            wait1=120
            red_enemy1=Picture('pics/enemy_red1.png', randint(0,1250),randint(0,650),50,50)  
            lvl4_score = lvl4_score + 1
            red_enemy_counter1=0
        else:
            red_enemy1.draw_picture()
            wait1 = wait1 - 1
            
        if wait2==0:
            wait2=120
            red_enemy2=Picture('pics/enemy_red1.png', randint(0,1250),randint(0,650),50,50)  
            lvl4_score = lvl4_score + 1
            red_enemy_counter2=0
        else:
            red_enemy2.draw_picture()
            wait2 = wait2 - 1
            
        if wait3==0:
            wait3=120
            green_enemy1=Picture('pics/enemy_green1.png', randint(0,1250),randint(0,650),50,50)  
            lvl4_score = lvl4_score + 1
            green_enemy_counter1=0
        else:
            green_enemy1.draw_picture()
            wait3 = wait3 - 1
        
        if wait4==0:
            wait4=120
            green_enemy2=Picture('pics/enemy_green1.png', randint(0,1250),randint(0,650),50,50)
            lvl4_score = lvl4_score + 1
            green_enemy_counter2=0
        else:
            green_enemy2.draw_picture()
            wait4 = wait4 + 1
            
            
            
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q and controls==1 or event.key == pygame.K_1 and controls==2:#було описане вище
                    if red_enemy1.rect.collidepoint(pygame.mouse.get_pos()):   
                        money = money+1
                        f = open('money_save.txt','w')
                        f.write(str(money))
                        f.close()
                        wait1=0
                        lvl4_score = lvl4_score - 1
                        red_enemy_counter1=0
                        
                    if red_enemy2.rect.collidepoint(pygame.mouse.get_pos()):   
                        money = money+1
                        f = open('money_save.txt','w')
                        f.write(str(money))
                        f.close()
                        wait2=0
                        lvl4_score = lvl4_score - 1
                        red_enemy_counter2=0
                        
                    
                if event.key == pygame.K_w and controls==1 or event.key == pygame.K_2 and controls==2:
                    
                    if green_enemy1.rect.collidepoint(pygame.mouse.get_pos()):
                        money = money+2
                        f = open('money_save.txt','w')
                        f.write(str(money))
                        f.close()
                        wait3=0
                        lvl4_score = lvl4_score - 1
                        green_enemy_counter1=0
                        
                    if green_enemy2.rect.collidepoint(pygame.mouse.get_pos()):
                        money = money+2
                        f = open('money_save.txt','w')
                        f.write(str(money))
                        f.close()
                        wait4=0
                        lvl4_score = lvl4_score - 1
                        green_enemy_counter2=0
                        
                if event.key == pygame.K_ESCAPE:#пауза була описана вище
                        pause=True
                        while pause==True:  
                            pause_cont.draw_picture()
                            pause_restart.draw_picture()
                            pause_to_levels.draw_picture()
                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                    pygame.quit()
                            
                                if event.type == pygame.MOUSEBUTTONDOWN:
                                    x,y = event.pos
                                    if pause_cont.rect.collidepoint(x,y):
                                        pause=False
                                    
                                    if pause_restart.rect.collidepoint(x,y):
                                        pause=False
                                        lvl4_score=-4
                                        lvl4_counter=0
                                        wait1=0
                                        wait2=0
                                        wait3=0
                                        wait4=0
                                    
                                    if pause_to_levels.rect.collidepoint(x,y):
                                        pause=False
                                        lvl4_score=-4
                                        lvl4_counter=0
                                        wait1=0
                                        wait2=0
                                        wait3=0
                                        wait4=0
                                        screen="levels"
                                        
                                if event.type == pygame.MOUSEMOTION:
                                    x,y = event.pos
                                    if pause_restart.rect.collidepoint(x,y):
                                        pause_restart=Picture('pics/pause_restart_light.png',620,325,50,50)
                                    elif not pause_restart.rect.collidepoint(x,y):
                                        pause_restart=Picture('pics/pause_restart.png',620,325,50,50)
                                        
                                    if pause_to_levels.rect.collidepoint(x,y):
                                        pause_to_levels=Picture('pics/pause_to_levels_light.png',702,325,50,50)
                                    elif not pause_to_levels.rect.collidepoint(x,y):
                                        pause_to_levels=Picture('pics/pause_to_levels.png',702,325,50,50)
                                        
                                    if pause_cont.rect.collidepoint(x,y):
                                        pause_cont=Picture('pics/pause_cont_light.png',537.5,325,50,50)
                                    elif not pause_cont.rect.collidepoint(x,y):
                                        pause_cont=Picture('pics/pause_cont.png',537.5,325,50,50)
                                    
                                    
                            clock.tick(40)
                            pygame.display.update()
                            
                            
        lvl4_counter=lvl4_counter+1
        if lvl4_counter>600 and lvl4_score>5:#екран поразки був описаний вище
            lost=True
            while lost==True:
                losing_text.draw_text()
                lose_restart.draw_picture()
                lose_to_levels.draw_picture()
                                        
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        x,y = event.pos
                        if lose_restart.rect.collidepoint(x,y):
                            lost=False
                            lvl4_score=-4
                            lvl4_counter=0
                            wait1=0
                            wait2=0
                            wait3=0
                            wait4=0
                            screen='level4'
                        
                        if lose_to_levels.rect.collidepoint(x,y):
                            lost=False
                            lvl4_score=-4
                            lvl4_counter=0
                            wait1=0
                            wait2=0
                            wait3=0
                            wait4=0
                            screen='levels'
                            
                    if event.type == pygame.MOUSEMOTION:
                        x,y = event.pos
                        if lose_restart.rect.collidepoint(x,y):
                            lose_restart=Picture('pics/pause_restart_light.png',620,325,50,50)
                        elif not lose_restart.rect.collidepoint(x,y):
                            lose_restart=Picture('pics/pause_restart.png',620,325,50,50)
                                    
                        if lose_to_levels.rect.collidepoint(x,y):
                            lose_to_levels=Picture('pics/pause_to_levels_light.png',702,325,50,50)
                        elif not lose_to_levels.rect.collidepoint(x,y):
                            lose_to_levels=Picture('pics/pause_to_levels.png',702,325,50,50)
                            
                clock.tick(40)
                pygame.display.update()

        if lvl4_counter>600 and lvl4_score<=5:#екран перемоги був описаний вище 
            win=True
            while win==True:
                winning_text.draw_text()
                win_restart.draw_picture()
                win_to_levels.draw_picture()
                                        
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        x,y = event.pos
                        if win_restart.rect.collidepoint(x,y):
                            win=False
                            lvl4_score=-4
                            lvl4_counter=0
                            wait1=0
                            wait2=0
                            wait3=0
                            wait4=0
                            
                            money = money+30
                            f = open('money_save.txt','w')
                            f.write(str(money))
                            f.close()
                            screen='level4'
                        
                        if win_to_levels.rect.collidepoint(x,y):
                            win=False
                            lvl4_score=-4
                            lvl4_counter=0
                            wait1=0
                            wait2=0
                            wait3=0
                            wait4=0
                            money = money+30
                            f = open('money_save.txt','w')
                            f.write(str(money))
                            f.close()
                            screen='levels'
                            
                    if event.type == pygame.MOUSEMOTION:
                        x,y = event.pos
                        if win_restart.rect.collidepoint(x,y):
                            win_restart=Picture('pics/pause_restart_light.png',620,325,50,50)
                        elif not win_restart.rect.collidepoint(x,y):
                            win_restart=Picture('pics/pause_restart.png',620,325,50,50)
                                        
                        if win_to_levels.rect.collidepoint(x,y):
                            win_to_levels=Picture('pics/pause_to_levels_light.png',702,325,50,50)
                        elif not pause_to_levels.rect.collidepoint(x,y):
                            win_to_levels=Picture('pics/pause_to_levels.png',702,325,50,50)

                clock.tick(40)
                pygame.display.update()
                
    elif screen=='level5':
        #відмальовування ворогів та фону для п'ятого рівня
        level_background.draw_picture()
        red_enemy_counter1 = red_enemy_func1(red_enemy_counter1)
        red_enemy_counter2 = red_enemy_func2(red_enemy_counter2)
        green_enemy_counter1 = green_enemy_func1(green_enemy_counter1)
        green_enemy_counter2 = green_enemy_func2(green_enemy_counter2)
        blue_enemy_counter1 = blue_enemy_func1(blue_enemy_counter1)
        
        if wait1==0:
            wait1=120
            red_enemy1=Picture('pics/enemy_red1.png', randint(0,1250),randint(0,650),50,50)  
            lvl5_score = lvl5_score + 1
            red_enemy_counter1=0
        else:
            red_enemy1.draw_picture()
            wait1 = wait1 - 1
            
        if wait2==0:
            wait2=120
            red_enemy2=Picture('pics/enemy_red1.png', randint(0,1250),randint(0,650),50,50)  
            lvl5_score = lvl5_score + 1
            red_enemy_counter2=0
        else:
            red_enemy2.draw_picture()
            wait2 = wait2 - 1
            
        if wait3==0:
            wait3=120
            green_enemy1=Picture('pics/enemy_green1.png', randint(0,1250),randint(0,650),50,50)  
            lvl5_score = lvl5_score + 1
            green_enemy_counter1=0
        else:
            green_enemy1.draw_picture()
            wait3 = wait3 - 1
        
        if wait4==0:
            wait4=120
            green_enemy2=Picture('pics/enemy_green1.png', randint(0,1250),randint(0,650),50,50)
            lvl5_score = lvl5_score + 1
            green_enemy_counter2=0
        else:
            green_enemy2.draw_picture()
            wait4 = wait4 + 1
            
        if wait5==0:
            wait5=120
            blue_enemy1=Picture('pics/enemy_blue1.png', randint(0,1250),randint(0,650),50,50)
            lvl5_score = lvl5_score + 1
            blue_enemy_counter1=0
        else:
            blue_enemy1.draw_picture()
            wait5 = wait5 + 1
            
            
            
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q and controls==1 or event.key == pygame.K_1 and controls==2:#було описане вище
                    if red_enemy1.rect.collidepoint(pygame.mouse.get_pos()):   
                        money = money+1
                        f = open('money_save.txt','w')
                        f.write(str(money))
                        f.close()
                        wait1=0
                        lvl5_score = lvl5_score - 1
                        red_enemy_counter1=0
                        
                    if red_enemy2.rect.collidepoint(pygame.mouse.get_pos()):   
                        money = money+1
                        f = open('money_save.txt','w')
                        f.write(str(money))
                        f.close()
                        wait2=0
                        lvl5_score = lvl5_score - 1
                        red_enemy_counter2=0
                        
                    
                if event.key == pygame.K_w and controls==1 or event.key == pygame.K_2 and controls==2:
                    
                    if green_enemy1.rect.collidepoint(pygame.mouse.get_pos()):
                        money = money+2
                        f = open('money_save.txt','w')
                        f.write(str(money))
                        f.close()
                        wait3=0
                        lvl5_score = lvl5_score - 1
                        green_enemy_counter1=0
                        
                    if green_enemy2.rect.collidepoint(pygame.mouse.get_pos()):
                        money = money+2
                        f = open('money_save.txt','w')
                        f.write(str(money))
                        f.close()
                        wait4=0
                        lvl5_score = lvl5_score - 1
                        green_enemy_counter2=0
                        
                if event.key == pygame.K_e and controls==1 or event.key == pygame.K_3 and controls==2:
                    
                    if blue_enemy1.rect.collidepoint(pygame.mouse.get_pos()):
                        money = money+3
                        f = open('money_save.txt','w')
                        f.write(str(money))
                        f.close()
                        wait5=0
                        lvl5_score = lvl5_score - 1
                        blue_enemy_counter1=0
                           
                if event.key == pygame.K_ESCAPE:#пауза була описана вище
                        pause=True
                        while pause==True:  
                            pause_cont.draw_picture()
                            pause_restart.draw_picture()
                            pause_to_levels.draw_picture()
                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                    pygame.quit()
                            
                                if event.type == pygame.MOUSEBUTTONDOWN:
                                    x,y = event.pos
                                    if pause_cont.rect.collidepoint(x,y):
                                        pause=False
                                    
                                    if pause_restart.rect.collidepoint(x,y):
                                        pause=False
                                        lvl5_score=-5
                                        lvl5_counter=0
                                        wait1=0
                                        wait2=0
                                        wait3=0
                                        wait4=0
                                        wait5=0
                                    
                                    if pause_to_levels.rect.collidepoint(x,y):
                                        pause=False
                                        lvl5_score=-5
                                        lvl5_counter=0
                                        wait1=0
                                        wait2=0
                                        wait3=0
                                        wait4=0
                                        wait5=0
                                        screen="levels"
                                        
                                        
                                if event.type == pygame.MOUSEMOTION:
                                    x,y = event.pos
                                    if pause_restart.rect.collidepoint(x,y):
                                        pause_restart=Picture('pics/pause_restart_light.png',620,325,50,50)
                                    elif not pause_restart.rect.collidepoint(x,y):
                                        pause_restart=Picture('pics/pause_restart.png',620,325,50,50)
                                        
                                    if pause_to_levels.rect.collidepoint(x,y):
                                        pause_to_levels=Picture('pics/pause_to_levels_light.png',702,325,50,50)
                                    elif not pause_to_levels.rect.collidepoint(x,y):
                                        pause_to_levels=Picture('pics/pause_to_levels.png',702,325,50,50)
                                        
                                    if pause_cont.rect.collidepoint(x,y):
                                        pause_cont=Picture('pics/pause_cont_light.png',537.5,325,50,50)
                                    elif not pause_cont.rect.collidepoint(x,y):
                                        pause_cont=Picture('pics/pause_cont.png',537.5,325,50,50)
                            clock.tick(40)
                            pygame.display.update()           
                                
                                    
        lvl5_counter=lvl5_counter+1
        if lvl5_counter>600 and lvl5_score>5:#екран поразки був описаний вище 
            lost=True
            while lost==True:
                losing_text.draw_text()
                lose_restart.draw_picture()
                lose_to_levels.draw_picture()
                                        
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        x,y = event.pos
                        if lose_restart.rect.collidepoint(x,y):
                            lost=False
                            lvl5_score=-5
                            lvl5_counter=0
                            wait1=0
                            wait2=0
                            wait3=0
                            wait4=0
                            wait5=0
                            screen='level5'
                        
                        if lose_to_levels.rect.collidepoint(x,y):
                            lost=False
                            lvl5_score=-5
                            lvl5_counter=0
                            wait1=0
                            wait2=0
                            wait3=0
                            wait4=0
                            wait5=0
                            screen='levels'
                            
                    if event.type == pygame.MOUSEMOTION:
                        x,y = event.pos
                        if lose_restart.rect.collidepoint(x,y):
                            lose_restart=Picture('pics/pause_restart_light.png',620,325,50,50)
                        elif not lose_restart.rect.collidepoint(x,y):
                            lose_restart=Picture('pics/pause_restart.png',620,325,50,50)
                                    
                        if lose_to_levels.rect.collidepoint(x,y):
                            lose_to_levels=Picture('pics/pause_to_levels_light.png',702,325,50,50)
                        elif not lose_to_levels.rect.collidepoint(x,y):
                            lose_to_levels=Picture('pics/pause_to_levels.png',702,325,50,50)
                            
                clock.tick(40)
                pygame.display.update()

        if lvl5_counter>600 and lvl5_score<=5:#екран перемоги був описаний вище
            win=True
            while win==True:
                winning_text.draw_text()
                win_restart.draw_picture()
                win_to_levels.draw_picture()
                                        
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        x,y = event.pos
                        if win_restart.rect.collidepoint(x,y):
                            win=False
                            lvl5_score=-5
                            lvl5_counter=0
                            wait1=0
                            wait2=0
                            wait3=0
                            wait4=0
                            wait5=0
                            money = money+40
                            f = open('money_save.txt','w')
                            f.write(str(money))
                            f.close()
                            screen='level5'
                        
                        if win_to_levels.rect.collidepoint(x,y):
                            win=False
                            lvl5_score=-5
                            lvl5_counter=0
                            wait1=0
                            wait2=0
                            wait3=0
                            wait4=0
                            wait5=0
                            money = money+40
                            f = open('money_save.txt','w')
                            f.write(str(money))
                            f.close()
                            screen='levels'
                            
                    if event.type == pygame.MOUSEMOTION:
                        x,y = event.pos
                        if win_restart.rect.collidepoint(x,y):
                            win_restart=Picture('pics/pause_restart_light.png',620,325,50,50)
                        elif not win_restart.rect.collidepoint(x,y):
                            win_restart=Picture('pics/pause_restart.png',620,325,50,50)
                                        
                        if win_to_levels.rect.collidepoint(x,y):
                            win_to_levels=Picture('pics/pause_to_levels_light.png',702,325,50,50)
                        elif not pause_to_levels.rect.collidepoint(x,y):
                            win_to_levels=Picture('pics/pause_to_levels.png',702,325,50,50)

                clock.tick(40)
                pygame.display.update()
                
                
                
                
                
    elif screen=='level6':
        #відмальовування ворогів та фону для шостого рівня
        level_background.draw_picture()
        red_enemy_counter1 = red_enemy_func1(red_enemy_counter1)
        red_enemy_counter2 = red_enemy_func2(red_enemy_counter2)
        green_enemy_counter1 = green_enemy_func1(green_enemy_counter1)
        green_enemy_counter2 = green_enemy_func2(green_enemy_counter2)
        blue_enemy_counter1 = blue_enemy_func1(blue_enemy_counter1)
        blue_enemy_counter2 = blue_enemy_func2(blue_enemy_counter2)
        
        if wait1==0:
            wait1=120
            red_enemy1=Picture('pics/enemy_red1.png', randint(0,1250),randint(0,650),50,50)  
            lvl6_score = lvl6_score + 1
            red_enemy_counter1=0
        else:
            red_enemy1.draw_picture()
            wait1 = wait1 - 1
            
        if wait2==0:
            wait2=120
            red_enemy2=Picture('pics/enemy_red1.png', randint(0,1250),randint(0,650),50,50)  
            lvl6_score = lvl6_score + 1
            red_enemy_counter2=0
        else:
            red_enemy2.draw_picture()
            wait2 = wait2 - 1
            
        if wait3==0:
            wait3=120
            green_enemy1=Picture('pics/enemy_green1.png', randint(0,1250),randint(0,650),50,50)  
            lvl6_score = lvl6_score + 1
            green_enemy_counter1=0
        else:
            green_enemy1.draw_picture()
            wait3 = wait3 - 1
        
            
        if wait4==0:
            wait4=120
            green_enemy2=Picture('pics/enemy_green1.png', randint(0,1250),randint(0,650),50,50)
            lvl6_score = lvl6_score + 1
            green_enemy_counter2=0
        else:
            green_enemy2.draw_picture()
            wait4 = wait4 + 1
            
            
        if wait5==0:
            wait5=120
            blue_enemy1=Picture('pics/enemy_blue1.png', randint(0,1250),randint(0,650),50,50)
            lvl6_score = lvl6_score + 1
            blue_enemy_counter1=0
        else:
            blue_enemy1.draw_picture()
            wait5 = wait5 + 1
               
        if wait6==0:
            wait6=120
            blue_enemy2=Picture('pics/enemy_blue1.png', randint(0,1250),randint(0,650),50,50)
            lvl6_score = lvl6_score + 1
            blue_enemy_counter2=0
        else:
            blue_enemy2.draw_picture()
            wait6 = wait6 + 1
            
            
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q and controls==1 or event.key == pygame.K_1 and controls==2:#було описане вище
                    if red_enemy1.rect.collidepoint(pygame.mouse.get_pos()):   
                        money = money+1
                        f = open('money_save.txt','w')
                        f.write(str(money))
                        f.close()
                        wait1=0
                        lvl6_score = lvl6_score - 1
                        red_enemy_counter1=0
                        
                    if red_enemy2.rect.collidepoint(pygame.mouse.get_pos()):   
                        money = money+1
                        f = open('money_save.txt','w')
                        f.write(str(money))
                        f.close()
                        wait2=0
                        lvl6_score = lvl6_score - 1
                        red_enemy_counter2=0
                        
                    
                if event.key == pygame.K_w and controls==1 or event.key == pygame.K_2 and controls==2:
                    
                    if green_enemy1.rect.collidepoint(pygame.mouse.get_pos()):
                        money = money+2
                        f = open('money_save.txt','w')
                        f.write(str(money))
                        f.close()
                        wait3=0
                        lvl6_score = lvl6_score - 1
                        green_enemy_counter1=0
                        
                    if green_enemy2.rect.collidepoint(pygame.mouse.get_pos()):
                        money = money+2
                        f = open('money_save.txt','w')
                        f.write(str(money))
                        f.close()
                        wait4=0
                        lvl6_score = lvl6_score - 1
                        green_enemy_counter2=0
                        
                if event.key == pygame.K_e and controls==1 or event.key == pygame.K_3 and controls==2:
                    
                    if blue_enemy1.rect.collidepoint(pygame.mouse.get_pos()):
                        money = money+3
                        f = open('money_save.txt','w')
                        f.write(str(money))
                        f.close()
                        wait5=0
                        lvl6_score = lvl6_score - 1
                        blue_enemy_counter1=0
                           
                    if blue_enemy2.rect.collidepoint(pygame.mouse.get_pos()):
                        money = money+3
                        f = open('money_save.txt','w')
                        f.write(str(money))
                        f.close()
                        wait6=0
                        lvl6_score = lvl6_score - 1
                        blue_enemy_counter2=0
                        
                        
                if event.key == pygame.K_ESCAPE:#пауза була описана вище
                        pause=True
                        while pause==True:  
                            pause_cont.draw_picture()
                            pause_restart.draw_picture()
                            pause_to_levels.draw_picture()
                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                    pygame.quit()
                            
                                if event.type == pygame.MOUSEBUTTONDOWN:
                                    x,y = event.pos
                                    if pause_cont.rect.collidepoint(x,y):
                                        pause=False
                                    
                                    if pause_restart.rect.collidepoint(x,y):
                                        pause=False
                                        lvl6_score=-6
                                        lvl6_counter=0
                                        wait1=0
                                        wait2=0
                                        wait3=0
                                        wait4=0
                                        wait5=0
                                        wait6=0
                                    
                                    if pause_to_levels.rect.collidepoint(x,y):
                                        pause=False
                                        lvl6_score=-6
                                        lvl6_counter=0
                                        wait1=0
                                        wait2=0
                                        wait3=0
                                        wait4=0
                                        wait5=0
                                        wait6=0
                                        screen="levels"
                                        
                                        
                                        
                                if event.type == pygame.MOUSEMOTION:
                                    x,y = event.pos
                                    if pause_restart.rect.collidepoint(x,y):
                                        pause_restart=Picture('pics/pause_restart_light.png',620,325,50,50)
                                    elif not pause_restart.rect.collidepoint(x,y):
                                        pause_restart=Picture('pics/pause_restart.png',620,325,50,50)
                                        
                                    if pause_to_levels.rect.collidepoint(x,y):
                                        pause_to_levels=Picture('pics/pause_to_levels_light.png',702,325,50,50)
                                    elif not pause_to_levels.rect.collidepoint(x,y):
                                        pause_to_levels=Picture('pics/pause_to_levels.png',702,325,50,50)
                                        
                                    if pause_cont.rect.collidepoint(x,y):
                                        pause_cont=Picture('pics/pause_cont_light.png',537.5,325,50,50)
                                    elif not pause_cont.rect.collidepoint(x,y):
                                        pause_cont=Picture('pics/pause_cont.png',537.5,325,50,50)
                            clock.tick(40)
                            pygame.display.update()          
                                        
        lvl6_counter=lvl6_counter+1
        if lvl6_counter>600 and lvl6_score>5:#екран поразки був описаний вище
            lost=True
            while lost==True:
                losing_text.draw_text()
                lose_restart.draw_picture()
                lose_to_levels.draw_picture()
                                        
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        x,y = event.pos
                        if lose_restart.rect.collidepoint(x,y):
                            lost=False
                            lvl6_score=-6
                            lvl6_counter=0
                            wait1=0
                            wait2=0
                            wait3=0
                            wait4=0
                            wait5=0
                            wait6=0
                            screen='level6'
                        
                        if lose_to_levels.rect.collidepoint(x,y):
                            lost=False
                            lvl6_score=-6
                            lvl6_counter=0
                            wait1=0
                            wait2=0
                            wait3=0
                            wait4=0
                            wait5=0
                            wait6=0
                            screen='levels'
                            
                    if event.type == pygame.MOUSEMOTION:
                        x,y = event.pos
                        if lose_restart.rect.collidepoint(x,y):
                            lose_restart=Picture('pics/pause_restart_light.png',620,325,50,50)
                        elif not lose_restart.rect.collidepoint(x,y):
                            lose_restart=Picture('pics/pause_restart.png',620,325,50,50)
                                    
                        if lose_to_levels.rect.collidepoint(x,y):
                            lose_to_levels=Picture('pics/pause_to_levels_light.png',702,325,50,50)
                        elif not lose_to_levels.rect.collidepoint(x,y):
                            lose_to_levels=Picture('pics/pause_to_levels.png',702,325,50,50)
                            
                clock.tick(40)
                pygame.display.update()

        if lvl6_counter>600 and lvl6_score<=5:#екран перемоги був описаний вище
            win=True
            while win==True:
                winning_text.draw_text()
                win_restart.draw_picture()
                win_to_levels.draw_picture()
                                        
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        x,y = event.pos
                        if win_restart.rect.collidepoint(x,y):
                            win=False
                            lvl6_score=-6
                            lvl6_counter=0
                            wait1=0
                            wait2=0
                            wait3=0
                            wait4=0
                            wait5=0
                            wait6=0
                            money = money+50
                            f = open('money_save.txt','w')
                            f.write(str(money))
                            f.close()
                            screen='level6'
                        
                        if win_to_levels.rect.collidepoint(x,y):
                            win=False
                            lvl6_score=-6
                            lvl6_counter=0
                            wait1=0
                            wait2=0
                            wait3=0
                            wait4=0
                            wait5=0
                            wait6=0
                            money = money+50
                            f = open('money_save.txt','w')
                            f.write(str(money))
                            f.close()
                            screen='levels'
                            
                    if event.type == pygame.MOUSEMOTION:
                        x,y = event.pos
                        if win_restart.rect.collidepoint(x,y):
                            win_restart=Picture('pics/pause_restart_light.png',620,325,50,50)
                        elif not win_restart.rect.collidepoint(x,y):
                            win_restart=Picture('pics/pause_restart.png',620,325,50,50)
                                        
                        if win_to_levels.rect.collidepoint(x,y):
                            win_to_levels=Picture('pics/pause_to_levels_light.png',702,325,50,50)
                        elif not pause_to_levels.rect.collidepoint(x,y):
                            win_to_levels=Picture('pics/pause_to_levels.png',702,325,50,50)

                clock.tick(40)
                pygame.display.update()
        
        
        
        
        
        
        
        
    
    clock.tick(40)
    pygame.display.update()