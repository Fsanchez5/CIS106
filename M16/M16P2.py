import tkinter as tk
from tkinter import simpledialog, messagebox
import os  


def load_players(filename):
    names = [] 
    averages = []  

    
    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split()  
            if len(parts) == 2:
                name, avg = parts  
                names.append(name)  
                averages.append(float(avg))  

    return names, averages  


def display_players(names, averages):
    print("Player Roster:")
    for name, avg in zip(names, averages):  
        print(f"{name}: {avg:.3f}")  

def search_player(name_list, avg_list, search_name):
    for i, name in enumerate(name_list):
        if name.lower() == search_name.lower():  
            return f"{name}'s batting average is {avg_list[i]:.3f}"  
    return f"{search_name} not found in the list."  

def write_to_file(result, filename="search_results.txt"):
   
    with open(filename, 'a') as file:
        file.write(result + "\n")  


def gui_search_loop(name_list, avg_list):
    root = tk.Tk()  
    root.withdraw()  

    while True:
       
        name_input = simpledialog.askstring("Player Search", "Enter a player's last name (Cancel to exit):")

        if name_input is None:  
            break

        result = search_player(name_list, avg_list, name_input)  

      
        messagebox.showinfo("Search Result", result)

       
        write_to_file(result)

 
if __name__ == "__main__":
    filename = "players.txt"  
    names, averages = load_players(filename)  
    display_players(names, averages)  
    gui_search_loop(names, averages)  