import random
import time

def elegir_personaje(lista):
    return random.choice(lista)

def esperar(segundos):
    time.sleep(segundos)

def batalla():
    heroinas = [
        "Yor Forger (Spy x Family)", "Rias Gremory (High School DxD)", "Hinata Hyuga (Naruto)",
        "Esdeath (Akame ga Kill!)", "Boa Hancock (One Piece)", "Faye Valentine (Cowboy Bebop)",
        "Zero Two (Darling in the Franxx)", "Makima (Chainsaw Man)", "Tsunade (Naruto)",
        "Kurisu Makise (Steins;Gate)", "Mereoleona Vermillion (Black Clover)", "Shinobu Kocho (Demon Slayer)",
        "Mitsuri Kanroji (Demon Slayer)", "Nico Robin (One Piece)", "Yoruichi Shihouin (Bleach)",
        "Kushina Uzumaki (Naruto)", "Mikasa Ackerman (Attack on Titan)", "Saber (Fate/Stay Night)",
        "Revy (Black Lagoon)", "Rukia Kuchiki (Bleach)"
    ]

    villanas = [
        "Lust (Fullmetal Alchemist)", "Medusa Gorgon (Soul Eater)", "Crona (Soul Eater)",
        "Esdeath (Akame ga Kill!)", "Toga Himiko (My Hero Academia)", "Yuno Gasai (Future Diary)",
        "Harley Quinn (Batman anime-style)", "Midari Ikishima (Kakegurui)", "Makima (Chainsaw Man)",
        "Shion (That Time I Got Reincarnated as a Slime)", "Isabella (The Promised Neverland)",
        "Albedo (Overlord)", "Android 21 (Dragon Ball)", "Jalter (Fate/Grand Order)",
        "Satella (Re:Zero)", "Kaguya Ōtsutsuki (Naruto)", "Arachne (Soul Eater)", "Ragyo Kiryuin (Kill la Kill)",
        "C.C. (Code Geass)", "Kurumi Tokisaki (Date A Live)"
    ]

    print("⚔️  ¡Comienza la batalla entre belleza y poder! ⚔️")
    esperar(2)

    heroina = elegir_personaje(heroinas)
    villana = elegir_personaje(villanas)

    print(f"\n✨ Heroína: {heroina}")
    print(f"🔥 Villana: {villana}")
    esperar(2)

    ganador = random.choice([heroina, villana])
    print(f"\n🏆 Ganadora: {ganador}")
    if ganador == heroina:
        print("✅ ¡La heroína se alza con la victoria!")
    else:
        print("❌ ¡La villana impone su voluntad!")

    esperar(2)

def main():
    while True:
        batalla()
        opcion = input("\n¿Quieres otra batalla? (s/n): ").strip().lower()
        if opcion != 's':
            print("\nGracias por jugar. ¡Hasta la próxima batalla!")
            break
        esperar(1)

if __name__ == "__main__":
    main()
