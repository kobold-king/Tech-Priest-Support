import time
from animations import line_print, loading
import tkinter as tk
from purity_seal_window import ImageWindow

def item_list_check(item):
    s_item = item.lower()
    # Each item in the catagory
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
        "workshops", "tools", "workshop tools", "automotive",
    ]
    lrg_appl = [
        "refrigerator", "oven", "stove", "dishwasher",
        "freezer", "washer", "dryer", "combo"
    ]
    sml_appl = [
        "microwave", "blender", "coffee maker", "slow cooker",
        "food processor", "mixer", "fryer", "garbage disposal",
        "steamer"
    ]

    #kitchen items 🔧
    if s_item in kitchen_items:
        if s_item == "toaster":
            toaster_response()
        elif s_item == "grill":
            grill_response()
        elif s_item in lrg_appl:
            large_appliances()
        elif s_item in sml_appl:
            small_appliances()

    # Garage/workshop items
    if s_item in garage_items:
        if s_item == "workshop" or "tools" or "workshop tools":
            workshop_fix()
        elif s_item == "automotive":
            car_fix()

    # Laundry items
    if s_item in laundry_items:
        if s_item == "clothes iron" or "iron":
            clothes_iron_fix()
        elif s_item in lrg_appl:
            large_appliances()
        elif s_item in sml_appl:
            small_appliances()

    # heating/cooling items
    if s_item == "electric blanket":
        e_blanket_fix()

    #yard items
    if s_item in yard_items:
        if s_item == "lawn mower":
            mower_fix()
        elif s_item == "trimmer" or "chain saw" or "tiller" or "aerator" or "power washer" or "leaf blower":
            yard_fix()
        elif s_item == "bucket":
            bucket_fix()

    else:
        line_print("Error: Pick a correct option")


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
    line_print("""
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
    line_print("""
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

        If the Rite was successfu, offer thanks to the Omnissiah and proceed with grilling.
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
        | ✠ Litany of Diagnostic Reawakening ✠ |
        +---------------------------------------+

        Required items:
            • Incense stick (or electronic duster for the machine spirit’s “anointment”)
            • Multitool (as sacred implement)
            • lumen-staff (optional, for dramatic lighting)
            • Red robe or towel-as-robe (for proper garb)
            • Cogwheel symbol or gear-shaped item
            • Binary chant playlist (optional but encouraged)
        """)
    time.sleep(1)
    line_print("""
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
    time.sleep(1)
    line_print("""
        Step II: The Prayer of Connection
            • Connect the sacred diagnostic cable to the Ritual Port (usually marked with a cog-tooth rune).
            • Whisper the Invocation of Protocol Compliance:
             “Blessed be thy circuit, blessed be thy logic, blessed be thy data stream.”
            • Await the machine spirit’s response. If silence ensues, chant louder.
        """)
    time.sleep(1)
    line_print("""
        Step III: The Purge of Heretekal Faults
            • If errors are found, consult the Tome of Known Errors
              (or refer to PDF-882.Gamma revision manuals).
            • Perform the Gesture of the Reset by cycling power while chanting:
             “Binary is truth, function is purity, reboot is rebirth.”
            • If a fuse is found blackened, replace it with a sanctified component,
              etched with micro-script prayers.
        """)
    time.sleep(1)
    line_print("""
        Step IV: The Re-Anointing of Functional Parts
            • Apply sacred unguents (dielectric grease or sacred machine oils) to connectors and hinges.
            • Ensure all bolts are re-tightened with the Torque of Precision (refer to Appendix Hex-33).
            • Align moving parts with a cogitator-assisted spirit level,
              so the balance of the spheres is maintained.
        """)
    time.sleep(1)
    line_print("""
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
        minor domestic spirits is a trivial endeavor, but one that can
        quickly escalate if the proper patterns are failed to be upheld.

        Now gather the listed materials and perform this ritual that
        even one as unenlihtened as yourself can replicate to a
        satisfactory level of completion.
        """)
    time.sleep(1)
    line_print("""
        +--------------------------------------------+
        | 🛠️ Ritual of the Omnissiah's Reawakening 🛠️ |
        +--------------------------------------------+

        Required items:
            • Incense stick (or electronic duster for the machine spirit’s “anointment”)
            • Multitool (as sacred implement)
            • lumen-staff (optional, for dramatic lighting)
            • Red robe or towel-as-robe (for proper garb)
            • Cogwheel symbol or gear-shaped item
            • Binary chant playlist (optional but encouraged)
        """)
    time.sleep(1)
    line_print("""
        Step I: Don the Vestments of Protection
            • Garb thyself in the sacred robes (or safety gloves) and visor of clarity
              (safety glasses), that thou may be protected from arc-sparks and heretical voltages.

        Step II: Disconnect the Machine-Spirit from the Motive Force
            • Unplug the appliance. Lay thy hand upon the cord and speak:
             "Blessed be thy flow, halted for thy own sanctity."
        """)
    time.sleep(1)
    line_print("""
        Step III: Examine the Outer Casing
            • Inspect for signs of distress, burns, cracks, or breaches.
            • If thou find any, whisper a prayer of solace to the wounded spirit.

        Step IV: Initiate the Rite of Disassembly
            • Use thy sacred tools (Phillips, Torx, or Flathead implements) and chant:
             "By the teeth of Mars, I unmake to remake."
            • Remove casing screws with due reverence. Keep each in its rightful order;
              confusion invites the scrapheap.
        """)
    time.sleep(1)
    line_print("""
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
    time.sleep(1)
    line_print("""
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
    time.sleep(1)
    line_print("""
        Step IX: Re-awaken the Machine-Spirit
            • Reconnect to power. Do not rush—first, recite:
             “Awaken, O slumbering one, thy function returns.”

        Step X: Test the Function
            • Press the buttons, turn the dials. Observe with reverent vigilance.
              If function is restored, proclaim:
             “The Omnissiah smiles upon this circuit.”
            • If not, document the failure and reinitiate diagnostic rites.

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
        will most likely be too daunting to you feeble mind so untrained in the finer
        studies of Mechanicus teachings. Worry not, for one of out more lively
        practitioners in the Priesthood has taken the time to produce a plentitude
        of vid-picts so that even one such as Servitor could easily replicate the instructiions.
        """)
    time.sleep(1)
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
    line_print("""

        Rites to Be Observed

            STEP I: Litany of Booting:
            Observe the sacred process of powering the cogitator. Listen well to the POST beeps —
            each a hymn of the Omnissiah.

            STEP II: Anointing of the Thermal Paste:
            See the sacred spread of thermal paste — the unguent of machine-flesh. Do not deviate
            from the holy quantity, lest overheating be thy punishment.
        """)
    time.sleep(1)
    line_print("""
            STEP III: Unbinding of Screws:
            Note the reverent removal of chassis panels. Every screw is a sacred fastener —
            do not misplace them, or invoke the ire of the machine spirit.

            STEP IV: Invocation of Peripheral Spirits:
            Acolyte Linus may perform the Rite of Input/Output Alignment.
            Pay heed to the USB sacrament and monitor calibration.

            STEP V: Chant of Troubleshooting:
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
    line_print("""
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
    time.sleep(1)
    line_print("""
        🛠️ 2. The Chant of Battery Maintenance

            • Without the Spark of Life, your chariot is but a metal coffin.
            • Inspect terminals for corrosion—clean with baking soda paste
              and a stiff-bristled brush.
            • Check charge with a multimeter. If it reads under 12.4V,
              the battery grows weary.
            • Apply dielectric grease to prevent future heresy (oxidation).
        """)
    time.sleep(1)
    line_print("""
        🛠️ 3. The Hymn of Tire Rotation and Pressure

            • The ground-contacting limbs must wear evenly,
              lest the vehicle wander the road like a lost servitor.
            • Rotate tires every 6,000 miles
              (or one lunar cycle of Terra, if you forget).
            • Inflate to the holy PSI as etched into the door jamb plaque.
        """)
    time.sleep(1)
    line_print("""
        🛠️ 4. The Purging of Air Filters

            • The engine breathes, and its breath must be pure.
            • Check air filter every 15,000 miles or when you
              sense the stench of clogging.
            • If it is blackened and crusty, replace it.
            • For cabin filters, cleanse thyself, for the
              dust of the outside world is impure.
        """)
    time.sleep(1)
    line_print("""
        🛠️ 5. The Illumination Ritual

            • The sacred lights must shine, lest the road
              be cloaked in darkness and doom."
            • Test all bulbs: headlights, brake lights, turn signals.
            • Replace any that have failed in silence.
            • Use gloves or cloth when installing—bare skin
              may offend the bulb’s Machine-Spirit.
        """)
    time.sleep(1)
    line_print("""
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
    time.sleep(3)
    line_print("""
        If the machine spirit approves, it shall hum in harmony. If not...
        then your ignorance shall be purged."

        Praise the Omnissiah. Do not touch the red tools."
        """)
    time.sleep(1)
    # Purity Seal window
    image_path = "./images/purity seal"
    root = tk.Tk()
    app = ImageWindow(root, image_path)
    root.mainloop()

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
    time.sleep(1)
    line_print("""
        Step III: Examine the control unit — the heart of this device.
            It speaks to the machine spirit. Open it only after
            triple-reciting the Catechism of Circuit Preservation.
            Look for signs of capacitor bulge, resistor degradation,
            or unsanctioned rodent gnawing.

        STEP IV: If the thermal fuse has sacrificed itself in
            loyal service, you must replace it with one of equal sanctity
            identical rating and tolerance. The spirits demand balance.
        """)
    time.sleep(1)
    line_print("""
        STEP V: Solder only with lead-free sanctified alloy.
            No impure metals. Bind wires with reverence.
            Insulate with holy heat-shrink tubing. Do not permit
            the coils to lay bare — they are sacred veins of warmth.

        When reassembly is complete, utter the Litany of Activation
        and reconnect the device to the sacred wall-socket. Observe.
        """)
    time.sleep(1)
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
    line_print("""
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
    time.sleep(1)
    line_print("""
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
    time.sleep(1)
    line_print("""
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
    time.sleep(1)
    line_print("""
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
    time.sleep(1)
    line_print("""
        +-----------------------------------------------+
        | 🛠️ The Rite of Electrica Lautus Reawakening 🛠️ |
        +-----------------------------------------------+

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
    time.sleep(1)
    line_print("""
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
    time.sleep(1)
    line_print("""
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
    line_print("""

        Step III: Diagnostic Rites

            Does the unit fail to start?

            • Battery model: Test voltage with a multimeter.
              If low, recharge or replace the power core.
            • Corded model: Check for damaged cable or faulty outlet.

            Is the blade not spinning?

            • Inspect the control switch, motor contacts, and fuse (if present).
              Use a multimeter to ensure circuit continuity.

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
    time.sleep(2)
    line_print("""

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
    line_print("""
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

def yard_fix():
    loading()
    line_print("""
        +++ Praise the Omnissiah! +++

        +----------------------------------------------------------------------------+
        | ++Restoration of the Machine-Spirits of Domestic Exterminatus Implements++ |
        +----------------------------------------------------------------------------+
        Initiated by: Tech-Priest Dominus Ferrox-91, Forge-Sector Suburbia


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
    line_print("""
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
    line_print("""
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
    line_print("""
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
    time.sleep(2)
