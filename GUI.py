from tkinter import*
from tkinter import filedialog
from main import send_letter



def list_client():
   return(List_clients.get("1.0",'end-1c').split('\n'))


def message_handler():
    return(str(messages.get("1.0",'end-1c')))


        

def start_sending():
    c = filedialog.askopenfilename()
    send_letter(mess_text=message_handler(), list_user=list_client(), filepath=str(c))
    print("OK")



root = Tk()
root.geometry("780x500")
root.resizable(0,0)



Lbl1 = Label(width=20,
                    fg = 'black',
                    text= "Почты",)
Lbl1.grid(row=0, column=0)

Lbl2 = Label(width=35,
                    fg = 'black',
                    text= "Сообщение")
Lbl2.grid(row=0, column=1)

List_clients = Text(width=  35, 
                    height= 20,
                    fg = 'white',
                    bg = "darkgreen",
                    font='Arial 14',
                    wrap= WORD)

List_clients.grid(row = 1, column=0)


messages= Text(width= 35, 
                    height= 20,
                    bg = "hotpink",
                    fg = "white",
                    font='Arial 14',
                    wrap= WORD)
messages.grid(row = 1, column=1)


but1 = Button(height=2,
              width=25,
              text= "Отправить",
            command= start_sending)
but1.grid(column=1, row=2)

root.mainloop()