import customtkinter as ctk # type: ignore



class PlayerFrame(ctk.CTkFrame):

    def __init__(self, master) -> None:

        super().__init__(master)

class PlayerEntryFrame(ctk.CTkFrame):

    def __init__(self, master) -> None:

        super().__init__(master)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.label = ctk.CTkLabel(self, text="Enter Player Name", font=('Arial', 14))
        self.label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        self.player_entry = ctk.CTkEntry(self)
        self.player_entry.grid(row=0, column=1, padx=10, pady=10, sticky="e")

        self.button = ctk.CTkButton(self, text="Add Player", command=self.button_callback)
        self.button.grid(row=1, column=1, padx=10, pady=10, sticky="e"+"w")
    
    def button_callback(self):
        print(f"Added Player {self.player_entry.get()}")

class ClueSolver(ctk.CTk):

    def __init__(self) -> None:
        
        super().__init__()
        
        
        self.title("Clue Solver")
        self.geometry("1000x700")

        self.label = ctk.CTkLabel(self, text="Clue Solver", font=('Arial', 18))
        self.label.pack(padx=10, pady=10)

        self.player_entry_frame = PlayerEntryFrame(self)
        self.player_entry_frame.pack(padx=10, pady=10)

        
        

    def show_message(self) -> None:
        for players in self.player_amount_box.get():
            print(f"test {players}")

    def shortcut(self, event):
        if event.state == 4 and event.keysym == "Return":
            self.show_message()





cs = ClueSolver()
cs.mainloop()
