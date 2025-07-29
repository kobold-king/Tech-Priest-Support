import time
from animations import loading_anim

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
