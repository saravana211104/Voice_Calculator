from tkinter import *
import pyttsx3
import speech_recognition as sr
import word2number as w2n

root = Tk()
root.title("Voice Calculator")
root.geometry("570x600+100+200")
root.resizable(False, False)
root.configure(bg=("#17161b"))

label_result = Label(root, width=25, height=2, text="", font=("arial", 30))
label_result.pack()

equation = ""

def show(value):
    global equation
    equation += value
    label_result.config(text=equation)
    en = pyttsx3.init()
    en.say(value)
    en.runAndWait()

def clear():
    global equation
    equation = ""
    label_result.config(text=equation)

def calculate():
    global equation
    result = ""
    if equation != "":
        try:
            result = eval(equation)
        except:
            result = "error"
            equation = ""
    label_result.config(text=result)
    en = pyttsx3.init()
    en.say(result)
    en.runAndWait()

def get_speech_input():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Say Something")
        audio=r.listen(source)
    try:
        text=r.recognize_google(audio)
        text=f"{text}"
        print("You said:", text)
        text=text.lower()
        a=text.split()
        var1 = int(a[0])
        var2= int(a[2])
        if(a[1]=="+"):
            text=var1+var2
        elif(a[1]=="-"):
            text=var1-var2
        elif(a[1]=="x"):
            text=var1*var2
        elif(a[1]=="/"):
            text=var1/var2
        else:
            print("correct")
    except sr.UnknownValueError:
        print("couldn't understand")
    except sr.RequestError as e:
        print("couldn't understand:".format(e))
    text=str(text)
    label_result.config(text=f"Converted Expression: {text}")
    show(text)
    

Button(root, text="C", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#3697f5",
       command=lambda: clear()).place(x=10, y=100)
Button(root, text="/", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36",
       command=lambda: show("/")).place(x=150, y=100)
Button(root, text="%", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36",
       command=lambda: show("%")).place(x=290, y=100)
Button(root, text="*", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36",
       command=lambda: show("*")).place(x=430, y=100)

Button(root, text="7", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36",
       command=lambda: show("7")).place(x=10, y=200)
Button(root, text="8", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36",
       command=lambda: show("8")).place(x=150, y=200)
Button(root, text="9", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36",
       command=lambda: show("9")).place(x=290, y=200)
Button(root, text="-", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36",
       command=lambda: show("-")).place(x=430, y=200)

Button(root, text="4", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36",
       command=lambda: show("4")).place(x=10, y=300)
Button(root, text="5", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36",
       command=lambda: show("5")).place(x=150, y=300)
Button(root, text="6", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36",
       command=lambda: show("6")).place(x=290, y=300)
Button(root, text="+", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36",
       command=lambda: show("+")).place(x=430, y=300)

Button(root, text="1", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36",
       command=lambda: show("1")).place(x=10, y=400)
Button(root, text="2", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36",
       command=lambda: show("2")).place(x=150, y=400)
Button(root, text="3", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36",
       command=lambda: show("3")).place(x=290, y=400)
Button(root, text="0", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36",
       command=lambda: show("0")).place(x=430, y=400)

Button(root, text=".", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#2a2d36",
       command=lambda: show(".")).place(x=290, y=500)
Button(root, text="=", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#fff", bg="#fe9037",
       command=lambda: calculate()).place(x=430, y=400)

Button(root, text="Speak", width=10, height=1, font=("arial", 15, "bold"), bd=1, fg="#fff", bg="#fe9037",
       command=lambda: get_speech_input()).place(x=10, y=500)

root.mainloop()
