# LLM Instructions – Local Rule-Based Chatbot Framework (Offline)

Diese Datei definiert alles, was ein LLM benötigt, um dieses Projekt vollständig selbständig umzusetzen:
- Input/Output-Protokoll
- Agenten-Logik
- Regelwerk
- Aufgabenbeschreibung
- Hardware-Constraints
- How-To-Use

---

## 1. Ziel

Erstelle ein System, das Benutzereingaben analysiert, Intents erkennt, passende Antworten generiert und einen Dialogkontext verwaltet — vollständig offline und deterministisch.

---

## 2. Hardware Constraints

Dieses Projekt muss vollständig auf normaler Consumer-Hardware lauffähig sein:

- CPU-only
- keine GPU-Abhängigkeiten
- keine Modelle > 1 GB
- keine externen APIs oder Cloud-Dienste
- alles offline
- Python-Standardbibliothek

---

## 3. Modul-Spezifikationen

### 3.1 Intent Detector (/src/intent_detector.py)

Signatur: detect(message: str) -> dict

Aufgabe:
- heuristische Intent-Erkennung
- Beispiele:
  - Begrüßung
  - Frage
  - Verabschiedung
  - Unbekannt

Rückgabeformat:
- intent: string
- confidence: float (0–1)

---

### 3.2 Rule Engine (/src/rule_engine.py)

Signatur: respond(intent: str, message: str) -> str

Aufgabe:
- Mapping von Intents zu Antworten
- deterministisch
- keine KI

---

### 3.3 Dialogue Manager (/src/dialogue_manager.py)

Signatur: update(context: dict, intent: str, message: str) -> dict

Aufgabe:
- Kontext aktualisieren
- z. B. letzter Intent, letzter User-Input

Rückgabeformat:
- context: dict

---

### 3.4 Agent (/src/agent.py)

Signatur: run(message: str, context: dict) -> dict

Aufgabe:
- orchestriert intent_detector, rule_engine, dialogue_manager
- Feedback-Loop (max. 1 Iteration)

Rückgabeformat:
- answer: string
- context: dict
- steps: list[str]

---

## 4. Orchestrator-Logik

1. intent = detect(message)
2. answer = respond(intent, message)
3. context = update(context, intent, message)
4. Ergebnis zurückgeben

---

## 5. Regelwerk / Constraints

### Intent Detection
- deterministisch
- regex oder einfache Regeln

### Rule Engine
- feste Antworttabellen
- keine freien Texte

### Dialogue Manager
- speichert minimalen Kontext

### Agent
- orchestriert deterministisch

---

## 6. Aufgaben an das LLM

Das LLM soll:

1. intent_detector.py implementieren  
2. rule_engine.py implementieren  
3. dialogue_manager.py implementieren  
4. agent.py implementieren  
5. architecture.md ergänzen  
6. Tests in /tests aktualisieren  

---

## 7. How-To-Use (für Code-Assistenten)

1. Öffne das Repository.  
2. Öffne `instructions.md`.  
3. Markiere den gesamten Inhalt.  
4. Sende ihn an deinen Code-Assistenten mit:

„Lies diese instructions.md vollständig. Implementiere dann alle beschriebenen Module und Dateien. Halte dich strikt an das Input/Output-Protokoll, das Regelwerk und die Hardware-Constraints. Beginne mit intent_detector.py.“

Damit kann ein LLM das Projekt vollständig autonom umsetzen.
