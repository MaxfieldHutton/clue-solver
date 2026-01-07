import customtkinter as ctk # type: ignore



class PlayerFrame(ctk.CTkFrame):

    def __init__(self, master) -> None:

        super().__init__(master)

        
    def setName(self, name: str) -> None:
        self.label = ctk.CTkLabel(self, text=name, font=('Arial', 14))
        self.label.pack(padx=10, pady=10)

class PlayerEntryFrame(ctk.CTkFrame):

    def __init__(self, master) -> None:

        super().__init__(master)

        

        ####
        self.text_label_frame = ctk.CTkFrame(self)
        self.text_label_frame.grid_columnconfigure(0, weight=1)
        self.text_label_frame.grid_rowconfigure(0, weight=1)
        self.text_label_frame.pack(padx=10, pady=10)

        self.label = ctk.CTkLabel(self.text_label_frame, text="Enter Player Name", font=('Arial', 14))
        self.label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        self.player_entry = ctk.CTkEntry(self.text_label_frame)
        self.player_entry.grid(row=0, column=1, padx=10, pady=10, sticky="e")
        ####

        self.button = ctk.CTkButton(self, text="Add Player", command=add_player_to_clue_solver)
        self.button.pack(padx=10, pady=10)
    
def add_player_to_clue_solver() -> None:
    print(f"Added Player {cs.player_entry_frame.player_entry.get()}")
    cs.frame = PlayerFrame(cs)
    cs.frame.setName(f"{cs.player_entry_frame.player_entry.get()}")
    cs.frame.pack(padx=10, pady=10,side="left", expand=True, fill="both")


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

    def shortcut(self, event) -> None:
        if event.state == 4 and event.keysym == "Return":
            self.show_message()





cs = ClueSolver()
cs.mainloop()
