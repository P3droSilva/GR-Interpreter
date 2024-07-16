
#module to interpret the grammar

def interpret(grammar, word):
    def check_final_state(current_state, word, path):
        rules = grammar.rules.get(current_state, [])
        for rule in rules:
            symbols = rule.split(' ')
            for symbol in symbols:
                if symbol == '&':
                    word_ = ' '.join(word)
                    path.append((current_state + ' -> ' + rule, word_))
                    return True
                elif symbol in grammar.non_terminals:
                    if check_final_state(symbol, word, path):
                        return True
                else:
                    break
                
        if(len(path) == 0):
            state = []
            for rule in rules:
                state.append(current_state + ' -> ' + rule)
            path.append("ERROR! Expected symbol: &" + "\nCurrent state: " + str(state))
        return False

    def match_rule(current_state, word, path):
        if not word:
            return check_final_state(current_state, word, path)
        
        rules = grammar.rules.get(current_state, [])
        for rule in rules:
            symbols = rule.split(' ')
            word_index = 0
            count = 0
            for symbol in symbols: 
                if symbol in grammar.non_terminals:
                    result = match_rule(symbol, word[word_index:], path)
                    if result:
                        word_ = ' '.join(word)
                        path.append((current_state + ' -> ' + rule, word_))
                        return True
                    else:
                        break
                elif symbol == word[word_index] and word_index < len(word) and symbol in grammar.terminals:
                    word_index += 1
                else:
                    break
                
                if word_index == len(word):
                    if symbol == '&' or count == len(symbols) - 1:
                        print("final")
                        word_ = ' '.join(word)
                        path.append((current_state + ' -> ' + rule, word_))
                        return True
                
                count += 1

        if(len(path) == 0):
            state = []
            for rule in rules:
                state.append(current_state + ' -> ' + rule)
            path.append("ERROR! Expected symbol: " + word[word_index] + "\nCurrent state: " + str(state))
        return False

    word = word.strip()
    word = word.split(' ')
    path = []
    return match_rule(grammar.initial_state, word, path), path[::-1]
