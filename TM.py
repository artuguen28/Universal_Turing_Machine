input_1 = { 
    'inicial': 0, 
    'aceita': 1, 
    'rejeita': 2,
    'delta': [ 
        (0,0,0,1,'D'),
        (0,0,1,0,'D'),
        (0,3,'b','b','E'), 
        (3,1,0,0,'P'),
        (3,1,1,1,'P')
    ] 
}

input_2 = {
    'inicial': 0,
    'aceita': 3,
    'rejeita': 2, 
    'delta': [
        (0, 0, 0, 0, "D"), 
        (0, 1, 1, 1, "D"), 
        (0, 3, "b", "b", "P"), 
        (1, 0, 1, 1, "D"), 
        (1, 1, 0, 0, "D"), 
        (1, 2, "b", "b", "P")
    ]
}

input_3 = {
    'inicial': 0, 
    'aceita': 1, 
    'rejeita': 2, 
    'delta': [
        (0, 0, 1, "#", "D"), 
        (0, 0, 0, "x", "D"), 
        (0, 1, "b", "b", "P"), 
        (0, 2, "x", "x", "P")
    ]
}

def TuringMachine(inp):
    words = []
    qtd = int(input())

    # Adding inputs 
    for i in range(0, qtd):
        word = str(input())
        words.append(word)

    # Running for each input
    for i in words:

        # default settings
        word_list = []
        current_state = inp['inicial']
        head = 0

        # Input and list initialization
        for w in i:
            word_list.append(w)
        word_list.append('b')

    

        # Turing Machine
        while(True): # Executar 5 ações

            # Testing each transition function
            for t in inp['delta']:

                # Executing transition
                if (t[0] == current_state) and (str(t[2]) == word_list[head]): 

                    #print(f"Transição aplicada: {t}")

                    word_list[head] = str(t[3])
                    current_state = t[1]

                    if t[4] == 'D':
                        head = head + 1
                        #print("incrementa head")
                    elif t[4] == 'E':
                        head = head - 1
                        #print("decrementa head")
                    else:
                        #print("para head")
                        continue
                
                    #print(f"Head: {head}")

                    break

                elif (t[0] == current_state) and (word_list[head] in ('x', '#', 'b') and t[2] == word_list[head]):

                    word_list[head] = str(t[3])
                    current_state = t[1]

                    if t[4] == 'D':
                        head = head + 1
                    elif t[4] == 'E':
                        head = head - 1
                    else:
                        continue

                    break
                
                else:
                    continue

            if (current_state == inp['aceita']):
                word_list.remove('b')
                final_word = ''.join(word_list)
                print(f"{final_word} ACEITA")
                break

            elif (current_state == inp['rejeita']):
                word_list.remove('b')
                final_word = ''.join(word_list)
                print(f"{final_word} REJEITA")
                break

            else:
                pass

TuringMachine(input_3)