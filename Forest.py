from tkinter import Tk
from tkinter import *
from tkinter import ttk
from tkinter import simpledialog
from tkinter import font

import GameObject

#make fishing work, add ability to get chain and brakes with tools

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

is_bat_gone = False
is_stirfry_given = False
know_about_berries = False

is_WATCH_TOWER_LOCATION_blocked = True
is_FOREST_PATH_E_LOCATION_blocked = True 
is_CAVE_LOCATION_blocked =True
is_MINE_B_LOCATION_blocked = True
is_FLOWER_FIELD_LOCATION_blocked = True

is_petrol_done = False
is_brakes_done = False
is_chain_done = False

dirt_bike_descriptions = {
    1: 'It\'s a broken dirt bike, and with a closer look, you can see that it\'s tank is empty and has no chain. You have a feeling that something else is wrong, but you cant put your finger on it...',
    2: 'It\'s a Broken dirt bike with an empty tank, no chain, and broken brakes',
    3: ', an empty tank',
    4: ', no chain',
    5: ', broken brakes'
    }

XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX = False

brake_pads_object = GameObject.GameObject('Brake Pads',RIVER_CLIFF_LOCATION,True,True,False,'Brake pads for a car, but with a little work you could probably get these to work for any vehicle.')
chain_object = GameObject.GameObject('Chain', MINE_A_LOCATION, True, True, False, 'A chain to make wheels spin.')
petrol_object = GameObject.GameObject('Petrol', 24, True, True, False, 'A full can of petrol.' )
berries_object = GameObject.GameObject('Berries', FOREST_PATH_END_LOCATION, True, True, False, 'A handful of berries.')
axe_object = GameObject.GameObject('Axe', CABIN_LOCATION, True, True, False, 'A good quality wood chopping axe.')
fishing_rod_object = GameObject.GameObject('Fishing rod', FRONT_OF_CABIN_LOCATION, True, True, False, 'A sturdy Fishing rod.')
fish_object = GameObject.GameObject('Fish', POND_LOCATION, True, False, False, "Its a fish. Probably a Carp or something.")
mech_book_object = GameObject.GameObject('Mechanic book', CABIN_LOCATION, True, False, False, 'Its a book on all sorts of basic repairs and maintenance of Vehicles.')
dirt_bike_object = GameObject.GameObject('Dirt bike', CAMP_LOCATION, False,True,False, dirt_bike_descriptions[1])
bookshelf_object = GameObject.GameObject('Bookshelf', CABIN_LOCATION, False, True, False, 'Its a basic wooden book shelf with a few books scattered about.')
cook_book_object = GameObject.GameObject('Cook book', CABIN_LOCATION, True, False, False, 'A book with a all sorts of basic recipes in it. Probably Useful for cooking anything.')
wood_stove_object = GameObject.GameObject('Wood Stove', CABIN_LOCATION, False, True, False, 'Its a slightly rusted stove, looks like it need wood to work.')
shrimp_object = GameObject.GameObject('Shrimp', RIVER_BEACH_B_LOCATION, True, False, False, 'A hand full of river shrimp caught in a trap.')
shrimp_stirfry_object = GameObject.GameObject('Shrimp Stirfry', CABIN_LOCATION, True, False, False, 'A Classic.')
golden_flower_a_object = GameObject.GameObject('Golden Flower', FLOWER_FIELD_LOCATION, True, True, False, 'looks very shiny in the sun.')
golden_leaf_object = GameObject.GameObject('Golden leaf', FLOWER_FIELD_LOCATION, True, True, False, 'looks very shiny in the sun.')
rice_object = GameObject.GameObject('Rice', WATCH_TOWER_LOCATION, True, False, False, 'A package of instant rice' )
mouse_shop = GameObject.GameObject('Mouse', WATCH_TOWER_LOCATION, False, True, False, 'You see a sign next to the mouse at his stand\n[Rice ====== 1 shiny thing]\n[Petrol ==== 1 shiny thing]' )
tools_object = GameObject.GameObject('Tools', RIVER_BEACH_C_LOCATION, True, False, True, 'A box of standered tools, good for fixing things.')

game_objects = [brake_pads_object, chain_object,petrol_object, dirt_bike_object, axe_object, fish_object,
                fishing_rod_object, berries_object, mech_book_object, bookshelf_object, cook_book_object,
                 golden_leaf_object, golden_flower_a_object, rice_object, wood_stove_object, shrimp_object,
                 shrimp_stirfry_object, mouse_shop]


XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX = False


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
        elif (verb == 'FIX'):
            perform_fix_command(noun)
        elif (verb == 'TALK'):
            perform_talk_command(noun)
        elif (verb == 'BUY'):
            perform_buy_command(noun)
        else:   
            print_to_description("huh?")
    else:
        perfrom_start_command(verb)       
        

def perform_buy_command(item):
    game_object = get_game_object(item)
    global rice_object
    global petrol_object
    global golden_flower_a_object
    global golden_leaf_object
    
   
    if current_location == WATCH_TOWER_LOCATION:
        if golden_flower_a_object.carried:
            if game_object == petrol_object:
                game_object.carried = True
                golden_flower_a_object.carried = False
            
             
            elif game_object == rice_object:
                game_object.carried = True
                golden_flower_a_object.carried = False
                
            else:
                ptd('What?')
            
        elif golden_leaf_object.carried:
            if game_object == petrol_object:
                game_object.carried = True
                golden_leaf_object.carried = False
            
             
            elif game_object == rice_object:
                game_object.carried = True
                golden_leaf_object.carried = False
            
            else:
                ptd('What?')
        
        else: 
            ptd('You can\'t Afford that!')   
    else:
        ptd('Where?')    
        
        
def perform_talk_command(person):   
    global is_CAVE_LOCATION_blocked
    global is_bat_gone
    global know_about_berries
    know_about_stirfry = True
    global is_stirfry_given
         
    if person == 'BAT' and is_bat_gone == False and current_location == CAVE_ENTRY_LOCATION and not berries_object.carried:
        
        ptd('Bat : "You know, I could really go for a snake right now."')
        know_about_berries = True
        
    elif person == 'BAT' and is_bat_gone == False and current_location == CAVE_ENTRY_LOCATION and berries_object.carried:
        if know_about_berries:
            ptd('Bat : "Hey, these look delicious, Thanks"\nThe bat flys away, effortlessly carrying away the bolder under it.')
            is_CAVE_LOCATION_blocked = False
            berries_object.carried = False
        else:
            ptd('Bat : "You know, I could really go for a snake right now."')
            know_about_berries = True
            
    elif person == 'PIRATE TURTLE' and current_location == RIVER_BEACH_C_LOCATION and is_stirfry_given == False:
        if shrimp_stirfry_object.carried and know_about_stirfry == True:
            shrimp_stirfry_object.carried = False
            tools_object.carried = True
            ('"Arrr, Thanks matey!"')
        else:
            ptd('"Arrr matey, You know what really helps me sail the Seven seas? A Warm plate of Shrimp Stir fry. Too bad I haven\'t caught any shrimp in forever"')
            know_about_stirfry = True
    else:
        #if the person doesn't exist 
        ptd('Who?')
    
    
    
    

def perform_fix_command(item):
    game_object = get_game_object(item)
    
    if not (game_object is None):
        
        if current_location == dirt_bike_object.location:
            #Checks if location is same as bike
            
            if game_object == petrol_object:
                is_petrol_done = True
                ptd('Filled the tank!')
            
            elif game_object == chain_object:                 
                if mech_book_object.carried:
                    is_chain_done = True
                    ptd('You Replaced the chain!')
                    
                else:
                    ptd('If only you knew how...')
                     
                     
            elif game_object == brake_pads_object:                
                if mech_book_object.carried:
                    is_brakes_done = True
                    ptd('You Replaced the brakes!')
                    
                else:    
                    ptd('If only you knew how...')
                    
            else:
                ptd("You can\'t think of any way to make this work.")
            
            
        else:
            ptd('Fix what?')
        
        
    else:
        ptd('How?')
        
def perform_make_command(object):
    global game_objects
    game_object = get_game_object(object)
    
    if game_object == shrimp_stirfry_object:
        if current_location == CABIN_LOCATION and shrimp_object.carried and rice_object.carried:
            #makes thing
            shrimp_stirfry_object.carried = True
            rice_object.carried = False
            shrimp_object.carried = False
            
        else:
            ptd('Your missing something...')
    else:
        ptd('You Can\'t make that!')
        
def perform_use_command(noun):
    
    global is_WATCH_TOWER_LOCATION_blocked
    global is_FOREST_PATH_E_LOCATION_blocked
    global is_FLOWER_FIELD_LOCATION_blocked
    global game_objects
    game_object = get_game_object(noun)
    
    if not (game_object is None):
        if (game_object.carried == True):         
            # Goes through the objects that can be used
            if game_object == axe_object:
                #This needs to be fixed later
                if current_location == FOREST_PATH_F_LOCATION or current_location == FOREST_PATH_E_LOCATION and is_FOREST_PATH_E_LOCATION_blocked == True:
                    is_FOREST_PATH_E_LOCATION_blocked = False
                    print_to_description('You chopped the log blocking the path.')
                
                elif current_location == FOREST_PATH_C_LOCATION or current_location == WATCH_TOWER_LOCATION and is_WATCH_TOWER_LOCATION_blocked == True:
                    is_WATCH_TOWER_LOCATION_blocked = False
                    print_to_description('You chopped the log blocking the path.')
                                      
                elif current_location == FOREST_PATH_G_LOCATION and is_FLOWER_FIELD_LOCATION_blocked == True:
                    is_FLOWER_FIELD_LOCATION_blocked = False
                    print_to_description('You chopped the log blocking the path.')
                else:
                    print_to_description('The trees around you look far to Strong to be chopped down.')
                    
            elif game_object == fishing_rod_object:
                
                if current_location == POND_LOCATION:
                    #fish carp
                    global fish_object
                    
                    if not fish_object.carried:
                        fish_object.carried = True
                        ptd('After some time, you feel a fish pull on you bob and reel it in')
                    else:
                        ptd('You cast you rod, but get no catch.')
                
                elif (current_location == RIVER_BEACH_B_LOCATION) or (current_location == RIVER_BEACH_LOCATION_A) or(current_location == RIVER_BEACH_C_LOCATION) or (current_location == RIVER_CLIFF_LOCATION):
                    #fish shrimp
                    global shrimp_object
                    
                    if not shrimp_object.carried:
                        shrimp_object.carried = True
                        ptd('You cast your rod into the river, and it catches on a small net trap with a few shrimp caught in it.')
                    else:
                        ptd('You cast you rod, but get no catch.')
                else:
                    print_to_description('Where?')
                    
            else:
                print_to_description('You scratch your head, Trying to figure out how to use {}.'.format(noun.upper()))
                
        else:   
            #if they don't have the item, but it exists
            print_to_description('You look in your pockets, and fail to locate {}.'.format(noun.upper()))
            
    else:        
        #object dosn't exist
        print_to_description('What is a(n) {}?'.format(noun.upper))
       
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
        if (game_object == bookshelf_object and current_location == bookshelf_object.location):
            global mech_book_object
            global cook_book_object
            print_to_description("You look inside of the bookshelf, and see a few books titles")
            cook_book_object.visible = True
            mech_book_object = True
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
        print_to_description("")
    elif (current_location == CABIN_LOCATION):
        print_to_description("You are in a small, basic log cabin with a bed, a tiny kitchen, and a couple other living items. It pretty cold without the stove going. ")
    else:
        print_to_description( current_location)

def set_current_image():
    
    if (current_location == TITLE_LOCATION):
        image_label.img = PhotoImage(file = 'res/Title.gif')
    elif (current_location == CABIN_LOCATION):
        image_label.img = PhotoImage(file = 'res/Cabin.gif')
    elif (current_location == RIVER_BEACH_B_LOCATION or current_location == RIVER_BEACH_C_LOCATION or current_location ==  RIVER_BEACH_LOCATION_A ):
        image_label.img = PhotoImage(file = 'res/Beach.gif')
        
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
    
def ptd(text):
    print_to_description(text)

def main():
    
    build_interface()
    set_current_state()
    root.mainloop()    


main()
