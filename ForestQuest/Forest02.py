from tkinter import Tk
from tkinter import *
from tkinter import ttk
from tkinter import simpledialog
from tkinter import font

import GameObject

TITLE_LOCATION = 0
MINE_A_LOCATION = 1
CAVE_LOCATION = 2
MINE_B_LOCATION =3
CAVE_ENTRY_LOCATION = 4
MINE_C_LOCATION = 5
POND_LOCATION = 6
RIVER_BEACH_LOCATION_A = 7
FOREST_PATH_A_LOCATION = 8
RIVER_BEACH_B_LOCATION = 9
FOREST_PATH_B_LOCATION = 10
FOREST_PATH_C_LOCATION = 11
FOREST_PATH_D_LOCATION = 12
FRONT_OF_CABIN_LOCATION = 13
CABIN_LOCATION = 14
RIVER_CLIFF_LOCATION = 15
WATCH_TOWER_LOCATION = 16
RIVER_BEACH_C_LOCATION = 17
FOREST_PATH_E_LOCATION =18
FOREST_PATH_F_LOCATION = 19
FOREST_PATH_G_LOCATION = 20
FLOWER_FIELD_LOCATION = 21 
CAMP_LOCATION = 22
FOREST_PATH_END = 23






command_widget = None
image_label = None
description_widget = None
inventory_widget = None
north_button = None
south_button = None
east_button = None
west_button = None
root = None

refresh_location = True
refresh_objects_visible = True

current_location = TITLE_LOCATION
traits = ['gambler','mechanic','camper']
end_of_game = False
starting = True
trait_picked = False

is_WATCH_TOWER_LOCATION_blocked = True
is_FOREST_PATH_E_LOCATION_blocked = True 
is_CAVE_LOCATION_blocked =True
is_MINE_B_LOCATION_blocked = True
is_FLOWER_FIELD_LOCATION_blocked = True

trait = ''


brake_pads_object = GameObject.GameObject()
game_objects = []





def perform_command(verb, noun):
    if starting == False:    
        if (verb == "GO"):
            perform_go_command(noun)
        elif ((verb == "N") or (verb == "S") or (verb == "E") or (verb == "W")):
            perform_go_command(verb)        
        elif ((verb == "NORTH") or (verb == "SOUTH") or (verb == "EAST") or (verb == "WEST")):
            perform_go_command(verb)        
        elif (verb == "GET"):
            perform_get_command(noun)
        elif (verb == "PUT"):
            perform_put_command(noun)
        elif (verb == "LOOK"):
            perform_look_command(noun)        
        elif (verb == "KILL"):
            perform_kill_command(noun)        
        elif (verb == "READ"):
            perform_read_command(noun)        
        elif (verb == "OPEN"):
            perform_open_command(noun)
        else:
            print_to_description("huh?")
    else:
        perfrom_start_command(verb)       
        

def perfrom_start_command(action):
    global trait_picked
    global starting
    global trait
    global refresh_location
    
    global current_location
    
    if trait_picked == True:
        #start game
        if action[0].lower() == 's':
            starting = False
            #put player in first room, refresh items and room
            
            current_location = MINE_A_LOCATION
            refresh_location = True
        else:
            print_to_description('you may need to "start" first.')
    else:
        #pick trait (gambler, mechanic, camper)
        if action.lower() == 'gambler':
            #gambler
            trait = traits[0]
            trait_picked = True
            print_to_description("Picked!")
        if action.lower() == 'mechanic':
            #mechanic
            trait = traits[1]
            trait_picked = True
            print_to_description("Picked!")
        if action.lower() == 'camper':
            #camper
            trait = traits[2]
            trait_picked = True
            print_to_description("Picked!")
        elif trait_picked == False:
            print_to_description("Pick a trait first") 

def perform_go_command(direction):

    global current_location
    global refresh_location
    
    if (direction == "N" or direction == "NORTH"):
        new_location = get_location_to_north()
    elif (direction == "S" or direction == "SOUTH"):
        new_location = get_location_to_south()
    elif (direction == "E" or direction == "EAST"):
        new_location = get_location_to_east()
    elif (direction == "W" or direction == "WEST"):
        new_location = get_location_to_west()
    else:
        new_location = 0
        
    if (new_location == 0):
        print_to_description("You can't go that way!")
    else:
        current_location = new_location
        refresh_location = True

def perform_get_command(object_name):
    
    global refresh_objects_visible
    game_object = get_game_object(object_name)
    
    if not (game_object is None):
        if (game_object.location != current_location or game_object.visible == False):
            print_to_description("You don't see one of those here!")
        elif (game_object.movable == False):
            print_to_description("You can't pick it up!")
        elif (game_object.carried == True):
            print_to_description("You are already carrying it")
        else:
            #handle special conditions
            if (False):
                print_to_description("special condition")
            else:
                #pick up the object
                game_object.carried = True
                game_object.visible = False
                refresh_objects_visible = True
    else:
        print_to_description("You don't see one of those here!")

# 
def perform_put_command(object_name):

    global refresh_objects_visible
    game_object = get_game_object(object_name)
    
    if not (game_object is None):
        if (game_object.carried == False):
            print_to_description("You are not carrying one of those.")
        else:
            #put down the object
            game_object.location = current_location
            game_object.carried = False
            game_object.visible = True
            refresh_objects_visible = True
    else:
        print_to_description("You are not carrying one of those!")
# 
def perform_look_command(object_name):

    global sword_found
    global refresh_location
    global refresh_objects_visible
    
    game_object = get_game_object(object_name)
 
    if not (game_object is None):

        if ((game_object.carried == True) or (game_object.visible and game_object.location == current_location)):
            print_to_description(game_object.description)
        else:
            #recognized but not visible
            print_to_description("You can't see one of those!")
 
        #special cases - when certain objects are looked at, others are revealed!
        if (False):
            print_to_description("special condition")
            global refresh_objects_visible
            refresh_objects_visible = True

    else:
        if (object_name == ""):
            #generic LOOK
            refresh_location = True
            refresh_objects_visible = True
        else:
            #not visible recognized
            print_to_description("You can't see one of those!")

def perform_kill_command(object_name):

    game_object = get_game_object(object_name)
 
    if not (game_object is None):
        if (False):
            print_to_description("special condition")
        else:
            print_to_description("You can't kill inanimate objects, silly!")
    else:
        #not visible recognized
        print_to_description("You can't kill what you can't see")

def perform_read_command(object_name):

    game_object = get_game_object(object_name)
 
    if not (game_object is None):
        if (game_object.carried == False):
            print_to_description('You don\'t seem to have one of those on you')
        elif(game_object.carried == True):
            pass
        
    else:
        print_to_description("I am not sure which " + object_name + "you are referring to")
# 
def perform_open_command(object_name):

    global door_openend
    game_object = get_game_object(object_name)
 
    if not (game_object is None):
        if (False):
            print_to_description("special condition")
        else:
            print_to_description("You can't open one of those.")
    else:
        print_to_description("You don't see one of those here.")
                
def describe_current_location():
        
    if (current_location == TITLE_LOCATION):
        print_to_description("Welcome to 'Lost: a game. To start, pick a trait(gambler, camper, or mechanic)'")
    elif (current_location == CABIN_LOCATION):
        print_to_description("You are in a small, basic log cabin with a bed, a tiny kitchen, and a couple other living items. It pretty cold without the stove going. ")
    else:
        print_to_description( current_location)

def set_current_image():
    
    if (current_location == TITLE_LOCATION):
        image_label.img = PhotoImage(file = 'res/Title.gif')
    elif (current_location == CABIN_LOCATION):
        image_label.img = PhotoImage(file = 'res/blank-1.gif')
    else:
        image_label.img = PhotoImage(file = 'res/blank-1.gif')
        
    image_label.config(image = image_label.img)
        

def get_location_to_north():
    if current_location == MINE_B_LOCATION :
        return MINE_A_LOCATION   #puzzle
    
    elif current_location ==CAVE_ENTRY_LOCATION :
        return   CAVE_LOCATION if is_CAVE_LOCATION_blocked == False else 0
    elif current_location ==MINE_C_LOCATION:
        return MINE_B_LOCATION 
    
    elif current_location ==FOREST_PATH_A_LOCATION:
        return  CAVE_ENTRY_LOCATION
    elif current_location == FOREST_PATH_D_LOCATION :
        return POND_LOCATION
    
    elif current_location ==RIVER_BEACH_B_LOCATION:
        return  RIVER_BEACH_LOCATION_A
    elif current_location ==FOREST_PATH_B_LOCATION:
        return FOREST_PATH_A_LOCATION 
    
    elif current_location ==RIVER_CLIFF_LOCATION :
        return RIVER_BEACH_B_LOCATION
    elif current_location == WATCH_TOWER_LOCATION:
        return FOREST_PATH_C_LOCATION
    elif current_location == FOREST_PATH_G_LOCATION  :
        return FRONT_OF_CABIN_LOCATION
    
    elif current_location ==RIVER_BEACH_C_LOCATION  :
        return RIVER_CLIFF_LOCATION
    elif current_location ==FOREST_PATH_E_LOCATION :
        return WATCH_TOWER_LOCATION
    
    elif current_location == FOREST_PATH_END:
        return FOREST_PATH_G_LOCATION
    else:
        return 0

def get_location_to_south():
    
    if current_location == MINE_A_LOCATION:
        return MINE_B_LOCATION
    
    elif current_location == CAVE_LOCATION :
        return  CAVE_ENTRY_LOCATION
    elif current_location ==MINE_B_LOCATION :
        return MINE_C_LOCATION
    
    elif current_location == CAVE_ENTRY_LOCATION:
        return FOREST_PATH_A_LOCATION
    elif current_location ==POND_LOCATION :
        return FOREST_PATH_D_LOCATION
    
    elif current_location == RIVER_BEACH_LOCATION_A:
        return RIVER_BEACH_B_LOCATION
    elif current_location ==FOREST_PATH_A_LOCATION :
        return FOREST_PATH_B_LOCATION
    
    elif current_location == RIVER_BEACH_B_LOCATION:
        return RIVER_CLIFF_LOCATION
    elif current_location == FOREST_PATH_C_LOCATION:
        return WATCH_TOWER_LOCATION if is_WATCH_TOWER_LOCATION_blocked == False else 0
    elif current_location == FRONT_OF_CABIN_LOCATION :
        return FOREST_PATH_G_LOCATION
    
    elif current_location ==RIVER_CLIFF_LOCATION :
        return RIVER_BEACH_C_LOCATION
    elif current_location == WATCH_TOWER_LOCATION:
        return FOREST_PATH_E_LOCATION
    
    elif current_location == FOREST_PATH_G_LOCATION :
        return FOREST_PATH_END
    else:    
        return 0
    
def get_location_to_east():
    
    if current_location == RIVER_BEACH_B_LOCATION :
        return FOREST_PATH_B_LOCATION
    
    elif current_location == CAVE_LOCATION:
        return MINE_B_LOCATION if is_MINE_B_LOCATION_blocked == True else 0
    elif current_location == FOREST_PATH_B_LOCATION :
        return FOREST_PATH_C_LOCATION
    
    elif current_location == FOREST_PATH_C_LOCATION:
        return FOREST_PATH_D_LOCATION
    elif current_location == FOREST_PATH_E_LOCATION  :
        return FOREST_PATH_F_LOCATION
    
    elif current_location == FOREST_PATH_D_LOCATION :
        return FRONT_OF_CABIN_LOCATION
    elif current_location == FOREST_PATH_F_LOCATION:
        return FOREST_PATH_G_LOCATION
    
    elif current_location == FRONT_OF_CABIN_LOCATION :
        return CABIN_LOCATION
    elif current_location == FOREST_PATH_G_LOCATION:
        return (FLOWER_FIELD_LOCATION if is_FLOWER_FIELD_LOCATION_blocked == False else 0)
    
    elif current_location == FLOWER_FIELD_LOCATION:
        return CAMP_LOCATION
    else:
        return 0

def get_location_to_west():
    if current_location ==FOREST_PATH_B_LOCATION  :
        return RIVER_BEACH_B_LOCATION
    
    elif current_location == MINE_B_LOCATION:
        return CAVE_LOCATION 
    elif current_location ==FOREST_PATH_C_LOCATION  :
        return FOREST_PATH_B_LOCATION
        
    elif current_location ==FOREST_PATH_D_LOCATION:
        return  FOREST_PATH_C_LOCATION
    elif current_location ==FOREST_PATH_F_LOCATION  :
        return FOREST_PATH_E_LOCATION if is_FOREST_PATH_E_LOCATION_blocked == False else 0
    
    elif current_location ==FRONT_OF_CABIN_LOCATION :
        return FOREST_PATH_D_LOCATION 
    elif current_location ==FOREST_PATH_G_LOCATION:
        return  FOREST_PATH_F_LOCATION
    
    elif current_location == CABIN_LOCATION  :
        return FRONT_OF_CABIN_LOCATION
    elif current_location ==FLOWER_FIELD_LOCATION :
        return FOREST_PATH_G_LOCATION
    
    elif current_location == CAMP_LOCATION :
        return FLOWER_FIELD_LOCATION
    else:   
        return 0
        
def get_game_object(object_name):
    sought_object = None
    for current_object in game_objects:
        if (current_object.name.upper() == object_name):
            sought_object = current_object
            break
    return sought_object

def describe_current_visible_objects():
    
    
    if starting == False:
        object_count = 0
        object_list = ""
        
        for current_object in game_objects:
            if ((current_object.location  == current_location) and (current_object.visible == True) and (current_object.carried == False)):
                object_list = object_list + ("," if object_count > 0 else "") + current_object.name
                object_count = object_count + 1
                
        print_to_description("You see: " + (object_list + "." if object_count > 0 else "nothing special.")) 

def describe_current_inventory():
    
    object_count = 0
    object_list = ""

    for current_object in game_objects:
        if (current_object.carried):
            object_list = object_list + ("," if object_count > 0 else "") + current_object.name
            object_count = object_count + 1
    
    inventory = "You are carrying: " + (object_list if object_count > 0 else "nothing")
    
    inventory_widget.config(state = "normal")
    inventory_widget.delete(1.0, END)
    inventory_widget.insert(1.0, inventory)
    inventory_widget.config(state = "disabled")

def handle_special_condition():
    
    global end_of_game
    
    if (False):
        print_to_description("GAME OVER")
        end_of_game = True

def print_to_description(output, user_input=False):
    description_widget.config(state = 'normal')
    description_widget.insert(END, output)
    if (user_input):
        description_widget.tag_add("blue_text", CURRENT + " linestart", END + "-1c")
        description_widget.tag_configure("blue_text", foreground = 'blue')
    description_widget.insert(END, '\n')        
    description_widget.config(state = 'disabled')
    description_widget.see(END)

def build_interface():
    
    global command_widget
    global image_label
    global description_widget
    global inventory_widget
    global north_button
    global south_button
    global east_button
    global west_button    
    global root
    

    root = Tk()
    root['bg'] = 'black'
    root.resizable(0,0)

    
 
    style = ttk.Style()
    style.theme_use('xpnative')
    style.configure("BW.TLabel", foreground="white", background="black", font = ('Terminal', 9))
    style.configure("BW.TButton", font = ('Terminal', 9), foreground="white", background="black", color = 'black')
   

    my_font = font.Font(family = 'Terminal', size = 9, name = 'my_font')

    image_label = ttk.Label(root)    
    image_label.grid(row=0, column=0, columnspan =3,padx = 0, pady = 0)

    description_widget = Text(root, width =50, height = 15, wrap = 'word', font = my_font, foreground="white", background="black",borderwidth=0)
    description_widget.insert(1.0, "Welcome to my game\n\nGood Luck!. ")
    description_widget.config(state = "disabled")
    description_widget.grid(row=1, column=0, columnspan =3, sticky=W, padx = 0, pady = 0)

    command_widget = ttk.Entry(root, width = 20 ,style="BW.TLabel", font = my_font)
    command_widget.bind('<Return>', return_key_enter)
    command_widget.grid(row=2, column=1, padx = 0, pady = 0)
#    command_widget.config(font = terminal_font)

    entry_label = Label(root,width = 1, height = 1, text ='>',font = ('Terminal', 9), foreground="white", background="black")
    entry_label.grid(row =2, column = 0)
    
    button_frame = Frame(root)
    button_frame.config(height = 150, width = 150, relief = GROOVE,background="black",)
    button_frame.grid(row=3, column=0, columnspan =2, padx = 0, pady = 0)

    north_button = Button(button_frame, text = "N", width = 5, foreground="white", background="black",font = ('Terminal', 9))
    north_button.grid(row=0, column=1, padx = 4, pady = 3)
    north_button.config(command = north_button_click)
    
    south_button = Button(button_frame, text = "S", width = 5,foreground="white", background="black",font = ('Terminal', 9))
    south_button.grid(row=2, column=1, padx = 4, pady =  4)
    south_button.config(command = south_button_click)

    east_button = Button(button_frame, text = "E", width = 5,foreground="white", background="black",font = ('Terminal', 9))
    east_button.grid(row=1, column=2, padx = 2, pady = 2)
    east_button.config(command = east_button_click)

    west_button = Button(button_frame, text = "W", width = 5, foreground="white", background="black",font = ('Terminal', 9))
    west_button.grid(row=1, column=0, padx = 2, pady = 2)
    west_button.config(command = west_button_click)
    
    inventory_widget = Text(root, width = 30, height = 8, relief = GROOVE , state=DISABLED, font = my_font, foreground="white", background="black",borderwidth=0)
    inventory_widget.grid(row=2, column=2, rowspan = 2, padx = 0, pady = 0,sticky=W)
    
def set_current_state():

    global refresh_location
    global refresh_objects_visible

    if (refresh_location):
        describe_current_location()
        set_current_image()
    
    if (refresh_location or refresh_objects_visible):
        describe_current_visible_objects()

    handle_special_condition()
    set_directions_to_move()            

    if (end_of_game == False):
        describe_current_inventory()
    
    refresh_location = False
    refresh_objects_visible = False
    
    command_widget.config(state = ("disabled" if end_of_game else "normal"))

def north_button_click():
    print_to_description("N", True)
    perform_command("N", "")
    set_current_state()

def south_button_click():
    print_to_description("S", True)
    perform_command("S", "")
    set_current_state()

def east_button_click():
    print_to_description("E", True)
    perform_command("E", "")
    set_current_state()

def west_button_click():
    print_to_description("W", True)
    perform_command("W", "")
    set_current_state()

def return_key_enter(event):
    if( event.widget == command_widget):
        command_string = command_widget.get()
        print_to_description(command_string, True)

        command_widget.delete(0, END)
        words = command_string.split(' ', 1)
        verb = words[0]
        noun = (words[1] if (len(words) > 1) else "")
        perform_command(verb.upper(), noun.upper())
        
        set_current_state()

def set_directions_to_move():

    move_to_north = (get_location_to_north() > 0) and (end_of_game == False)
    move_to_south = (get_location_to_south() > 0) and (end_of_game == False)
    move_to_east = (get_location_to_east() > 0) and (end_of_game == False)
    move_to_west = (get_location_to_west() > 0) and (end_of_game == False)
    
    north_button.config(state = ("normal" if move_to_north else "disabled"))
    south_button.config(state = ("normal" if move_to_south else "disabled"))
    east_button.config(state = ("normal" if move_to_east else "disabled"))
    west_button.config(state = ("normal" if move_to_west else "disabled"))

def main():
    
    build_interface()
    set_current_state()
    root.mainloop()
        

main()
