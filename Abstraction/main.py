# Ye Python ka program ek `Car` class define karta hai jo **abstraction** ka concept use karta hai — 
# yani internal engine ke kaam (jaise engine start ya stop karna) user se chhupaye jate hain.
# Isme ek khas feature hai **idle stop**, 
# jo agar car 5 seconds tak idle rahe (jaise red signal par),
# to engine ko automatic band kar deta hai taake fuel save ho.
# `from rich import print` ka use is liye kiya gaya hai taake terminal ka output colorful aur readable ho,
# jaise messages bold ya colored nazar aayein.

from rich import print
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self._engine_status = False
        self._ideling_time = 0
        self.traffic_signal = None

# Expose a drive method without revealing internal mechanics
def drive(self):
    if self._engine_status and self.traffic_signal == "green":
        print(f"You are driving a {self.brand} {self.model}.")
    elif self._traffic_signal == "red":
        print(f"You stopped at the red light in a {self.brand} {self.model}.")
        self._idle_stop_engine()
    else:
        self._start_engine()
        printprint(f"You are driving a {self.brand} {self.model}.")


# Expose a stop method to stop the car
def stop(self):
    if self._engine_status:
        print(f"You stopped the {self.brand} {self.model}.")
        self._idle_stop_engine()
    else:
        print(f"The {self.brand} {self.model} is already stopped.")