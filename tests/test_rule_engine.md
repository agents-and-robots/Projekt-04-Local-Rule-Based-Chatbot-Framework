# Test: Rule Engine

## Natürliche Sprache
Die Rule Engine soll für den Intent "greeting" eine Begrüßung zurückgeben.

## Maschinenlesbare Struktur
input:
  intent: "greeting"
  message: "Hallo"

expected_contains:
  "Hallo"
