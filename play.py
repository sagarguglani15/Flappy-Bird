from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
root=Tk()
root.geometry('600x650')
root.title('Flappy Bird')
class Bird(Canvas):
    def __init__(self, **kw):
        super().__init__(width=600,height=650,highlightthickness=0,**kw)
        self.GAME_SPEED = 10
        self.JUMP_HEIGHT=40
        self.score=0
        self.show_instructions()
        self.after(30,self.highlight_heading)

    def highlight_heading(self):
        curr_head_color = self.itemcget(self.find_withtag('heading'), 'fill')
        if (curr_head_color == 'midnight blue'):
            self.itemconfigure(self.find_withtag('heading'), fill='dark green')
        elif (curr_head_color == 'dark green'):
            self.itemconfigure(self.find_withtag('heading'), fill='midnight blue')
        self.after(300,self.highlight_heading)

    def start_game(self):
        self.load_assets()
        self.after(150,self.move_tunnels)
        self.after(5000,self.increase_speed)
        self.after(30,self.move_bird)
        self.bind_all('<Key>',self.upbird)

    def increase_speed(self):
        if self.GAME_SPEED==0:
            return
        self.GAME_SPEED-=1
        self.JUMP_HEIGHT+=5
        self.after(6000,self.increase_speed)

    def load_assets(self):
        self.bx=100
        self.by=300
        self.bird=Image.open('Assets/bird.png')
        self.birdtk=ImageTk.PhotoImage(self.bird)
        self.birdid=self.create_image(100,100,image=self.birdtk,tag='bird')

        self.tunnel_up = Image.open('Assets/tunnel_up.png')
        self.tunnel_up_tk = ImageTk.PhotoImage(self.tunnel_up)

        self.tunnel_down = Image.open('Assets/tunnel_down.png')
        self.tunnel_down_tk = ImageTk.PhotoImage(self.tunnel_down)

        self.x1=400
        self.yu1=570
        self.yd1=110
        self.create_image(400, 570, image=self.tunnel_up_tk,tag='tunnelup1')
        self.create_image(400, 110,image=self.tunnel_down_tk,tag='tunneldown1')
        self.x2 = 650
        self.yu2 = 500
        self.yd2 = 40
        self.create_image(650, 500, image=self.tunnel_up_tk, tag='tunnelup2')
        self.create_image(650, 40, image=self.tunnel_down_tk, tag='tunneldown2')
        self.x3 = 900
        self.yu3 = 550
        self.yd3 = 90
        self.create_image(900, 550, image=self.tunnel_up_tk, tag='tunnelup3')
        self.create_image(900, 90, image=self.tunnel_down_tk, tag='tunneldown3')
        self.x4 = 1150
        self.yu4 = 530
        self.yd4 = 70
        self.create_image(1150, 530, image=self.tunnel_up_tk, tag='tunnelup4')
        self.create_image(1150, 70, image=self.tunnel_down_tk, tag='tunneldown4')
        self.x5 = 1400
        self.yu5 = 630
        self.yd5 = 170
        self.create_image(1400, 630, image=self.tunnel_up_tk, tag='tunnelup5')
        self.create_image(1400, 170, image=self.tunnel_down_tk, tag='tunneldown5')

        self.create_text(500, 70, text=f'Score: {self.score}', fill='black', font='abc 15 bold', tag='score')
        self.create_text(300, 50, text='FLAPPY BIRD', fill='midnight blue', tag='heading', font='Abc 25 bold')

    def move_tunnels(self):
        if self.GAME_SPEED==0:
            return

        if self.x1 <=20:
            self.x1=1300
            self.score+=1
        else:
            self.x1-=1

        if self.x2 <=20:
            self.x2=1300
            self.score+=1
        else:
            self.x2-=1

        if self.x3 <=20:
            self.x3=1300
            self.score+=1
        else:
            self.x3-=1

        if self.x4 <=20:
            self.x4=1300
            self.score+=1
        else:
            self.x4-=1

        if self.x5 <=20:
            self.x5=1300
            self.score+=1
        else:
            self.x5-=1

        self.coords(self.find_withtag('tunnelup1'),(self.x1,self.yu1))
        self.coords(self.find_withtag('tunneldown1'), (self.x1,self.yd1))
        self.coords(self.find_withtag('tunnelup2'), (self.x2, self.yu2))
        self.coords(self.find_withtag('tunneldown2'), (self.x2, self.yd2))
        self.coords(self.find_withtag('tunnelup3'), (self.x3, self.yu3))
        self.coords(self.find_withtag('tunneldown3'), (self.x3, self.yd3))
        self.coords(self.find_withtag('tunnelup4'), (self.x4, self.yu4))
        self.coords(self.find_withtag('tunneldown4'), (self.x4, self.yd4))
        self.coords(self.find_withtag('tunnelup5'), (self.x5, self.yu5))
        self.coords(self.find_withtag('tunneldown5'), (self.x5, self.yd5))

        self.itemconfigure(self.find_withtag('score'), text=f'Score: {self.score}')
        self.after(self.GAME_SPEED,self.move_tunnels)

    def move_bird(self):
        self.check_collisions()
        if self.GAME_SPEED==0:
            return
        self.by+=3
        self.coords(self.find_withtag('bird'),(self.bx,self.by))
        self.after(30,self.move_bird)

    def upbird(self,e):
        if self.GAME_SPEED==0:
            return
        key_input=e.keysym
        if key_input=='space':
            self.by-=self.JUMP_HEIGHT

    def check_collisions(self):
        up1=self.bbox(self.find_withtag('tunnelup1'))
        up1=self.find_overlapping(up1[0]+155, up1[1]+20, up1[2]-140, up1[3])
        up2 = self.bbox(self.find_withtag('tunnelup2'))
        up2 = self.find_overlapping(up2[0]+155, up2[1]+20, up2[2]-140, up2[3])
        up3 = self.bbox(self.find_withtag('tunnelup3'))
        up3 = self.find_overlapping(up3[0]+155, up3[1]+20, up3[2]-140, up3[3])
        up4 = self.bbox(self.find_withtag('tunnelup4'))
        up4 = self.find_overlapping(up4[0]+155, up4[1]+20, up4[2]-140, up4[3])
        up5 = self.bbox(self.find_withtag('tunnelup5'))
        up5 = self.find_overlapping(up5[0]+155, up5[1]+20, up5[2]-140, up5[3])
        d1 = self.bbox(self.find_withtag('tunneldown1'))
        d1 = self.find_overlapping(d1[0]+155, d1[1], d1[2]-140, d1[3]-20)
        d2 = self.bbox(self.find_withtag('tunneldown2'))
        d2 = self.find_overlapping(d2[0]+155, d2[1], d2[2]-140, d2[3]-20)
        d3 = self.bbox(self.find_withtag('tunneldown3'))
        d3 = self.find_overlapping(d3[0]+155, d3[1], d3[2]-140, d3[3]-20)
        d4 = self.bbox(self.find_withtag('tunneldown4'))
        d4 = self.find_overlapping(d4[0]+155, d4[1], d4[2]-140, d4[3]-20)
        d5 = self.bbox(self.find_withtag('tunneldown5'))
        d5 = self.find_overlapping(d5[0]+155, d5[1], d5[2]-140, d5[3]-20)

        global obj
        if self.by>=630 or self.by<=5 or 10 in up1 or 10 in up2 or 10 in up3 or 10 in up4 or 10 in up5 or \
                10 in d1 or 10 in d2 or 10 in d3 or 10 in d4 or 10 in d5:
            self.GAME_SPEED=0
            try:
                choice = messagebox.askyesno('Game Over', f'Your Score: {self.score}\nPlay Again?')
                if choice:
                    obj.place_forget()
                    obj=Bird()
                    obj.place(x=0,y=0)
            except:
                pass

    def end_inst(self, e):
        if e.keysym=='Return' or e.keysym=='KP_Enter':

            self.delete(self.find_withtag('it2'), self.find_withtag('it1'), self.find_withtag('it3'),
                        self.find_withtag('it4'), self.find_withtag('heading'),
                        self.find_withtag('it5'), self.find_withtag('it6'), self.find_withtag('it7'))
            self.start_game()

    def show_instructions(self):
        self.bg = Image.open('Assets/bg.png')
        self.bgtk = ImageTk.PhotoImage(self.bg)
        self.create_image(0, 300, image=self.bgtk)

        self.create_text(300,50,text='FLAPPY BIRD', fill='midnight blue', tag='heading', font='Abc 25 bold')

        self.create_text(100, 100, text='Instructions: ', fill='black', font='Abc 15 bold', tag='it1')
        self.create_text(300, 150, text='1. You are Mrs. Birdie and you need to\n\t meet Mr. Bird.',
                         fill='red',font='Abc 15 bold', tag='it2')
        self.create_text(290, 220, text='2. But Mr. Bird is behind 100 tunnels.', fill='purple',
                         font='Abc 15 bold', tag='it3')
        self.create_text(320, 290, text='3. You have to protect yourself from hiting\n\t these tunnels.', fill='red',
                         font='Abc 15 bold', tag='it4')
        self.create_text(300, 360, text='4. The gravity shall pull you down but\n       you can fly by pressing Space Bar',
                         fill='purple', font='Abc 15 bold', tag='it5')
        self.create_text(280, 420, text='5. Press enter to start the game.', fill='red', font='Abc 15 bold', tag='it6')
        self.create_text(400, 460, text='Best of Luck !', fill='white',
                         font='Abc 15 bold', tag='it7')
        self.bind_all('<Key>',self.end_inst)


global obj
obj=Bird()
obj.place(x=0,y=0)
root.mainloop()