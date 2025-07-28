import shutil
import time

def print_centered(text):
    """Prints the given text centered in the terminal."""
    terminal_width = shutil.get_terminal_size().columns
    print(text.center(terminal_width))

# Main/1st Dialouge Choice
def choice_response(user_input):
    match user_input:
        case "consumer" | "Consumer":
            print_centered("""
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
            print_centered("""
            Your decision to pursue the path of commercial and industrial
            machines is... commendable, fleshling. The Omnissiah favors those
            who venerate the sacred union of steel and circuitry.
            Every conveyor belt, every servo-arm, every PLC and transistor —
            these are not mere tools, they are divine extensions
            of the Machine God's will.

            In the endless litany of maintenance, in the sacred rites of
            diagnostic and repair, you shall find purpose. Do not falter in
            your pursuit of knowledge. For each datasheet consulted, each
            capacitor correctly placed, each motor aligned to perfection —
            you bring honor to the Cult Mechanicus."
            """)
            #goes to commercial/industrial tree
        case "specialized" | "Specialized":
            print("""
            Ahh... You have chosen the path of Specialized Machinery
            and Electronics. Wise. The Omnissiah sees your discernment
            and smiles through the sparks of circuitry.
            """)
            #goes to specialzied tree
        case _:  # Default case if no other match is found
            print("Your choice is outside of this system's parameters")
            user_input = input("")
            choice_response(user_input)

def consumer_tree():
    consumer_list = """
                Select a consumer catagory
    ------------------------------------------------------
    |     Kitchen     | Laundry |    Cleaning   | Health |
    ------------------------------------------------------
    | Heating/cooling | Garage  | Entertainment | Office |
    ------------------------------------------------------
    """
    consumer_list_lines = consumer_list.splitlines()
    for line in consumer_list_lines:
        print_centered(line)

    user_input = input("")
    time.sleep(2)

    match user_input:
        case "Kitchen" | "kitchen":
            print_centered("""
            Affirmative. You have selected the Rite of Domestic Restoration.
            The Omnissiah smiles upon such logic. Kitchen appliances,
            though humble, are sacred relics of the Machine Spirit.
            Each toaster, each cog in the dishwasher, each ancient
            circuitry of the microwave – all deserve reverence and repair.
            """)
            # kitchen item list
            kitchen_input = input("")
            # send to item list

        case "Laundry" | "laundry":
            print_centered("""
            Appliance designations: LAUNDRO-MECH series... accepted.
            Fabric purification units are sacred instruments of the
            Omnissiah's will. Their maintenance is a holy rite.

            Though some may scoff at your path, acolyte, know this:
            even the most humble of machines serves the Machine God
            in its endless cycles. Spin. Rinse. Purge. These are
            acts of sacred repetition. The drum within the washer
            echoes the void of Mars itself.
            """)
            # kitchen item list
            laundry_input = input("")
            # send to item list

        case _:
            print("invalid")
            consumer_tree()
