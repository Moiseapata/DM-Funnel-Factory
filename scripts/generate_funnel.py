import json
import os
# Note: Vous simuleriez l'appel à l'API Claude ici.
# Pour l'entretien, vous pouvez montrer une version qui lit un fichier de config.
from utils import call_claude_api  # Votre fonction helper

def load_prompt(prompt_name):
    """Charge un prompt depuis le dossier /prompts"""
    with open(f"../prompts/{prompt_name}.md", "r") as f:
        return f.read()

def generate_funnel(client_brief):
    """
    Génère un DM funnel complet à partir d'un brief.
    client_brief = {
        "client_name": "Amy Porterfield",
        "webinar_title": "How to Launch Your First Online Course",
        "tone": "inspirational",
        "target_audience": "entrepreneurs",
        "key_benefits": ["Validate course idea", "3-step launch framework", "Attract first students"],
        "cta_trigger": "WEBINAR"
    }
    """
    funnel = {}
    steps = ["opt-in-dm", "nurture-dm", "reminder-dm", "sales-dm"]
    
    for step in steps:
        prompt_template = load_prompt(step)
        # Remplacer les variables dans le prompt par les infos du brief
        formatted_prompt = prompt_template.format(**client_brief)
        # Appel à l'API Claude (simulé ici)
        funnel[step] = call_claude_api(formatted_prompt)
    
    return funnel

# Exemple d'utilisation
if __name__ == "__main__":
    amy_brief = {
        "client_name": "Amy Porterfield",
        "webinar_title": "How to Launch Your First Online Course",
        "tone": "inspirational",
        "target_audience": "entrepreneurs",
        "key_benefit_1": "How to validate your course idea",
        "key_benefit_2": "The 3-step launch framework",
        "key_benefit_3": "How to attract your first students",
        "cta_trigger": "WEBINAR",
        "program_name": "Course Launch Lab"
    }
    
    funnel = generate_funnel(amy_brief)
    
    # Sauvegarde dans un fichier JSON
    with open("../examples/amy_porterfield_funnel.json", "w") as f:
        json.dump(funnel, f, indent=2)
    
    print("✅ Funnel generated and saved!")
