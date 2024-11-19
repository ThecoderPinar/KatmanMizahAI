from transformers import pipeline

def saka_uret(keywords):
    espri_uretici = pipeline("text-generation", model="gpt-3.5-turbo")
    input_text = f"{keywords} ile komik bir şaka üret"
    espri = espri_uretici(input_text, max_length=50, num_return_sequences=1)
    return espri[0]['generated_text']
