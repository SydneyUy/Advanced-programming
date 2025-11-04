import random
#what if use the ? to split and then add it back in the input statement

def read_file():
    jokes = []
    with open ("randomJokes.txt", 'r', encoding='utf-8') as f:
        for line in f:
            clean_line = line.strip()
            if '?' in clean_line:
                joke, punch = clean_line.split('?', 1)
                joke = joke.strip() + '?'
                punch = punch.strip()
            jokes.append((joke,punch))
        return jokes


def main():
    '''Write a program that when prompted with the phrase "Alexa tell me a Joke" responds with a random joke from the dataset. The program should first present the setup then allow the user to enter a key to display the punchline. 
        The user should be able to continue requesting new jokes until they decide to quit the program. '''
    jokes = read_file()
    
    user_input = input("Ask Alexa to tell a joke by typing 'Alexa tell me a joke' below. (input quit to exit)\n ")

    while user_input.lower() != 'quit':
        if user_input.lower() == 'alexa tell me a joke':  
            setup, punch = random.choice(jokes)
            print('\n',setup)
            input('Press Enter to see the punchline...')
            print(punch,'\n')
        user_input = input("Ask Alexa to tell a joke by typing 'Alexa tell me a joke' below. (input quit to exit)\n ")

print("closing program.")

main()