from tkinter import *
import tkinter.scrolledtext as tkscrolled
import Predict


class App(Tk):
    # Instances for suggest list,text box,suggest box
    suggestion_dict = []
    scr = None
    scr1 = None
    limit =None

    def __init__(self):
        super().__init__()
        self.setup()
        self.boxes()

    #setup window
    def setup(self):
        self.title("Word Prediction")
        self.geometry("1280x720")
        #Max, min size of window
        self.maxsize(1280, 720)
        self.minsize(1280, 720)
        self.configure(background="#e0e0e0")

    # Update the listbox
    def update(self,data):
        self.scr1.delete(0, END)
        count = 0
        m=self.limit.get()
        print(m)
        for item in data[:m]:
            self.scr1.insert(END, item)

    #Bind the listbox to check
    def check(self):
        self.deploy()
        typed = self.scr.get('insert -1c wordstart', 'insert')
        print(typed)
        try:
            if typed == "":
                data = []
            else:
                data = []
                for item in self.suggestion_dict:
                    #The condition is to search the most similar between the two

                    data.append(item)
            self.update(data)
        except:
            pass

    #Bind the ListBoxSelect to fill in the text box
    def fillout(self,e):
        #self.scr.delete("insert-1c wordstart", "insert")  (delete a whole word in insert mouse)

        #Insert word after the insert mouse
        self.scr.insert("insert wordstart"," "+self.scr1.get(ANCHOR)+" ")
        self.scr1.delete(0,END)

    def deploy(self):
        try:
            m =self.scr.get('insert -1c wordstart', 'insert')
            #print(m)
            self.suggestion_dict = Predict.Predict_Next_Words(m,self.limit.get())
            print(self.suggestion_dict)
        except:
            print("Deploy error")

    #Create Frame, textbox, listbox, slideBar, button
    def boxes(self):

        #Frame
        top_frame = Frame(self, width=1280, height=720)
        top_frame.pack(side = TOP,expand=YES)

        #Slide Bar limit
        labelLimit = Label(top_frame,text = "1  / 2  / 3  / 4  / 5", font =(20))
        labelLimit.pack(side = TOP,expand=YES)

        self.limit = Scale(top_frame,from_= 1, to = 5, orient = 'horizontal',width=20,length = 200)
        self.limit.pack(side = TOP,expand=YES)

        #Text box
        Label1 = Label(top_frame, text = "Type a word and press space to get suggestions", font =(20))

        Label1.pack(side = TOP,expand=YES)
        self.scr = tkscrolled.ScrolledText(top_frame,width=50,height=7,font =(20))
        self.scr.pack(side = TOP,expand=YES)

        #Preict Button
        button = Button(top_frame, text = "Predict", command = self.check)
        button.pack(side = TOP,expand=YES)

        # Listbox
        self.scr1 = Listbox(top_frame, width=80, height=10)
        self.scr1.pack(side=TOP, expand=YES)
        self.scr1.bind("<<ListboxSelect>>", self.fillout)

#run main
if __name__ == '__main__':
    root = App()
    root.mainloop()
