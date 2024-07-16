import grammar as gr
import interpreter as ip

def main():
    gramatica = gr.Grammar('GLD.txt')

    if not gramatica.parser():
        print("The grammar is not valid")
        return
    else:
        print("The grammar is valid")
    
    word = input("Enter a word to be interpreted by the GLD: ")
    accepted, path = ip.interpret(gramatica, word)
    if accepted:
        print("The word is accepted by the GLD")
    else:
        print("The word is not accepted by the GLD")

    print("Path: ")
    for p in path:
        print(p)
    


if __name__ == '__main__':
    main()