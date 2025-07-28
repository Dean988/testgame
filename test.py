import random


def play() -> None:
    """Gestisce una singola partita."""
    target = random.randint(1, 100)
    attempts = 0
    print("\nHo pensato a un numero tra 1 e 100. Riuscirai a indovinarlo?")

    while True:
        try:
            guess = int(input("Inserisci la tua ipotesi: "))
            attempts += 1

            if guess < target:
                print("Troppo basso! Prova ancora.")
            elif guess > target:
                print("Troppo alto! Prova ancora.")
            else:
                print(f"Complimenti! Hai indovinato il numero {target} in {attempts} tentativi.")
                break
        except ValueError:
            print("Per favore, inserisci un numero intero valido.")


def main() -> None:
    """Funzione principale che permette di giocare più partite."""
    print("=== Benvenuto/a al gioco 'Indovina il numero'! ===")
    while True:
        play()
        again = input("Vuoi giocare di nuovo? (s/n): ").strip().lower()
        if again != 's':
            print("Grazie per aver giocato! A presto.")
            break


if __name__ == "__main__":
    main()