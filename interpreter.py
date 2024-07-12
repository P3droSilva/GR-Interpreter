import grammar as gr

#module to interpret the grammar

def interpret(grammar, word):
    def check_final_state(current_state, word):
        print(f"Current state: {current_state}, word: {word}")
        for rule in grammar.rules.get(current_state, []):
            if rule == '~':
                return True
            elif len(rule) == 1 and rule in grammar.non_terminals:
                if check_final_state(rule, word):
                    return True
        return False

    def match_rule(current_state, word):
        if not word:
            return check_final_state(current_state, word)
        else:
            print(f"Current state: {current_state}, word: {word}")
        
        for rule in grammar.rules.get(current_state, []):
            word_index = 0
            i = 0

            while i < len(rule):
                if rule[i] in grammar.non_terminals:
                    # Try to match the non-terminal
                    result = match_rule(rule[i], word[word_index:])
                    if result:
                        return True
                    else:
                        # Reset and try next rule
                        break
                elif rule[i] == word[word_index] and word_index < len(word):
                    word_index += 1
                else:
                    break
                i += 1
            
            # if rule == '~' and word_index == len(word):
            #     print("current state " + current_state)
            #     return True

        return False

    return match_rule(grammar.initial_state, word)
