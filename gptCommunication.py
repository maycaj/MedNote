from openai import OpenAI
client = OpenAI(api_key="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")

content = '''Patient – Good Morning, doctor. May I come in?
Doctor – Good Morning. How are you? You do look quite pale this morning.
Patient – Yes, doctor. I’ve not been feeling well for the past few days. I’ve been having a stomach ache for a few days and feeling a bit dizzy since yesterday.
Doctor – Okay, let me check. (applies pressure on the stomach and checks for pain) Does it hurt here?
Patient – Yes, doctor, the pain there is the sharpest.
Doctor – Well, you are suffering from a stomach infection, that’s the reason you are having a stomach ache and also getting dizzy. Did you change your diet recently or have something unhealthy?
Patient – Actually, I went to a fair last week and ate food from the stalls there.
Doctor – Okay, so you are probably suffering from food poisoning. Since the food stalls in fairs are quite unhygienic, there’s a high chance those uncovered food might have caused food poisoning.
Patient – I think I will never eat from any unhygienic place in the future.
Doctor – That’s good. I’m prescribing some medicines, have them for one week and come back for a checkup next week. And please try to avoid spicy and fried foods for now.
Patient – Okay, doctor, thank you.
Doctor – Welcome.'''

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", 
         "content": "This is a transcription of a patient-doctor conversation. Have one paragraph which concisely summarizes the interaction. Have a second paragraph that ONLY defines terms a college graduate would not understand. Say 'have a nice day' at the end"},
        {"role": "user",   
         "content": content}
    ]
)

print(completion.choices[0].message)