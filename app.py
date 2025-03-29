from tkinter import*
import overschrijven_app 
import weerstanden

class Window():
    def __init__(self):
        self.root = Tk()
        self.set_up_overschrijven()
        self.set_up()
        self.weerstanden()
        self.root.state('zoomed')
        self.root.mainloop()  # mainloop() wordt maar één keer aangeroepen -> moet laatst
        

    def set_up(self):
        root = self.root
        menu = Menu(root)
        root.config(menu=menu)
        file_menu = Menu(menu)
        menu.add_command(label="Home", command=self.startpage)
        menu.add_cascade(label='navigate',menu=file_menu)
        file_menu.add_command(label='overschrijven',command=self.overschrijven)
        file_menu.add_command(label='weerstanden',command=self.weerstanden)
        file_menu.add_separator()
        file_menu.add_command(label='Exit', command=root.quit)
        info_menu = Menu(menu)
        menu.add_cascade(label="info",menu=info_menu)
        info_menu.add_command(label='gemaakt door Casper Vanbeselaere',)
        

    def startpage(self):
        self.clear_wondow()
        root = self.root
        root.title("Home Page")
        Label(self.root, text="Start page!").grid(column=0, row=0)
        
    def overschrijven(self):
        self.clear_wondow()
        root = self.root
        root.title("overschrijven")
        Label(self.root, text="Overschrijven").grid(column=0, row=0)
        Label(self.root,text = self.woord ).grid(column=0,row=1)
        print(f"woord = {self.woord}")

        user_input = Entry(root)
        user_input.grid(row=5,column=0)
        user_input.bind("<Return>",self.is_zelfde_overschrijven)
        self.user_input = user_input
        
        button_new_word = Button(root, text="V", command= self.set_word_overschrijven)
        button_new_word.grid(row=5,column=1)

        button_new_log = Button(root,text="new Log", command=self.new_file_helper)
        button_new_log.grid(row=5,column=2)
        

        user_input.focus()
        groot_lettertype = ("Arial", 20)
        listbox = Listbox(root, height= self.groote_list, width= 20, bg="grey", activestyle="dotbox",font= groot_lettertype, fg = "yellow")
        ansors = self.ansors


        kleuren = []
        for i in range(self.groote_list):
            getal_waarde = len(ansors) -self.groote_list + i
            #print(f"getalwaaarde: {getal_waarde}, index {i}")
            if self.juist[getal_waarde] == True:
                color = "Green"
            elif self.juist[len(ansors) -self.groote_list + i] == False:
                color = "Red"
            else:
                color = "Blue"
            kleuren.append(color)
            if len(kleuren) > 5:
                kleuren.remove[1]
            listbox.insert(i+1,str(ansors[getal_waarde]))
        listbox.grid(column=0,row=2)
        for i in range(self.groote_list):
            listbox.itemconfig(i,foreground= kleuren[i])
        self.root.tk.call('tk', 'scaling', 5.0)
        
    def new_file_helper(self):
        overschrijven_app.make_new_file()

    def set_up_overschrijven(self):
        self.groote_list = 5
        self.woord = ""
        self.ansors = []
        self.juist = []
        for i in range(self.groote_list):
            self.ansors.append("")
            self.juist.append(None)
        print(self.juist)
    def clear_box_overschrijven(self):
        self.user_input.delete(0,END)

    def set_word_overschrijven(self, event = None):
        self.woord = self.user_input.get()
        overschrijven_app.set_word(self.woord)
        self.clear_box_overschrijven()
        self.overschrijven()
    
    def is_zelfde_overschrijven(self,event = None):
        ansor = self.user_input.get()
        ansors = self.ansors
        ansors.append(ansor)
        self.ansors = ansors
        overschrijven_evaluatie = overschrijven_app.controleer(self.woord,ansor)
        self.juist.append(overschrijven_evaluatie)
        print(f"list met inputs: {ansors}"f"lijst met correctie: {self.juist}")
        self.clear_box_overschrijven()
        self.overschrijven()
        
    def print_waarde(self,event = None):
        waarde = self.user_input.get()
        print(f"Opgeslagen: {waarde}")
        self.clear_box_overschrijven()
        self.overschrijven()
    
   
        
    def weerstanden(self):
        self.clear_wondow() 
        root = self.root
        Label(self.root, text="Weerstanden").grid(column=0, row=0)
        root.title("Weerstanden")
        weerstanden.draw_weerstand(self)
        
        
    def copirite(self):
        print("Casper Vanbeselaere")
    

    def clear_wondow(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        self.set_up()

