import re
from .speech_normalizer import normalize_for_speech


def extract_speakable_text(text: str) -> str:
    # Eliminar bloques de código
    text = re.sub(r"```.*?```", "", text, flags=re.DOTALL)

    clean_lines = []
    for line in text.splitlines():
        line = line.strip()
        if not line:
            continue
        if is_technical_line(line):
            continue
        clean_lines.append(line)

    raw_text = " ".join(clean_lines)
    return normalize_for_speech(raw_text)


def is_technical_line(line: str) -> bool:
    technical_markers = [
        "#include", "void ", "def ", "{", "}", ";",
        "int ", "float ", "double ",
        "for(", "while(", "if(",
        "setup()", "loop()"
    ]
    return any(marker in line for marker in technical_markers)
