import sounddevice as sd
import wavio

def grabar_audio(nombre_archivo, duracion=5, frecuencia=44100):
    print("Grabando...")
    audio = sd.rec(int(duracion * frecuencia), samplerate=frecuencia, channels=2, dtype='int16')
    sd.wait()
    print("Grabación finalizada.")
    wavio.write(nombre_archivo, audio, frecuencia, sampwidth=2)

if __name__ == "__main__":
    archivo = "grabacion.wav"
    duracion = int(input("Duración en segundos: "))
    grabar_audio(archivo, duracion)
    print(f"Audio guardado como {archivo}")
