from transformers import pipeline

generator = pipeline("text2text-generation", model="google/flan-t5-base")

def generate_notes(text):
    prompt = f"Convert to bullet point notes:\n{text}"

    result = generator(prompt, max_length=256, do_sample=False)
    return result[0]['generated_text']