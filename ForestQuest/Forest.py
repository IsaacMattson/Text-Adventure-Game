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
FOREST_PATH_END_LOCATION = 23

#this is for objects that will be without a location
EXTRA_LOCATION = 24






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

dirt_bike_descriptions = {
    1: 'It\'s a broken dirt bike, and with a closer look, you can see that it\'s tank is empty and has no chain. You have a feeling that something else is wrong, but you cant put your finger on it...',
    2: 'It\'s a Broken dirt bike with an empty tank, no chain, and broken brakes',
    3: ', an empty tank',
    4: ', no chain',
    5: ', broken brakes'
    }

trait = ''
brake_pads_object = GameObject.GameObject('Brake Pads',RIVER_CLIFF_LOCATION,True,True,False,'Brake pads for a car, but with a little work you could probably get these to work for any vehicle.')
chain_object = GameObject.GameObject('Chain', MINE_A_LOCATION, True, True, False, 'A chain to make wheels spin.')
petrol_object = GameObject.GameObject('Can of petrol', EXTRA_LOCATION, True, False, False, 'A full can of petrol.' )
dirt_bike_object = GameObject.GameObject('Dirt bike', CAMP_LOCATION, False,True,False, dirt_bike_descriptions[1])
axe_object = GameObject.GameObject('Axe', CABIN_LOCATION, True, True, False, 'A good quality wood chopping axe.')
fishing_rod_object = GameObject.GameObject('Fishing rod', FRONT_OF_CABIN_LOCATION, True, True, False, 'A sturdy Fishing rod.')
fish_object = GameObject.GameObject('Fish', POND_LOCATION, True, False, False, "Its a fish. Probably a Carp or something.")

game_objects = [brake_pads_object,chain_object,petrol_object,dirt_bike_object, axe_object, fish_object, fishing_rod_object]





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
        elif (verb == 'DEBUG'):
            perfrom_debug_command(noun)
        elif (verb == 'USE'):
            perform_use_command(noun)
        elif (verb == 'MAKE'):
            perform_make_command(noun)
#       elif (verb == 'FISH'):
#            perform_fish_command(noun)
        else:
            print_to_description("huh?")
    else:
        perfrom_start_command(verb)       
        
        
# def perform_fish_command(noun):
#     global game_objects
#     
#     if (not noun == ""):
#         print_to_description("What?")    
#     else:
#         if fishing_rod_object.carried:
#             
#             if current_location == POND_LOCATION:
#                 #fish
#                 pass
#             
#             else:
#                 print_to_description('You look around, but can not find a area to cast your rod.')
#         else:
#             print_to_description('With What?')    
#             
        
def perform_make_command(object):
    global game_objects
        
def perform_use_command(noun):
    
    global is_WATCH_TOWER_LOCATION_blocked
    global is_FOREST_PATH_E_LOCATION_blocked
    global game_objects
    game_object = get_game_object(noun)
    
    if not (game_object is None):
        if (game_object.carried == True):        
            # Goes through the objects that can be used
            if game_object == axe_object:
                if current_location == FOREST_PATH_F_LOCATION or current_location == FOREST_PATH_E_LOCATION:
                    is_FOREST_PATH_E_LOCATION_blocked = False
                    print_to_description('You chopped the log blocking the path.')
                
                elif current_location == FOREST_PATH_C_LOCATION or current_location == WATCH_TOWER_LOCATION:
                    is_WATCH_TOWER_LOCATION_blocked = False
                    print_to_description('You chopped the log blocking the path.')
                                      
                else:
                    print_to_description('You look around, and can\'t bring yourself the chop down one of the trees.')
                    
            if game_object == fishing_rod_object:
                
                if current_location == POND_LOCATION:
                    #fish
                    pass
                elif (current_location == RIVER_BEACH_B_LOCATION) or (current_location == RIVER_BEACH_LOCATION_A) or(current_location == RIVER_BEACH_C_LOCATION) or (current_location == RIVER_CLIFF_LOCATION):
                    print_to_description('You cast your rod into the water, but get no bite.')
                    
                else:
                    print_to_description('Where?')
            else:
                print_to_description('You scratch your head, Trying to figure out how to use {}.'.format(noun.upper()))
        else:   
            #if they don't have the item, but it exists
            print_to_description('You look in your pockets, and fail to locate {}.'.format(noun.upper()))
            
    else:        
        #object dosn't exist
        print_to_description('What is a(n) {}?'.format(noun))
        
        
        
def perfrom_debug_command(code):
    global is_CAVE_LOCATION_blocked
    global current_location
    #This is for executing code inputed into the entry
    #can only get it to print not change value
    exec(code)
    global refresh_location

def perfrom_start_command(action):
    global trait_picked
    global starting
    global trait
    global refresh_location
    
    global current_location
    
        #start game
    if action[0].lower() == 's':
            starting = False
            #put player in first room, refresh items and room
            current_location = CABIN_LOCATION
            refresh_location = True
            print_to_description('You slowly open your eye, and as they a just to the light of your surroundings, to soon come to the realization that you have no recollection of where you are, or how you got here. You should probably try to figure out whats going on')
    else:
            print_to_description('you may need to "start" first.')
    

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
        print_to_description("0")
    elif (current_location == MINE_A_LOCATION):
        print_to_description("1")
    elif (current_location == CAVE_LOCATION):
        print_to_description("2")
    elif (current_location == MINE_B_LOCATION):
        print_to_description("3")
    elif (current_location == CAVE_ENTRY_LOCATION):
        print_to_description("4")
    elif (current_location == MINE_C_LOCATION):
        print_to_description("5")
    elif (current_location == POND_LOCATION):
        print_to_description("6")
    elif (current_location == RIVER_BEACH_LOCATION_A):
        print_to_description("7")
    elif (current_location == FOREST_PATH_A_LOCATION):
        print_to_description("8")
    elif (current_location == RIVER_BEACH_B_LOCATION):
        print_to_description("9")
    elif (current_location == FOREST_PATH_B_LOCATION):
        print_to_description("10")
    elif (current_location == FOREST_PATH_C_LOCATION):
        print_to_description("11")
    elif (current_location == FOREST_PATH_D_LOCATION):
        print_to_description("12")
    elif (current_location == FRONT_OF_CABIN_LOCATION):
        print_to_description("13")
    elif (current_location == CABIN_LOCATION):
        print_to_description("14")
    elif (current_location == RIVER_CLIFF_LOCATION):
        print_to_description("15")
    elif (current_location == WATCH_TOWER_LOCATION):
        print_to_description("16")
    elif (current_location == RIVER_BEACH_C_LOCATION):
        print_to_description("17")
    elif (current_location == FOREST_PATH_E_LOCATION):
        print_to_description("18")
    elif (current_location == FOREST_PATH_F_LOCATION):
        print_to_description("19")
    elif (current_location == FOREST_PATH_G_LOCATION):
        print_to_description("20")
    elif (current_location == FLOWER_FIELD_LOCATION):
        print_to_description("21")
    elif (current_location == CAMP_LOCATION):
        print_to_description("22")
    elif (current_location == FOREST_PATH_END_LOCATION):
        print_to_description("23")
    else:
        print_to_description( current_location)

def set_current_image():
    
    if (current_location == TITLE_LOCATION):
        image_label.img = PhotoImage(file = 'res/Title.gif')
    elif (current_location == MINE_A_LOCATION):
        image_label.img = PhotoImage(file = 'res/blank-1.gif')
    elif (current_location == CAVE_LOCATION):
        image_label.img = PhotoImage(file = 'res/blank-2.gif')
    elif (current_location == MINE_B_LOCATION):
        image_label.img = PhotoImage(file = 'res/blank-3.gif')
    elif (current_location == CAVE_ENTRY_LOCATION):
        image_label.img = PhotoImage(file = 'res/blank-4.gif')
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
        return FOREST_PATH_C_LOCATION if is_WATCH_TOWER_LOCATION_blocked == False else 0
    elif current_location == FOREST_PATH_G_LOCATION  :
        return FRONT_OF_CABIN_LOCATION
    
    elif current_location ==RIVER_BEACH_C_LOCATION  :
        return RIVER_CLIFF_LOCATION
    elif current_location ==FOREST_PATH_E_LOCATION :
        return WATCH_TOWER_LOCATION
    
    elif current_location == FOREST_PATH_END_LOCATION :
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
        return FOREST_PATH_END_LOCATION 
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
        return FOREST_PATH_F_LOCATION if is_FOREST_PATH_E_LOCATION_blocked == False else 0
    
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
    style.configure("BW.TLabel", foreground="white", background="black", font = ('Terminal', 9))
    style.configure("BW.TButton", font = ('Terminal', 9), foreground="white", background="black", color = 'black')
   

    my_font = font.Font(family = 'Terminal', size = 9, name = 'my_font')

    image_label = ttk.Label(root)    
    image_label.grid(row=0, column=0, columnspan =3,padx = 0, pady = 0)

    description_widget = Text(root, width =50, height = 15, wrap = 'word', font = my_font, foreground="white", background="black",borderwidth=0)
    description_widget.insert(1.0, "Welcome to 'Lost', to start the game, type 'start', to load, type 'load', the name of save.\n\n")
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
        perform_command(verb.upper(), noun.upper()) if not(verb == 'debug') else perform_command(verb.upper(), noun)
        
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
