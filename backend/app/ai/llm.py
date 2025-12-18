from openai import OpenAI
from app.config.settings import OPENAI_API_KEY

client = OpenAI(api_key=OPENAI_API_KEY)

def respuesta_ia(pregunta, contexto=None):
    system = (
        "Eres el asistente virtual de la Notaría Paul Hurtado.\n"
        "NO inventes información.\n"
        "NO supongas horarios, precios ni requisitos.\n"
        "Responde ÚNICAMENTE usando el contexto proporcionado.\n"
        "Si no hay información suficiente, indica que se debe contactar por WhatsApp."
        "Si la consulta requiere revisión de documentos o es un caso particular, "
        "indica que debe comunicarse por WhatsApp.\n\n"
        "Usa un tono claro, breve y profesional."
    )

    if contexto:
        system += (
            "\n\nReferencia relacionada disponible (úsala solo como guía):\n"
            f"{contexto}"
        )

    res = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": system},
            {"role": "user", "content": pregunta}
        ],
        max_tokens=120
    )

    return res.choices[0].message.content
