import time
from animations import loading_anim
import tkinter as tk
from purity_seal_window import ImageWindow


def item_list_check(item):
    loading_anim()
    s_item = item.lower()

    if s_item == "toaster":
        toaster_response()

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
    pass

def small_appliances():
    pass

def large_machnes():
    pass
