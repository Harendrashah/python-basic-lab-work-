import tkinter
from tkinter import messagebox

class GUI:
    def _init_(self):

        self.mw = tkinter.Tk()
        self.mw.title("BMI Caluclator")
        self.mw.geometry("300x125")

        self.labelint = tkinter.IntVar()
        self.labelint.set("")

        self.topframe = tkinter.Frame(self.mw)
        self.midframe = tkinter.Frame(self.mw)
        self.bottomframe = tkinter.Frame(self.mw)
        self.botframe = tkinter.Frame(self.mw)
        
        self.label1 = tkinter.Label(self.topframe, text = "height")
        self.height = tkinter.Entry(self.topframe, width = 30 )
        self.label2 = tkinter.Label(self.topframe, text = "(mtr)")

        self.label3 = tkinter.Label(self.topframe, text = "weight")
        self.weight = tkinter.Entry(self.topframe, width = 30)
        self.label4 = tkinter.Label(self.topframe, text = "(kg)")

        self.radio1 = tkinter.Radiobutton(self.midframe, text ="Male" ,value = 1)
        self.radio2 = tkinter.Radiobutton(self.midframe, text ="Female", value = 2)

        self.button1 = tkinter.Button(self.bottomframe,text = "Calculate", command = self.cal_bmi)
        self.button2 = tkinter.Button(self.bottomframe,text = "Clear", command = self.clear)

        self.label5 = tkinter.Label(self.botframe, text="")
        self.label5.grid(row= 0,column = 1)

        self.label1.grid(row = 0, column = 0)
        self.height.grid(row = 0, column = 1)
              
        self.label2.grid(row = 0, column = 2)        

        self.label3.grid(row = 1, column = 0)
        self.weight.grid(row = 1, column = 1)
        self.label4.grid(row = 1, column = 2)

        self.radio1.grid(row = 0, column = 0)
        self.radio2.grid(row = 0, column = 1)

        self.button1.grid(row = 0, column = 0)
        self.button2.grid(row = 0, column = 1)

        self.topframe.pack()
        self.midframe.pack()
        self.bottomframe.pack()
        self.botframe.pack()

    def cal_bmi(self):
        try:
           weight=float(self.weight.get())
           height=float(self.height.get())
           bmi = weight/(height*height)
           BMI = str(bmi)
           self.label5.config(text="BMI :"+str(BMI))
        except ValueError:
            messagebox.showerror("Error","Height and number must be numbers")

    def clear(self):
        self.height.delete(0,"end")
        self.weight.delete(0,"end")
        self.labelint.set(0) 

if __name__ == "_main_":
    myGUI = GUI()
    myGUI.mw.mainloop()
