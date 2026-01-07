from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage
from datetime import datetime
import requests
SLACK_WEBHOOK_URL = "https://hooks.slack.com/services/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"


# Initialisation du modèle
llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0
)

# Message système (règles métier)
system_message = SystemMessage(
    content=(
        "Tu es un assistant interne d'entreprise.\n"
        "Règles strictes :\n"
        "- Tu réponds UNIQUEMENT à partir des informations internes fournies.\n"
        "- Tu ne fais AUCUNE supposition.\n"
        "- Si l'information n'est pas présente, réponds exactement : "
        "'Je ne dispose pas de cette information.'\n"
        "- Réponses courtes, claires et professionnelles."
    )
)

# Charger la base de connaissances
with open("connaissance.txt", "r", encoding="utf-8") as f:
    knowledge = f.read()

# === REGLES DE SECURITE ===
mots_sensibles = [
    "salaire",
    "contrat",
    "licenciement",
    "direction",
    "finance",
    "confidentiel",
    "personnel",
]

# === INTERACTION UTILISATEUR ===
question = input("Question interne : ")

# Vérification humaine si question sensible
if any(mot in question.lower() for mot in mots_sensibles):
    print("\n⚠️ Question sensible détectée.")
    validation = input("Validation humaine requise (oui/non) : ")

    if validation.lower() != "oui":
        print("\nRéponse bloquée. Un humain doit traiter cette demande.")
        exit()



messages = [
    system_message,
    HumanMessage(content=f"Informations internes : {knowledge}"),
    HumanMessage(content=question),
]

# Appel du modèle
response = llm.invoke(messages)
import requests

payload = {
    "text": f"🧠 *Assistant interne*\n\n❓ Question : {question}\n💬 Réponse : {response.content}"
}

requests.post(SLACK_WEBHOOK_URL, json=payload)


print("\nRéponse de l'agent :")
print(response.content)

# === LOGS ENTREPRISE ===
with open("logs.txt", "a", encoding="utf-8") as log_file:
    log_file.write(
        f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}]\n"
        f"QUESTION: {question}\n"
        f"REPONSE: {response.content}\n"
        f"{'-'*40}\n"
    )

SLACK_WEBHOOK_URL = "https://hooks.slack.com/services/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"
