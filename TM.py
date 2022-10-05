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

qtd = int(input())

for i in range(0, qtd):

    word_list = []
    word = str(input())

    for w in word:
        word_list.append(w)
    
    print(word_list)

