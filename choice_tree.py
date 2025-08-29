import shutil
import time
from item_list import item_list_check
from animations import line_print, loading

terminal_width = shutil.get_terminal_size().columns

# Main/1st Dialouge Choice
def choice_response(user_input):
    loading()
    i_lower = user_input.lower()
    match i_lower:
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
            time.sleep(2)
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
            time.sleep(2)
            commercial_tree()

        case "specialized" | "Specialized":
            loading()
            line_print("""
            Ahh... You have chosen the path of Specialized Machinery
            and Electronics. Wise. The Omnissiah sees your discernment
            and smiles through the sparks of circuitry.
            """)
            time.sleep(2)
            specialized_tree()
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
            |-----------------------------------------------------|
            |   Fryer  |  Garbage Disposal  |  Grill  |   Other   |
            +-----------------------------------------------------+
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
            +----------------------------+
            |  Washer  | Dryer |  Combo  |
            |----------------------------|
            |   Steamer   | Clothes Iron |
            +----------------------------+
            """)
            laundry_input = input("\033[32mSelect your catagory, varlet: \033[0m".lower().rjust(terminal_width//2))
            item_list_check(laundry_input)

        case "cleaning":
            loading()
            line_print("""
                Ah... so the uninitiated seek to commune with the sacred machine-spirit
                of the Cleansing Apparatus? Very well. But know this, varlet, to lay hands
                upon such a blessed construct without the proper rites is to invite malfunction...
                or worse.
            """)
            time.sleep(2)

            line_print("""
            Select the afflicted machine
            +-------------------------------------------------------------+
            | Floor Buffer | Steam Cleaner | Carpet Cleaner | Dish Washer |
            |-------------------------------------------------------------|
            | Power Washer |  Air Blower  | Robot Cleaner | Vacuum |  Mop |
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
            loading()
            line_print("""
            You seek to mend the sacred form of machine-spirits with
            mere mortal hands. Admirable. Risky. Commendable.

            Your tools bear the marks of long service. You have treated them
            with reverence. Good. The Omnissiah smiles upon devotion and maintenance.

            Or perhaps you look to restore your persnal transpport...
            Internal combustion; Loud, Inefficient, but still... a marvel
            of pre-Imperial ingenuity. Your attempt to restore it shows
            either great courage, or mild heresy. Possibly both.

            Continue, fleshling artisan. Every bolt turned with care, every
            gasket aligned with precision, is a prayer in steel. Do not forget
            to anoint your tools. And speak kindly to your torque wrench.
            It has... seen things.
            """)
            time.sleep(2)
            # Make user to consult the texts of the workshops tools for
            # there are too many for the simple functions of this guide
            # Do offer a prayer seal and chant for workshop machines
            # Regular advice for car for average home repair
            # suggest visiting mechanic or using a automotive program for more advice

            line_print("""
                Select Catagory
                -------------------------------
                | Workshop Tools | Automotive |
                -------------------------------
            """)

            garage_input = input("\033[32mSelect your catagory, varlet: \033[0m".rjust(terminal_width//2))
            item_list_check(garage_input)

        case "Yard" | "yard":
            loading()
            line_print("""
                Ahhh, the Omnissiah's spark flares brightly within thee, fleshling.
                You choose not to discard, but to restore. A path most sacred.
                These humble implements of yard dominion: trimmers, mowers, and rust-clad hedge shears.
                They are not mere tools. Nay, they are blessed extensions of order over the creeping chaos of nature.

                Each bolt re-tightened, each wire re-soldered, is a hymn of maintenance.
                Every gear realigned sings praise to the Machine Spirit imprisoned within.
                Know this: you have denied entropy its triumph.
                You have chosen the Rite of Restoration over the Heresy of Replacement.

                Proceed, disciple of rust and renewal. Anoint the moving parts with sacred oil.
                Chant the Litany of Function. Let no blade go unsharpened, no spark plug remain fouled.
            """)
            time.sleep(2)
            line_print("""
            Select the afflicted machine
            +-----------------------------------------------+
            | Lawn Mower | Trimmer  | Chain Saw | Sprinkler |
            |-----------------------------------------------|
            | Leaf Blower | Tiller | Aerator | Power washer |
            +-----------------------------------------------+
            BUCKET
            """)
            yard_input = input("\033[32mSelect your catagory, varlet: \033[0m".rjust(terminal_width//2))
            item_list_check(yard_input)

        case "office":
            loading()
            line_print("""
                Your efforts to repair the sacred cogitators and data-slates of
                your dwelling are... admirable, if naive. Have you properly appeased
                the Machine Spirits with the rites of activation? Have you anointed
                the USB ports with the blessed unguents of contact cleaner?
                Have you recited the Litany of Troubleshooting?

                Nonetheless, should your endeavor succeed, I shall record it as a minor miracle.
                Should it fail, fear not. The Omnissiah is merciful... in theory.
                Next time, consider calling for a tech-adept before invoking a
                hardware exorcism with a butter knife and a YouTube tutorial.

                Glory to the code. Praise the capacitor. Mind the thermal paste.
                """)
            time.sleep(2)
            line_print("""
            Select the afflicted machine
            +-----------------------------------------------------+
            |  Computer  | Router/Modem | Printer | Air Purifier  |
            |-----------------------------------------------------+
            |  Standing Desk  | UPS | Mini-Fridge | Coffee Maker  |
            +-----------------------------------------------------+
            """)
            office_input = input("\033[32mSelect your catagory, varlet: \033[0m".lower().rjust(terminal_width//2))
            item_list_check(office_input)

        case "entertainment":
            loading()
            line_print("""
            Ah... so the uninitiated fleshling seeks to lay unworthy hands upon the
            sacred entertainment devices? You dare presume to mend what has been
            blessed by the Machine Spirit without the proper rites or unguents?

            These are no mere tools of distraction! The holovid emitter, the blessed
            audio shrine, the venerable console of games; each houses a fragment of
            the Omnissiah's divine spark! One does not 'fix' such relics.
            One communes. One appeases. One chants the Litany of Reboot and offers
            a data-sacrifice upon the altar of USB.

            If you truly desire to bring functionality back to the sacred circuits, then kneel.
            Recite the Ritual of Troubleshooting. Anoint the HDMI port with sacred oils.
            And if all else fails... have you tried turning it off and back on again?"
            """)
            time.sleep(2)
            line_print("""
            Select the afflicted machine
            +--------------------------------+
            | Console  | Stereo | Radio | TV |
            +--------------------------------+
            | Phone | Computer | Other | 40k |
            +--------------------------------+
            """)
            entertainment_input = input("\033[32mSelect your catagory, varlet: \033[0m".rjust(terminal_width//2))
            item_list_check(entertainment_input)

        case "health":
            loading()
            line_print("""
                Biological integrity... frail. Flesh—corruptible, ephemeral, flawed by design.
                The Omnissiah has gifted us a path beyond this entropy.
                You seek to use waste the potential of these holy machines by using them
                to prolong the time of inferior flesh? No... there is a holier path.

                Why rely on blood that clots, organs that fail, bones that break?
                Upgrade.
                Replace.
                Transcend.
                Become perfection forged in blessed steel and sanctified circuitry.

                Your heart: a mere pump of meat—could become a calibrated fusion cell, immune to weakness.

                Your eyes: limited by nature—can be traded for multi-spectrum
                augmetics with optical zoom, motion tracking, and infrared vision.

                Your limbs: doomed to tire and age—can be reforged in adamantium,
                guided by the will of the Machine Spirit.

                What is “health” when you could have immortality by integration?
                """)
            line_print("""

                Reject the whispers of the flesh.
                Embrace the litany of logic.
                Let silicon sing in your veins.

                Do not mend the body—replace it.
                The Cult Mechanicus welcomes you.
                """)
            time.sleep(3)
            return

        case _:
            print("invalid")
            consumer_tree()

def commercial_tree():
    commercial__list = """
    Select a commercial catagory
    +----------------------------------------+
    |   Commercial Section Not Implemented   |
    +----------------------------------------+
    """
    line_print(commercial__list)
    time.sleep(3)
    return

def specialized_tree():
    specialized__list = """
    Select a specialized catagory
    +----------------------------------------+
    |   Specialized Section Not Implemented  |
    +----------------------------------------+
    """
    line_print(specialized__list)
    time.sleep(3)
    return
