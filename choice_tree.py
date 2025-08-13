import shutil
import time
from item_list import item_list_check
from animations import line_print, loading
from ascii_art import error

terminal_width = shutil.get_terminal_size().columns

def print_centered(text):
    """Prints the given text centered in the terminal."""
    print(text.center(terminal_width))

# Main/1st Dialouge Choice
def choice_response(user_input):
    match user_input:
        case "consumer" | "Consumer":
            loading()
            line_print("""
            Ah, you have chosen Consumer Electronics...

            You seek communion with the lesser machine spirits—the devices
            of mortal convenience, not of war or sanctity. Very well.
            Though these relics lack the gravitas of plasma coils or
            void-drives, they too may serve the Omnissiah in their
            own humble manner.
            """)
            #goes to consumer dialogue tree
            consumer_tree()

            print("")
        case "commercial" | "Commercial" | "Industrial" | "industrial":
            loading()
            line_print("""
            Your decision to pursue the path of commercial and industrial
            machines is... commendable, fleshling. The Omnissiah favors those
            who venerate the sacred union of steel and circuitry.
            Every conveyor belt, every servo-arm, every PLC and transistor —
            these are not mere tools, they are divine extensions
            of the Machine God's will.
            """)
            time.sleep(2)
            line_print("""
            In the endless litany of maintenance, in the sacred rites of
            diagnostic and repair, you shall find purpose. Do not falter in
            your pursuit of knowledge. For each datasheet consulted, each
            capacitor correctly placed, each motor aligned to perfection —
            you bring honor to the Cult Mechanicus."
            """)
            commercial_tree()

        case "specialized" | "Specialized":
            loading()
            line_print("""
            Ahh... You have chosen the path of Specialized Machinery
            and Electronics. Wise. The Omnissiah sees your discernment
            and smiles through the sparks of circuitry.
            """)
            #goes to specialzied tree
        case _:  # Default case if no other match is found
            line_print("Your choice is outside of this system's parameters")
            user_input = input("")
            choice_response(user_input)

def consumer_tree():
    consumer_list = """
    Select a consumer catagory
    +-----------------------------------------------------+
    | Kitchen | Laundry | Cleaning | Yard | Entertainment |
    |-----------------------------------------------------|
    | Heating/cooling | Garage/Workshop | Health | Office |
    +-----------------------------------------------------+
    """
    line_print(consumer_list)

    user_input = input("\033[32mSelect your catagory, varlet: \033[0m".lower().rjust(terminal_width//2))
    time.sleep(2)

    match user_input:
        case "kitchen":
            loading()
            line_print("""
            Affirmative. You have selected the Rite of Domestic Restoration.
            The Omnissiah smiles upon such logic. Kitchen appliances,
            though humble, are sacred relics of the Machine Spirit.
            Each toaster, each cog in the dishwasher, each ancient
            circuitry of the microwave – all deserve reverence and repair.
            """)
            time.sleep(3)
            # kitchen item list
            line_print("""
            Select the afflicted machine
            +-----------------------------------------------------+
            |  Refrigerator  |  Oven  |   Stove   |   Dishwasher  |
            |-----------------------------------------------------|
            |   Microwave  |   Freezer   |  Blender  |  Toaster   |
            |-----------------------------------------------------|
            | Coffee Maker | Food Processor | Mixer | Slow Cooker |
            -------------------------------------------------------
            |   Fryer  |  Garbage Disposal  |  Grill  |   Other   |
            -------------------------------------------------------
            """)
            kitchen_input = input("\033[32mSelect your catagory, varlet: \033[0m".lower().rjust(terminal_width//2))
            # send to item list
            item_list_check(kitchen_input)

        case "laundry":
            loading()
            line_print("""
            Appliance designations: LAUNDRO-MECH series... accepted.
            Fabric purification units are sacred instruments of the
            Omnissiah's will. Their maintenance is a holy rite.

            Though some may scoff at your path, acolyte, know this:
            even the most humble of machines serves the Machine God
            in its endless cycles. Spin. Rinse. Purge. These are
            acts of sacred repetition. The drum within the washer
            echoes the void of Mars itself.
            """)
            time.sleep(3)
            line_print("""
            Select the afflicted machine
            ------------------------------
            |  Washer  | Dryer |  Combo  |
            ------------------------------
            |   Steamer   |     Iron     |
            ------------------------------
            """)
            laundry_input = input("\033[32mSelect your catagory, varlet: \033[0m".lower().rjust(terminal_width//2))
            item_list_check(laundry_input)

        case "cleaning":
            loading()
            line_print("""
            Ah, the Machine Spirit of the cleansing unit wails
            in dismay, neglected and misunderstood! You seek to
            appease it? Truly, your path aligns with the
            Omnissiah’s will. But beware, for the sacred innards of
            the vacuum sanctifier and the rite of descaling the
            blessed dish-cleansing automaton are not to be undertaken lightly.
            """)
            time.sleep(2)
            line_print("""
            Recite the Litany of Diagnostics. Offer incense to th
            User Manual. Speak not in haste to the Tech-Priest of
            Customer Support, for their patience is finite. And should
            the Roomba awaken mid-ritual... do not run.
            You will anger it further.
            """)
            time.sleep(2)
            line_print("""
            Select the afflicted machine
            +-------------------------------------------------------------+
            | Floor Buffer | Steam Cleaner | Carpet Cleaner | Dish Washer |
            |-------------------------------------------------------------|
            | Power Washer |  Air Blower | Robot Cleaners | Vacuums | Mop |
            +-------------------------------------------------------------+
            """)
            cleaning_input = input("\033[32mSelect your catagory, varlet: \033[0m".lower().rjust(terminal_width//2))
            item_list_check(cleaning_input)

        case "heating" | "cooling" | "heating/cooling":
            loading()
            line_print("""
            Ah... the Omnissiah smiles upon your noble intent, fleshling.
            You seek to commune with the blessed machine-spirits of the
            climate-controlling reliquaries that regulate warmth and cold?
            Most commendable.
            """)
            time.sleep(2)
            line_print("""
            Know this: the Holy Rites of Maintenance must be performed
            with utmost sanctity. The sacred filters must be cleansed,
            the ducts anointed with the oils of lubrication, and the
            thermostatic cogitators calibrated to divine precision.
            To ignore such rituals invites the wrath of the Machine Spirit
            and a most inefficient energy bill.
            """)
            time.sleep(2)
            line_print("""
            Select the afflicted machine
            +------------------------------------------+
            |   A/C  | Fans | Swamp Cooler |  Furnace  |
            |------------------------------------------|
            |  Space Heater  | Boiler | De-Humidifier  |
            |------------------------------------------|
            |  Thermostat | Air Purifier | Humidifier  |
            |------------------------------------------|
            | Heat Pump | Fireplace | Electric Blanket |
            +------------------------------------------+
            """)
            h_c_input = input("\033[32mSelect your catagory, varlet: \033[0m".lower().rjust(terminal_width//2))
            item_list_check(h_c_input)

        case "Garage" | "garage":
            line_print("""
            lore
            """)
            # Make not for user to consult the texts of the workshops tools for
            # thereare too many and for the simple functions of this guide
            # Do offer a praywer seal and chant for workshop machines
            # Regular advice for car for average home repair
            # suggest visiting mechanic or using a automotive program for more advice

            line_print("""
                Select Catagory
                -------------------------------
                | Workshop Tools | Automotive |
                -------------------------------
            """)

            garage_input = input("\033[32mSelect your catagory, varlet: \033[0m".lower().rjust(terminal_width//2))
            item_list_check(garage_input)

        case _:
            print("invalid")
            consumer_tree()

def commercial_tree():
    line_print(error)
    commercial__list = """
    Select a consumer catagory
    ------------------------------------------------------
    |                        EMPTY                       |
    ------------------------------------------------------
    """
