# Assistant Interne IA (Python + Slack)

## 🎯 Objectif
Créer un assistant interne d’entreprise capable de :
- répondre à partir d’une base de connaissances interne
- appliquer des règles métier strictes
- demander validation humaine sur les sujets sensibles
- tracer toutes les interactions
- s’intégrer à Slack

## 🧠 Fonctionnalités
- LLM (OpenAI)
- Base documentaire interne
- Guardrails métier
- Human-in-the-loop
- Logs entreprise
- Intégration Slack (webhook)

## 🛠️ Stack
- Python 3.11
- LangChain
- OpenAI API
- Slack Webhooks

## ▶️ Lancer le projet
```bash
pip install -r requirements.txt
python agent.py
