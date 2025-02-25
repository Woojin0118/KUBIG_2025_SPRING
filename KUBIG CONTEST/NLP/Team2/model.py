import json
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

MODEL_NAME = "chentong00/propositionizer-wiki-flan-t5-large"
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)

def generate_explanation(query, results):
    context_texts = []

    for result in results:
        title = result.metadata.get("title", "Unknown")
        text = result.page_content.strip()
        context_texts.append(f"{title}: {text}")

    combined_context = "\n\n".join(context_texts)

    prompt = (
        f"Based on the following information, provide a detailed explanation of '{query}'.\n\n"
        f"Context:\n{combined_context}\n\n"
        f"Explanation:"
    )

    inputs = tokenizer(prompt, return_tensors="pt", truncation=True, max_length=1024)

    output_ids = model.generate(**inputs, max_length=512)
    explanation = tokenizer.decode(output_ids[0], skip_special_tokens=True)

    try:
        explanation_json = json.loads(explanation)
        if isinstance(explanation_json, list):
            explanation = " ".join(explanation_json)
    except json.JSONDecodeError:
        pass

    return explanation.replace("\\", "").replace("\"", "").strip()
