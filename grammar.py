class Grammar:
    def __init__(self, file):
        self.non_terminals, self.terminals, self.rules, self.initial_state = self.readGrammarFile(file)

    def readGrammarFile(self, file):
        rule = ''
        rules = {}

        with open(file, 'r') as f:
            for line in f:
                line = line.strip()

                if 'G =' in line:
                    line = line.replace(' ', '')
                    line = line.replace('G=','')
                    line = line.replace('(','')
                    line = line.replace(')','')
                    non_terminals, terminals, rule, initial_state = line.split(';')

                    non_terminals = non_terminals.replace('{','')
                    non_terminals = non_terminals.replace('}','')
                    non_terminals = [n for n in non_terminals.split(',')]

                    terminals = terminals.replace('{','')
                    terminals = terminals.replace('}','')
                    terminals = [t for t in terminals.split(',')]

                    initial_state = initial_state.strip()

                else:
                    r = rule + ':'
                    line_ = line
                    if r in line:
                        line_ = line.replace(r, '')

                    if '->' in line_:
                        left, right = line_.split('->')
                        left = left.strip()
                        right = [r.strip() for r in right.split('|')]
                        rules[left] = right
                    
        return non_terminals, terminals, rules, initial_state

    def parser(self):
        if self.initial_state not in self.non_terminals:
            print("The initial state is not a valid non-terminal")
            return False
        
        if len(self.terminals) != len(set(self.terminals)):
            print("The grammar contains repeated terminal symbols")
            return False

        
        if len(self.non_terminals) != len(set(self.non_terminals)):
            print("The grammar contains repeated non terminal symbols")
            return False
        
        for t in self.terminals:
            if t.isupper(): 
                print(t + " is not a valid terminal")
                return False

        for nt in self.non_terminals:
            if nt.islower(): 
                print(nt + " is not a valid non-terminal")
                return False
            
            for rule in self.rules[nt]:
                symbols = rule.split(' ')
                count = 0
                lastSymbolIdx = len(symbols) - 1     
                for symbol in symbols:
                    if symbol.isupper():
                        if symbol not in self.non_terminals: # verify if the non-terminal is an existing rule
                            print(symbol + " is not a valid rule")
                            return False
                        
                        if count != lastSymbolIdx: # verify if the non-terminal is in the last position
                            print("The non-terminal " + symbol + " is not in the last position")
                            return False   
                        
                    elif symbol.islower():
                        if symbol not in self.terminals and symbol != '&':
                            print(symbol + " is not a valid terminal")
                            return False 

                    if symbol == '&': # verify if the empty string is in the last position
                        if count != lastSymbolIdx:
                            print("The empty string is not in the last position")
                            return False
                        
                        
                    count += 1
        return True