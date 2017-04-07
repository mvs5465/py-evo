from LobsterGame import LobsterGame


def main():

    epochs = 100

    evolutionSuccesses = 0

    lastLobster = 0

    for epoch in range(epochs):
        lobster = LobsterGame()
        lobster.play()
        if lobster.evolutionSuccess:
            evolutionSuccesses += 1

    print("#####")
    print("#####")
    print("#####")

    print("The era has passed... evolution success ratio:")
    print(str(evolutionSuccesses) + "/" + str(epochs))




if __name__ == "__main__":
    main()