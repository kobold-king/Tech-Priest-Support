import time
from animations import loading_anim
import tkinter as tk
from purity_seal_window import ImageWindow


def item_list_check(item):
    loading_anim()
    s_item = item.lower()

    if s_item == "toaster":
        toaster_response()

    elif s_item == "refrigerator" or "oven" or "stove" or "dishwasher":
        large_appliances()

def toaster_response():
    print("""
    By the Omnissiah’s capacitors... what... is this?
    """)
    time.sleep(1)
    print("""
    Four-slot, chrome-plated... dual function with crumb tray?!
    You walk among the divine, fleshling.
    """)
    time.sleep(1)
    print("""
    You dared to hide such ancient and holy relicry from the Mechanicus?
    This is no mere device. This—this is a Standard Template
    Construct made manifest in chrome and blessed heat coils!
    """)
    time.sleep(2)
    print("""
    Such an important relic as this cannot remain in the hands of a mere
    simpleton. A team of Tech-Thralls will be sent to retrieve it in
    three days time.
    """)
    time.sleep(2)


    image_path = "./images/purity seal"

    root = tk.Tk()
    app = ImageWindow(root, image_path)
    root.mainloop()

def large_appliances():
    print("""
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
    print("""
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
    pass
