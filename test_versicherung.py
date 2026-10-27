"""
Automatisierte Tests fuer versicherung.py

Starten mit:  pytest -v
"""

import pytest

from versicherung import Vertrag, altersgruppe, beitrag_berechnen


# ---------- Tests fuer die Beitragsberechnung ----------

def test_beitrag_normalfall():
    # 30 Jahre, 100.000 Euro: 100 * 1.0 / 12 = 8.33 Euro
    assert beitrag_berechnen(30, 100_000) == 8.33


def test_beitrag_raucher_zahlt_mehr():
    nichtraucher = beitrag_berechnen(40, 100_000)
    raucher = beitrag_berechnen(40, 100_000, raucher=True)
    assert raucher > nichtraucher
    assert raucher == 25.0  # 100 * 2.0 * 1.5 / 12


# ---------- Grenzwerte (wichtig beim Testen!) ----------

def test_altersgruppe_grenzwerte():
    assert altersgruppe(18) == "jung"
    assert altersgruppe(30) == "jung"
    assert altersgruppe(31) == "mittel"
    assert altersgruppe(45) == "mittel"
    assert altersgruppe(46) == "alt"
    assert altersgruppe(65) == "alt"


def test_zu_jung_gibt_fehler():
    with pytest.raises(ValueError):
        beitrag_berechnen(17, 100_000)


def test_zu_alt_gibt_fehler():
    with pytest.raises(ValueError):
        beitrag_berechnen(66, 100_000)


def test_summe_zu_klein_gibt_fehler():
    with pytest.raises(ValueError):
        beitrag_berechnen(30, 5_000)


# ---------- Tests fuer die Geschaeftsvorfaelle ----------

def test_neuer_vertrag_ist_aktiv():
    vertrag = Vertrag("LV-001", 30, 100_000)
    assert vertrag.status == "aktiv"
    assert vertrag.monatsbeitrag == 8.33


def test_beitragsfreistellung():
    vertrag = Vertrag("LV-002", 30, 100_000)
    vertrag.beitragsfrei_stellen()
    assert vertrag.status == "beitragsfrei"
    assert vertrag.monatsbeitrag == 0


def test_gekuendigter_vertrag_kann_nicht_beitragsfrei_werden():
    vertrag = Vertrag("LV-003", 30, 100_000)
    vertrag.kuendigen()
    with pytest.raises(ValueError):
        vertrag.beitragsfrei_stellen()


def test_doppelte_kuendigung_gibt_fehler():
    vertrag = Vertrag("LV-004", 30, 100_000)
    vertrag.kuendigen()
    with pytest.raises(ValueError):
        vertrag.kuendigen()
