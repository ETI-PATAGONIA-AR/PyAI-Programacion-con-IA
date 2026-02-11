import re


def normalize_for_speech(text: str) -> str:
    # 1. Eliminar URLs completas
    text = re.sub(r"https?://\S+", "", text)

    # 2. Eliminar markdown fuerte y cursiva
    text = text.replace("**", "")
    text = text.replace("*", "")

    # 3. Eliminar comillas innecesarias
    text = text.replace('"', "")
    text = text.replace("'", "")

    # 4. Encabezados tipo "Estructura:" → pausa natural
    text = re.sub(r"\b([A-ZÁÉÍÓÚÑ][\w\s]+):", r"\1.", text)

    # 5. Listas con guiones o puntos
    text = re.sub(r"[-•]\s*", "", text)

    # 6. Espacios múltiples
    text = re.sub(r"\s{2,}", " ", text)

    return text.strip()
