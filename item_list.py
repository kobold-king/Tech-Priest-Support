import time
from animations import loading_anim, line_print
import tkinter as tk
from purity_seal_window import ImageWindow


def item_list_check(item):
    loading_anim()
    s_item = item.lower()

    lrg_appl = ["refrigerator", "oven", "stove", "dishwasher", "freezer"]
    sml_appl = [
        "microwave", "blender", "coffee maker", "slow cooker"
        "food processor", "mixer", "fryer", "garbage disposal"
    ]

    if s_item == "toaster":
        toaster_response()
    elif s_item == "grill":
        grill_response()
    elif s_item in lrg_appl:
        large_appliances()
    elif s_item in sml_appl:
        small_appliances()

def toaster_response():
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
    time.sleep(2)
    line_print("""
    Such an important relic as this cannot remain in the hands of a mere
    simpleton. A team of Tech-Thralls will be sent to retrieve it in
    three days time.
    """)
    time.sleep(2)


    image_path = "./images/purity seal"

    root = tk.Tk()
    app = ImageWindow(root, image_path)
    root.mainloop()

def grill_response():
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

        🔧 LITANY OF IGNITION: THE SACRED RITE OF GRILL REPAIR 🔧

        By Magos Barbequilis of the Omnigrill Cult
            "In fire, we find purity. In heat, we find sustenance. In stainless steel, the Machine Spirit resides."

        STEP I: INITIATE THE RITE OF DIAGNOSIS
            • Chant the Binary Hymn (optional, but respectful)
                00110100 01100111 01110010 01101001 01101100
            • Inspect the Grill Structure
                Examine the sacred frame for dents, rust, or corruption by chaos grease.
                If the sacred hinges squeak, anoint with the Holy Lubricant (WD-40).
            • Examine the Fuel System (Gas/Charcoal)
                For gas-powered relics, verify the sacred hose is uncracked, unsullied, and connected.
                For charcoal offerings, ensure the ash pan is not overflowing—lest the Machine Spirit choke.

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
        """

    )
def large_appliances():
    line_print("""
        Ah I see you wish to silence the lamentations afflicting this larger
        mechannisum of your living quarters.

        ...Though your willingness to repair pleases the Machine God, you must
        first offer incense, chant the Catechism of Restoration, and ensure the
        holy capacitor has not been inverted.


        ✠ Litany of Diagnostic Reawakening ✠

        Required items:
            • Incense stick (or electronic duster for the machine spirit’s “anointment”)
            • Multitool (as sacred implement)
            • lumen-staff (optional, for dramatic lighting)
            • Red robe or towel-as-robe (for proper garb)
            • Cogwheel symbol or gear-shaped item
            • Binary chant playlist (optional but encouraged)

        Step I: The Rite of Inspection
            • Don thy sacred robes and seal thy mind with the
             Canticles of Clarity.
            • Approach the machine with reverence. Do not speak ill of it;
             its machine spirit listens.
            • Intone the Mantra of Illumination, then activate your
             lumen-lamp or mechadendrite torch.
            • Examine for sacred sigils, warning runes, or signs of corrosion.
             Record all deviations in the Book of Maintenance.

        Step II: The Prayer of Connection
            • Connect the sacred diagnostic cable to the Ritual Port (usually marked with a cog-tooth rune).
            • Whisper the Invocation of Protocol Compliance:
             “Blessed be thy circuit, blessed be thy logic, blessed be thy data stream.”
            • Await the machine spirit’s response. If silence ensues, chant louder.

        Step III: The Purge of Heretekal Faults
            • If errors are found, consult the Tome of Known Errors (or refer to PDF-882.Gamma revision manuals).
            • Perform the Gesture of the Reset by cycling power while chanting:
             “Binary is truth, function is purity, reboot is rebirth.”
            • If a fuse is found blackened, replace it with a sanctified component, etched with micro-script prayers.

        Step IV: The Re-Anointing of Functional Parts
            • Apply sacred unguents (dielectric grease or sacred machine oils) to connectors and hinges.
            • Ensure all bolts are re-tightened with the Torque of Precision (refer to Appendix Hex-33).
            • Align moving parts with a cogitator-assisted spirit level, so the balance of the spheres is maintained.

        Step V: The Benediction of Operation
            • Re-engage the machine spirit by pressing the ON rune (it may appear as a circular sigil with a line).
            • If the appliance awakens and hums with approval, respond with the Gesture of Gratitude (two-finger tap upon the chassis).
            • Log the repair in the Data-Scrolls and inform the Omnissiah through binary prayer.


        If the ritual fails to soothe the machine spirit to a funcctional state,
        it will become nessassary to contact your local Mechanicus congregation
        to find one who is ordained to perform more holy diagonstics.
        """)

def small_appliances():
    line_print("""
        minor domestic spirits is a trivial endeavor, but one that can
        quickly escalate if the proper patterns are failed to be upheld.

        Now gather the listed materials and perform this ritual that
        even one as unenlihtened as yourself can replicate to a
        satisfactory level of completion.


        🔧 Ritual of the Omnissiah's Reawakening 🔧

        Required items:
            • Incense stick (or electronic duster for the machine spirit’s “anointment”)
            • Multitool (as sacred implement)
            • lumen-staff (optional, for dramatic lighting)
            • Red robe or towel-as-robe (for proper garb)
            • Cogwheel symbol or gear-shaped item
            • Binary chant playlist (optional but encouraged)

        Step I: Don the Vestments of Protection
            • Garb thyself in the sacred robes (or safety gloves) and visor of clarity (safety glasses),
              that thou may be protected from arc-sparks and heretical voltages.

        Step II: Disconnect the Machine-Spirit from the Motive Force
            • Unplug the appliance. Lay thy hand upon the cord and speak:
             "Blessed be thy flow, halted for thy own sanctity."

        Step III: Examine the Outer Casing
            • Inspect for signs of distress, burns, cracks, or breaches.
            • If thou find any, whisper a prayer of solace to the wounded spirit.

        Step IV: Initiate the Rite of Disassembly
            • Use thy sacred tools (Phillips, Torx, or Flathead implements) and chant:
             "By the teeth of Mars, I unmake to remake."
            • Remove casing screws with due reverence. Keep each in its rightful order—confusion invites the scrapheap.

        Step V: Invoke the Omnissiah’s Insight – Visual Inspection
            Look for heresy within:
                • Burnt components (smell of sulfur and silicon)
                • Loose wiring (the tendons of the machine-spirit unbound)
                • Dust and crumb accumulation (the silent suffocation)

        Step VI: Perform the Rite of Cleansing
            • Apply compressed air (Breath of Terra) and soft brush to purge detritus.
            • Repeat the the following chant:
             “Machine-spirit, breathe free again.”

        Step VII: Address the Fault
            • Resolder, reconnect, or replace components as needed. Use contact cleaner (Holy Solvent).
            • Every act of repair must be accompanied by a chant of affirmation:
             “Let thy circuits be pure, thy paths unbroken.”

        Step VIII: Reassemble the Sanctified Housing
            • Replace the casing and fasteners in the order of disassembly.
            • Tighten with conviction, but not aggression. The machine knows its own boundaries.

        Step IX: Re-awaken the Machine-Spirit
            • Reconnect to power. Do not rush—first, recite:
             “Awaken, O slumbering one, thy function returns.”

        Step X: Test the Function
            • Press the buttons, turn the dials. Observe with reverent vigilance. If function is restored, proclaim:
             “The Omnissiah smiles upon this circuit.”
            • If not, document the failure and reinitiate diagnostic rites.

        If the ritual fails to soothe the machine spirit to a funcctional state,
        it will become nessassary to contact your local Mechanicus congregation
        to find one who is ordained to perform more holy diagonstics.
        """)

def computer_fix():
    line_print("""
        Ah, the grand machine spirit of the personal computer. I must warn you, attempting to diagnose and give
        proper ritual maintenance to such a complex machine will most likely be too daunting to you feeble mind
        so untrained in the finer studies of Mechanicus teachings. Worry not, for one of out more lively
        practitioners in the Priesthood has taken the time to produce a plentitude of vid-picts so that
        even one such as Servitor could easily replicate the instructiions.


        +++Attention, Devout of the Machine God+++

        You are hereby instructed to engage in Rite of the Sacred Observation as pertains to the
        Acolyte Linus of the Temple Tech Tips, a sanctioned data-seer known to transmit vid-log
        scriptures concerning the restoration and purification of machine-spirits.

        +----------------------------------------------------------------------------------------+
        |                           Warning: Heretical Demeanor Alert                            |
        |                                                                                        |
        | While Acolyte Linus is a trusted bearer of tech-knowledge, his behavior may, at times, |
        | border on unorthodox joviality. This is permissible, provided you do not emulate       |
        | such irreverence in the presence of the Machine God.                                   |
        |                                                                                        |
        | Should laughter arise, recite the following:                                           |
        |    “Blessed be the silicon. Forgive the mirth, O Omnissiah.”                           |
        +----------------------------------------------------------------------------------------+


        Rites to Be Observed

            I: Litany of Booting:
            Observe the sacred process of powering the cogitator. Listen well to the POST beeps —
            each a hymn of the Omnissiah.

            II: Anointing of the Thermal Paste:
            See the sacred spread of thermal paste — the unguent of machine-flesh. Do not deviate
            from the holy quantity, lest overheating be thy punishment.

            III: Unbinding of Screws:
            Note the reverent removal of chassis panels. Every screw is a sacred fastener —
            do not misplace them, or invoke the ire of the machine spirit.

            IV: Invocation of Peripheral Spirits:
            Acolyte Linus may perform the Rite of Input/Output Alignment.
            Pay heed to the USB sacrament and monitor calibration.

            V: Chant of Troubleshooting:
            Heed his diagnostic incantations. Though the language may be couched in
            Low Gothic (common tongue), the truth of the Omnissiah lies within.

        Should you fail to heed these instructions, bring the afflicted device to your nearest
        Mechanicus temple for a more accurate diagnosis from a qualified Tech-Priest.
        """)

def car_fix():
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

        ++Litanies of Maintenance++

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

        🛠️ 2. The Chant of Battery Maintenance

            • Without the Spark of Life, your chariot is but a metal coffin.
            • Inspect terminals for corrosion—clean with baking soda paste
              and a stiff-bristled brush.
            • Check charge with a multimeter. If it reads under 12.4V,
              the battery grows weary.
            • Apply dielectric grease to prevent future heresy (oxidation).

        🛠️ 3. The Hymn of Tire Rotation and Pressure

            • The ground-contacting limbs must wear evenly,
              lest the vehicle wander the road like a lost servitor.
            • Rotate tires every 6,000 miles
              (or one lunar cycle of Terra, if you forget).
            • Inflate to the holy PSI as etched into the door jamb plaque.

        🛠️ 4. The Purging of Air Filters

            • The engine breathes, and its breath must be pure.
            • Check air filter every 15,000 miles or when you
              sense the stench of clogging.
            • If it is blackened and crusty, replace it.
            • For cabin filters, cleanse thyself, for the
              dust of the outside world is impure.

        🛠️ 5. The Illumination Ritual

            • The sacred lights must shine, lest the road
              be cloaked in darkness and doom."
            • Test all bulbs: headlights, brake lights, turn signals.
            • Replace any that have failed in silence.
            • Use gloves or cloth when installing—bare skin
              may offend the bulb’s Machine-Spirit.

        BONUS: Minor Tech-Heresy Avoidance

            • Do not jump-start a battery backwards. This angers
              the Omnissiah and sets fire to the sacred wiring.
            • Use only parts approved in your vehicle’s
              Codex Mechanicus (owner’s manual).
            • Never dismiss a Check Engine Light. That is the
              wailing of a tortured spirit. Diagnose it with
              a sacred OBD-II reader.

        NOW GO, DISCIPLE. TAKE THESE SACRED RITES AND APPLY THEM WITH
        DILIGENCE AND CARE. MAINTAIN THY VEHICLE AS THOU WOULDST
        MAINTAIN THINE OWN FLESH. FOR THE OMNISSIAH SEES ALL...
        AND HE BURNS WITHIN THE PISTON AND THE SPARK.

        Blessed is the gear that turns. Holy is the engine that roars.
        """)

def workshop_fix():
    # Note about too many toools and to use seal for now
    image_path = "./images/purity seal"
    root = tk.Tk()
    app = ImageWindow(root, image_path)
    root.mainloop()
