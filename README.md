# Trabalho Final de Compiladores GR-Interpreter
## Integrantes: Pedro Henrique da Silva Hinerasky e Ramon Godoy Izidoro

### Padrão a ser seguido pela grámatica:
* Gramática deve estar no arquivo GLD.txt
* Vazio representado por '&'
1. Primeira linha:
    * Símbolo representante da grámatica: 'G ='
    * Dentro de parenteses, separados por ponto e vírgula conter respectivamente: conjunto de não terminais, conjunto de terminais, conjunto de regras de produção e símbolo inicial da grámatica
      * Conjunto de não terminais: Dentro de chaves, separados por vírgula e letras maiusculas
      * Conjunto de terminais: Dentro de chaves, separado por vírgula e letras minusculas, NÃO deve conter vazio
      * Conjunto de regras: letra maiuscula
      * Símbolo inicial da grámatica: letra maiuscula, deve estar dentro do conjunto de não terminais
2. Segunda linha:
    * Deve iniciar com o símbolo do conjunto de regras seguido de ':'
    * Cada regra deve ser definida pela sequencia: símbolo não terminal + '->' + apenas símbolos terminais OU apenas um símbolo não terminal OU terminais seguido de um não terminal (esse deve estar à extrema direita para ser GLD). Para adicionar mais caminhos usar '|' e seguir a definição citada acima logo após '->'
        * Espaços irão definir um símbolo terminal ou não terminal, por exemplo: 'id' (único símbolo terminal) e 'i d'(dois símbolos terminais)
3. Terceira linha e adiante:
    * Apenas respeitar a regra da segunda linha sem iniciar com o símbolo do conjunto de regras

* Para rodar, no terminal, digite: python3 main.py
* A verificação da gramática ocorre pelas funções readGrammarFile e parser, dentro do arquivo grammar.py
* Se a verificação for um sucesso, o programa irá pedir uma palavra para ser analisada pela gramática, essa palavra deve ser escrita com espaços que determinarão cada símbolo a ser procurado no conjunto de regras
* Por fim, o programa dirá se a palavra foi aceita ou não, demonstrando o caminho percorrido pelas suas regras ou a regra que causou o erro  

* EXEMPLO de gramática aceita:
 
    G = ({S',A}; {a,b,id}; P; S') 

    P:  S' -> a S' | A 
    
    A -> b A | id | & 

     