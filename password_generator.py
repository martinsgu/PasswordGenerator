import random
def index():

    def gerar_senha_letras():
        def shuffle(string):
            temp_list = list(string)
            random.shuffle(temp_list)
            return "".join(temp_list)

        def uppercase_letter_generator():
            uppercase_letter = chr(random.randint(65, 90))
            return uppercase_letter

        def lowercase_letter_generator():
            lowercase_letter = chr(random.randint(97, 122))
            return lowercase_letter

        uppercase_letter_1 = uppercase_letter_generator()  # ASCII code / https://www.ascii-code.com/
        uppercase_letter_2 = uppercase_letter_generator()
        uppercase_letter_3 = uppercase_letter_generator()
        uppercase_letter_4 = uppercase_letter_generator()
        uppercase_letter_5 = uppercase_letter_generator()
        uppercase_letter_6 = uppercase_letter_generator()

        lowercase_letter_1 = lowercase_letter_generator()
        lowercase_letter_2 = lowercase_letter_generator()
        lowercase_letter_3 = lowercase_letter_generator()
        lowercase_letter_4 = lowercase_letter_generator()
        lowercase_letter_5 = lowercase_letter_generator()
        lowercase_letter_6 = lowercase_letter_generator()

        password_part_1 = uppercase_letter_1 + uppercase_letter_2 + uppercase_letter_3 + lowercase_letter_1 + lowercase_letter_2 + lowercase_letter_3
        password_part_2 = uppercase_letter_4 + uppercase_letter_5 + uppercase_letter_6 + lowercase_letter_4 + lowercase_letter_5 + lowercase_letter_6

        password_part_1 = shuffle(password_part_1)
        password_part_2 = shuffle(password_part_2)

        password = password_part_1 + "-" + password_part_2

        print(password)
    def gerar_senha_numeros():
        def shuffle(string):
            temp_list = list(string)
            random.shuffle(temp_list)
            return "".join(temp_list)
        def number_generator():
            number = int(random.randint(0, 9))
            return number

        number_1 = str(number_generator())
        number_2 = str(number_generator())
        number_3 = str(number_generator())
        number_4 = str(number_generator())
        number_5 = str(number_generator())
        number_6 = str(number_generator())
        number_7 = str(number_generator())
        number_8 = str(number_generator())
        number_9 = str(number_generator())
        number_10 = str(number_generator())
        number_11 = str(number_generator())
        number_12 = str(number_generator())

        password_part_1 = number_1 + number_2 + number_3 + number_4 + number_5 + number_6
        password_part_2 = number_7 + number_8 + number_9 + number_10 + number_11 + number_12

        password_part_1 = shuffle(password_part_1)
        password_part_2 = shuffle(password_part_2)

        password = password_part_1 + "-" + password_part_2

        print(password)

    def gerar_senha_letras_e_numeros():
        def shuffle(string):
            temp_list = list(string)
            random.shuffle(temp_list)
            return "".join(temp_list)

        def uppercase_letter_generator():
            uppercase_letter = chr(random.randint(65, 90))
            return uppercase_letter

        def lowercase_letter_generator():
            lowercase_letter = chr(random.randint(97, 122))
            return lowercase_letter

        def number_generator():
            number = int(random.randint(0, 9))
            return number

        uppercase_letter_1 = uppercase_letter_generator()  # ASCII code / https://www.ascii-code.com/
        uppercase_letter_2 = uppercase_letter_generator()
        uppercase_letter_3 = uppercase_letter_generator()
        uppercase_letter_4 = uppercase_letter_generator()

        lowercase_letter_1 = lowercase_letter_generator()
        lowercase_letter_2 = lowercase_letter_generator()
        lowercase_letter_3 = lowercase_letter_generator()
        lowercase_letter_4 = lowercase_letter_generator()

        number_1 = str(number_generator())
        number_2 = str(number_generator())
        number_3 = str(number_generator())
        number_4 = str(number_generator())

        password_part_1 = uppercase_letter_1 + uppercase_letter_2 + lowercase_letter_1 + lowercase_letter_2 + number_1 + number_2
        password_part_2 = uppercase_letter_3 + uppercase_letter_4 + lowercase_letter_3 + lowercase_letter_4 + number_3 + number_4

        password_part_1 = shuffle(password_part_1)
        password_part_2 = shuffle(password_part_2)

        password = password_part_1 + "-" + password_part_2

        print(password)

    def gerar_senha_letras_numero_e_simbolos():
        def shuffle(string):
            temp_list = list(string)
            random.shuffle(temp_list)
            return "".join(temp_list)

        def number_generator():
            number = int(random.randint(0, 9))
            return number

        def uppercase_letter_generator():
            uppercase_letter = chr(random.randint(65, 90))
            return uppercase_letter

        def lowercase_letter_generator():
            lowercase_letter = chr(random.randint(97, 122))
            return lowercase_letter

        def character_generator():
            character = random.choice('!@#$%&*.')
            return character

        uppercase_letters = 2
        uppercase_letters = 2
        numbers = 2
        characters = 2

        uppercase_letter_1 = uppercase_letter_generator()  # ASCII code / https://www.ascii-code.com/
        uppercase_letter_2 = uppercase_letter_generator()
        uppercase_letter_3 = uppercase_letter_generator()
        uppercase_letter_4 = uppercase_letter_generator()

        lowercase_letter_1 = lowercase_letter_generator()
        lowercase_letter_2 = lowercase_letter_generator()
        lowercase_letter_3 = lowercase_letter_generator()
        lowercase_letter_4 = lowercase_letter_generator()

        number_1 = str(number_generator())
        number_2 = str(number_generator())
        number_3 = str(number_generator())
        number_4 = str(number_generator())

        character_1 = character_generator()
        character_2 = character_generator()
        character_3 = character_generator()
        character_4 = character_generator()

        password_part_1 = uppercase_letter_1 + uppercase_letter_2 + lowercase_letter_1 + lowercase_letter_2 + number_1 + number_2 + character_1 + character_2
        password_part_2 = uppercase_letter_3 + uppercase_letter_4 + lowercase_letter_3 + lowercase_letter_4 + number_3 + number_4 + character_3 + character_4

        password_part_1 = shuffle(password_part_1)
        password_part_2 = shuffle(password_part_2)

        password = password_part_1 + "-" + password_part_2

        print(password)

    def gerar_senha():
        if password_type == "1":
            gerar_senha_letras()
        elif password_type == "2":
            gerar_senha_numeros()
        elif password_type == "3":
            gerar_senha_letras_e_numeros()
        elif password_type == "4":
            gerar_senha_letras_numero_e_simbolos()

    def password_quantity():
        passwords_times = int(input("Certo. Deseja gerar quantas senhas? "))
        print("Gerando senhas....")

        print("Senha(s) gerada(s):")
        for password_time_selected in range(passwords_times):
            gerar_senha()

    print("(1) Apenas letras  /  (2) Apenas números  /  (3) Letras e números  /  (4) Letras números e símbolos")

    password_type = input("Deseja gerar qual dos tipos de senha? ")

    password_quantity()

def after():
    generate_again = (input("Deseja gerar novamente? SIM (1) / NÃO (2)"))
    after_verification = False

    if generate_again == "1":
        index()
        after()
        after_verification = True
    elif generate_again == "2":
        print("Obrigado, até mais!")
        after_verification = True

    if after_verification == False:
        print("Valor inválido")
        after()

index()

after()