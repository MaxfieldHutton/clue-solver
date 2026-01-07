import customtkinter as ctk # type: ignore


class ClueFrame(ctk.CTkFrame):

    def __init__(self, master) -> None:

        super().__init__(master)

        self.frame = ctk.CTkFrame(self)
        self.frame.grid_rowconfigure(0, weight=0)
        
        self.frame.grid_columnconfigure(1, minsize=3)
        self.frame.grid_columnconfigure(2, minsize=3)
        self.frame.grid_columnconfigure(3, minsize=3)

        self.frame.grid_columnconfigure(0, weight=1)
        self.frame.grid_columnconfigure(1, weight=0)
        self.frame.grid_columnconfigure(2, weight=0)
        self.frame.grid_columnconfigure(3, weight=0)

        self.frame.pack()





def add_clue(master: ctk.CTkFrame, clue: str) -> ClueFrame:
    cf: ClueFrame = ClueFrame(master)

    cf.frame.name = ctk.CTkLabel(cf.frame, text=clue, font=('Arial', 12), width=100, anchor="w").grid(row=0, column=0, padx=0, pady=0, sticky="w")

    cf.frame.check_1 = ctk.CTkCheckBox(cf.frame, text="", width=18).grid(row=0, column=1, padx=0, pady=0)

    cf.frame.check_2 = ctk.CTkCheckBox(cf.frame, text="", width=18).grid(row=0, column=2, padx=0, pady=0)

    cf.frame.check_2 = ctk.CTkCheckBox(cf.frame, text="", width=18).grid(row=0, column=3, padx=0, pady=0)
    return cf




class PlayerFrame(ctk.CTkFrame):


    def __init__(self, master) -> None:

        super().__init__(master)

        self.label = ctk.CTkLabel(self, text=f"{mf.player_entry_frame.player_entry.get()}", font=('Arial', 18))
        self.label.pack(padx=10, pady=5)

        self.frame = ctk.CTkFrame(self)
        self.frame.grid_columnconfigure(0, weight=1)
        self.frame.grid_rowconfigure(0, weight=1)
        self.frame.pack(padx=5, pady=5)


        self.label_frame: ctk.CTkFrame = ctk.CTkFrame(self.frame)
        self.label_frame.grid_columnconfigure(0, weight=1)
        self.label_frame.grid_rowconfigure(0, weight=1)
        self.label_frame.grid(row=0, column=0, padx=3, pady=3)

        self.they_have_this_label: ctk.CTkLabel = ctk.CTkLabel(self.label_frame, text="Has this |", font=('Arial', 10)).grid(row=0, column=1, padx=0, pady=3)
        self.they_showed_me_this: ctk.CTkLabel = ctk.CTkLabel(self.label_frame, text="Showed me |", font=('Arial', 10)).grid(row=0, column=2, padx=0, pady=3)
        self.i_showed_them_this: ctk.CTkLabel = ctk.CTkLabel(self.label_frame, text="Showed them", font=('Arial', 10)).grid(row=0, column=3, padx=0, pady=3)


        self.clue_names: list[str] = ["Colonel Mustard","Miss Scarlet","Mrs Peacock","Mrs White",
                                 "Mr Green","Prof Plum","Candlestick","Knife","Pipe",
                                 "Revolver","Rope","Wrench","Kitchen","Ballroom","Conservatory",
                                 "Dining Room","Billiard Room","Library","Lounge","Hall","Study"]
        self.clues: list[ClueFrame] = []
        for _row, name in enumerate(self.clue_names, start=1):
            cf: ClueFrame = add_clue(self.frame, name)
            cf.grid(row=_row, column=0, padx=0, pady=0)
            self.clues.append(cf)
        

class PlayerEntryFrame(ctk.CTkFrame):

    def __init__(self, master) -> None:

        super().__init__(master)


        ####
        self.text_label_frame = ctk.CTkFrame(self)
        self.text_label_frame.grid_columnconfigure(0, weight=1)
        self.text_label_frame.grid_rowconfigure(0, weight=1)
        self.text_label_frame.pack(padx=10, pady=5)

        self.label = ctk.CTkLabel(self.text_label_frame, text="Enter Player Name", font=('Arial', 14))
        self.label.grid(row=0, column=0, padx=10, pady=5, sticky="w")

        self.player_entry = ctk.CTkEntry(self.text_label_frame)
        self.player_entry.bind("<KeyPress>", self.run_add_player)
        self.player_entry.grid(row=0, column=1, padx=10, pady=5, sticky="e")
        ####

        self.button = ctk.CTkButton(self, text="Add Player", command=add_player_to_clue_solver)
        self.button.pack(padx=10, pady=5)

    def run_add_player(self, event) -> None:
        if event.keysym == "Return":
            add_player_to_clue_solver()
    
def add_player_to_clue_solver() -> None:
    if len(mf.player_entry_frame.player_entry.get()) > 0:
        print(f"Added Player {mf.player_entry_frame.player_entry.get()}")
        mf.frame = PlayerFrame(mf)
        mf.frame.pack(padx=10, pady=5,side="left", expand=True, fill="both")
        mf.player_entry_frame.player_entry.delete(0, 'end')


class MainFrame(ctk.CTk):

    def __init__(self) -> None:
        
        super().__init__()
        
        
        self.title("Clue Solver")
        self.geometry("1000x700")

        self.label = ctk.CTkLabel(self, text="Clue Solver", font=('Arial', 18))
        self.label.pack(padx=10, pady=5)

        self.player_entry_frame = PlayerEntryFrame(self)
        self.player_entry_frame.pack(padx=10, pady=5)



mf = MainFrame()
mf.mainloop()
