# Local Rule-Based Chatbot Framework (Offline, CPU-only)

Dieses Projekt implementiert einen vollständig lokalen, regelbasierten Chatbot.
Er benötigt keine KI-Modelle, keine GPU und keine Internetverbindung.

Der Chatbot besteht aus:
- Intent Detector (heuristisch)
- Rule Engine (Antwortlogik)
- Dialogue Manager (Kontext)
- Agent (Orchestrierung)

Das Projekt demonstriert:
- regelbasierte NLP
- deterministische Dialogführung
- modulare Architektur
- Prompt-Driven Development (PDD)

## Projektstruktur

/src  
    intent_detector.py  
    rule_engine.py  
    dialogue_manager.py  
    agent.py  

/docs  
    architecture.md  

/tests  
    test_intent_detector.md  
    test_rule_engine.md  
    test_dialogue_manager.md  
    test_agent.md  

hardware-requirements.md  
instructions.md  
README.md  
credits.md

## Hardware Requirements

Dieses Projekt ist vollständig lokal ausführbar und benötigt keine spezielle Hardware.
Siehe `hardware-requirements.md`.

## Lizenz

MIT License.

## Credits

Siehe `credits.md`.
