import grammar as gr
import interpreter as ip

def main():
    gramatica = gr.Grammar('GLD.txt')
    if not gramatica.validate():
        print("The grammar is not valid")
        return
    
    word = input("Enter a word to be interpreted by the GLD: ")
    if ip.interpret(gramatica, word):
        print("The word is accepted by the GLD")
    else:
        print("The word is not accepted by the GLD")
    


if __name__ == '__main__':
    main()