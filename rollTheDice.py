# # =============== ROLLING DICE ===============================
import random
#función que imprime cara del dado seleccionada
def showDice(number):
    #Tupla de Strings que contiene cada cara del dado
    dice=("""[------------]
[            ]
[     0      ]
[            ]
[------------]""","""[------------]
[     0      ]
[            ]
[     0      ]
[------------]""","""[------------]
[     0      ]
[     0      ]
[     0      ]
[------------]""","""[------------]
[   0   0    ]
[            ]
[   0   0    ]
[------------]""","""[------------]
[   0   0    ]
[     0      ]
[   0   0    ]
[------------]""","""[------------]
[   0   0    ]
[   0   0    ]
[   0   0    ]
[------------]""")
    print(dice[number]) #se imprime cara correspondiente

showDice(random.randint(0,5)) # se llama a la función para mostrar cara considerando
#un número random entre 0 y 5. (Seleccionaran caras del 1 al 6)
while(input("Presione y para rodar nuevamente...")=="y"):
    #mientras se siga presionando la tecla "y" se mostrará otra cara del dado de forma aleatoria.
    showDice(random.randint(0,5))
# =================================================================
# =================================================================
