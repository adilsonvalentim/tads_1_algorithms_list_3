'''1. Dobrar elementos de uma lista (com map)
Escreva uma função que, utilizando map e uma função lambda, receba uma lista
de números inteiros e retorne uma nova lista com todos os elementos dobrados.
Exemplo de entrada: [1, 2, Exemplo de saída: [2, 4, 6, 8]'''

def presentation():
    """
    Show the name of the program

    Prints a formatted title of the program, which
    doubles the elements of a list.
    """
    print('\n* * * PROGRAM TO DOUBLE ELEMENTS OF A LIST * * *')

def ask_name():
    """
    Prompt the user to enter their name.

    Asks the user for their name via input
    and returns it as a string.

    Returns:
        str: The name entered by the user.
    """
    name = input('\nPlease user, input your name: ')
    return name

def introduction(name: str):
    """
    Provide an introduction to the program.

    This function explains to the user, via a printed message,
    how the program works and how to interact with it.

    Args:
        name (str): The name of the user, as entered earlier.
    """
    print(
        f'\nWelcome {name}! In this program you will enter as many integers as you want and you '
        '\nwill receive a list of these duplicate numbers. Enter "e" when you want to end the '
        '\nentries and receive the list with the duplicate values.'
    )

def receive_integers():
    """
    Prompt the user to input integers and return them as a list.

    This function repeatedly asks the user to input integers until they
    enter "e" to signal the end. The integers are collected in a list
    and returned once the input process is complete.

    Returns:
        list: A list containing the integers entered by the user.
    """
    user_insertion = ''
    integers = []
    
    while user_insertion != 'e':
        user_insertion = input('\nEnter an integer to insert it into the list that will be duplicated. Enter "e" when you want to end the insertions: ').lower()
        insertion_analysis(user_insertion, integers)
    return integers

def insertion_analysis(insertion: str, int_list: list):
    if insertion == 'e':
        return
    else:
        try:
            insertion = int(insertion)
            return int_list.append(insertion)
        except ValueError:
            print('\nError! Invalid input. You must enter an integer, or "e" to end inputs.')

def doubling_list(int_list: list):
    doubled_list = []
    doubled_list = list(map(lambda x: x*2, int_list))
    return doubled_list

def printing_result(original_list: list, doubled_list: list):
    print(
        '\nThis was the list you entered:'
        f'\n{" ".join(str(x) for x in original_list)}'
        '\nAnd this is the doubled list:'
        f'\n{" ".join(str(x) for x in doubled_list)}'
    )

def ask_to_continue(name: str):
    keep_running = ''
    options = {'y': True, 'n': False}
    while keep_running not in options:
        keep_running = input(
            f'\nOkay, {name}, would you like to duplicate the values of a new list?'
            '\nIf yes, enter "y", otherwise enter "n" to end the program: '
        ).lower()
        if keep_running in options:
            return options[keep_running]
        else:
            print('\nError! Invalid option. Input options are only "y" or "n". Try again.')

def ending_w_credits(name: str):
    print(
        f'\nThank you very much for using my program, {name}.'
        '\n\nCredits: Adilson Valentim - 1st Period Student of TADS - IFMS Três Lagoas Campus - 2025'
    )

running = True
presentation()
name = ask_name()
introduction(name)
while running:
    integers = receive_integers()
    doubled_list = doubling_list(integers)
    printing_result(integers, doubled_list)
    running = ask_to_continue(name)
    if running:
        print("\nPerfect! Let's double more integers!")
ending_w_credits(name)