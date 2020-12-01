import getch
import os
import sys
from math import floor


NORMAL = "\033[0;0m"
BLACK   = "\033[0;30m"
RED   = "\033[0;31m"  
GREEN = "\033[0;32m"
YELLOW = "\033[0;33m"
BLUE  = "\033[0;34m"
PINK =  "\033[0;35m"
CYAN  = "\033[0;36m"

INVERT_NORMAL = "\033[30;7m"
INVERT_BLACK = "\033[30;40m"
INVERT_RED = "\033[30;41m"
INVERT_GREEN = "\033[30;42m"
INVERT_YELLOW = "\033[30;43m"
INVERT_BLUE = "\033[30;44m"
INVERT_PINK = "\033[30;45m"
INVERT_CYAN = "\033[30;46m"


colors_list = [NORMAL, BLACK,RED,GREEN,YELLOW,BLUE,PINK,CYAN]
invert_list = [INVERT_NORMAL,INVERT_BLACK,INVERT_RED,INVERT_GREEN,INVERT_YELLOW,INVERT_BLUE,INVERT_PINK,INVERT_CYAN]

class Menu_Box:
    def __init__(self, x_size, y_size, **kargs):
        # Build Grid
        y = []
        y_color = []
        y_index = 0
        try:
             color = kargs['color']
        except:
            color = NORMAL

        while (y_index < y_size):
            x_color = [color]
            if (y_index == 0):
                x = ["╔"]
            elif (y_index == y_size-1):
                x = ["╚"]
            else:
                x = ["║"]

            for i in range(0,x_size-2):
                x_color.append(color)
                if (y_index == 0) or (y_index == y_size-1):
                    x.append('═')
                else:
                    x.append(' ')

            x_color.append(color)        
            if (y_index == 0):
                x.append("╗")
            elif (y_index == y_size-1):
                x.append("╝")
            else:
                x.append("║")

            y_index += 1
            y.append(x)
            y_color.append(x_color)

        self.screen = y
        self.screen_color = y_color
        self.box_options = {}
        self.color = color
        try:
            title = kargs['title']
            self.add_box(0,0,x_size-1,2,title,[],color)
        except:
            pass

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def display(self):
        self.clear_screen()
        i = 0
        while (i < len(self.screen)):
            j = 0
            while (j < len(self.screen[i])):
                sys.stdout.write(self.screen_color[i][j])
                print(self.screen[i][j], end="")
                j+=1
            print("")
            i+=1
        sys.stdout.write(NORMAL)

    def invert_color(self,color):
        i = 0
        while i < len(colors_list):
            if colors_list[i] == color:
                invert_color = invert_list[i]
                break
            elif invert_list[i] == color:
                invert_color = colors_list[i]
                break
            else:
                i+=1
        return invert_color
            
    def add_box(self, x_start, y_start, x_size, y_size, title, options, color=NORMAL):
        if self.screen[y_start][x_start] == "║":
            self.screen[y_start][x_start] = "╠"
        elif self.screen[y_start][x_start] == "═":
            self.screen[y_start][x_start] = "╦"
        else:
            self.screen[y_start][x_start] = "╔"
        self.screen_color[y_start][x_start] = color

        if self.screen[y_start+y_size][x_start] == "║":
            self.screen[y_start+y_size][x_start] = "╠"
        elif self.screen[y_start+y_size][x_start] == "═":
            self.screen[y_start+y_size][x_start] = "╩"
        else:
            self.screen[y_start+y_size][x_start] = "╚"
        self.screen_color[y_start+y_size][x_start] = color
        

        for i in range (y_start+1, y_start+y_size):
            self.screen[i][x_start] = "║"
            self.screen_color[i][x_start] = color
            self.screen[i][x_start+x_size] = "║"
            self.screen_color[i][x_start+x_size] = color
        
        for i in range (x_start+1, x_start+x_size):
            self.screen[y_start][i] = "═"
            self.screen_color[y_start][i] = color
            self.screen[y_start+y_size][i] = "═"
            self.screen_color[y_start+y_size][i] = color

        if self.screen[y_start][x_start+x_size] == "║":
            self.screen[y_start][x_start+x_size] = "╣"
        elif self.screen[y_start][x_start+x_size] == "═":
            self.screen[y_start][x_start+x_size] = "╦"
        else:
            self.screen[y_start][x_start+x_size] = "╗"
        self.screen_color[y_start][x_start+x_size] = color

        if self.screen[y_start+y_size][x_start+x_size] == "║":
            self.screen[y_start+y_size][x_start+x_size] = "╣"
        elif self.screen[y_start+y_size][x_start+x_size] == "═":
            self.screen[y_start+y_size][x_start+x_size] = "╩"
        else:
            self.screen[y_start+y_size][x_start+x_size] = "╝"
        self.screen_color[y_start+y_size][x_start+x_size] = color

        for i in range(0, y_size-3):
            if (i < len(options)):
                j = 0
                while (j < x_size-1):
                    if (i==0):
                        self.screen_color[y_start+3+i][x_start+1+j] = color
                    if  (j < len(options[i])):
                        self.screen[y_start+3+i][x_start+1+j] = options[i][j]
                        if i == 0:
                           self.screen_color[y_start+3+i][x_start+1+j] = self.invert_color(color) 
                        else:
                            self.screen_color[y_start+3+i][x_start+1+j] = color
                    else:
                        self.screen[y_start+3+i][x_start+1+j] = ' '
                        if i == 0:
                            self.screen_color[y_start+3+i][x_start+1+j] = self.invert_color(color)
                        else:
                            self.screen_color[y_start+3+i][x_start+1+j] = color
                    j+=1
  
        self.screen[y_start+2][x_start] = "╟"
        self.screen_color[y_start+2][x_start] = color
        self.screen[y_start+2][x_start+x_size] = "╢"
        self.screen_color[y_start+2][x_start+x_size] = color

        for i in range(0, x_size-1):
            self.screen[y_start+2][x_start+1+i] = '─'
            self.screen_color[y_start+2][x_start+1+i] = color

        i = 0
        if len(title) < x_size-2:
            offset = floor((x_size - len(title) - 2)/2) + 1
        else:
            offset = 1
        while (i < x_size-1) and (i < len(title)):
            self.screen[y_start+1][x_start+offset+i] = title[i]
            self.screen_color[y_start+1][x_start+offset+i] = color
            i += 1
        self.box_options[title] = {'options':options}
        self.box_options[title]['x_start']= x_start+1
        self.box_options[title]['x_size']= x_size
        self.box_options[title]['y_size']= y_size
        self.box_options[title]['y_start']= y_start+3
        self.box_options[title]['selected'] = 0
        self.selected = title

    def get_input(self):
        old_input = ''
        print(self.box_options[self.selected]['options'][self.box_options[self.selected]['selected']])
        while True:
            usr_input = getch.getch()
            if old_input == '[':
                if usr_input == 'A':
                    if self.box_options[self.selected]['selected'] > 0:
                        for i in range(0,self.box_options[self.selected]['x_size']-1):
                            self.screen_color[self.box_options[self.selected]['y_start']+self.box_options[self.selected]['selected']][self.box_options[self.selected]['x_start']+i] = \
                                self.invert_color(self.screen_color[self.box_options[self.selected]['y_start']+self.box_options[self.selected]['selected']][self.box_options[self.selected]['x_start']+i])
                            self.display()
                        self.box_options[self.selected]['selected'] -= 1
                        for i in range(0,self.box_options[self.selected]['x_size']-1):
                            self.screen_color[self.box_options[self.selected]['y_start']+self.box_options[self.selected]['selected']][self.box_options[self.selected]['x_start']+i] = \
                                self.invert_color(self.screen_color[self.box_options[self.selected]['y_start']+self.box_options[self.selected]['selected']][self.box_options[self.selected]['x_start']+i])
                            self.display()
                elif usr_input == 'B':
                    if self.box_options[self.selected]['selected'] < len(self.box_options[self.selected]['options'])-1:
                        for i in range(0,self.box_options[self.selected]['x_size']-1):
                            self.screen_color[self.box_options[self.selected]['y_start']+self.box_options[self.selected]['selected']][self.box_options[self.selected]['x_start']+i] = \
                                self.invert_color(self.screen_color[self.box_options[self.selected]['y_start']+self.box_options[self.selected]['selected']][self.box_options[self.selected]['x_start']+i])
                            self.display()
                        self.box_options[self.selected]['selected'] += 1
                        for i in range(0,self.box_options[self.selected]['x_size']-1):
                            self.screen_color[self.box_options[self.selected]['y_start']+self.box_options[self.selected]['selected']][self.box_options[self.selected]['x_start']+i] = \
                                self.invert_color(self.screen_color[self.box_options[self.selected]['y_start']+self.box_options[self.selected]['selected']][self.box_options[self.selected]['x_start']+i])
                            self.display()
            old_input = usr_input
            if usr_input == '\n' or usr_input == '\t':
                pass

            elif usr_input == 'q':
                sys.stdout.write("\033[?25h")
                sys.stdout.flush()
                print(self.box_options[self.selected]['options'][self.box_options[self.selected]['selected']])
                for i in self.box_options:
                    if i != 'Password Manager':
                        print(i)
                break

if __name__ == "__main__":
    title = "Password Manager"
    box = Menu_Box(80,40, title=title, color=BLUE)
    box.add_box(1,3,10,35,"Test",['one','two','three','four'], color=GREEN)
    box.add_box(12,3,15,35,"Second One",['opt 1','opt 2','opt 3','opt 4','opt 5','opt 6'], color=PINK)
    box.display()
    box.get_input()