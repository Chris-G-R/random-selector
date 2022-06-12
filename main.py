import random as r

from tkinter import *
from tkinter import ttk

#Selects a random item from the text entries
def pick_random():
    #Extracts the text entry content and assigns it to a list variable
    random_strings = [i.get() for i in random_list]
    
    #Set the output widget to select a random element from our newly created list variable
    text_var.set(r.choice(random_strings))
    
    #text_var.set('it works...')

#Since every created text entry has an ID, we use the ID to find its location within the lists
def get_widget_index(unique_id):
    for i,v in enumerate(unique_id_list):
        if v == unique_id:
            return i

#Remove the widget given their unique ID
def remove_widget(unique_id):

    #Use their unique ID to get their position in the lists
    widget_index = get_widget_index(unique_id)
    
    #Removes the corresponding entry-widget list item from the app and the list
    entry_list[widget_index].grid_forget()
    entry_list.pop(widget_index)
    
    #Removes their entry content from the list
    random_list.pop(widget_index)
    
    #Removes the corresponding [-] button next to the entry widget from app and list
    modify_widget_button_list[widget_index].grid_forget()
    modify_widget_button_list.pop(widget_index)
    
    #Removes their unique id from the list
    unique_id_list.pop(widget_index)

#Adds an entry widget with a corresponding remove button widget
def add_widget():
    
    #Create a variable to store the entry widget content
    random_list.append(StringVar())
    
    #Create a unique ID for these widgets
    unique_id_list.append(unique_id_list[-1] + 1)
    
    #Stores their location in the lists
    widget_index = len(random_list) - 1
    
    #Stores the widgets' unique ID
    unique_id = unique_id_list[-1]
    
    #Creates the entry list and assigns the previously created variable for it to store info
    entry_list.append(ttk.Entry(input_frame, textvariable=random_list[-1]))
    entry_list[widget_index].grid(row=unique_id_list[-1], column=0)

    #Creates a button that removes itself and its corresponding entry widget
    modify_widget_button_list.append(ttk.Button(input_frame, text="-", command=lambda: remove_widget(unique_id)))
    modify_widget_button_list[widget_index].grid(row=unique_id_list[-1], column=1)

#Creating the window and its title
root = Tk()
root.title("Random Selector")

#Creating the output frame of the app
output_frame = ttk.Frame(root)
output_frame.grid(column=0, row=0)

#Creating the contents of the output frame
text_var = StringVar()
output_text = ttk.Label(output_frame, textvariable=text_var)
output_text.grid(row=0, column=0)

#Creates the button that would output a random item from the entries
execution_button = ttk.Button(root, text="Pick at random!", command=pick_random)
execution_button.grid(row=1, column=0)

#Creating the output frame of the app
input_frame = ttk.Frame(root)
input_frame.grid(row=2, column=0)

#Creates a list containing a variable that the first entry uses as a variable to store info
random_list = [StringVar()]

#Assigns the first widget a unique ID
unique_id_list = [0]

#Creates the first entry and uses the previously created random_list item to store info
entry_list = [ttk.Entry(input_frame, textvariable=random_list[0])]
entry_list[0].grid(row=0, column=0)

#Creates a widget that creates 2 widgets - another entry widget and a button that removes itself and the corresponding entry widget
modify_widget_button_list = [ttk.Button(input_frame, text="+", command=add_widget)]
modify_widget_button_list[0].grid(row=0, column=1)

#Main loop
root.mainloop()
