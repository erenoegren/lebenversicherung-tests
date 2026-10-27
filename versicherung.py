"""
Einfacher Beitragsrechner fuer eine Risikolebensversicherung.

Das Programm:
- berechnet den Monatsbeitrag fuer einen Vertrag
- bildet zwei Geschaeftsvorfaelle ab: Beitragsfreistellung und Kuendigung
"""

# Jahresbeitrag pro 1.000 Euro Versicherungssumme, je nach Altersgruppe
BEITRAGSSAETZE = {
    "jung": 1.0,     # 18 bis 30 Jahre
    "mittel": 2.0,   # 31 bis 45 Jahre
    "alt": 4.0,      # 46 bis 65 Jahre
}

RAUCHER_ZUSCHLAG = 1.5  # Raucher zahlen 50 % mehr


def altersgruppe(alter):
    """Gibt die Altersgruppe fuer ein Alter zurueck."""
    if alter < 18 or alter > 65:
        raise ValueError("Alter muss zwischen 18 und 65 liegen")
    if alter <= 30:
        return "jung"
    if alter <= 45:
        return "mittel"
    return "alt"


def beitrag_berechnen(alter, versicherungssumme, raucher=False):
    """Berechnet den Monatsbeitrag in Euro (auf 2 Stellen gerundet)."""
    if versicherungssumme < 10_000 or versicherungssumme > 1_000_000:
        raise ValueError("Versicherungssumme muss zwischen 10.000 und 1.000.000 Euro liegen")

    satz = BEITRAGSSAETZE[altersgruppe(alter)]
    jahresbeitrag = versicherungssumme / 1000 * satz

    if raucher:
        jahresbeitrag = jahresbeitrag * RAUCHER_ZUSCHLAG

    return round(jahresbeitrag / 12, 2)


class Vertrag:
    """Ein Lebensversicherungsvertrag mit Status."""

    def __init__(self, vertragsnummer, alter, versicherungssumme, raucher=False):
        self.vertragsnummer = vertragsnummer
        self.alter = alter
        self.versicherungssumme = versicherungssumme
        self.raucher = raucher
        self.monatsbeitrag = beitrag_berechnen(alter, versicherungssumme, raucher)
        self.status = "aktiv"

    def beitragsfrei_stellen(self):
        """Geschaeftsvorfall: Der Kunde zahlt keine Beitraege mehr."""
        if self.status != "aktiv":
            raise ValueError("Nur aktive Vertraege koennen beitragsfrei gestellt werden")
        self.status = "beitragsfrei"
        self.monatsbeitrag = 0

    def kuendigen(self):
        """Geschaeftsvorfall: Der Vertrag wird beendet."""
        if self.status == "gekuendigt":
            raise ValueError("Vertrag ist schon gekuendigt")
        self.status = "gekuendigt"
        self.monatsbeitrag = 0


if __name__ == "__main__":
    vertrag = Vertrag("LV-001", alter=30, versicherungssumme=100_000)
    print(f"Vertrag {vertrag.vertragsnummer}: {vertrag.monatsbeitrag} Euro pro Monat, Status: {vertrag.status}")

    vertrag.beitragsfrei_stellen()
    print(f"Nach Beitragsfreistellung: {vertrag.monatsbeitrag} Euro, Status: {vertrag.status}")
