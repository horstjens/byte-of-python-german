class Robot:
    """Repräsentiert einen Roboter mit einem Namen"""

    # Eine class variable, sie zählt die Anzahl der Roboter
    population = 0

    def __init__(self, name):
        """Intitialisiere Daten"""
        self.name = name
        print("(Initializing {})".format(self.name))

        # Der "frisch gebackene" Robotor erhöht die Roboter-Population
        Robot.population += 1

    def stirb(self):
        """Ich sterbe."""
        print("{} ist zerstört!".format(self.name))

        Robot.population -= 1

        if Robot.population == 0:
            print("{} war der letzte seiner Art.".format(self.name))
        else:
            print("Es sind noch {} Roboter übrig.".format(
                Robot.population))

    def sag_hallo(self):
        """
        Roboter können grüßen.
        Wirklich!
        """
        print("Grüße, ich werde {} genannt.".format(self.name))

    @classmethod
    def wieviele_gibt_es(cls):
        """druckt die Anzahl aller Roboter aus."""
        print("Derzeit gibt es {} Roboter.".format(cls.population))


droid1 = Robot("R2-D2")
droid1.sag_hallo()
Robot.wieviele_gibt_es()

droid2 = Robot("C-3PO")
droid2.sag_hallo()
Robot.wieviele_gibt_es()

print("\nHier könnten die Roboter arbeiten\n")

print("Arbiet ist fertig, Roboter werden zerstört....")
droid1.stirb()
droid2.stirb()

Robot.wieviele_gibt_es()
