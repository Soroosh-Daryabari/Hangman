from random import choice

HANGMAN = [
    "___________",
    "|         |",
    "|         O",
    "|         |",
    "|        /|\ ",
    "|         |",
    "|        / \ ",
    "______________",
    "|            |"
]

WORDS = [
    "django", "react", "python", "javascript",
    "java", "flutter", "csharp", "xamarin", "dart", "golang",
    "angular", "cplusplus", "c", "spring", "css"
]


def checkInputValue(userInput):
    return userInput.isdigit() or (userInput.isalpha() and len(userInput) > 1)


def getUserInput():
    userInput = input("Please type a letter : ").lower().strip()
    return userInput


class Hangman:
    def __init__(self, word_to_guess):
        self.word_to_guess = word_to_guess
        self.failedAttempts = 0
        self.gameProgress = list("_" * len(self.word_to_guess))

    def findIndexes(self, letter):
        return [key for key, value in enumerate(self.word_to_guess) if value == letter]

    def printGameStatus(self):
        print("\n")
        print("\n".join(HANGMAN[:self.failedAttempts]))
        print("\n")
        print(" ".join(self.gameProgress))

    def updateGame(self, letter, indexes):
        for index in indexes:
            self.gameProgress[index] = letter

    def playGame(self):
        while self.failedAttempts <= len(HANGMAN):
            self.printGameStatus()
            userInput = getUserInput()
            if checkInputValue(userInput):
                print("This isn't a valid letter")
                continue

            elif userInput in self.word_to_guess:
                indexes = self.findIndexes(userInput)
                self.updateGame(userInput, indexes)
                if self.gameProgress.count("_") == 0:
                    print(f"You Win! The word is {self.word_to_guess}")
                    quit()

            else:
                self.failedAttempts += 1
        print(f"You lost!! The word is {self.word_to_guess}")


if __name__ == "__main__":
    word_to_guess = choice(WORDS)
    Hangman = Hangman(word_to_guess)
    Hangman.playGame()
