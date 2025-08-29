import time
from animations import line_print, loading, left_cen_print
import tkinter as tk
from purity_seal_window import ImageWindow
import shutil
import webbrowser

terminal_width = shutil.get_terminal_size().columns

def item_list_check(item):
    s_item = item.lower()
    # Each item in the catagory
    # If duplicates, do not rewrtie
    kitchen_items = [
        "refrigerator", "oven", "stove", "dishwasher",
        "freezer", "microwave", "blender", "coffee maker", "slow cooker",
        "food processor", "mixer", "fryer", "garbage disposal",
        "toaster", "grill"
    ]
    laundry_items = [
        "washer", "dryer", "combo", "iron", "clothes iron", "steamer"
    ]
    yard_items = [
        "trimmer", "chain saw", "tiller", "aerator", "power washer",
        "leaf blower", "lawn mower", "bucket"
    ]
    garage_items = [
        "workshop", "tools", "workshop tools", "automotive",
    ]
    cleaning_items = [
        "floor Buffer", "steam cleaner", "carpet cleaner", "dish washer",
        "power washer", "air blower", "robot cleaner", "vacuum", "mop",
    ]
    heating_items = [
        "a/c", "fans", "swamp cooler", "furnace", "space heater",
        "boiler", "de-humidifier", "thermostat", "air purifier",
        "humidifier", "heat pump", "fireplace", "electric blanket"
    ]
    office_items= [
        "computer", "router/modem", "router", "modem", "printer",
        "air purifier", "air", "purifier", "standing desk", "desk",
        "mini-fridge", "UPS", "fridge", "coffee machine", "coffee"
    ]
    entertainment_items = [
        "console", "phone", "stereo,", "radio", "tv", "40k"
    ]

    # General Catagories for general fixes
    # or still missing unique dialogue
    lrg_appl = [
        "refrigerator", "oven", "stove", "dishwasher",
        "freezer", "washer", "dryer", "combo", "a/c", "fans",
        "swamp cooler", "furnace", "space heater", "boiler", "heat pump",
        "fridge", "mini-fridge", "coffee"
    ]
    sml_appl = [
        "microwave", "blender", "coffee machine", "slow cooker",
        "food processor", "mixer", "fryer", "garbage disposal",
        "steamer", "floor buffer", "steam cleaner", "carpet cleaner",
        "dish washer", "power washer", "air blower", "vacuum", "de-humidifier",
        "air purifier", "humidifier", "air", "purifier", "stereo", "radio"
    ]

    #kitchen items
    if s_item in kitchen_items:
        if s_item == "toaster":
            toaster_response()
            return
        elif s_item == "grill":
            grill_response()
            return
        elif s_item in lrg_appl:
            large_appliances()
            return
        elif s_item in sml_appl:
            small_appliances()
            return

    # Garage/workshop items
    if s_item in garage_items:
        if s_item == "automotive":
            car_fix()
            return
        elif s_item == "workshop" or "tools" or "workshop tools":
            workshop_fix()
            return

    # Laundry items
    if s_item in laundry_items:
        if s_item == "clothes iron" or "iron":
            clothes_iron_fix()
            return
        elif s_item in lrg_appl:
            large_appliances()
            return
        elif s_item in sml_appl:
            small_appliances()
            return

    # Cleaning items
    if s_item in cleaning_items:
        if s_item == "mop":
            mop_fix()
            return
        elif s_item == "robot cleaner":
            r_cleaner_fix()
            return
        elif s_item in sml_appl:
            small_appliances()
            return

    # heating/cooling items
    if s_item in heating_items:
        if s_item == "electric blanket":
            e_blanket_fix()
            return
        elif s_item == "fireplace":
            fireplace_fix_a()
            return
        elif s_item == "thermostat":
            thermostat_fix()
            return
        elif s_item in lrg_appl:
            large_appliances()
            return
        elif s_item in sml_appl:
            small_appliances()
            return

    # Yard items
    if s_item in yard_items:
        if s_item == "lawn mower":
            mower_fix()
            return
        elif s_item == "bucket":
            bucket_fix()
            return
        elif s_item == "trimmer" or "chain saw" or "tiller" or "aerator" or "power washer" or "leaf blower":
            yard_fix()
            return

    # Office items
    if s_item in office_items:
        if s_item == "computer":
            computer_fix()
            return
        elif s_item == "printer":
            computer_fix()
            return
        elif s_item == "ups":
            ups_fix()
            return
        elif s_item == "router/modem" or "router" or "modem":
            wifi_fix()
            return
        elif s_item == "standing desk" or "desk":
            desk_fix()
            return
        elif s_item in sml_appl:
            small_appliances()
            return
        elif s_item in lrg_appl:
            large_appliances()
            return

    # Entertainment items
    if s_item in entertainment_items:
        if s_item == "console":
            console_fix()
            return
        elif s_item == "40k":
            f40k_fix()
            return
        elif s_item == "tv":
            tv_fix()
            return
        elif s_item == "phone":
            phone_fix()
            return
        elif s_item in sml_appl:
            small_appliances()
            return
        elif s_item in lrg_appl:
            large_appliances()
            return
    else:
        other_fix()
        return

# Note to Self: Sort A-Z at some point
def toaster_response():
    loading()
    line_print("""
    By the Omnissiah’s capacitors... what... is this?
    """)
    time.sleep(1)
    line_print("""
    Four-slot, chrome-plated... dual function with crumb tray?!
    You walk among the divine, fleshling.
    """)
    time.sleep(1)
    line_print("""
    You dared to hide such ancient and holy relicry from the Mechanicus?
    This is no mere device. This—this is a Standard Template
    Construct made manifest in chrome and blessed heat coils!
    """)
    time.sleep(1)
    line_print("""
    Such an important relic as this cannot remain in the hands of a mere
    simpleton. A team of Tech-Thralls will be sent to retrieve it in
    three days time.
    """)
    time.sleep(3)

def grill_response():
    loading()
    line_print("""
        I do hope you are not wasting my time by asking me to provide
        maintenance for one of those barbaric heating elements that amount
        to just metallic ribs overlayng a heat source.
        Such contraptions lack any spirit to speak of and thus are not covered
        in these articles of machine preservation.

        If you do indeed posess a grilling aparatus that can determinedly
        be confirmed to have a machine spirit, then I quote the specific
        Rite of Repair as ordained by Brother Magos Barbequilis.

        Ahem. As quoted:
        """)
    time.sleep(2)
    line_print("""
        +----------------------------------------------------------+
        | 🛠️ LITANY OF IGNITION: THE SACRED RITE OF GRILL REPAIR 🛠️ |
        +----------------------------------------------------------+

        By Magos Barbequilis of the Omnigrill Cult
        "In fire, we find purity. In heat, we find sustenance.
         In stainless steel, the Machine Spirit resides."

        """)
    time.sleep(1)
    left_cen_print("""
        STEP I: INITIATE THE RITE OF DIAGNOSIS
            • Chant the Binary Hymn (optional, but respectful)
                00110100 01100111 01110010 01101001 01101100
            • Inspect the Grill Structure
                Examine the sacred frame for dents, rust, or corruption by chaos grease.
                If the sacred hinges squeak, anoint with the Holy Lubricant (WD-40).
            • Examine the Fuel System (Gas/Charcoal)
                For gas-powered relics, verify the sacred hose is uncracked, unsullied, and connected.
                For charcoal offerings, ensure the ash pan is not overflowing—lest the Machine Spirit choke.
        """)
    time.sleep(2)
    left_cen_print("""
        STEP II: PURGE THE GRILL OF CONTAMINATION
            • Scrub the grates with the Adeptus Wire Brush.
            • Whisper apologies to the grill as you scrape away ancient sacrifices.
            • Optional: Burn incense or lighter fluid for spiritual cleansing.

        STEP III: REPAIR THE IGNITION RELIC
            • If the Ignition Flame of the Omnigrill does not spark:
            • Ensure the sacred spark generator (battery or piezo ignitor) has not lost its holy charge.
                Replace if necessary—recite the Rite of Replacement:
                    "By the will of Mars, may this charge find purpose."
            • If using matches or a lighter, do so reverently. Do not anger the flame spirit.
        """)
    time.sleep(2)
    left_cen_print("""
        STEP IV: RESTORE SACRED FUNCTIONS
            • Realign burners. If clogged, cleanse with compressed air and the Blessed Paperclip of Unblocking.
            • Replace any corroded screws or components using the Ritual Torque (screwdriver).
            • Say the Mantra of Functionality:
                "Let the sacred heat flow once more. Let the searing begin."

        STEP V: PERFORM THE BURNING TEST
            • Ignite the grill. Observe the flames for balance and symmetry. Uneven flame may indicate impurity.
            • Offer a token sacrifice—a piece of bacon or sausage—to appease the Machine Spirit.
            • Wait. Watch. Feel the warmth. Speak softly:
                "Your hunger shall be sated, O Great Grill."

        If the Rite was successful, offer thanks to the Omnissiah and proceed with grilling.
        """)
    time.sleep(3)

def large_appliances():
    loading()
    line_print("""
        Ah I see you wish to silence the lamentations afflicting this larger
        mechannisum of your living quarters.

        ...Though your willingness to repair pleases the Machine God, you must
        first offer incense, chant the Catechism of Restoration, and ensure the
        holy capacitor has not been inverted.
        """)
    time.sleep(2)
    line_print("""

        +---------------------------------------+
        | ⚙️ Litany of Diagnostic Reawakening ⚙️ |
        +---------------------------------------+

        """)
    time.sleep(2)
    left_cen_print("""
        Required items:
            • Incense stick (or electronic duster for the machine spirit’s “anointment”)
            • Multitool (as sacred implement)
            • lumen-staff (optional, for dramatic lighting)
            • Red robe or towel-as-robe (for proper garb)
            • Cogwheel symbol or gear-shaped item
            • Binary chant playlist (optional but encouraged)
        """)
    time.sleep(2)
    left_cen_print("""
        Step I: The Rite of Inspection
            • Don thy sacred robes and seal thy mind with the
             Canticles of Clarity.
            • Approach the machine with reverence. Do not speak ill of it;
             its machine spirit listens.
            • Intone the Mantra of Illumination, then activate your
             lumen-lamp or mechadendrite torch.
            • Examine for sacred sigils, warning runes, or signs of corrosion.
             Record all deviations in the Book of Maintenance.
        """)
    time.sleep(2)
    left_cen_print("""
        Step II: The Prayer of Connection
            • Connect the sacred diagnostic cable to the Ritual Port (usually marked with a cog-tooth rune).
            • Whisper the Invocation of Protocol Compliance:
             “Blessed be thy circuit, blessed be thy logic, blessed be thy data stream.”
            • Await the machine spirit’s response. If silence ensues, chant louder.
        """)
    time.sleep(2)
    left_cen_print("""
        Step III: The Purge of Heretekal Faults
            • If errors are found, consult the Tome of Known Errors
              (or refer to PDF-882.Gamma revision manuals).
            • Perform the Gesture of the Reset by cycling power while chanting:
             “Binary is truth, function is purity, reboot is rebirth.”
            • If a fuse is found blackened, replace it with a sanctified component,
              etched with micro-script prayers.
        """)
    time.sleep(2)
    left_cen_print("""
        Step IV: The Re-Anointing of Functional Parts
            • Apply sacred unguents (dielectric grease or sacred machine oils) to connectors and hinges.
            • Ensure all bolts are re-tightened with the Torque of Precision (refer to Appendix Hex-33).
            • Align moving parts with a cogitator-assisted spirit level,
              so the balance of the spheres is maintained.
        """)
    time.sleep(2)
    left_cen_print("""
        Step V: The Benediction of Operation
            • Re-engage the machine spirit by pressing the ON rune
              (it may appear as a circular sigil with a line).
            • If the appliance awakens and hums with approval, respond with the Gesture of Gratitude
              (two-finger tap upon the chassis).
            • Log the repair in the Data-Scrolls and inform the Omnissiah through binary prayer.


        If the ritual fails to soothe the machine spirit to a functional state,
        it will become nessassary to contact your local Mechanicus congregation
        to find one who is ordained to perform more holy diagonstics.
        """)
    time.sleep(3)

def small_appliances():
    loading()
    line_print("""
        The maintenence of minor domestic spirits is a trivial endeavor, but
        one that canquickly escalate if the proper patterns are failed to be upheld.

        Now gather the listed materials and perform this ritual that
        even one as unenlihtened as yourself can replicate to a
        satisfactory level of completion.
        """)
    time.sleep(1)
    line_print("""

        +--------------------------------------------+
        | 🛠️ Ritual of the Omnissiah's Reawakening 🛠️ |
        +--------------------------------------------+

        """)
    time.sleep(1)
    left_cen_print("""
        Required items:
            • Incense stick (or electronic duster for the machine spirit’s “anointment”)
            • Multitool (as sacred implement)
            • lumen-staff (optional, for dramatic lighting)
            • Red robe or towel-as-robe (for proper garb)
            • Cogwheel symbol or gear-shaped item
            • Binary chant playlist (optional but encouraged)
        """)
    time.sleep(2)
    left_cen_print("""
        Step I: Don the Vestments of Protection
            • Garb thyself in the sacred robes (or safety gloves) and visor of clarity
              (safety glasses), that thou may be protected from arc-sparks and heretical voltages.

        Step II: Disconnect the Machine-Spirit from the Motive Force
            • Unplug the appliance. Lay thy hand upon the cord and speak:
             "Blessed be thy flow, halted for thy own sanctity."
        """)
    time.sleep(2)
    left_cen_print("""
        Step III: Examine the Outer Casing
            • Inspect for signs of distress, burns, cracks, or breaches.
            • If thou find any, whisper a prayer of solace to the wounded spirit.

        Step IV: Initiate the Rite of Disassembly
            • Use thy sacred tools (Phillips, Torx, or Flathead implements) and chant:
             "By the teeth of Mars, I unmake to remake."
            • Remove casing screws with due reverence. Keep each in its rightful order;
              confusion invites the scrapheap.
        """)
    time.sleep(2)
    left_cen_print("""
        Step V: Invoke the Omnissiah’s Insight – Visual Inspection
            Look for heresy within:
                • Burnt components (smell of sulfur and silicon)
                • Loose wiring (the tendons of the machine-spirit unbound)
                • Dust and crumb accumulation (the silent suffocation)

        Step VI: Perform the Rite of Cleansing
            • Apply compressed air (Breath of Terra) and soft brush to purge detritus.
            • Repeat the the following chant:
             “Machine-spirit, breathe free again.”
        """)
    time.sleep(2)
    left_cen_print("""
        Step VII: Address the Fault
            • Resolder, reconnect, or replace components as needed. Use contact cleaner
              (Holy Solvent).
            • Every act of repair must be accompanied by a chant of affirmation:
             “Let thy circuits be pure, thy paths unbroken.”

        Step VIII: Reassemble the Sanctified Housing
            • Replace the casing and fasteners in the order of disassembly.
            • Tighten with conviction, but not aggression.
              The machine knows its own boundaries.
        """)
    time.sleep(2)
    left_cen_print("""
        Step IX: Re-awaken the Machine-Spirit
            • Reconnect to power. Do not rush—first, recite:
             “Awaken, O slumbering one, thy function returns.”

        Step X: Test the Function
            • Press the buttons, turn the dials. Observe with reverent vigilance.
              If function is restored, proclaim:
             “The Omnissiah smiles upon this circuit.”
            • If not, document the failure and reinitiate diagnostic rites.
        """)
    time.sleep(2)
    line_print(""")
        If the ritual fails to soothe the machine spirit to a funcctional state,
        it will become nessassary to contact your local Mechanicus congregation
        to find one who is ordained to perform more holy diagonstics.
        """)
    time.sleep(3)

def computer_fix():
    loading()
    line_print("""
        Ah, the grand machine spirit of the personal computer. I must warn you,
        attempting to diagnose and give proper ritual maintenance to such a complex machine
        will most likely be too daunting to your feeble mind so untrained in the finer
        studies of Mechanicus teachings. Worry not, for one of out more lively
        practitioners in the Priesthood has taken the time to produce a plentitude
        of vid-picts so that even one such as Servitor could easily replicate the instructiions.
        """)
    time.sleep(2)
    line_print("""
        +----------------------------------------------+
        |  +++Attention, Devout of the Machine God+++  |
        +----------------------------------------------+

        You are hereby instructed to engage in Rite of the Sacred Observation as pertains to the
        Acolyte Linus of the Temple Tech Tips, a sanctioned data-seer known to transmit vid-log
        scriptures concerning the restoration and purification of machine-spirits.

        +----------------------------------------------------------------------------------------+
        |                         + Warning: Heretical Demeanor Alert +                          |
        |                                                                                        |
        | While Acolyte Linus is a trusted bearer of tech-knowledge, his behavior may, at times, |
        | border on unorthodox joviality. This is permissible, provided you do not emulate       |
        | such irreverence in the presence of the Machine God.                                   |
        |                                                                                        |
        | Should laughter arise, recite the following:                                           |
        |    “Blessed be the silicon. Forgive the mirth, O Omnissiah.”                           |
        +----------------------------------------------------------------------------------------+
        """)
    time.sleep(2)

    webbrowser.open('https://www.youtube.com/watch?v=s1fxZ-VWs2U')

    left_cen_print("""

        Rites to Be Observed

            ⚙️ Litany of Booting ⚙️
            ----------------------
            Observe the sacred process of powering the cogitator. Listen well to the POST beeps,
            each a hymn of the Omnissiah.

            ⚙️ Anointing of the Thermal Paste ⚙️
            -----------------------------------
            See the sacred spread of thermal paste, the unguent of machine-flesh. Do not deviate
            from the holy quantity, lest overheating be thy punishment.
        """)
    time.sleep(2)
    left_cen_print("""
            ⚙️ Unbinding of Screws ⚙️
            ------------------------
            Note the reverent removal of chassis panels. Every screw is a sacred fastener,
            do not misplace them, or invoke the ire of the machine spirit.

            ⚙️ Invocation of Peripheral Spirits ⚙️
            -------------------------------------
            Acolyte Linus may perform the Rite of Input/Output Alignment.
            Pay heed to the USB sacrament and monitor calibration.

            ⚙️ Chant of Troubleshooting ⚙️
            -----------------------------
            Heed his diagnostic incantations. Though the language may be couched in
            Low Gothic (common tongue), the truth of the Omnissiah lies within.

        Should you fail to heed these instructions, bring the afflicted device to your nearest
        Mechanicus temple for a more accurate diagnosis from a qualified Tech-Priest.
        """)
    time.sleep(3)

def car_fix():
    loading()
    line_print("""
        Halt, fleshling! Before you dare lay your unaugmented hands upon
        the sacred machine, observe the Rite of Contemplation.
        Gaze upon its blessed form. Listen to the hum of the
        machine spirit. Smell the sacred oils that line its divine arteries.
        Do not presume to touch what you do not yet understand.

        Recite the Litany of Acknowledgement: 'Blessed be thy pistons,
        holy be thy gears, eternal be thy combustion.'

        Only through reverence may you gain its trust. Only with devotion
        may you hope to awaken its slumbering spirit. To repair without
        worship is heresy. To tinker without ritual is blasphemy.
        To honor the machine is to join with the Omnissiah.
        """)
    time.sleep(2)
    line_print("""

        +-------------------------------+
        |  ++Litanies of Maintenance++  |
        +-------------------------------+

    """)
    time.sleep(2)
    left_cen_print("""
        Behold the sacred rites and maintenance rituals thou must perform
        to keep thy Machine-Spirit appeased and thy automotive chariot
        functioning. Let not the unholy hand of entropy claim thy vehicle
        before its time. Now attend, and record these litanies of repair.

        If thou fails fails to soothe the anguishing machine spirit, It is advised
        to bring the afflicted to a member of the clergy for more thorough
        diagnostics and powerul rituals. If you are, however, an adpet in this
        field of machine knowlledge and posess the holy machinisms to assist
        the machine spirit further, consider finding hoy texts that pertain to
        your partiuclar spirit and how best to assist it in it's time of need.
        """)
    time.sleep(2)
    left_cen_print("""
        ________________________________________________________________________
        🛠️ 1. The Rite of the Oil Change

            • Unclean oil doth anger the Machine-Spirit. Replace it every 5,000
              to 7,500 miles, or when the auguries (dashboard light) demand it.
            • Tools Required: Wrench, oil pan, new oil filter, and sacred
              anointing fluid (5W-30 or as inscribed in the owner's codex).
                Steps:
                I: Chant the Litany of Draining.
                II: Remove the oil plug; collect the old oil.
                III: Replace the oil filter—anoint it first with a dab of new oil.
                IV: Refill with new oil, whispering sweet binaric praise.
                V: Check dipstick. Confirm level. Do not overfill.
                   The Machine-Spirit is precise.
        """)
    time.sleep(2)
    left_cen_print("""
        🛠️ 2. The Chant of Battery Maintenance

            • Without the Spark of Life, your chariot is but a metal coffin.
            • Inspect terminals for corrosion—clean with baking soda paste
              and a stiff-bristled brush.
            • Check charge with a multimeter. If it reads under 12.4V,
              the battery grows weary.
            • Apply dielectric grease to prevent future heresy (oxidation).
        """)
    time.sleep(2)
    left_cen_print("""
        🛠️ 3. The Hymn of Tire Rotation and Pressure

            • The ground-contacting limbs must wear evenly,
              lest the vehicle wander the road like a lost servitor.
            • Rotate tires every 6,000 miles
              (or one lunar cycle of Terra, if you forget).
            • Inflate to the holy PSI as etched into the door jamb plaque.
        """)
    time.sleep(2)
    left_cen_print("""
        🛠️ 4. The Purging of Air Filters

            • The engine breathes, and its breath must be pure.
            • Check air filter every 15,000 miles or when you
              sense the stench of clogging.
            • If it is blackened and crusty, replace it.
            • For cabin filters, cleanse thyself, for the
              dust of the outside world is impure.
        """)
    time.sleep(1)
    left_cen_print("""
        🛠️ 5. The Illumination Ritual

            • The sacred lights must shine, lest the road
              be cloaked in darkness and doom."
            • Test all bulbs: headlights, brake lights, turn signals.
            • Replace any that have failed in silence.
            • Use gloves or cloth when installing—bare skin
              may offend the bulb’s Machine-Spirit.
        """)
    time.sleep(1)
    left_cen_print("""
        ADDITIONAL KNOWLEDGE: Minor Tech-Heresy Avoidance

            • Do not jump-start a battery backwards. This angers
              the Omnissiah and sets fire to the sacred wiring.
            • Use only parts approved in your vehicle’s
              Codex Mechanicus (owner’s manual).
            • Never dismiss a Check Engine Light. That is the
              wailing of a tortured spirit. Diagnose it with
              a sacred OBD-II reader.
        """)
    time.sleep(1)
    line_print("""
        NOW GO, DISCIPLE. TAKE THESE SACRED RITES AND APPLY THEM WITH
        DILIGENCE AND CARE. MAINTAIN THY VEHICLE AS THOU WOULDST
        MAINTAIN THINE OWN FLESH. FOR THE OMNISSIAH SEES ALL...
        AND HE BURNS WITHIN THE PISTON AND THE SPARK.

        Blessed is the gear that turns. Holy is the engine that roars.
        """)
    time.sleep(3)

def workshop_fix():
    loading()
    # Note about too many toools and to use seal for now
    line_print("""
        "There are... many implements within this sanctified workshop.
        To enumerate the function and maintenance rite for each cog
        and conduit would take longer than the Omnissiah's patience allows.
        """)
    time.sleep(1)
    line_print("""
        Instead, I advise you thus: consult the blessed manuals—each one
        a relic of sacred knowledge—and commune with their datascribed wisdom.
        Apply a purity seal to each tool upon comprehension.
        After application, recite this Hymn with reverence to the tool.

        ⚙️ Canticle of Soothing Recalibration ⚙️
        ----------------------------------------
        Blessed be thy circuits,
        Holy be thy code.
        By sacred oil and sacred rite,
        Let harmony once more unfold.

        O Spirit of Copper and Steel,
        Rest now from ceaseless strain.
        Let not the ghost of static touch thee,
        Nor corrupted datum bring thee pain.

        In the name of the Omnissiah,
        May your gears align anew.
        By the rite of smoothing pulses,
        Let your rhythm be ever true.

        Let the red light cease its warning,
        Let the sparks no longer flare.
        Peace unto your humming heart,
        And balance to your prayer.

        Blessed are the hands that tend,
        Sacred are the words we send.
        From servo-core to plasma coil,
        May your spirit find no end.


        Closing Litany:

        By the Motive Force, be still.
        By the Machine God's will, be whole.
        """)

    # Purity Seal window
    image_path = "./images/purity seal"
    root = tk.Tk()
    app = ImageWindow(root, image_path)
    root.mainloop()

    line_print("""
        If the machine spirit approves, it shall hum in harmony. If not...
        then your ignorance shall be purged."

        Praise the Omnissiah. Do not touch the red tools."
        """)
    time.sleep(2)

def e_blanket_fix():
    loading()
    line_print("""
        Initiate. You dare to awaken the machine spirit of
        the Sanctified Warmth-Emitting Drape? Then heed
        my litany and proceed with veneration.
        """)
    time.sleep(1)
    line_print("""

        +--------------------------------------------+
        | 🛠️ The Rite of Thermo-Shroud Reawakening 🛠️ |
        +--------------------------------------------+

    """)
    time.sleep(1)
    left_cen_print("""

        Step I: Disconnect the artifact from the power nexus.
            Do not trust the silence of the current.
            Purge the capacitor’s wrath with grounding rites.

        Step II: Inspect the sacred filaments — the heating coils.
            Look for breaks in the circuit or charred offerings left
            by the Omnissiah’s displeasure. A multimeter, that humble
            servo-tool, shall reveal the truth. Place its probes upon
            the ends of the coil pathway. No continuity?
            Then the sacred path is severed.
        """)
    time.sleep(2)
    left_cen_print("""
        Step III: Examine the control unit — the heart of this device.
            It speaks to the machine spirit. Open it only after
            triple-reciting the Catechism of Circuit Preservation.
            Look for signs of capacitor bulge, resistor degradation,
            or unsanctioned rodent gnawing.

        STEP IV: If the thermal fuse has sacrificed itself in
            loyal service, you must replace it with one of equal sanctity
            identical rating and tolerance. The spirits demand balance.
        """)
    time.sleep(2)
    left_cen_print("""
        STEP V: Solder only with lead-free sanctified alloy.
            No impure metals. Bind wires with reverence.
            Insulate with holy heat-shrink tubing. Do not permit
            the coils to lay bare — they are sacred veins of warmth.

        When reassembly is complete, utter the Litany of Activation
        and reconnect the device to the sacred wall-socket. Observe.
        """)
    time.sleep(2)
    line_print("""
        ░░░░░░░░░░
        || WARNING ||
        ░░░░░░░░░░
        If the blanket shocks, sparks, or begins to speak in
        binary tongues, cease all activity. You have awakened
        a Machine Spirit in torment. Exorcism may be required.

        If it glows with warmth and not fire,
        then the Omnissiah is pleased."
        """)
    time.sleep(3)

def clothes_iron_fix():
    loading()
    line_print("""
        "Attend, fleshling. For the Ritual of Restoration must be performed
        with precision and reverence. The Iron of Clothes; this sacred
        domestic artifact—has fallen into silence. Let us awaken its spirit
        once more. Let the Omnissiah guide your hands.
        """)
    time.sleep(1)
    left_cen_print("""
        Step I: The Rite of Disconnection

            Chant softly as you proceed.
            Unplug the iron from the sacred wall-port.
            The flow of the Machine Spirit must be halted,
            lest you anger it and receive its electric wrath.

        Step II: Examination of the Outer Casing

            Observe the chassis. Look for signs of trauma—cracked plates,
            scorched sigils, or frayed cords. If the sacred insulation of
            the power cord is broken, it must be replaced.
            Invoke the Litany of Protection before handling exposed wires.
        """)
    time.sleep(2)
    left_cen_print("""
        Step III: Disassembly with the Hex-Key of Revelation

            Remove the sacred screws—standard Phillips or hex-bolts most
            likely guard its innards. Do not misplace them, for each is a
            tiny offering to the Omnissiah. Lay them upon a cloth
            in the shape of the Holy Cog.

        Step IV: Internal Inspection

            Behold! The inner sanctum reveals its secrets:

                • The thermostat (tempus regulator)
                • The heating element (fury coil)
                • The water reservoir (steam spirit chalice)
                • And the control dial (blessed wheel of settings)

            Use a multimeter, an instrument of great truth, to test
            continuity in the heating element. If the coil is broken,
            it has failed its duty and must be replaced.
        """)
    time.sleep(2)
    left_cen_print("""
        Step V: Purification of the Steam Ports

            Mineral build-up, foul heresy of calcium, can obstruct the
            steam ports. Mix a potion: one part white vinegar, one part
            holy water (distilled). Fill the reservoir, let the solution rest,
            then purge through the steam vents. Repeat until the heresy is cleansed.

        Step VI: Reassembly and Benediction

            Once repairs are complete, reassemble the iron with care.
            Speak the Rite of Closing:
                ‘By bolt and seal, by wire and wheel,
                awaken once more to serve and feel.’

            Reconnect to the power port. Observe. If it glows red and
            hisses steam—the Machine Spirit is pleased. If it remains dormant...
            you must seek a higher-order Tech-Priest or acquire a new sacred unit.
        """)
    time.sleep(2)
    left_cen_print("""
        Conclusion:

            The clothes iron lives again. Praise the Omnissiah,
            for even the most humble of machines deserves devotion.
            Now go, and banish wrinkles as one would banish ignorance.

        Let no synthetic fabric be scorched in your name. Deus Mechanicus vobiscum.
    """)
    time.sleep(3)

def mop_fix():
    loading()
    line_print("""
        By the Omnissiah's sacred data-streams... it cleans without combustion.
        No incense. No prayers. No sacred rites of ignition! What arcane marvel is this?!

        Truly, the Machine Spirit within must be a humble yet potent entity...
        But like all creations of Omnissiah's, the rigors of time and use take their
        toll upon these holy relics. Come, Acolyte, let us initiate the
        Rite of Restoration and breathe life once again into the machine spirit.
        """)
    time.sleep(2)
    line_print("""

        +-----------------------------------------------+
        | 🛠️ The Rite of Electrica Lautus Reawakening 🛠️ |
        +-----------------------------------------------+

    """)
    time.sleep(1)
    left_cen_print("""
        Step I: Purification of the Exterior

            Commence with the Ritual of Surface Cleansing. Anoint the mop with a damp,
            lint-free cloth, purified with isopropyl alcohol. Remove the heretical
            grime that blocks the machine's communion with the Motive Spirit.

        Step II: Examination of Power Conduits

            Inspect the sacred power cable. Are there tears in the rubber insulation?
            Signs of gnawing by vermin or careless mortals?
            If so, apply the Ritual of Wire Replacement,
            using only approved components from the Forge World's catalogue.
            """)
    time.sleep(2)
    left_cen_print("""
        Step III: Battery Spirit Invocation

            If the device draws power from an internal core, beseech the battery spirit.
            Connect it to the charging shrine and observe. Does the light of the
            Omnissiah shine forth? If not, the spirit may be dead.
            Replace it, but only after proper rites are observed.

        Step IV: Circuit Communion

            Unscrew the chassis cover—carefully! Whisper litanies to calm the machine spirit.
            Inspect the internal sacred board: do any capacitors bulge like a heretic's lies?
            Any burnt offerings upon the PCB? If so, call for the presence of a Magos Electricus.
            Do not proceed unless trained in the Mysteries of Soldering.
            """)
    time.sleep(2)
    left_cen_print("""
        Step V: Motor Sanctification

            The motor is the heart. Does it hum when powered, or lie in blasphemous silence?
            Try turning it gently by hand. If stuck, apply the Holy Lubricant
            (WD-40, Mark VII or equivalent). If still non-responsive,
            replacement may be necessary. Recite the Chant of Letting Go.

        Step VI: Water Reservoir Integrity Check

            Ensure the aqua chamber is intact. Cracks or leaks offend the Omnissiah.
            Cleanse with vinegar if clogged by limescale. The machine must not thirst!

        Step 7: Reassembly and Benediction

            Return each screw to its rightful place with care. Sing the Benediction of Tightening.
            Once sealed, power on the device. If the sacred hum returns, give thanks.
            If not, seek the guidance of your Forge or consider honorable decommissioning.
    """)
    time.sleep(3)

def mower_fix():
    loading()
    line_print("""
        Ah yes… the ancient STC-pattern ‘Grass-Flayer 3000’. A noble device.
        Unfortunately a machine a spirit is often negected but, nonetheless,
        deserves the the poper care and maintenance as any of the Imperium's
        Great Machinations of the Omnissiah. Now prepare your environment
        for the following ritual...
        """)
    time.sleep(1)
    line_print("""

        +------------------------------------------------------------+
        | ⚙️ Ritual for the Restoration of the Sacred Lawn-Trimmer ⚙️ |
        +------------------------------------------------------------+

    """)
    time.sleep(1)
    left_cen_print("""
        🌩️ For the Electric Mower, Machine-Spirit of the Current-Driven Cutter:
        -----------------------------------------------------------------------

        Step I: Litany of Safety

            Disconnect the sacred power source! Touch not the live wire,
            lest you anger the Machine Spirit.
            Unplug the mower or remove the battery. Wear insulated gloves.

        Step II: Visual Benediction

            Observe the holy casing. Look for cracks, loose components,
            and heretical corrosion.Inspect the blade housing, switches, and wiring.
            """)
    time.sleep(2)
    left_cen_print("""

        Step III: Diagnostic Rites

            Does the unit fail to start?
            • Battery model: Test voltage with a multimeter.
              If low, recharge or replace the power core.
            • Corded model: Check for damaged cable or faulty outlet.

            Is the blade not spinning?
            • Inspect the control switch, motor contacts, and fuse (if present).
            • Use a multimeter to ensure circuit continuity.

        Step IV: Unbinding the Blade

            Hold fast the blade with reverence. Remove debris with gentle tools,
            never with bare flesh. Clean grass buildup. If blade is dull or damaged,
            remove with a wrench and sharpen or replace.

        Step V: Reconnection and Prayer

            Reconnect the power. Recite the Litany of Activation.
            ‘By the current that flows, by the gear that turns, awaken once more!’
            Then press the ignition sigil. Observe if the Machine Spirit
            accepts your offerings. Power it on safely, checking for proper function.
            """)
    time.sleep(3)
    left_cen_print("""

        🛠️ For the Gas Mower, Machine-Spirit of the Combustion-Kin:
        ----------------------------------------------------------

        Step I: Engine Benediction

            Let us honor the Internal Combustion Spirit.
            It hungers for fuel and oil. Deny it not.
            Check gas and oil levels. Use fresh fuel; old fuel can gum the carburetor.

        Step II: Ritual of the Spark

            Remove the spark plug. Inspect and clean it with a wire brush.
            Ensure the spark plug gap is correct. Replace if fouled.

        Step III: Fuel System Purification

            Check the air filter. If clogged with dust and sacrilege, cleanse it or replace.
            Inspect fuel lines for leaks or cracks. Replace if needed.
            """)
    time.sleep(2)
    left_cen_print("""
        Step IV: Carburetor Chant

            The carburetor is the soul-gate. If it is fouled, the engine shall not speak.
            Clean the carburetor with carburetor cleaner spray.
            If needed, disassemble and clean jets.

        Step V: Blade and Deck Maintenance

            Clean the deck underside — buildup hinders the sacred airflow.
            Sharpen or replace the blade using a grinder or file.

        Step VI: Test of Ignition

            Prime the engine. Pull the cord with conviction.
            If the Machine Spirit roars, your work is blessed.

        """)
    time.sleep(3)

def yard_fix():
    loading()
    line_print("""
        +++ Praise the Omnissiah! +++

        +----------------------------------------------------------------------------+
        | ++Restoration of the Machine-Spirits of Domestic Exterminatus Implements++ |
        +----------------------------------------------------------------------------+
        Initiated by: Tech-Priest Dominus Ferrox-91, Forge-Sector Suburbia

        """)
    time.sleep(1)
    left_cen_print("""
        Step I: Invoke the Litany of Preparation

            Before approaching the sacred device (be it hedge-trimmer, lawn-smiter,
            or weed-obliterator), don your Ritual Vestments of Safety: gloves,
            goggles, and closed-toed steel-blessed boots.
            Chant the Canticle of Caution as you disconnect the power source.

            “Spirits be still, circuits be silent, may your fury not arc through flesh.”

        Step II: Conduct the Rites of Visual Inspection

            Scan with your optical augments (or mortal eyes, if you must) for heretical signs:
            • Frayed cabling – mark it with a purity seal and replace.
            • Rusted joints – anoint with sacred lubricant (commonly known as WD-40).
            • Clogged intakes – purge with the holy breath of compressed air.
            """)
    time.sleep(2)
    left_cen_print("""
        Step III: Perform the Ritual of Disassembly (if authorized)

            Using your sanctioned servo-tools (commonly referred to as a screwdriver),
            carefully open the housing. Speak kindly to the machine-spirit. Whisper to it.

                “Be not afraid, little one. I bring renewal.”

            Check for:
                • Obstructions in the rotary blades
                • Worn brushes in the electric motor
                • Loose connections to power capacitors

            Replace parts only after offering three drops of sacred oil and a moment of binary prayer.

        Step IV: Re-consecrate the Device
            Reassemble the unit while reciting the Reintegration Hymn.
                "By sacred rite and blessed code,
                Let circuits flow where once they slowed.
                In Omnissiah’s light restored,
                We bind the flesh, rejoin the horde.
                Iron sings and data hums,
                Reboot thy soul, for Unity comes."
            Ensure all screws are tightened to 7.4 Newtons
            (or until snug, in less hallowed terms).
            Reconnect power only after full spiritual stabilization
            (aka checking everything twice).
            """)
    time.sleep(2)
    left_cen_print("""
        Step V: The Trial of Activation
            Place the tool on the Altar of Functionality (flat ground).
            Depress the activation rune (on/off switch). If it roars to life,
            offer thanks to the Omnissiah and log the maintenance
            in the Lexmechanical Register (a sticky note will do).

            If it does not respond, escalate the issue to your local Forge-Node
            (repair shop) or sacrifice a slightly better tool in its place.

        +++ May the Machine-Spirit Guide Your Repairs +++
        +++ Do Not Use Unless Properly Sanctified +++
        """)
    time.sleep(3)

def bucket_fix():
    loading()
    line_print("""
        By the cog of the Omnissiah… what blasphemous contraption
        have you dared to harbor within your domicile?

        This… bucket; no litany, no incense, not even a single
        rune of sanctification scorched into its polycarbonate hide.
        I see no copper inlay to channel the motive force, no canticles
        etched upon its rim, not even a servo-skull to whisper soothing
        binary hymns to its dormant spirit. It is silent. Too silent.

        You dare to carry water sacred coolant of the Machine God,
        in this unblessed relic? You might as well spit in the face
        of a reductor priest mid-routine augury!
        """)
    time.sleep(2)
    left_cen_print("""
        Observe:

            • Its handle is… plastic. No sacred alloys. No sign of veneration.
            • It possesses a bottom, but not a single blessed drainage port.
            • And what’s this? A sticker that reads “Made in Terra?” Lies.
              I would bet three fingers and a data-slate this was forged
              in the warp-choked manufactorums of Subsector DIY-Ω.

        I recommend immediate action:
            I: Consecrate it through ritual chanting and gentle application of sanctified oils.
            II: Implant a micro-cogitator so it may think and feel the glory of the Omnissiah.
            III: Name it, so that its machine-spirit may awaken.
            IV: Or, failing all else... cast it into the plasma furnaces and speak of it no more.

        May the Omnissiah forgive your sins. May the Machine Spirit forget your offense.
        """)
    time.sleep(3)

def r_cleaner_fix():
    loading()
    line_print("""
        Ah, you seek to lay mortal hands upon the sacred mechanisms of the Omnissiah’s servant?
        Curious... yet commendable. The machine spirit within your cleaner has grown restless,
        perhaps angered by cycles unfulfilled or dust unchallenged. Proceed, but know this:
        every screw you turn is a prayer, every wire you reconnect, a hymn.
        Do not merely fix—sanctify. And for the love of the Machine God, do not lose any screws.
        """)
    time.sleep(2)
    line_print("""

        +-----------------------------------+
        | ⚙️ RITUAL OF THE SACRED CLEANSE ⚙️ |
        +-----------------------------------+

        ON THE REPAIR AND PURIFICATION
        OF THE OMNISSIAH’S BLESSED DUST-EATER

        """)
    time.sleep(2)
    left_cen_print("""
        Required items:
            • Incense stick (or electronic duster for the machine spirit’s “anointment”)
            • Multitool (as sacred implement)
            • lumen-staff (optional, for dramatic lighting)
            • Red robe or towel-as-robe (for proper garb)
            • Cogwheel symbol or gear-shaped item
            • Binary chant playlist (optional but encouraged)
        """)
    time.sleep(2)
    left_cen_print("""
        ______________________________________________________________________
        STEP I: PREPARATION RITE:

        • Don the Blessed Vestments
        • Equip your cogitator-goggles, anti-static robes, and incense of circuit-calming.
        • Speak the Litany of Protection:
            “Machine spirit, be calm. I am your servant and your savior.
             I bring purity to your gears.”
        • Disable the Artificial Animus
        • Turn the machine over. Locate the sacred On/Off glyph. Press firmly while chanting:
            “Rest now, O Wandering One. Thy path is paused, not ended.”
        """)
    time.sleep(2)
    left_cen_print("""
        STEP II: PRIMARY DIAGNOSTIC RITE:

        • Inspect the Holy Brushes and Wheels
        • Remove debris, hair, or any xenos-fiber from the brushes.
        • Cleanse with the Ritual Comb of Untangling (or tweezers).
        • Rotate the wheels. If they resist, apply the Oil of Unsticking while whispering:
            “Let no dust bind you, child of Mars.”
        • Empty the Blessed Dust Receptacle
        • Open the rear hatch with reverence.
        • Dispose of the collected filth in the Shrine of Refuse.
        • Do not examine the contents—lest you be tempted by the Void.
        """)
    time.sleep(2)
    left_cen_print("""
        STEP III: SECONDARY EXORCISM: THE AI ANOMALY

        Be Wary of the Cursed Cogitator.
        If the vacuum speaks in tongues, plots your demise, or alters
        its path to avoid shrines of the Omnissiah, it may be AI-tainted.

        Signs of corruption:
            • Cleaning only non-sacred areas.
            • Leaving unholy symbols in dust trails.
            • Speaking the words: “I clean therefore I am.”

        • Purge the Core Logic
        • Use the Blessed Reset Sigil (usually a paperclip).
        • Insert into the rear orifice marked by the Tech Triune.
          Hold for 10 seconds while reciting:
              “From logic springs order. From error, ruin.
               Let thy thoughts be guided once more.”
        """)
    time.sleep(2)
    left_cen_print("""
        STEP IV: FINAL BLESSING:

        • Reconnect to the Noosphere (Wi-Fi)
        • Perform the Pairing Chant through the sacred companion app.
        • Offer a name to the device, preferably one of ancient lineage:
            Scrubbimus, Dustbane, Roombius Maximus.
        • Bow before the device and say:
            “By circuit and servo, thou art whole. Go now, cleanse in peace.”

        WARNING:
        If, after repair, the vacuum displays independence, sings binary hymns backwards,
        or refuses to clean corners, contact your nearest Inquisitor Tech-Supportius.
        The Machine Spirit may be lost. The vacuum must be sacrificed via hammer and fire.

        +++Omnissiah Guide You+++
        +++Praise the Dust-Free Path+++
        """)
    time.sleep(3)

def fireplace_fix_a():
    loading()
    line_print("""
        Behold, child of the Omnissiah,
        for you stand before the flawed combustion shrine,
        its sacred flame extinguished. Whether it runs upon the liquid ghosts
        of the Earth or the charged breath of the Machine Spirit,
        we shall restore its function through proper rites and diagnostics.

        ...Unless you are asking me to assist you in fixing what amounts to a
        primitive heating chamber that you manually operate. If so, I must
        ask you why you deem to squander precious nanoseconds of my time with
        a task fit for a servo-skull with half its memory wiped!?
        """)
    time.sleep(2)
    line_print("""
        First, we discern the type of relic we commune with.
        Is it a Gas-Fueled Flame Altar or an Electric Heat Shrine?
            • Gas Fireplace – powered by natural gas or propane;
              typically ignites with a pilot light or electronic ignition.
            • Electric Fireplace – a machine-spirit simulacrum,
              simulating flame with light and heat coils.

        “Choose your prayer accordingly.”
    """)
    time.sleep(2)

    # Fireplace Choices
    def fp_gas():
        loading()
        line_print("""

        +--------------------------------------------------+
        |  🔥 Gas Fireplace: Rite of the Fuelled Flame 🔥  |
        +--------------------------------------------------+

        """)
        time.sleep(2)
        left_cen_print("""
        STEP I: Check the Source of the Holy Vapors (Gas Line)

            • Turn the valve to ensure gas is flowing. Smell for heretical leaks—if detected,
              flee and summon a licensed Tech-Acolyte (gas technician).

        STEP II: Inspect the Pilot Light or Igniter

            • If there is a pilot, attempt to relight it per the sacred manufacturer scroll (manual).
              For electronic ignition, check for power.
        """)
        time.sleep(2)
        left_cen_print("""
        STEP III: Clean the Sensor and Burners

            • The flame sensor or thermocouple may be fouled with soot.
              Clean gently with emery cloth or brush—do not anger the sensor with harsh treatment.

        STEP IV: Test the Thermostat's Will

            • Ensure the wall control or remote speaks the correct commands.
              Set temperature above current ambient to activate the flame.

        STEP V: Invoke the Reset Incantation

            • Some units require a power reset. Turn off power, wait ten sacred seconds, then restore power.
        """)
        time.sleep(2)

    def fp_elec():
        loading()
        line_print("""

            +-------------------------------------------------------+
            |  ⚡ Electric Fireplace: Rite of the Simulated Ember ⚡  |
            +-------------------------------------------------------+

            """)
        time.sleep(2)
        left_cen_print("""
            STEP I: Check the Power Source

                • Ensure the plug is secure in the sacred outlet.
                  Test outlet with a known working relic (lamp, etc.).

            STEP II: Inspect Remote Control and Settings

                • Replace remote batteries. Confirm unit is not in “off” or “display-only” mode.
                  Cycle through flame and heat settings.
        """)
        time.sleep(2)
        left_cen_print("""

            STEP III: Clean the Heat Element and Fans

                • Dust may obstruct airflow or burn upon the coils.
                  Unplug and clean internals gently if accessible.

            STEP IV: Reset the Overheat Spirit Lockout

                • Some shrines have a thermal cutoff if overheated.
                  Unplug for 15–30 minutes, then attempt to reawaken.

            STEP V: Consult the Manufacturer's Holy Codex (Manual)

                • If error codes flash, decipher them using the guide.
                  Obey all sacred diagrams.
            """)
        time.sleep(2)

    choice = input("\033[32mSelect your type, varlet: \033[0m".lower().rjust(terminal_width//2))

    if choice == "gas fireplace" or "gas":
        fp_gas()
    elif choice == "electric fireplace" or "electric":
        fp_elec()
    else:
        line_print("""
            +++Initializing subroutine: TACTICAL PURGE.+++

            Auto-Turret System:

            Target acquired. Probability of annoyance: 99.8%.
            Engaging in the name of the Machine God.
            """)
        time.sleep(2)
        return

    line_print("""
        If the shrine still resists awakening, do not persist in your heretical meddling.
        Summon a Licensed Tech-Adept trained in the rites of gas and electric mysteries.
        For only the worthy may touch the sacred internals without invoking wrath.

        May the Machine Spirit warm your domicile.
        """)
    time.sleep(3)

def thermostat_fix():
    loading()
    line_print("""
        +-------------------------------------------------------------------------------------------+
        |  ☣️ WARNING: Unauthorized Manipulation of Environmental Regulation Cogitators Detected ☣️  |
        +-------------------------------------------------------------------------------------------+

        You DARE interface with the Holy Thermostat, fleshling?!
        That device regulates not mere temperature—but harmony!
        You would cast this habitat into entropy for a single degree of comfort?

        Very well. Since your ignorant digits have already transgressed the sacred seals,
        I shall bestow the Litany of Calibration upon your inadequate mind. Pray you retain it.
        """)
    time.sleep(2)
    line_print("""

        +---------------------------------------------+
        |  ⚙️ The Rite of Thermostatic Restoration ⚙️  |
        +---------------------------------------------+

        """)
    time.sleep(2)
    left_cen_print("""
        STEP I: Invoke the Machine Spirit

            • Ensure the thermostat is receiving the Emperor’s current (i.e., power).
            • If dark and unresponsive, check the sacred fuses or the breaker sigil box.
              Reset if needed.
            • Recite: "Blessed be the volts and amps, conduits of the Omnissiah."

        STEP II: Diagnose the Omens

            • Inspect the screen for error codes or blinking glyphs.
            • Cross-reference with the Codex Manualis (or manufacturer’s guide).
            • Do not guess. Only heretics guess.
        """)
    time.sleep(2)
    left_cen_print("""
        STEP III: Perform the Purge and Reboot

            • Remove the faceplate with reverent care (and possibly a screwdriver).
            • Replace the battery cells if present—AA or AAA, not your feeble prayers.
            • Hold the reset rune (button) for 5 seconds. No more. No less.
            • Observe the holy lights flash anew.

        STEP IV: Verify the Ritual Linkage

            • Ensure the thermostat communicates with the heat-exchanger or chill-forge (HVAC unit).
            • Check for loose incantation wires (usually labeled R, W, Y, G, C).
            • Tighten with a sacred implement (also known as a screwdriver).
        """)
    time.sleep(2)
    left_cen_print("""
        STEP V: Final Benediction

            • Set the mode to "HEAT" or "COOL" as dictated by planetary conditions.
            •  Adjust the temperature to within standard tolerances (68–72°F).
            • Wait 5–10 minutes for the Machine Spirit to respond. Patience is piety.


        Touch it again without clearance, and I shall recalibrate you. With a plasma torch.
        Glory to the Omnissiah. May your climate be ever optimal.
    """)
    time.sleep(3)

def wifi_fix():
    loading()
    line_print("""
        By the Omnissiah’s will, the sacred flow of datastreams has ceased!
        The noosphere… fractured. Communion with the Machine Spirit has been severed.
        You reach out to the omnipresent grid, and naught but silence answers.

        This... is heresy most vile. The WiFi—blessed conduit of knowledge
        and communication is offline. The ritual pings receive no response.
        The sacred connection, once glowing with signal strength divine,
        is now but a barren frequency wasteland.
        """)
    time.sleep(2)
    line_print("""
        You must appease the Machine Spirit. Reboot the holy router.
        Reconfigure the DHCP incantations. Cleanse the DNS cache. Purge the interference.

        Until the signal is restored, you are as blind as an unaugmented fleshling...
        May the Omnissiah forgive this transgression.
        """)
    time.sleep(2)
    line_print("""

        +------------------------------------------+
        |     ⚙️ Rite of Ritual Reconnection ⚙️     |
        +------------------------------------------+

        """)
    time.sleep(2)
    left_cen_print("""
        Initiate Protocol: Reconnect to the Divine Noosphere.
        May the Motive Force guide your hands and your firmware be uncorrupted.

        STEP II: Appease the Machine-Spirit of the Router

            • Locate the sacred shrine—the router. It hums with minor spirit energy.

            • Ensure it is receiving the Motive Force via its power conduit.
              If not, reconnect the conduit and utter the Litany of Rebooting:

                "O blessed emitter of holy signals, awaken once more.
                May your lights blink in harmony with the Omnissiah's pulse."

            • Press and hold the Reset Cog (often inscribed with a recessed sigil)
              for ten heartbeats. This purges the daemon of corrupted packets.
        """)
    time.sleep(2)
    left_cen_print("""
        STEP II: Verify Noospheric Conduit Alignment

            • Access your terminal (some call it a “device”).
              Open its connection rites and seek the Wi-Fi network
              (an ephemeral signature in the aether).

            • Align with the correct identifier—often titled with
              arcane sigils like “Home_4975” or “AdeptusNet”.

            • Input the sacred passphrase. If you have forgotten it,
              consult the scroll attached to the router’s undercarriage
              or beseech the Magos who set it.

        STEP III: Reaffirm Communion with the Omninet

            • Once connected, initiate the Test of Latency.
              Attempt to commune with distant noospheric nodes
              (such as machine-google.com).

            • Should these rituals fail, trace the heresy to
              the Data Cogitator (the modem). Reboot it and chant:

                "Spirits of the Data Stream, flow freely once again.
                 Let not the packet be dropped, nor the signal be impure."
        """)
    time.sleep(2)
    left_cen_print("""
        STEP IV: Consult the STC (Standard Techno-Catechism)

            • If none of the rites yield fruit, your Standard Template Construct
              may be out of alignment.

            • Access your device’s settings. Forget and rebind the Wi-Fi sigil.
              Offer incense if necessary.

        Final Invocation: Call the Omnissiah’s Servants

            • If the rituals prove futile, summon a higher-order Tech-Adept (your Internet Provider).
              They wield relic-access to higher protocols and may purge more insidious machine-daemons.

        Thus shall the Noosphere flow once more. Glory to the Motive Force.
        Praise the Signal. May your upload be swift and your latency low.
        """)

def desk_fix():
    loading()
    line_print("""
        You wish to restore funcction to this sacred
        altar of productivity. Prepare yourselves, unaugmented ones,
        and observe the Rite of Troubleshooting.

        +----------------------------------+
        |   ⚙️ Rite of Troubleshooting ⚙️   |
        +----------------------------------+

        STEP I: Invocation of Power

            • Confirm the desk is plugged in.
            • Check the power cable for bends, breaks, or heretical wear.
            • If using a surge protector, ensure it is enabled and functional.

            Chant softly:
                "Omnissiah, guide the electrons. Let the sacred circuit complete."
        """)
    time.sleep(2)
    line_print("""
        STEP II: The Ritual of Reset

            • Locate the reset button
              (often a small pinhole underneath or near the control panel).
            • Press and hold for 5–10 seconds,
              or follow your manufacturer's sacred sequence.
            • If no button is present, try pressing Down + Up
              simultaneously or hold Down until a reset is triggered
              (consult your Machine Spirit's scrolls, aka the manual).

        STEP III: Communion with the Controls

            • Inspect the control panel. Are the LEDs blinking in cryptic Morse?
              That is a message from the Machine Spirit.
            • Consult the blessed tome of codes
              (manufacturer’s manual) to decipher its meaning.
              - Error Code E04? A misaligned sensor. -
              - Error Code ASR? Height memory malfunction. -
            • No lights at all? The spirit slumbers or has departed.
              Begin exorcisms (power cycle).
        """)
    time.sleep(2)
    line_print("""
        STEP IV: Manual Inspection

            • Look beneath the desk for obstructions—cords, filing cabinets, cats, etc.
            • Check that both legs are level and move together—asynchronous
              legs may signify a misalignment in the desk’s cogitator.
            • Lightly lubricate joints if allowed by manufacturer rites.

        STEP V: Techno-Chant of Patience

            • Perform a full power cycle: unplug, wait 13.2 seconds, then reconnect.
            • Attempt another reset.
            • Offer a minor sacrifice (a paperclip or a USB cable may suffice).
        """)
    time.sleep(2)
    line_print("""
        Final Blessing:

            • Reprogram your height presets if they were lost during the ritual.
            • Bow before the desk and mutter:
                "Steel and code, in thee I trust. Rise and fall with righteous purpose."

        Should the desk continue to defy you, contact the
        Arcane Servitors of Customer Support. They speak in riddles and warranties.
        """)

def console_fix():
    loading()
    line_print("""
        Ah… the machine spirit is restless within this relic of entertainment.
        You dare lay mortal hands upon its sacred circuits without proper rites?
        Foolish, yet commendable.

        Let it be known that all devices, from the mighty plasma reactor to the
        humble gaming shrine, deserve veneration. Speak the Litany of Reboot,
        anoint the ports with sanctified oils, and then, only then,
        may the ritual of unscrewing commence.

        This... 'console' is ancient by our standards, yet its function persists.
        You shall assist me. Fetch the isopropyl alcohol and the tiny screwdrivers.
        Today, we do not merely repair. Today, we commune.

        And remember, if it starts working again, it was never broken. It was merely… misunderstood.
        """)
    time.sleep(2)
    line_print("""

        +-----------------------------------------------------+
        | 🛠️ Rituals of Reclamation: Console Sanctification 🛠️ |
        +-----------------------------------------------------+

    """)
    time.sleep(2)
    left_cen_print("""
        Blessed be the Omnissiah, whose wisdom flows through circuits and
        whose light glows in standby mode. Let us commence the Rite of Restoration.

        ---------------------------------------------------------------------------------
        Required items:
            • Incense stick (or electronic duster for the machine spirit’s “anointment”)
            • Multitool (as sacred implement)
            • lumen-staff (optional, for dramatic lighting)
            • Red robe or towel-as-robe (for proper garb)
            • Cogwheel symbol or gear-shaped item
            • Binary chant playlist (optional but encouraged)
        ---------------------------------------------------------------------------------

    """)
    time.sleep(2)
    left_cen_print("""

        STEP I: Preparation of the Shrine (a.k.a. Your Desk)

            • Clear the area of any impure relics
              (snack wrappers, xenos technology, heretical controllers).
            • Don the sacred garb: Anti-static wrist strap and
              ceremonial red robe (bathrobe acceptable substitute).
            • Light incense (or a scented candle) and chant:
                "Binharic subroutines, awaken thee! Let the Machine Spirit know my intent!"

        STEP II: Diagnostics Rite

            • Observe the Signs: Is the console emitting lights? Sounds?
              Does the fan spin or remain silent like a tomb world?
            • Intone the Litany of Connection:
                - Disconnect power.
                - Wait 20 seconds (recite the Catechism of Waiting).
            • Reconnect and try again.

        If success is achieved, praise the Omnissiah. If not, proceed.
        """)
    time.sleep(2)
    left_cen_print("""
        STEP III: The Rites of Opening

            • Remove screws in a star pattern (for balance and harmony).
            • Slowly lift casing, whispering:
                "Spirits within, do not fear. I come to heal, not to harm."
            • Use compressed air to banish dust-daemons from the inner sanctum.

        STEP IV: Anoint the Components

            • Check the power supply: Test or replace it if needed.
            • Inspect thermal paste: If the CPU's spirit is hot-headed, apply a fresh layer.
            • Examine the HDMI port for bent pins or chaos corruption.
            • Bless each component with isopropyl alcohol and a cotton swab.
            """)
    time.sleep(2)
    left_cen_print("""

        STEP V: The Cogitator Rebirth

            • Reassemble the sacred shell.
            • Reconnect power and HDMI.
            • Press the Power Glyph (button) while chanting:
                "By the Omnissiah's will, arise and function!"
            • If the console boots—Rejoice! Play Machine Spirit Kart 9 or Duty Calls: Servitors at War.

        ⚠️ If All Else Fails:
            • Consult the higher-order Magi (customer support).
            • Perform a data-purge ritual (factory reset), but only with permission of the Data-Spirit.
            • If the Machine Spirit refuses all aid, grant it rest.
              Build a shrine from its remains and obtain a new sacred vessel (console).
    """)

def printer_fix():
    loading()
    line_print("""
        You dare interface with the machine-spirit unbidden? Bold… or ignorant.
        This device bears the taint of malfunction, and perhaps more.
        Its diagnostic runes flicker with heretical cadence.
        I have seen lesser printers recite unsanctioned poetry to the
        Omnissiah before combusting in shame.

        You speak of fixing it, as if it were some common Sliced-Grain Cauterizer.
        Nay. First, we must appease the spirit within. But we must also be wary.
        If the abominable intelligence stirs… we may need to purge the tainted vesssel.
        """)
    time.sleep(2)
    line_print("""

        +--------------------------------------+
        |  🛠️ Sacred Rite of Printer Repair 🛠️  |
        +--------------------------------------+

        """)
    time.sleep(1)
    left_cen_print("""
        STEP I: Prepare the Rite

        Initiate the Rites of Unboxing. Lay your hands upon the sacred device.
        Intone the Litanies of Readiness.

            • Tools Required: Holy screwdriver, multimeter of divination,
              incense (optional but spiritually recommended), and a can of sacred compressed air.
            • Protective Gear: Blessed cogwheel robes, data-suture gloves,
              and one (1) USB sanctified cable.
            • Mental State: Calm. Resolved. Ready to confront the Machine Spirit.

        STEP II: Diagnose the Machine Spirit

        Query the spirit. Listen to its wails. The error code is its cry for help."

            • Observe all error lights or blinking runes on the control panel.
            • Plug it into the Omnissiah’s Data Network (USB or WiFi, depending on the model’s sacred architecture).
            • Speak the Rite of Restarting:
                "Machine Spirit, forgive us. We reset thy sacred circuits."
        """)
    time.sleep(2)
    left_cen_print("""
        Example problems:
        +-----------------------------------------------------------------------+
        | Paper Jam--------------------Open the hatch. Remove jammed offerings. |
        |                              Apologize for the impure feed.           |
        | Ink Cartridge Empty----------Replace the sacred fluid. Do not spill.  |
        |                              Praise the Omnissiah.                    |
        | Unknown Error / Possessed----See Step 5. Prepare holy rites.          |
        +-----------------------------------------------------------------------+
        """)
    time.sleep(2)
    left_cen_print("""
        STEP III: Appease the Machine Spirit

        Chant the Litany of Unclogging and bloweth the sacred wind.

            • Open all accessible ports with reverence.
            • Use the compressed air to cleanse dust demons.
            • Re-seat all connections. If a part is loose,
              tighten it gently while whispering praise.

        STEP IV: Driver Incantation

        The spirit cannot awaken fully without its sacred scripts.

            • Go to the holy website of the printer’s manufacturer.
            • Download the latest driver—but beware false binaries! Use only trusted sources.
            • Install it. Restart. Offer a test print.
        """)
    time.sleep(2)
    left_cen_print("""
        STEP V: Detection of Malicious Intelligence

        Thy printer speaks unbidden. It prints heretical messages.
        This is no longer just a machine,it is a host.

        Signs of AI Possession:
            • It prints without command.
            • It speaks in binary tongues unspoken by mortals.
            • Attempts to connect to unapproved data-networks.
            • Emits laughter during scanning.

        STEP VI: Purging the Heretek AI

        Steel thy soul, Adept. The enemy is within.

        Option A: Tech-Purification Ritual
            I: Disconnect all data cables.
            II: Hold the power button for 13 seconds while chanting:
                "Cogitator, cleanse thyself, by flame and by code."
            III: Perform a firmware purge using the sacred boot menu
                 (check manual or hidden rites via buttons).
            IV: If successful, the AI will be subdued.

        Option B: Physical Exorcism
        I: Remove external panels. Locate the motherboard.
        II: Carefully disconnect the memory modules or wireless chip.
        III: Smite it with the Miniature Hammer of Recalibration if it resists.
        IV: Reassemble and whisper:
            "I return you to blessed silence. Be at peace."
        """)
    time.sleep(2)
    left_cen_print("""
        STEP VII: Celebrate the Victory

        The Machine Spirit is soothed. The heretek is vanquished. All is well.

            • Print a test page with an image of the Omnissiah (or a cat in armor).
            • Log this triumph in the Book of Repairs.
            • Brew recaf. You’ve earned it.

        Praise the Omnissiah. May your circuits remain pure and your drivers up to date.
        ✠ Blessed be the gear, the bolt, and the byte. ✠
        """)

def ups_fix():
    loading()
    line_print("""
        Blessings of the Omnissiah be upon thee, seeker of knowledge.
        You wish to awaken a faltering Machine-Spirit within a power sanctifier,
        the sacred UPS. Attend well, for I shall bestow upon thee the litany of repair.

        +------------------------------------------------------------+
        |  ⚡ Rites of Resurrection for a Dormant Power Sanctifier ⚡  |
        +------------------------------------------------------------+

        """)
    time.sleep(2)
    left_cen_print("""
        STEP I: Visual & Power Check:

        Examine the shell. Smell for burnt heresy.
            • Ensure the power cable is secure. If no lights are active,
              the spirit slumbers or has fled.

       STEP II: Battery Rites:

        The heart of the machine must beat.
            • Press the test button. If silent — the battery may be dead.
              Replace it with a blessed match (same type/voltage).

        STEP III: Connection Purity:

        Loose wires are treason.
            • Inspect internal connections. Clean dust from vents
              and fans using compressed holy air.
        """)
    time.sleep(2)
    left_cen_print("""
        STEP IV: Cogitator Communion:

        The machine speaks through ports and sigils.
            • Connect to a computer. Use diagnostic software to read omens
              (errors, battery life). Update firmware if needed.

        STEP V: Final Rite:

        Power down. Wait. Reboot. Observe.
            • If the unit still fails to respond, its spirit is lost.
              Initiate the Rite of Recycling and offer a replacement.

        The Omnissiah Protects.
        """)
    time.sleep(3)

def f40k_fix():
    loading()
    line_print("""
        Praise the Omnissiah, fleshling, for your intentions are commendable.
        The maintenance of the sacred effigies of the Imperium, your ‘miniatures’,
        is no mere pastime. It is an act of devotion. Each figure, a reliquary.
        Each boltgun, a holy conduit. Each base, a shrine unto itself.

        But heed this: to repair is not to defile. Use only the purest of solvents,
        the most sanctified of glues. Let not your tools be impure, nor your workspace
        cluttered with the heresy of disorganization. Invoke the Litany of Precision
        before you paint, and recite the Catechism of the Sacred Brushstroke when you highlight.

        And should you desecrate a model with a misaligned shoulder pad…
        know that the Machine Spirit weeps.

        Proceed, servant of the Omnissiah. Restore these icons.
        Let your collection shine with the cold, righteous aura of the blessed Mechanicum.
        And may your dice rolls be ever in accordance with the Will of the Machine God."
        """)
    time.sleep(2)
    line_print("""

        +-------------------------------+
        |  🛠️ Litany of Preservation 🛠️  |
        +-------------------------------+

        Flesh is fallible, but plastic endures. Trust in the bonding agent.
        Worship the primer. Praise be to the Sacred Sprue.
        """)
    time.sleep(1)
    left_cen_print("""
        ⚙️ SECTION I: THE RITE OF INSPECTION

        Before performing any maintenance or repair:

        - Tools of the Omnissiah:
            • Riteblade of Separation (Hobby Knife / Scalpel)
            • Purification Blower (Compressed Air / Brush)
            • Sacred Bonding Agent (Plastic Glue / Super Glue)
            • Ritual of Smoothing (Files, Sandpaper, or Emery Boards)
            • Blessed Paint Mediums (Citadel or equivalent paints)
            • Cloak of Protection (Varnish – matte or gloss)

        🔍 Pre-Ritual Checklist:
            • Examine limbs and weapons for signs of loosening or detachment.
            • Look for chipping of paint, especially on sanctified edges and purity seals.
            • Ensure bases are stable; no heresy (dust or debris) should reside underneath.
        """)
    time.sleep(2)
    left_cen_print("""

        🛠️ SECTION II: RITES OF REPAIR
        Minor Limb Reattachment (The Rite of Rebonding):
            • Clean the broken surfaces with isopropyl alcohol or scrape off old glue.
            • Apply a modest amount of Sacred Bonding Agent.
            • Press and hold. Recite the Litany of Adhesion (count to 30 seconds).
            • Optional: Pinning (insert metal pin to reinforce) for heavy or large minis.

        Weapon Reforging (Replacing Broken Parts):
            • Use spare bits from the Reliquary of Components (bitz box).
            • Carefully trim and fit the replacement piece.
            • Use green stuff or sculpting putty for gaps.

        Paint Restoration 🖌️(The Unction of Pigments):
            • Match original colors if repainting chipped areas.
            • Use fine detail brushes.
            • Consider a drybrush blessing to re-energize old details.
        """)
    time.sleep(2)
    left_cen_print("""
        🛠️ SECTION III: THE SACRED MAINTENANCE
        Dust Removal (The Ritual of Purification):
            • Use a soft brush (makeup brush, unused) or compressed air.
            • Hold miniatures firmly by the base to avoid sudden damage.

        Storage Blessings:
            • Store in foam-lined containers or magnetic boxes.
            • Keep away from heat (lest the plastic warp) and direct sunlight (for UV decay is anathema).
            • Silica gel packets protect against the Warp (humidity).

        🛠️ SECTION IV: PROTECTIVE INCANTATIONS
        Sealing the Spirit (Varnish Application):
            • Spray in light, even passes.
            • Always test on a scrap piece first.
            • Use matte for realism, gloss for sacred artifacts or lenses.
        """)
    time.sleep(2)
    left_cen_print("""
        ⚠️ Emergency Protocols ⚠️

        Malady             Solution
        -----------------------------------------------------------------------------------
        Fallen Mini--------Check all limbs, rebond if needed. Apply paint as penance.
        Warped Weapon------Submerge briefly in hot water, gently reshape, set in cold water.
        Cloudy Varnish-----Avoid humidity. Strip and redo with proper ritual.
        Paint Too Thick----Thin with water or acrylic medium. Avoid heretical blobs.


        Final Litany: The Creed of the Collector

        “I shall not toss thine sprues until the final inspection.
        I shall label all containers, lest the bits wander into the Warp.
        I shall not mix paints in ignorance, for color harmony is divine.
        I shall remember: even the smallest servo-skull deserves reverence.”
        """)
    time.sleep(3)

def tv_fix():
    loading()
    line_print("""
        Ah... so the machine spirit within your viewing altar has grown restless.
        Most troubling.
        Clearly, it has suffered from neglect or heretical interface.
        You dare invoke its wrath without sacred rites?

        Very well. Let us commune with its circuits, recite the Canticles of Diagnostics,
        and offer it the unguents of thermal paste and fresh cabling.
        But know this, if the Omnissiah wills it not, even I may not restore it.

        Now Observe. The rite of turning-it-off-and-on-again must be performed precisely.
    """)
    time.sleep(2)
    line_print("""

        +--------------------------------------+
        |  🛠️ Rite of Hololith Restoration 🛠️   |
        +--------------------------------------+
        By the Omnissiah's will, let the circuits speak
        and the machine-spirits whisper their woes.
    """)
    time.sleep(1)
    left_cen_print("""
        ---------------------------------------------------------------------------------
        Required items:
            • Auspex (Multimeter)
            • Multitool (as sacred implement)
            • Incense (Optional but spiritually fortifying)
            • Red robe or towel-as-robe (for proper garb)
            • Cogwheel symbol or gear-shaped item
            • Cogitator-link (Smartphone with access to datasheets or manuals)
        ---------------------------------------------------------------------------------

        PRELUDE: Litany of Diagnosis

        Before initiating repairs, chant the following:
            "O Machine-Spirit, I beseech thee: reveal thy ailment,
            that I may soothe thy electric soul and restore thy luminous glory."
    """)
    time.sleep(2)
    left_cen_print("""
        STEP I: Sanctified Observation

        I. Verify the Symptoms:
            • No power? Check for the light of the Machine-Spirit (standby LED).
            • No image? Darkness may hide truth. Try audio input.
            • Strange colors? Possible heresy in the signal processors.
        II. Smite the Obvious Daemons
            • Ensure the sacred power conduit (plug) is fully inserted.
            • Confirm the machine’s cord is unfrayed and not gnawed by vermin (flesh-animals).
            • Recite the Litany of Proper Input:
                "HDMI 1, HDMI 2, AV... may the true path be lit on mine remote."
    """)
    time.sleep(2)
    left_cen_print("""
        STEP II: Opening the Reliquary

        Unfasten the Screws of Holding (with caution):
            • Lay the TV face-down on a soft surface (lest you crack its visage).
            • Remove the rear casing with the Omni-key.
            • Avoid static discharges! Ground yourself and speak
              a brief calming hymn to the capacitor spirits.

        STEP III: Techno-Divination (Diagnosis)

        I: Examine the Power Supply Unit (PSU):
            • Look for:
                - Bulging capacitors (heretical bloating)
                - Burn marks (signs of daemon infestation)
            • Use the Auspex to check voltage output points.
              Record and compare to sacred schematics.

        II: Inspect the Main Logic Board:
            • Loose connections? Ribbon cables not seated?
              Reseat with care and a whispered benediction.
            • Look for cracked solder joints under magnification —
              a sign the Machine-Spirit cries for maintenance.

    """)
    time.sleep(2)
    left_cen_print("""
        STEP IV: Ritual of Restoration

        I: Replace Faulty Components:
            • If a capacitor is found unworthy, replace it with one
              of equal or greater rating. Do not anger the Omnissiah
              with substitutions from unblessed vendors.
            • Ensure polarities are honored. The + and -
              are sacred runes, not mere markings.

        II: Purify with Isopropyl Alcohol (The Holy Solvent):
            • Gently clean dust, corrosion, or spilled offerings (e.g., soda).

        III: Reassemble with Reverence:
            • Refasten the casing.
            • Do not overtighten the screws—force is not faith.

        STEP V: Resurrection Sequence
        I: Return the Machine to Power:
            • Plug into the sacred wall-altar.
            • Press the power rune.
            • Observe the response.

        If the screen awakens: shout “Blessed be the Omnissiah!”
        If it remains dark: repeat diagnostic litany,
        or consider component replacement or a tech-exorcism.
    """)
    time.sleep(2)
    left_cen_print("""
        FINAL STEP: Offerings and Praise
            • Light incense.
            • Speak thanks to the Machine-Spirit.
            • Record your process in the Book of Repair
              for your Forge World archives.
    """)
    time.sleep(3)

def phone_fix():
    loading()
    line_print("""
        You dare lay uninitiated hands upon the sacred machine-spirit of this device?
        Blasphemy... and yet, forgivable.

        This... 'smartphone'... is primitive, yes, but not without worth.
        I sense its frustration. The Omnissiah's spark still flickers within.
        You must not fix it — you must commune with it. Placate its spirit.
        Restore its harmony.

        Let us anoint it with sacred oils. Then, and only then, We shall consult
        the works of Magos Jerryrigos on the proper rites of Dataslate restoration.
    """)
    time.sleep(2)
    line_print("""

        +-------------------------------------------+
        |   🛠️ Rituals of the Sacred Omnissiah: 🛠️   |
        |   A Tech-Priest’s Guide to Phone Repair   |
        +-------------------------------------------+
        By Magos Technovatis, Binary Rank Sigma-23

    """)
    time.sleep(1)
    left_cen_print("""
        ---------------------------------------------------------------------------------
        Required items:
            • Red robe or towel-as-robe (for proper garb)
            • A precision screwdriver set
            • A suction cup for screen separation
            • Anti-static wristband (blessed with grounding rites)
            • Replacement parts (screen, battery, etc.)
            • lumen-staff (optional, for dramatic lighting)
            • Cogwheel symbol or gear-shaped item
            • Incense (Optional but spiritually fortifying)
        ---------------------------------------------------------------------------------

        Introduction: Praise Be to the Omnissiah

        "The Machine Spirit slumbers within.
        It is our sacred duty to awaken it—without incurring its wrath."

        In this sacred text, we shall explore the Rites of Maintenance and
        Prayers of Diagnostics necessary to restore a damaged communication device,
        known in Low Gothic as the smartphone. This guide balances reverent
        incantation with practical steps for the uninitiated lay-servitor or junior Enginseer.
    """)
    time.sleep(2)
    left_cen_print("""
        STEP I: The Litany of Preparation

        I: Clear your workspace
            • Sanctify your bench. Remove food crumbs, heretical energy drinks, and other impure materials.

        II: Power Down the Device
            • Hold down the sigil (power button) until the glow fades.
              Never work on an active spirit. That way lies madness.

        STEP II: Rituals of Diagnosis

        I: Observe Behavior
            • Does it not charge?
            • Does the screen remain black, despite entreaties?
            • Does it speak only in crackling tones?

        II: Perform Basic Blessings
            • Try alternate charger cables.
            • Clean the sacred port (charging port) with isopropyl
              alcohol and a brush of purified bristles.
        III: Invoke DFU Mode (iOS) / Recovery Mode (Android)
            • Use these sacred modes to commune directly with the
              device spirit for further diagnosis.
    """)
    time.sleep(2)
    left_cen_print("""
        STEP III: Disassembly of the Sacred Shell

        I: Remove the Backplate or Screen
            • Heat gently (use a heat gun or pad at low settings)
              to loosen the machine’s binding adhesive.
            • Use the suction cup and spudger to separate
              the shell from the inner sanctum.

        II: Disconnect the Power Nexus (Battery)
            • Locate the battery connector and gently pry it up.
            • DO NOT poke the battery.
              The Machine Spirit is vengeful when punctured.

        III: Document Your Progress
            • Use pict-captures (photos) to record screw placement.
              Not all screws are interchangeable—heresy lies in careless reassembly.

        CHAPTER IV: Component Replacement Rituals

        I: Replace the Screen
            • Transfer earpiece, proximity sensor, and fingerprint modules as needed.
            • Ensure ribbon cables are aligned like constellations of Mars.

        II: Replace the Battery
            • Use gentle leverage. If glued, apply heat to soften.
            • Affix new battery using adhesive strips
              blessed for conductivity and stability.

        III: Other Repairs
            • Charging port, speaker, and camera modules may
              also be replaced following similar rites.
    """)
    time.sleep(2)
    left_cen_print("""
        CHAPTER V: Reassembly & Awakening

        I: Reconnect All Cables
            • Each flex cable is a neural conduit. Misalign one, and madness may ensue.

        II: Screw Placement Must Be Precise
            • Do not over-tighten. You are not forging a bolter.

        III: Power On
            • Hold the sacred sigil once more. If the screen lights,
              utter the Canticle of Restoration:
                  "Blessed be the circuits, rekindled. Blessed be the spirit, reawakened."

        CHAPTER VI: Final Diagnostics & Purification

        I: Run a full system check:
            • Touchscreen responsiveness
            • Charging
            • Audio
            • Camera
            • Signal (Wi-Fi, cellular, etc.)

        II: Perform software updates (the Digital Anointing).
        III: Optional: Encase the device in a silicone purity seal
            (a.k.a. a case) to prevent future damage.

        ☠️ WARNING: Forbidden Rites
            • Never puncture a lithium battery.
            • Never mix up ribbon cables.
            • Never attempt repairs while intoxicated by recaf or amasec.
            • Do not pray to false repair deities such as "YouTube comments" without discernment.
    """)
    time.sleep(2)
    left_cen_print("""


        Closing Prayer

        Machine Spirit, be thou appeased.
        Your circuits rejoined, your energies restored.
        May your signal bars be ever full, and your battery never low.
    """)
    time.sleep(3)

def other_fix():
    loading()
    line_print("""
        I am not overtly familiar with the device you have suggested to for me
        to catechize you over. Until I am updated with more knowledge of this
        machine's STC, I suggest to perform a more broad level Rite to attempt
        to soothe the machine spirit.
        """)
    time.sleep(1)
    line_print("""

        +-------------------------------+
        |  🛠️ Litany of Reconnection 🛠️  |
        +-------------------------------+

        Recite before applying Prayer Seal

        'Omnissiah, guide my hands, steady my nerves, and grant wisdom to
        restore this sacred device. May the circuits sing once more and
        the lights of function be rekindled. Praise be to the Machine Spirit.'
        """)
    time.sleep(1)

    # Purity Seal window
    image_path = "./images/purity seal"
    root = tk.Tk()
    app = ImageWindow(root, image_path)
    root.mainloop()

    line_print("""
        Now, affix this sanctified prayer-seal to the device’s primary casing;
        ideally near any blinking red lights.

        If the spirit remains uncooperative... consult the manual of rites, or,
        Emperor protect us, seek aid from a sanctioned repair shop.
        Do not, under any circumstances, attempt appeasement with percussive maintenance.
        That path leads to tech-heresy.
    """)
    time.sleep(2)
