class Grammar:
    def __init__(self, file):
        self.non_terminals, self.terminals, self.rules, self.initial_state = self.readGrammarFile(file)

    def readGrammarFile(self, file):
        rule = ''
        rules = {}

        with open(file, 'r') as f:
            for line in f:
                line = line.replace(' ', '')

                if 'G=' in line:
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

    def validate(self):
        if self.initial_state not in self.non_terminals:
            print("The initial state is not a valid non-terminal")
            return False

        for nt in self.non_terminals:

            if nt.islower(): 
                print(nt + " is not a valid non-terminal")
                return False
            
            for rule in self.rules[nt]:
                count = 0
                lastCharIdx = len(rule) - 1
                for c in rule:
                    if c.isupper():
                        if c not in self.non_terminals: # verify if the non-terminal is an existing rule
                            print(c + " is not a valid rule")
                            return False
                        
                        if count != lastCharIdx: # verify if the non-terminal is in the last position
                            print("The non-terminal " + c + " is not in the last position")
                            return False   
                        
                    elif c.islower():
                        if c not in self.terminals and c != '~':
                            print(c + " is not a valid terminal")
                            return False 

                    if c == '~': # verify if the empty string is in the last position
                        if count != lastCharIdx:
                            print("The empty string is not in the last position")
                            return False
                        
                        
                    count += 1
        return True