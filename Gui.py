from tkinter import *
import urllib.request
import urllib.parse
import subprocess
import re
import os
import datetime





def test_ip():
    with open(os.devnull, "wb") as limbo:
        ip = "175.24.1.100"
        result = subprocess.Popen(["ping", "-c", "1", "-n", "-W", "2", ip],
                                  stdout=limbo, stderr=limbo).wait()
        if result:
            return False
        else:
            return True

def print_time():
    currentDT = datetime.datetime.now()
    label_time = Label(window, text=str(currentDT.time()))
    label_time.grid(column=6, row=5)



window = Tk()

window.title("Cluster monitoring application")

window.geometry('450x300')

label_temp = Label(window, text = "")
label_temp.grid(column = 0, row = 0)
label_temp = Label(window, text = "")
label_temp.grid(column = 2, row = 1)
label_temp = Label(window, text = "")
label_temp.grid(column = 3, row = 2)
label_temp = Label(window, text = "")
label_temp.grid(column = 4, row = 3)
label_temp = Label(window, text = "      Time")
label_temp.grid(column = 4, row = 5)



lbl1 = Label(window, text="      Status")
lbl1.grid(column=4, row=4)

lbl = Label(window, text="      Server_Status")
lbl.grid(column=6, row=4)




def clicked():
    url = 'http://gg.gg/dbw9u'
    values = {'s': 'basics', 'submit': 'search'}
    data = urllib.parse.urlencode(values)
    data = data.encode('utf-8')
    check_server = True
    check_server_=True


    if test_ip() :
        req = urllib.request.Request(url, data)
        resp = urllib.request.urlopen(req)
        respData = resp.read()
        respData = str(respData)


        if "server 1 active now" in respData:
            if check_server:
                lbl.configure(text="      Server 1 active now    (Server 2 turned off)")
                print_time()






        elif "server 2 active now" in respData:
            if check_server_:
                lbl.configure(text="      Server 2 active now    (Server 1 turned off)")
                print_time()


    else:
        return



btn = Button(window, text="Refresh", command=clicked)
btn.grid(column=7, row=6)






window.mainloop()