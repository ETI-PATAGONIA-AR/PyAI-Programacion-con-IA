import pyttsx3

def listar_voces():
    engine = pyttsx3.init("sapi5")
    voices = engine.getProperty("voices")

    print("\nVOCES DISPONIBLES EN EL SISTEMA:\n")

    for i, voice in enumerate(voices):
        print(f"Indice: {i}")
        print(f"  ID        : {voice.id}")
        print(f"  Nombre    : {voice.name}")
        print(f"  Idiomas   : {voice.languages}")
        print(f"  Genero    : {voice.gender}")
        print("-" * 40)

if __name__ == "__main__":
    listar_voces()
