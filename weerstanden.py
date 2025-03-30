from tkinter import *
import settings,Debug
import coordinaten_ui_weerstanden as cw
reeks_Weerstanden = []
standaard_weerstand_waarde = settings.standaard_waarde_weerstand

class Weerstanden_app():
    def __init__(self,window):
        
        self.window = window
        self.window.canvas = Canvas(self.window.root, width=cw.canvas_grote_x, height=cw.canvas_grote_y, bg="white")
        self.window.canvas.place(x=cw.canvas_x,y=cw.canvas_y)
        self.window.canvas.bind("<Button>", self.klik)
        self.window.canvas.bind("<B1-Motion>",self.verslepen)

        self.reset_button = Button(self.window.root,text="reset",command=self.clear)
        self.plus_button = Button(self.window.root,text="plus",command=self.plus_activated_fuctie)
        self.min_button = Button(self.window.root,text="min",command=self.min_activated_fuctie)
        self.button_serie = Button(self.window.root,text="serie",command=self.bereken_serie)
        self.button_parralel = Button(self.window.root,text="parralel",command=self.bereken_R)
        
        self.reset_button.place(x= cw.reset_knop_x,y=cw.reset_knop_y,width=cw.reset_knop_size_x,height=cw.reset_knop_size_y)
        self.plus_button.place(x= cw.plus_knop_x,y=cw.plus_knop_y,width=cw.plus_knop_size_x,height=cw.plus_knop_size_y)
        self.min_button.place(x= cw.min_knop_x,y=cw.min_knop_y,width=cw.min_knop_size_x,height=cw.min_knop_size_y)
        self.button_serie.place(x = cw.serie_knop_x,y = cw.serie_knop_y,height=cw.serie_knop_size_y,width=cw.serie_knop_size_x)
        self.button_parralel.place(x = cw.parralel_knop_x,y = cw.parralel_knop_y,height=cw.serie_knop_size_y,width=cw.serie_knop_size_x)
        

        self.input_frame = Frame(self.window.root,width=cw.input_breete_x,height=cw.input_breete_y,bd= 5, relief="groove") 
        self.input_frame.place(x=cw.input_box_x,y=cw.input_box_y)

        self.weerstand_waarde_input = Entry(window.root)
        self.U_waarde_input = Entry(window.root)
        self.I_waarde_input = Entry(window.root)

        self.weerstand_waarde_input.bind("<Return>",self.R_set_waarde)
        self.U_waarde_input.bind("<Return>",self.U_set_waarde)
        self.I_waarde_input.bind("<Return>",self.I_set_waarde)

        self.weerstand_waarde_input.focus()
        self.U_waarde_input.focus()
        self.I_waarde_input.focus()

        self.weerstand_waarde_input.place(x=cw.R_input_x,y=cw.R_input_y)
        self.U_waarde_input.place(x=cw.U_input_x,y=cw.U_input_y)
        self.I_waarde_input.place(x=cw.I_input_x,y=cw.I_input_y)

        self.R_text = Label(window.root,text="R :")
        self.U_text = Label(window.root,text="U :")
        self.I_text = Label(window.root,text="I :")

        self.R_text.place(x = cw.R_text_x, y = cw.R_text_y)
        self.U_text.place(x = cw.U_text_x, y = cw.U_text_y)
        self.I_text.place(x = cw.I_text_x, y = cw.I_text_y)

        # ------------------------------------------ BRON ---------------------------

    
        self.input_frame = Frame(self.window.root,width=cw.bron_input_breete_x,height=cw.bron_input_breete_y,bd= 5, relief="groove") 
        self.input_frame.place(x=cw.bron_input_box_x,y=cw.bron_input_box_y)


        self.bron_R_text = Label(window.root,text="Substitutie weerstand = 0Ω")
        self.bron_U_text = Label(window.root,text="Spanning = 0V")
        self.bron_I_text = Label(window.root,text="stroomsterkte = 0A")

        self.bron_R_text.place(x = cw.bron_R_text_x, y = cw.bron_R_text_y)
        self.bron_U_text.place(x = cw.bron_U_text_x, y = cw.bron_U_text_y)
        self.bron_I_text.place(x = cw.bron_I_text_x, y = cw.bron_I_text_y)








        
        self.var_binden = IntVar()
        self.button_binden = Checkbutton(self.window.root,text="binden",variable=self.var_binden,onvalue=True,offvalue=False,height = 2, width = 10)
        self.button_binden.place(x = cw.binden_x, y = cw.binden_y)
        self.binding_weerstand_temp = []
        self.window.canvas.bind("<Button>", self.klik)
    
        
        self.R = 0
        self.U = 0
        self.I = 0

        self.binding_lijnen = []
        self.gebonden_weerstanden = []
        self.plus_activated = False
        self.min_activated = False
        self.min = Min(window,settings.groote_min)
        self.plus = Plus(window,settings.groote_plus)
        self.geselecteerde_weerstand = None
        standaard_weerstand_waarde = settings.standaard_waarde_weerstand

    def plus_activated_fuctie(self):
        self.plus_activated = True
        print(f"self.plus_activated == {self.plus_activated}")

    def min_activated_fuctie(self):
        self.min_activated = True
        print(f"self.min_activated == {self.min_activated}")


    def draw_new_resistor(self,event):
        mogelijk = True
        # TODO hier beperking om niet op Plus/min pool te plaatsen 
        for weerstand in reeks_Weerstanden:
            x_cursor,y_cursor = event.x, event.y
            berijk_x = weerstand.berijk_x 
            berijk_y = weerstand.berijk_y 
            controle_x1 = berijk_x[0] - weerstand.size_x/2
            controle_x2 = berijk_x[1] + weerstand.size_x/2
            controle_y1 = berijk_y[0] - weerstand.size_y/2
            controle_y2 = berijk_y[1] + weerstand.size_y/2
            if Debug.weerstanden_draw:
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
        if len(reeks_Weerstanden) == 0 and not self.plus_activated and not self.min_activated:
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
                        self.delete_weerstand_binding(reeks_Weerstanden[i])
                        del reeks_Weerstanden[i]
                        self.reload()
                    if event.num == 1 and not self.var_binden.get(): # linker muisknop

                        self.verslepen_start(event,i)

                        weerstand = reeks_Weerstanden[i]
                        weerstand.omkader_resistor()
                        self.geselecteerde_weerstand = weerstand

                    if event.num == 2 or (event.num == 1 and self.var_binden.get()):
                        self.binding_weerstand_temp.append(reeks_Weerstanden[i])
                        for weerstand in self.binding_weerstand_temp:
                            if weerstand != "min" and weerstand != "plus":
                                weerstand.omkader_resistor()
                        self.controleer_temp_bindingen()
                
                
                min_voorwaarde_x = self.min.x - settings.weerstand_size_x/2< cursor_x < self.min.x + self.min.grote + settings.weerstand_size_x/2
                min_voorwaarde_y = self.min.y - self.min.grote/2 < cursor_y < self.min.y + self.min.grote/2
                
                plus_voorwaarde_x =  self.plus.x - settings.weerstand_size_x/2< cursor_x < self.plus.x + self.plus.grote + settings.weerstand_size_x/2
                plus_voorwaarde_y = self.plus.y - self.plus.grote/2 < cursor_y < self.plus.y + self.plus.grote/2

                if min_voorwaarde_x and min_voorwaarde_y:
                    op_weerstand = True
                    if event.num == 1 and not self.var_binden.get():
                        self.verslepen_start(event,"min")
                    elif event.num == 2 or (event.num == 1 and self.var_binden.get()):
                        self.binding_weerstand_temp.append("min")
                        self.controleer_temp_bindingen()
                        
                        
                elif plus_voorwaarde_x and plus_voorwaarde_y:
                    op_weerstand = True
                    if event.num ==1 and not self.var_binden.get():
                        self.verslepen_start(event,"plus")
                    elif event.num == 2 or (event.num == 1 and self.var_binden.get()):
                        self.binding_weerstand_temp.append("plus")
                        self.controleer_temp_bindingen()

            # TODO -> dedecteren van plus en min pool 
            if not op_weerstand and event.num == 1:
                if self.plus_activated:
                    self.plus.draw(event.x,event.y)
                    self.plus_activated = False
                elif self.min_activated:
                    self.min.draw(event.x,event.y)
                    self.min_activated = False
                else:
                    self.draw_new_resistor(event)
    
    def controleer_temp_bindingen(self):
        if len(self.binding_weerstand_temp) == 2:
            voorwaarde_niet_2x = self.binding_weerstand_temp[0] != self.binding_weerstand_temp[1]
            voorwaarde_niet_voorkomen = (self.binding_weerstand_temp not in self.gebonden_weerstanden) and ([self.binding_weerstand_temp[1],self.binding_weerstand_temp[0]] not in  self.gebonden_weerstanden)
            if voorwaarde_niet_2x and voorwaarde_niet_voorkomen:
                self.gebonden_weerstanden.append([self.binding_weerstand_temp[0],self.binding_weerstand_temp[1]])
            self.teken_bindingen()
            self.binding_weerstand_temp.clear()
        


    def verslepen_start(self,event,weerstand_nr):
        self.start_x = event.x
        self.start_y = event.y
        self.beweeg_weerstand_nr = weerstand_nr
    
    def verslepen(self,event):
        if self.beweeg_weerstand_nr is not None:
            dx = event.x - self.start_x
            dy = event.y - self.start_y
            self.start_x = event.x
            self.start_y = event.y
            if self.beweeg_weerstand_nr == "min":
                self.window.canvas.move(self.min.symbol,dx,dy)
                self.min.update_cordinates(dx,dy)
                xm = self.min.xm
                ym = self.min.ym
                verplaatste_element = "min"
            elif self.beweeg_weerstand_nr == "plus":
                self.window.canvas.move(self.plus.symbol_H,dx,dy)
                self.window.canvas.move(self.plus.symbol_v,dx,dy)
                self.plus.update_cordinates(dx,dy)
                xm = self.plus.xm
                ym = self.plus.ym
                verplaatste_element = "plus"
            else:
                weerstand = reeks_Weerstanden[self.beweeg_weerstand_nr]
                self.window.canvas.move(weerstand.weerstand_symbool,dx,dy)
                weerstand.update_coordinaten(dx,dy)
                xm = weerstand.xm
                ym = weerstand.ym
                verplaatste_element = weerstand

            for lijn in self.binding_lijnen:
                if verplaatste_element in lijn.binding:
                    plaats = lijn.binding.index(verplaatste_element)
                    if plaats == 0:
                        lijn.update(xm, ym, lijn.x2, lijn.y2)
                    elif plaats == 1:
                        lijn.update(lijn.x1, lijn.y1,xm, ym)
        self.reload()
        self.geselecteerde_weerstand = None

    def delete_weerstand_binding(self,weerstand_nr):
        if Debug.delete_weerstand_binding:
            print(f"Verwijderen weerstand: {weerstand_nr}")
            print(f"Bindings voor verwijderen: {self.gebonden_weerstanden}")
        self.gebonden_weerstanden = [
            binding for binding in self.gebonden_weerstanden
            if weerstand_nr not in binding
        ]
        self.reload()
        if Debug.delete_weerstand_binding:
            print(f"Bindings na verwijderen : {self.gebonden_weerstanden}")


    def teken_bindingen(self):
        for binding in self.gebonden_weerstanden:
            if Debug.delete_weerstand_binding:
                print(binding)
            R1, R2 = binding
            if Debug.plus_min_lijn:
                print(f"R1 = {R1}\n R2 = {R2}")
            
            if R1 == "min":
                x1 = self.min.xm
                y1 = self.min.ym
                x2 = R2.xm
                y2 = R2.ym
            elif R2 == "min":
                x2 = self.min.xm
                y2 = self.min.ym
                x1 = R1.xm
                y1 = R1.ym
            elif R1 == "plus":
                x1 = self.plus.xm
                y1 = self.plus.ym
                x2 = R2.xm
                y2 = R2.ym
            elif R2 == "plus":
                x2 = self.plus.xm
                y2 = self.plus.ym
                x1 = R1.xm
                y1 = R1.ym
            else:
                x1 = R1.xm
                y1 = R1.ym
                x2 = R2.xm
                y2 = R2.ym
            if Debug.plus_min_lijn:
                print(f"     x1 = {x1}\n     y1 = {y1}\n     x2 = {x2}\n     y2 = {y2}\n")
            lijn = Bindingslijn(self.window.canvas, x1, y1, x2, y2,binding,self)
            self.binding_lijnen.append(lijn)
            self.reload()
        if Debug.delete_weerstand_binding:
            print(f"Na teken_bindingen: {self.gebonden_weerstanden}")

    def R_set_waarde(self,event):
        if self.geselecteerde_weerstand is not None:
            waarde = self.weerstand_waarde_input.get()
            self.geselecteerde_weerstand.R = int(waarde)
            print(f"weerstand waarde = {self.geselecteerde_weerstand.R}")
            self.reload()
            self.reload_text()
        else:
            waarde = self.weerstand_waarde_input.get()
            global standaard_weerstand_waarde
            standaard_weerstand_waarde = int(waarde)

    def I_set_waarde(self,event):
        waarde = self.I_waarde_input.get()
        self.plus.I = int(waarde)
        print(f"stroomsterkte = {self.plus.I}")
        self.reload()
        self.reload_text()

    def U_set_waarde(self,event):
        waarde = self.U_waarde_input.get()
        self.plus.U = int(waarde)
        print(f"spanning = {self.plus.U}")
        self.reload( )
        self.reload_text()
    




        
    def bereken_serie(self):
        self.waarde_serie_weerstanden = 0
        te_overlopen_bindingen = self.gebonden_weerstanden[:]
        oude_weerstand = None

        for i, binding in enumerate(self.gebonden_weerstanden):
            if "plus" in binding:
                i_plus = binding.index("plus")
                if i_plus == 0:
                    start_weerstand = binding[1]
                elif i_plus == 1:
                    start_weerstand = binding[0]
                else:
                    print(f"ERROR binding = {binding}")
                te_overlopen_bindingen.pop(i)
                self.waarde_serie_weerstanden += start_weerstand.R
                oude_weerstand = start_weerstand
                break
        
        
        while te_overlopen_bindingen:
            for i, binding in enumerate(te_overlopen_bindingen):
                print(f"binding = {binding}")
                if oude_weerstand in binding:
                    i_oude_weerstand = binding.index(oude_weerstand)
                    if i_oude_weerstand ==0:
                        nieuwe_weerstand = binding[1]
                    elif i_oude_weerstand == 1:
                        nieuwe_weerstand = binding[0]
                    if nieuwe_weerstand == "min":
                        te_overlopen_bindingen = []
                    else:
                        te_overlopen_bindingen.remove(binding)
                        oude_weerstand = nieuwe_weerstand
                        self.waarde_serie_weerstanden += nieuwe_weerstand.R
                    break
        print(f"weerstandwaarde in serie = {self.waarde_serie_weerstanden}")
        print(f"stroomsterkte bron = {self.plus.bereken(self.waarde_serie_weerstanden)}")
        self.reload()
        self.reload_text()

    def bereken_parallel(self):
        weerstanden_parralel = []
        weerstand_waarde_parralel = 0
        for binding in self.gebonden_weerstanden:
            if "plus" in binding:
                i_plus = binding.index("plus")
                weerstanden_parralel.append(binding[1-i_plus])
        for weerstand in weerstanden_parralel:
            weerstand_waarde_parralel += 1/weerstand.R 
        print(1/weerstand_waarde_parralel)
        self.plus.bereken(1/weerstand_waarde_parralel)
        self.reload()
        self.reload_text()


    def bereken_R(self):
        weerstand_waarde = 0
        verbonden_met_plus = []
        for binding in self.gebonden_weerstanden:
            if 'plus' in binding:
                Index_plus = binding.index('plus')
                verbonden_met_plus.append(binding[1-Index_plus])
        if len(verbonden_met_plus) != 1:
            # parralel
            weerstand_waarde_temp = 0
            for weerstand in verbonden_met_plus:
                weerstand_waarde_temp += 1/weerstand.R
            weerstand_waarde = 1/weerstand_waarde_temp
        print(weerstand_waarde)



    
    def reload_text(self):
        self.bron_R_text = Label(self.window.root,text=f"Substitutie weerstand = {self.plus.R}Ω")
        self.bron_U_text = Label(self.window.root,text=f"Spanning = {self.plus.U}V")
        self.bron_I_text = Label(self.window.root,text=f"stroomsterkte = {self.plus.I}A")

        self.bron_R_text.place(x = cw.bron_R_text_x, y = cw.bron_R_text_y)
        self.bron_U_text.place(x = cw.bron_U_text_x, y = cw.bron_U_text_y)
        self.bron_I_text.place(x = cw.bron_I_text_x, y = cw.bron_I_text_y)


    def reload(self):
        self.window.canvas.delete("all")
        self.min.update()
        self.plus.update()
        for line in self.binding_lijnen:
            line.draw()
        for weerstand in reeks_Weerstanden:
            weerstand.draw_resistor()
        



    def clear(self):
        self.window.canvas.delete("all")
        reeks_Weerstanden.clear()
        self.binding_lijnen.clear()
        self.binding_weerstand_temp.clear()
        self.gebonden_weerstanden.clear()












class Bindingslijn():
    def __init__(self,canvas,x1,y1,x2,y2,binding = [],self_weerstand=None):
        self.canvas = canvas
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.lijn = self.canvas.create_line(x1,y1,x2,y2,width = 5)
        self.binding = binding
        self.weerstand_ap = self_weerstand
        #TODO -> lijnen verdwijnen als één van de binding paren niet meer bestaan
        # doen door gewoon te popen uit lijst 

    def update(self, x1, y1, x2, y2):
        self_weerstanden_ap = self.weerstand_ap
        self_weerstanden_ap.reload()
        self.canvas.coords(self.lijn, x1, y1, x2, y2)
        self.x1, self.y1, self.x2, self.y2 = x1, y1, x2, y2

    def controleer(self):
        for weerstand in self.binding:
            if weerstand not in reeks_Weerstanden and weerstand != "min" and weerstand != "plus" :
                return False
        return True
            
    
    def draw(self):
        if  self.controleer():
            self.lijn = self.canvas.create_line(self.x1,self.y1,self.x2,self.y2,width = 5)




class Min():
    def __init__(self,window,grote):
        self.self_window = window
        self.grote = grote
        self.x = -1000
        self.y = -1000
        self.dim = -11000101011010
        self.xm = None
    def draw(self,x,y):
        self.symbol = self.self_window.canvas.create_line(x,y,x+self.grote,y,width = settings.width_min)
        self.x = x
        self.y = y
        self.xm = x + self.grote/2
        self.ym = self.y + settings.width_min/2
    def update(self):
        x = self.x
        y = self.y
        self.symbol = self.self_window.canvas.create_line(x,y,x+self.grote,y,width = settings.width_min)
    def update_cordinates(self,dx,dy):
        self.x += dx
        self.y += dy 
        self.xm = self.x + self.grote/2
        self.ym = self.y + settings.width_min/2




class Plus():
    def __init__(self,window,grote):
        self.self_window = window
        self.grote = grote
        self.x = -1000
        self.y = -1000
        self.dim = self.grote/2
        self.ym = None
        self.xm = None
        self.U = 0
        self.I = 0
        self.R = 0
    def draw(self,x,y):
        self.x = x
        self.y = y
        dim = self.dim 
        self.symbol_H = self.self_window.canvas.create_line(x,y,x+ self.grote ,y, width = settings.width_plus)
        self.symbol_v = self.self_window.canvas.create_line(x+dim,y - dim ,x+dim,y +dim, width = settings.width_plus)
        self.xm = self.x + self.grote/2
        self.ym = self.y 
    
    def update(self):
        x = self.x
        y = self.y
        dim = self.dim
        self.symbol_H = self.self_window.canvas.create_line(x,y,x+ self.grote ,y, width = settings.width_plus)
        self.symbol_v = self.self_window.canvas.create_line(x+dim,y - dim ,x+dim,y +dim, width = settings.width_plus)
    
    def update_cordinates(self,dx,dy):
        self.x += dx
        self.y += dy
        self.xm = self.x + self.grote/2
        self.ym = self.y
    
    def bereken(self,R):
        if not self.U  is None:
            self.I = self.U / R
            self.R = R
            return self.I


class Weerstanden():
    def __init__(self,window):
        self.window = window
        self.R = standaard_weerstand_waarde
        print("nieuw")
        self.I = 10
        self.U = 10
    def create(self, waarde):
        self.waarde = waarde
    def draw_new_resistor(self,event):
        self.mogelijk = True
        self.size_x = settings.weerstand_size_x
        self.size_y = settings.weerstand_size_y
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
        self.weerstand_symbool = self.window.canvas.create_rectangle(self.x1,self.y1,self.x2,self.y2,fill = "red",width = 5)
        self.text = f"{self.R}Ω"
        self.window.canvas.create_text(self.x1 + settings.weerstand_size_x/2, self.y1 + settings.weerstand_size_y/2, text=self.text, font=("Arial", 14), fill="black")
    def omkader_resistor(self):
        self.weerstand_symbool = self.window.canvas.create_rectangle(self.x1,self.y1,self.x2,self.y2,fill = "red",outline='Green',width = 5)
        self.window.canvas.create_text(self.x1 + settings.weerstand_size_x/2, self.y1 + settings.weerstand_size_y/2, text=self.text, font=("Arial", 14), fill="black")


def nieuwe_weerstand(self_window):
    nieuwe_weerstand = Weerstanden(self_window)



def draw_weerstand(self_window):
    Label(self_window.root, text="test").grid(column=333, row=3)
    weerstanden_app = Weerstanden_app(self_window)
    