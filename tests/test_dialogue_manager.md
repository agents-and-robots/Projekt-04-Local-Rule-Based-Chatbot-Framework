# Test: Dialogue Manager

## Natürliche Sprache
Der Dialogue Manager soll den letzten Intent speichern.

## Maschinenlesbare Struktur
input:
  context: {}
  intent: "greeting"
  message: "Hallo"

expected:
  last_intent: "greeting"
