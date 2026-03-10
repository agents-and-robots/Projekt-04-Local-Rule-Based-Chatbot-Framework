# Architektur – Local Rule-Based Chatbot Framework

## Module

- intent_detector.py – erkennt Intents
- rule_engine.py – generiert Antworten
- dialogue_manager.py – verwaltet Kontext
- agent.py – orchestriert den Prozess

## Datenfluss

1. Intent Detector analysiert Nachricht
2. Rule Engine generiert Antwort
3. Dialogue Manager aktualisiert Kontext
4. Agent orchestriert alles
