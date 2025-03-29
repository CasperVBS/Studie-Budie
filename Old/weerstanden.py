from tkinter import *
import settings
reeks_Weerstanden = []

class Weerstanden_app():
    def __init__(self,window):
        self.window = window
        self.window.canvas = Canvas(self.window.root, width=1000, height=600, bg="white")
        self.window.canvas.grid(column=0,row=0)
        self.window.canvas.bind("<Button>", self.klik)
        self.window.canvas.bind("<B1-Motion>",self.verslepen)


        self.reset_button = Button(self.window.root,text="reset",command=self.clear)
        self.reset_button.grid(row=0, column=1)
        self.binding_weerstand_temp = []
        self.gebonden_weerstanden = []
        self.binding_lijnen = []

    def draw_new_resistor(self,event):
        mogelijk = True
        for weerstand in reeks_Weerstanden:
            x_cursor,y_cursor = event.x, event.y
            berijk_x = weerstand.berijk_x 
            berijk_y = weerstand.berijk_y 
            controle_x1 = berijk_x[0] - weerstand.size_x/2
            controle_x2 = berijk_x[1] + weerstand.size_x/2
            controle_y1 = berijk_y[0] - weerstand.size_y/2
            controle_y2 = berijk_y[1] + weerstand.size_y/2
            if settings.weerstanden_draw_debug:
                print(f"cursorx = {x_cursor}\n"
                    f"cursory = {y_cursor}\n"
                    f"berijk_x = {berijk_x}\n"
                    f"berijk_y = {berijk_y}\n")
            if controle_x1 <= x_cursor <= controle_x2 and controle_y1 <= y_cursor <= controle_y2:
                mogelijk = False
                break
        if mogelijk:
            reeks_Weerstanden.append(Weerstanden(self.window))
            weerstand_temp = reeks_Weerstanden[-1]
            weerstand_temp.draw_new_resistor(event)
            
    def klik(self,event):
        self.beweeg_weerstand_nr = None
        op_weerstand = False
        cursor_x = event.x
        cursor_y = event.y
        if len(reeks_Weerstanden) == 0:
            self.draw_new_resistor(event)
        else:
            for i, weerstand in enumerate(reeks_Weerstanden):
                x_begin, x_eind = weerstand.berijk_x
                y_begin, y_eind = weerstand.berijk_y
                if x_begin <= cursor_x <= x_eind and y_begin <= cursor_y <= y_eind:
                    op_weerstand = True
                    print("KLIK")
                    print(event.num)
                    if event.num == 3: # rechter muisknop 
                        del reeks_Weerstanden[i]
                        self.reload()
                        
                    elif event.num == 1: # linker muisknop
                        self.verslepen_start(event,i) 
                    
                    elif event.num == 2:
                        self.binding_weerstand_temp.append(i)
                        print(self.binding_weerstand_temp)
                        if len(self.binding_weerstand_temp) == 2:
                            self.gebonden_weerstanden.append(self.binding_weerstand_temp)
                            self.teken_bindingen()
                            self.binding_weerstand_temp.clear()
                    break
            if not op_weerstand and event.num == 1:
                self.draw_new_resistor(event)
    

    def verslepen_start(self,event,weerstand_nr):
        self.start_x = event.x
        self.start_y = event.y
        self.beweeg_weerstand_nr = weerstand_nr
    
    def verslepen(self,event):
        if self.beweeg_weerstand_nr is not None:
            weerstand = reeks_Weerstanden[self.beweeg_weerstand_nr]
            dx = event.x - self.start_x
            dy = event.y - self.start_y
            self.start_x = event.x
            self.start_y = event.y

            self.window.canvas.move(weerstand.weerstand_symbool,dx,dy)

            weerstand.update_coordinaten(dx,dy)

            for lijn in self.binding_lijnen:
                if lijn.x1 == weerstand.xm and lijn.y1 == weerstand.ym:
                    lijn.update(weerstand.xm, weerstand.ym, lijn.x2, lijn.y2)

                elif lijn.x2 == weerstand.xm and lijn.y2 == weerstand.ym:
                    lijn.update(lijn.x1, lijn.y1, weerstand.xm, weerstand.ym)


    def teken_bindingen(self):
        for binding in self.gebonden_weerstanden:
            print(binding)
            R1_nr, R2_nr = binding
            R1 = reeks_Weerstanden[R1_nr]
            R2 = reeks_Weerstanden[R2_nr]
            x1 = R1.xm
            y1 = R1.ym
            x2 = R2.xm
            y2 = R2.ym
            lijn = Bindingslijn(self.window.canvas, x1, y1, x2, y2)
            self.binding_lijnen.append(lijn)


        



    def reload(self):
        self.window.canvas.delete("all")
        for weerstand in reeks_Weerstanden:
            weerstand.draw_resistor()

    def clear(self):
        print("CLEAR")
        self.window.canvas.delete("all")
        reeks_Weerstanden.clear()
        self.binding_lijnen.clear()
        self.binding_weerstand_temp.clear()
        self.gebonden_weerstanden.clear()
        print(reeks_Weerstanden)


class Bindingslijn():
    def __init__(self,canvas,x1,y1,x2,y2):
        self.canvas = canvas
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.lijn = self.canvas.create_line(x1,y1,x2,y2)

    def update(self, x1, y1, x2, y2):
        print("update")
        self.canvas.coords(self.lijn, x1, y1, x2, y2)
        self.x1, self.y1, self.x2, self.y2 = x1, y1, x2, y2
        


class Weerstanden():
    def __init__(self,window):
        pass
        self.window = window
    def create(self, waarde):
        self.waarde = waarde
    def draw_new_resistor(self,event):
        self.mogelijk = True
        self.size_x = 100
        self.size_y = 40
        self.x1 = event.x - self.size_x /2
        self.y1 = event.y - self.size_y /2
        self.x2 = self.x1 + self.size_x 
        self.y2 = self.y1 + self.size_y 
        self.berijk_x = (self.x1,self.x2)
        self.berijk_y = (self.y1,self.y2)
        self.xm = (self.x1 + self.x2) / 2
        self.ym = (self.y1 + self.y2) / 2
        self.draw_resistor()
    
    def update_coordinaten(self, dx, dy):
        self.x1 += dx
        self.x2 += dx
        self.y1 += dy
        self.y2 += dy
        self.berijk_x = (self.x1, self.x2)
        self.berijk_y = (self.y1, self.y2)
        self.xm = (self.x1 + self.x2) / 2
        self.ym = (self.y1 + self.y2) / 2

    def draw_resistor(self):
        self.weerstand_symbool = self.window.canvas.create_rectangle(self.x1,self.y1,self.x2,self.y2,fill = "white",width = 5)


def nieuwe_weerstand(self_window):
    nieuwe_weerstand = Weerstanden(self_window)



def draw_weerstand(self_window):
    Label(self_window.root, text="test").grid(column=3, row=3)
    print("draw_weerstanden gerund")
    weerstanden_app = Weerstanden_app(self_window)
    