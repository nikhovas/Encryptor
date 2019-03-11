from tkinter import *
# import ttk

root = Tk()
root.title("Encryptor")
root.geometry("500x300")

source_file_txt = Label(root, text="Source file path: ")
# source_file_txt.grid(row=0, column=1, columnspan=3, sticky=tkinter.W+tkinter.E, pady=10, padx=10)
source_file_txt.place(x=5, y=5)
source_file = Entry(root)
# source_file.grid(row=0, column=1, columnspan=3, sticky=W+E, padx=10)
# source_file.pack()

dest_file_txt = Label(root, text="Destination file path: ")
dest_file_txt.place(x=5, y=30)
dest_file = Entry(root)
dest_file.pack()



# hatchCount = 0
#
# eggPicture = tkinter.PhotoImage(file="eggdemo.png")
# wasBornPicture = tkinter.PhotoImage(file="goshademo.png")
# skullPicture = tkinter.PhotoImage(file="skull.png")
# dyingPicture = tkinter.PhotoImage(file="dyingpicture.png")
# hungryphoto = tkinter.PhotoImage(file="hungerphoto.png")
#
# text = tkinter.Text(root, height=2, width=40, wrap='word')
# phrase = tkinter.Text(root, height=2, width=40)
#
# GoshaPic = tkinter.Label(root, image=eggPicture)
# GoshaPic.pack()
#
# buttonBorn = tkinter.Button(root, text="BORN!!!", command=toBornEvent, width=20, height=3)
# buttonBorn.pack()
# buttonQuit = tkinter.Button(root, text="Exit", command=quit) # это походу из-за exit справа все едет
# buttonQuit.place(relx=0.92, rely=0.016, relwidth=0.07)
#
# parLabel = tkinter.Label(root,
# text="Health: {0}/40\nHunger: {1}/50\nMood: {2}/50".format(str(Gosha.Health),
# str(Gosha.Hunger),
# str(Gosha.Mood)), justify='left')
# dayLabel = tkinter.Label(root, text="Day: " + str(day))
#
# actionsMenu = tkinter.LabelFrame(text="Actions")
#
#
# # buttonPlay = tkinter.Button(actionsMenu, text="Play", command=Gosha.play)
#
# buttonEat = tkinter.Button(actionsMenu, text="Eat", command=Gosha.eat)
# buttonEat.pack(side='left')
# buttonSay = tkinter.Button(actionsMenu, text="Say", command=Gosha.say)
# buttonSay.pack(side='left')
# buttonHear = tkinter.Button(actionsMenu, text="Hear", command=Gosha.hear)
# buttonGet = tkinter.Button(root, text="Teach", command=Gosha.getText)
# buttonHear.pack(side='left')
# buttonCure = tkinter.Button(actionsMenu, text="Cure", command=Gosha.cure)
# buttonCure.pack(side='left')
# # buttonSleep = tkinter.Button(actionsMenu, text="Sleep", command=Gosha.sleep)
#
# # root.bind('<Return>', toBornEvent)

root.mainloop()