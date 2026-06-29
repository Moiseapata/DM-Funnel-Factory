def adapt_message_for_brand(original_message, brand):
    """
    Adapte un message à la voix d'une marque spécifique.
    brand: 'prince_ea', 'nike', 'mindvalley'
    """
    tone_prompts = {
        "prince_ea": "Rewrite this message with an inspirational, storytelling tone. Focus on changing lives and purpose. Use emotive language.",
        "nike": "Rewrite this message with a direct, no-fluff, action-oriented tone. Use short sentences. Channel 'Just Do It' energy.",
        "mindvalley": "Rewrite this message with a mysterious, spiritual tone. Use words like 'hidden path', 'uncover', 'transform'. Create curiosity."
    }
    
    adaptation_prompt = f"""
    Original message: {original_message}
    {tone_prompts[brand]}
    """
    
    return call_claude_api(adaptation_prompt)

# Exemple
amy_opt_in = "Hey [First Name]! Want to turn your expertise into a profitable online course—but not sure where to start? My free webinar shows you the exact steps to launch in 30 days. Reply ‘WEBINAR’ for the link!"

prince_ea_version = adapt_message_for_brand(amy_opt_in, "prince_ea")
nike_version = adapt_message_for_brand(amy_opt_in, "nike")
print(f"Prince EA: {prince_ea_version}")
print(f"Nike: {nike_version}")
