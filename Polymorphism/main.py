# Polymorphisim
class Circket:
    def Play(self,game):
        print(f"I am playing {game}")

class Football(Circket):
    def play(self,game):
        print(f"I am playing {game}")

p2: Circket = Football()
p2.Play("Football")