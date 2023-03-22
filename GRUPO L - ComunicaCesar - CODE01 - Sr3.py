import sqlite3

banco = sqlite3.connect('GRUPO L - ComunicaCesar - DATABASE01 - Sr3.db')

cursor = banco.cursor()
#cursor.execute("CREATE TABLE alunos(nome text, sobrenome text, email text, senha integer, turma integer, opcao_esta integer, opcao_genero integer, opcao_even integer)")
#cursor.execute("CREATE TABLE professores(nome text, sobrenome text, email text, senha integer)")
#cursor.execute("CREATE TABLE avisos_s(cod_turma integer, aviso text)")
#cursor.execute("CREATE TABLE datas_provas(cod_turma integer, data_prova text)")
#Para criar as tabelas e cadastrar no banco de dados tem que retirar o hashtag da frente das linhas 6,7,8,9 para o programa criar o seu banco de dados e depois de rodar uma vez colocar novamente as hashtag

cargo = 0
opcao_s = 0
opcao_p = 0
opcao_a = 0

while cargo!=-1:
    try:
        print(' ')
        print('-----ComunicaCesar-----')
        print('1 - Secretaria')
        print('2 - Professor')
        print('3 - Aluno')
        print("-1 - Encerrar programa")
        cargo = int(input('Digite o número equivalente a seu cargo na CESAR School: '))
    except ValueError:
        print('Digite o seu cargo usando dígitos entre 1-3 ou -1')
    if cargo==1:
        while opcao_s!=5:
            try:
                print(' ')
                print('-----secretaria-----')
                print("1- Cadastrar aluno(a) ")
                print("2- Cadastrar professor(a) ")
                print('3- Enviar mensagens direcionadas')
                print('4- Enviar mensagens para todas as turmas')
                print('5- Voltar ao Menu')
                opcao_s = int(input('O que você deseja: '))
            except ValueError:
                print('Digite sua escolha usando dígitos entre 1-5')
            if opcao_s == 1:
                print(' ')
                print('---Cadastro de alunos(as)---')
                nome_a = input("Digite o nome: ")
                sobrenome_a = input("Digite o sobrenome: ")
                email_a = input("Digite o e-mail: ")
                senha_a = int(input("Digite uma senha de quatro dígitos: "))
                confirm_senha = int(input("Confirme a senha: "))
                print('Configurações de Gênero')
                print('1- Masculino')
                print('0- Feminino')
                genero = int(input('Digite 1 ou 0: '))
                print("1- cc_2018_1")
                print("2- ds_2018_1")
                print("3- cc_2018_2")
                print("4- ds_2018_2")
                print("5- cc_2019_1")
                print("6- ds_2019_1")
                print("7- cc_2019_2")
                print("8- ds_2019_2")
                print("9- cc_a_2020_1")
                print("10- ds_a_2020_1")
                print("11- cc_b_2020_1")
                print("12- ds_b_2020_1")
                turma_a = int(input("Escolha sua turma: "))
                if turma_a<1 or turma_a>12:
                    print('Turma não existente')
                if senha_a == confirm_senha:
                    cursor.execute("INSERT INTO alunos (nome, sobrenome, email, senha, turma, opcao_esta, opcao_genero, opcao_even) VALUES (?,?,?,?,?,?,?,?)",
                                   (nome_a, sobrenome_a, email_a, senha_a, turma_a, 1, genero, 1))
                    banco.commit()
                    print('Aluno cadastrado com sucesso')

                else:
                    print("Senha está diferente da Senha confirmada")

            elif opcao_s == 2:
                print(' ')
                print('---Cadastro de professores(as)---')
                nome_p = input("Digite o nome: ")
                sobrenome_p = input("Digite o sobrenome: ")
                email_p = input("Digite o e-mail: ")
                senha_p = int(input("Digite a senha: "))
                confirm_senha_p = int(input("Confirme a sua senha: "))
                if senha_p == confirm_senha_p:
                    cursor.execute("INSERT INTO professores (nome, sobrenome, email, senha) VALUES (?,?,?,?)",
                                   (nome_p, sobrenome_p, email_p, senha_p))
                    banco.commit()
                    print('Professor cadastrado com sucesso')
                else:
                    print("Senha está diferente da Senha confirmada")

            elif opcao_s == 3:
                try:
                    print(' ')
                    print('-----Informações Direcionados-----')
                    print('1- Avisos por turmas')
                    print('2- Avisos por curso')
                    print('3- Avisos por gênero')
                    print('4- Avisos de estagio')
                    print('5- Avisos de eventos')
                    opcao_escolha = int(input('O que você deseja: '))
                    if opcao_escolha == 1:
                        try:
                            print(' ')
                            print('-----Avisos por turmas-----')
                            informacao = input('Digite a informação a ser enviada: ')
                            quant_turmas = int(input('Para quantas turmas você deseja enviar: '))
                            print("1- cc_2018_1")
                            print("2- ds_2018_1")
                            print("3- cc_2018_2")
                            print("4- ds_2018_2")
                            print("5- cc_2019_1")
                            print("6- ds_2019_1")
                            print("7- cc_2019_2")
                            print("8- ds_2019_2")
                            print("9- cc_a_2020_1")
                            print("10- ds_a_2020_1")
                            print("11- cc_b_2020_1")
                            print("12- ds_b_2020_1")
                            for envio in range (quant_turmas):
                                turma_inf = int(input("Qual turma deverá receber a informação: "))
                                if turma_inf == 1:
                                    cursor.execute('INSERT INTO avisos_s (cod_turma, aviso) VALUES (?,?)', (1, informacao))
                                    banco.commit()
                                    print('Aviso enviado com sucesso')
                                elif turma_inf == 2:
                                    cursor.execute('INSERT INTO avisos_s (cod_turma, aviso) VALUES (?,?)', (2, informacao))
                                    banco.commit()
                                    print('Aviso enviado com sucesso')
                                elif turma_inf == 3:
                                    cursor.execute('INSERT INTO avisos_s (cod_turma, aviso) VALUES (?,?)', (3, informacao))
                                    banco.commit()
                                    print('Aviso enviado com sucesso')
                                elif turma_inf == 4:
                                    cursor.execute('INSERT INTO avisos_s (cod_turma, aviso) VALUES (?,?)', (4, informacao))
                                    banco.commit()
                                    print('Aviso enviado com sucesso')
                                elif turma_inf == 5:
                                    cursor.execute('INSERT INTO avisos_s (cod_turma, aviso) VALUES (?,?)', (5, informacao))
                                    banco.commit()
                                    print('Aviso enviado com sucesso')
                                elif turma_inf == 6:
                                    cursor.execute('INSERT INTO avisos_s (cod_turma, aviso) VALUES (?,?)', (6, informacao))
                                    banco.commit()
                                    print('Aviso enviado com sucesso')
                                elif turma_inf == 7:
                                    cursor.execute('INSERT INTO avisos_s (cod_turma, aviso) VALUES (?,?)', (7, informacao))
                                    banco.commit()
                                    print('Aviso enviado com sucesso')
                                elif turma_inf == 8:
                                    cursor.execute('INSERT INTO avisos_s (cod_turma, aviso) VALUES (?,?)', (8, informacao))
                                    banco.commit()
                                    print('Aviso enviado com sucesso')
                                elif turma_inf == 9:
                                    cursor.execute('INSERT INTO avisos_s (cod_turma, aviso) VALUES (?,?)', (9, informacao))
                                    banco.commit()
                                    print('Aviso enviado com sucesso')
                                elif turma_inf == 10:
                                    cursor.execute('INSERT INTO avisos_s (cod_turma, aviso) VALUES (?,?)', (10, informacao))
                                    banco.commit()
                                    print('Aviso enviado com sucesso')
                                elif turma_inf == 11:
                                    cursor.execute('INSERT INTO avisos_s (cod_turma, aviso) VALUES (?,?)', (11, informacao))
                                    banco.commit()
                                    print('Aviso enviado com sucesso')
                                elif turma_inf == 12:
                                    cursor.execute('INSERT INTO avisos_s (cod_turma, aviso) VALUES (?,?)', (12, informacao))
                                    banco.commit()
                                    print('Aviso enviado com sucesso')
                        except ValueError:
                            print('Digite a quantidade de turmas usando dígitos entre 1-14 e/ou a informação em forma de texto')
                    elif opcao_escolha == 2:
                        try:
                            print(' ')
                            print('-----Avisos por curso-----')
                            informacao = input('Digite a informação a ser enviada: ')
                            print(' ')
                            print('---Curso---')
                            print('1- Ciências da computação')
                            print('2- Design')
                            curso_inf = int(input("Qual curso deverá receber a informação: "))
                            if curso_inf == 1:
                                cursor.execute('INSERT INTO avisos_s (cod_turma, aviso) VALUES (?,?)', (30, informacao))
                                banco.commit()
                                print('Aviso enviado com sucesso')
                            elif curso_inf == 2:
                                cursor.execute('INSERT INTO avisos_s (cod_turma, aviso) VALUES (?,?)', (31, informacao))
                                banco.commit()
                                print('Aviso enviado com sucesso')
                        except ValueError:
                            print('Digite a opcão de curso usando dígitos entre 1-2 e/ou a informação em forma de texto')

                    elif opcao_escolha == 3:
                        try:
                            print(' ')
                            print('-----Avisos por gênero-----')
                            informacao = input('Digite a informação a ser enviada: ')
                            print(' ')
                            print('---Gênero---')
                            print('1- Masculino')
                            print('2- Feminino')
                            genero_inf = int(input("Qual gênero deverá receber a informação: "))
                            if genero_inf == 1:
                                cursor.execute('INSERT INTO avisos_s (cod_turma, aviso) VALUES (?,?)', (32, informacao))
                                banco.commit()
                                print('Aviso enviado com sucesso')
                            elif genero_inf == 2:
                                cursor.execute('INSERT INTO avisos_s (cod_turma, aviso) VALUES (?,?)', (33, informacao))
                                banco.commit()
                                print('Aviso enviado com sucesso')
                        except ValueError:
                            print('Digite a opcão de curso usando dígitos entre 1-2 e/ou a informação em forma de texto')


                    elif opcao_escolha == 4:
                        try:
                            print(' ')
                            print('---Notícia(s) de estágio---')
                            informacao = input('Digite a informação a ser enviada: ')
                            cursor.execute('INSERT INTO avisos_s (cod_turma, aviso) VALUES (?,?)', (34, informacao))
                            banco.commit()
                            print('Aviso enviado com sucesso')
                        except ValueError:
                            print('Digite a informação em forma de texto')

                    elif opcao_escolha == 5:
                        try:
                            print(' ')
                            print('---Notícia(s) de evento(s)---')
                            informacao = input('Digite a informação a ser enviada: ')
                            cursor.execute('INSERT INTO avisos_s (cod_turma, aviso) VALUES (?,?)', (35, informacao))
                            banco.commit()
                            print('Aviso enviado com sucesso')
                        except ValueError:
                            print('Digite a informação em forma de texto')
                except ValueError:
                    print('Digite a opção desejada usando dígitos entre 1-5')

            elif opcao_s == 4:
                print(' ')
                print('-----Informações Gerais-----')
                informacao_g = input('Digite a informação a ser enviada: ')
                cursor.execute('INSERT INTO avisos_s (cod_turma, aviso) VALUES (?,?)', (100, informacao_g))
                banco.commit()
                print('Aviso enviado com sucesso')


            elif opcao_s > 5 or opcao_s == 0:
                print('Função não indentificada')

        opcao_s = 0

    elif cargo == 2:
        sql_prof = 'SELECT * FROM professores WHERE email = ? and senha = ?'
        print(' ')
        print('-----Log in Professor(a)-----')
        email_log = input("Digite o seu e-mail: ")
        senha_log = int(input("Digite uma senha de quatro dígitos: "))
        def login_prof(WordUsed):
            for row in cursor.execute(sql_prof, (email_log, senha_log)):
                chave_pf = 10
                return chave_pf
        key_master = login_prof(email_log)
        if key_master == 10:
            while opcao_p != 5:
                try:
                    print(' ')
                    print('-----Professor(a)-----')
                    print('1- Visualizar seu Perfil')
                    print('2- Enviar mensagens direcionadas')
                    print('3- Enviar mensagens para todas as Turmas')
                    print('4- Enviar a data da prova para determinada(s) turma(s)')
                    print('5- Voltar ao Menu')
                    opcao_p = int(input('O que você deseja: '))
                except ValueError:
                    print('Digite sua escolha usando dígitos entre 1-5')

                if opcao_p == 1:
                    def perfil_professor(WordUsed):
                        for row in cursor.execute(sql_prof, (email_log, senha_log)):
                            print(' ')
                            print('-----Perfil Professor(a)-----')
                            print('Nome: ', row[0])
                            print('Sobrenome: ', row[1])
                            print('E-mail: ', row[2])
                            print('Senha: ', row[3])
                    perfil_professor(email_log)
                elif opcao_p == 2:
                    try:
                        print(' ')
                        print('-----Informações Direcionados-----')
                        print('1- avisos por turmas')
                        print('2- avisos por curso')
                        print('3- avisos por gênero')
                        print('4- avisos de estagio')
                        print('5- avisos de eventos')
                        opcao_escolha = int(input('O que você deseja: '))
                        if opcao_escolha == 1:
                            try:
                                informacao = input('Digite a informação a ser enviada: ')
                                quant_turmas = int(input('Para quantas turmas você deseja enviar: '))
                                print("1- cc_2018_1")
                                print("2- ds_2018_1")
                                print("3- cc_2018_2")
                                print("4- ds_2018_2")
                                print("5- cc_2019_1")
                                print("6- ds_2019_1")
                                print("7- cc_2019_2")
                                print("8- ds_2019_2")
                                print("9- cc_a_2020_1")
                                print("10- ds_a_2020_1")
                                print("11- cc_b_2020_1")
                                print("12- ds_b_2020_1")
                            except ValueError:
                                print('Digite a quantidade de turmas usando dígitos entre 1-14 e/ou a informação em forma de texto')
                                for envio in range(quant_turmas):
                                    turma_inf = int(input("Qual turma deverá receber a informação: "))
                                    if turma_inf == 1:
                                        cursor.execute('INSERT INTO avisos_s (cod_turma, aviso) VALUES (?,?)',
                                                       (1, informacao))
                                        banco.commit()
                                        print('Aviso enviado com sucesso')
                                    elif turma_inf == 2:
                                        cursor.execute('INSERT INTO avisos_s (cod_turma, aviso) VALUES (?,?)',
                                                       (2, informacao))
                                        banco.commit()
                                        print('Aviso enviado com sucesso')
                                    elif turma_inf == 3:
                                        cursor.execute('INSERT INTO avisos_s (cod_turma, aviso) VALUES (?,?)',
                                                       (3, informacao))
                                        banco.commit()
                                        print('Aviso enviado com sucesso')
                                    elif turma_inf == 4:
                                        cursor.execute('INSERT INTO avisos_s (cod_turma, aviso) VALUES (?,?)',
                                                       (4, informacao))
                                        banco.commit()
                                        print('Aviso enviado com sucesso')
                                    elif turma_inf == 5:
                                        cursor.execute('INSERT INTO avisos_s (cod_turma, aviso) VALUES (?,?)',
                                                       (5, informacao))
                                        banco.commit()
                                        print('Aviso enviado com sucesso')
                                    elif turma_inf == 6:
                                        cursor.execute('INSERT INTO avisos_s (cod_turma, aviso) VALUES (?,?)',
                                                       (6, informacao))
                                        banco.commit()
                                        print('Aviso enviado com sucesso')
                                    elif turma_inf == 7:
                                        cursor.execute('INSERT INTO avisos_s (cod_turma, aviso) VALUES (?,?)',
                                                       (7, informacao))
                                        banco.commit()
                                        print('Aviso enviado com sucesso')
                                    elif turma_inf == 8:
                                        cursor.execute('INSERT INTO avisos_s (cod_turma, aviso) VALUES (?,?)',
                                                       (8, informacao))
                                        banco.commit()
                                        print('Aviso enviado com sucesso')
                                    elif turma_inf == 9:
                                        cursor.execute('INSERT INTO avisos_s (cod_turma, aviso) VALUES (?,?)',
                                                       (9, informacao))
                                        banco.commit()
                                        print('Aviso enviado com sucesso')
                                    elif turma_inf == 10:
                                        cursor.execute('INSERT INTO avisos_s (cod_turma, aviso) VALUES (?,?)',
                                                       (10, informacao))
                                        banco.commit()
                                        print('Aviso enviado com sucesso')
                                    elif turma_inf == 11:
                                        cursor.execute('INSERT INTO avisos_s (cod_turma, aviso) VALUES (?,?)',
                                                       (11, informacao))
                                        banco.commit()
                                        print('Aviso enviado com sucesso')
                                    elif turma_inf == 12:
                                        cursor.execute('INSERT INTO avisos_s (cod_turma, aviso) VALUES (?,?)',
                                                       (12, informacao))
                                        banco.commit()
                                        print('Aviso enviado com sucesso')
                        elif opcao_escolha == 2:
                            try:
                                informacao = input('Digite a informação a ser enviada: ')
                                print(' ')
                                print('---Curso---')
                                print('1- Ciências da computação')
                                print('2- Design')
                                curso_inf = int(input("Qual curso deverá receber a informação: "))
                                if curso_inf == 1:
                                    cursor.execute('INSERT INTO avisos_s (cod_turma, aviso) VALUES (?,?)',
                                                   (30, informacao))
                                    banco.commit()
                                    print('Aviso enviado com sucesso')
                                elif curso_inf == 2:
                                    cursor.execute('INSERT INTO avisos_s (cod_turma, aviso) VALUES (?,?)',
                                                   (31, informacao))
                                    banco.commit()
                                    print('Aviso enviado com sucesso')
                            except ValueError:
                                print('Digite a opcão de curso usando dígitos entre 1-2 e/ou a informação em forma de texto')

                        elif opcao_escolha == 3:
                            try:
                                informacao = input('Digite a informação a ser enviada: ')
                                print(' ')
                                print('---Gênero---')
                                print('1- Masculino')
                                print('2- Feminino')
                                genero_inf = int(input("Qual gênero deverá receber a informação: "))
                                if genero_inf == 1:
                                    cursor.execute('INSERT INTO avisos_s (cod_turma, aviso) VALUES (?,?)',
                                                   (32, informacao))
                                    banco.commit()
                                    print('Aviso enviado com sucesso')
                                elif genero_inf == 2:
                                    cursor.execute('INSERT INTO avisos_s (cod_turma, aviso) VALUES (?,?)',
                                                   (33, informacao))
                                    banco.commit()
                                    print('Aviso enviado com sucesso')
                            except ValueError:
                                print(
                                    'Digite a opcão de curso usando dígitos entre 1-2 e/ou a informação em forma de texto')


                        elif opcao_escolha == 4:
                            try:
                                print(' ')
                                print('---Notícia(s) de estágio---')
                                informacao = input('Digite a informação a ser enviada: ')
                                cursor.execute('INSERT INTO avisos_s (cod_turma, aviso) VALUES (?,?)', (34, informacao))
                                banco.commit()
                                print('Aviso enviado com sucesso')
                            except ValueError:
                                print('Digite a informação em forma de texto')

                        elif opcao_escolha == 5:
                            try:
                                print(' ')
                                print('---Notícia(s) de evento(s)---')
                                informacao = input('Digite a informação a ser enviada: ')
                                cursor.execute('INSERT INTO avisos_s (cod_turma, aviso) VALUES (?,?)', (35, informacao))
                                banco.commit()
                                print('Aviso enviado com sucesso')
                            except ValueError:
                                print('Digite a informação em forma de texto')
                    except ValueError:
                        print('Digite a opção desejada usando dígitos entre 1-5')

                elif opcao_p == 3:
                    print(' ')
                    print('-----Informações Gerais-----')
                    informacao_g = input('Digite a informação a ser enviada: ')
                    cursor.execute('INSERT INTO avisos_s (cod_turma, aviso) VALUES (?,?)', (100, informacao_g))
                    banco.commit()
                    print('Aviso enviado com sucesso')

                elif opcao_p == 4:
                    try:
                        print(' ')
                        print('-----Data de Prova-----')
                        data_prova = str(input('Qual a data de sua prova, digite da seguinte forma "20/05": '))
                        quant_t_prova = int(input('Para quantas turmas você deseja enviar: '))
                        print("1- cc_2018_1")
                        print("2- ds_2018_1")
                        print("3- cc_2018_2")
                        print("4- ds_2018_2")
                        print("5- cc_2019_1")
                        print("6- ds_2019_1")
                        print("7- cc_2019_2")
                        print("8- ds_2019_2")
                        print("9- cc_a_2020_1")
                        print("10- ds_a_2020_1")
                        print("11- cc_b_2020_1")
                        print("12- ds_b_2020_1")
                    except ValueError:
                        print(
                            'Digite a quantidade de turmas usando dígitos entre 1-14 e/ou a informação em forma de texto')
                    for envio in range(quant_t_prova):
                        turma_inf = int(input("Qual turma deverá receber a informação: "))
                        if turma_inf == 1:
                            cursor.execute('INSERT INTO datas_provas (cod_turma, data_prova) VALUES (?,?)', (1, data_prova))
                            banco.commit()
                            print('Aviso enviado com sucesso')
                        elif turma_inf == 2:
                            cursor.execute('INSERT INTO datas_provas (cod_turma, data_prova) VALUES (?,?)', (2, data_prova))
                            banco.commit()
                            print('Aviso enviado com sucesso')
                        elif turma_inf == 3:
                            cursor.execute('INSERT INTO datas_provas (cod_turma, data_prova) VALUES (?,?)', (3,data_prova))
                            banco.commit()
                            print('Aviso enviado com sucesso')
                        elif turma_inf == 4:
                            cursor.execute('INSERT INTO dt_provas (cod_turma, data_prova) VALUES (?,?)', (4, data_prova))
                            banco.commit()
                            print('Aviso enviado com sucesso')
                        elif turma_inf == 5:
                            cursor.execute('INSERT INTO datas_provas (cod_turma, data_prova) VALUES (?,?)', (5, data_prova))
                            banco.commit()
                            print('Aviso enviado com sucesso')
                        elif turma_inf == 6:
                            cursor.execute('INSERT INTO datas_provas (cod_turma, data_prova) VALUES (?,?)', (6, data_prova))
                            banco.commit()
                            print('Aviso enviado com sucesso')
                        elif turma_inf == 7:
                            cursor.execute('INSERT INTO datas_provas (cod_turma, data_prova) VALUES (?,?)', (7, data_prova))
                            banco.commit()
                            print('Aviso enviado com sucesso')
                        elif turma_inf == 8:
                            cursor.execute('INSERT INTO datas_provas (cod_turma, data_prova) VALUES (?,?)', (8, data_prova))
                            banco.commit()
                            print('Aviso enviado com sucesso')
                        elif turma_inf == 9:
                            cursor.execute('INSERT INTO datas_provas (cod_turma, data_prova) VALUES (?,?)', (9, data_prova))
                            banco.commit()
                            print('Aviso enviado com sucesso')
                        elif turma_inf == 10:
                            cursor.execute('INSERT INTO datas_provas (cod_turma, data_prova) VALUES (?,?)', (10, data_prova))
                            banco.commit()
                            print('Aviso enviado com sucesso')
                        elif turma_inf == 11:
                            cursor.execute('INSERT INTO datas_provas (cod_turma, data_prova) VALUES (?,?)', (11, data_prova))
                            banco.commit()
                            print('Aviso enviado com sucesso')
                        elif turma_inf == 12:
                            cursor.execute('INSERT INTO datas_provas (cod_turma, data_prova) VALUES (?,?)', (12, data_prova))
                            banco.commit()
                            print('Aviso enviado com sucesso')
                elif opcao_p > 5 or opcao_p == 0:
                    print('Função não indentificada')

            opcao_p = 0
        elif key_master != 10:
            print('E-mail ou Senha digitados estão incorretos')

    elif cargo == 3:
        sql_aluno = 'SELECT * FROM alunos WHERE email = ? and senha = ?'
        print(' ')
        print('-----Log in Aluno(a)-----')
        email_log = input("Digite o seu e-mail: ")
        senha_log = int(input("Digite uma senha de quatro dígitos: "))
        def login_alunos(WordUsed):
            for row in cursor.execute(sql_aluno, (email_log, senha_log)):
                key_master = 10
                return key_master
        key_master = login_alunos(email_log)
        if key_master == 10:
            while opcao_a != 6:
                try:
                    print(' ')
                    print('-----Aluno(a)-----')
                    print('1- Ver Perfil')
                    print('2- Visualizar seus avisos')
                    print('3- Visualizar Avisos Gerais')
                    print('4- Visualizar Data de Provas')
                    print('5- Editar Configurações de preferências')
                    print('6- Voltar ao Menu')
                    opcao_a = int(input("O que você deseja: "))
                except ValueError:
                    print('Digite sua escolha usando dígitos entre 1-5')

                if opcao_a == 1:
                    def perfil_aluno(WordUsed):
                        for row in cursor.execute(sql_aluno, (email_log,senha_log)):
                            print(' ')
                            print('-----Perfil Aluno(a)-----')
                            print('Nome: ', row[0])
                            print('Sobrenome: ', row[1])
                            print('E-mail: ', row[2])
                            print('Senha: ', row[3])
                            if row[4] == 1:
                                print("Turma: cc_2018_1")
                            elif row[4] == 2:
                                print("Turma: ds_2018_1")
                            elif row[4] == 3:
                                print("Turma: cc_2018_2")
                            elif row[4] == 4:
                                print("Turma: ds_2018_2")
                            elif row[4] == 5:
                                print("Turma: cc_2019_1")
                            elif row[4] == 6:
                                print("Turma: ds_2019_1")
                            elif row[4] == 7:
                                print("Turma: cc_2019_2")
                            elif row[4] == 8:
                                print("Turma: ds_2019_2")
                            elif row[4] == 9:
                                print("Turma: cc_a_2020_1")
                            elif row[4] == 10:
                                print("Turma: ds_a_2020_1")
                            elif row[4] == 11:
                                print("Turma: cc_b_2020_1")
                            elif row[4] == 12:
                                print("Turma: ds_b_2020_1")

                            if row[5] == 1:
                                print("Notîcias estãgio: Sim")
                            elif row[5] == 0:
                                print("Notîcias estãgio: Não")

                            if row[6] == 1:
                                print('Gênero: Masculino')
                            elif row[6] == 0:
                                print('Gênero: Feminino')

                            if row[5] == 1:
                                print("Notîcias evento: Sim")
                            elif row[5] == 0:
                                print("Notîcias evento: Não")



                    perfil_aluno(email_log)

                elif opcao_a == 2:
                    print(' ')
                    print('-----Seus avisos-----')
                    def avisos_turma():
                        for row in cursor.execute(sql_aluno, (email_log, senha_log)):
                            if row[4] == 1:
                                sql_av = 'SELECT * FROM avisos_s WHERE cod_turma = 1'
                                def aviso():
                                    for row in cursor.execute(sql_av):
                                        print(row[1])
                                aviso()
                            elif row[4] == 2:
                                sql_av = 'SELECT * FROM avisos_s WHERE cod_turma = 2'
                                def aviso():
                                    for row in cursor.execute(sql_av):
                                        print(row[1])
                                aviso()
                            elif row[4] == 3:
                                sql_av = 'SELECT * FROM avisos_s WHERE cod_turma = 3'
                                def aviso():
                                    for row in cursor.execute(sql_av):
                                        print(row[1])
                                aviso()
                            elif row[4] == 4:
                                sql_av = 'SELECT * FROM avisos_s WHERE cod_turma = 4'
                                def aviso():
                                    for row in cursor.execute(sql_av):
                                        print(row[1])
                                aviso()
                            elif row[4] == 5:
                                sql_av = 'SELECT * FROM avisos_s WHERE cod_turma = 5'
                                def aviso():
                                    for row in cursor.execute(sql_av):
                                        print(row[1])
                                aviso()
                            elif row[4] == 6:
                                sql_av = 'SELECT * FROM avisos_s WHERE cod_turma = 6'
                                def aviso():
                                    for row in cursor.execute(sql_av):
                                        print(row[1])
                                aviso()
                            elif row[4] == 7:
                                sql_av = 'SELECT * FROM avisos_s WHERE cod_turma = 7'
                                def aviso():
                                    for row in cursor.execute(sql_av):
                                        print(row[1])
                                aviso()
                            elif row[4] == 8:
                                sql_av = 'SELECT * FROM avisos_s WHERE cod_turma = 8'
                                def aviso():
                                    for row in cursor.execute(sql_av):
                                        print(row[1])
                                aviso()
                            elif row[4] == 9:
                                sql_av = 'SELECT * FROM avisos_s WHERE cod_turma = 9'
                                def aviso():
                                    for row in cursor.execute(sql_av):
                                        print(row[1])
                                aviso()
                            elif row[4] == 10:
                                sql_av = 'SELECT * FROM avisos_s WHERE cod_turma = 10'
                                def aviso():
                                    for row in cursor.execute(sql_av):
                                        print(row[1])
                                aviso()
                            elif row[4] == 11:
                                sql_av = 'SELECT * FROM avisos_s WHERE cod_turma = 11'
                                def aviso():
                                    for row in cursor.execute(sql_av):
                                        print(row[1])
                                aviso()
                            elif row[4] == 12:
                                sql_av = 'SELECT * FROM avisos_s WHERE cod_turma = 12'
                                def aviso():
                                    for row in cursor.execute(sql_av):
                                        print(row[1])
                                aviso()

                            if row[5] == 1:
                                sql_av = 'SELECT * FROM avisos_s WHERE cod_turma = 34'
                                def aviso():
                                    for row in cursor.execute(sql_av):
                                        print(row[1])
                                aviso()

                            if row[6] == 1:
                                sql_av = 'SELECT * FROM avisos_s WHERE cod_turma = 32'
                                def aviso():
                                    for row in cursor.execute(sql_av):
                                        print(row[1])
                                aviso()

                            elif row[6] == 0:
                                sql_av = 'SELECT * FROM avisos_s WHERE cod_turma = 33'
                                def aviso():
                                    for row in cursor.execute(sql_av):
                                        print(row[1])
                                aviso()

                            if row[7] == 1:
                                sql_av = 'SELECT * FROM avisos_s WHERE cod_turma = 35'
                                def aviso():
                                    for row in cursor.execute(sql_av):
                                        print(row[1])
                                aviso()

                            if row[4]%2 != 0:
                                sql_av = 'SELECT * FROM avisos_s WHERE cod_turma = 30'
                                def aviso():
                                    for row in cursor.execute(sql_av):
                                        print(row[1])
                                aviso()

                            if row[4]%2 == 0:
                                sql_av = 'SELECT * FROM avisos_s WHERE cod_turma = 31'
                                def aviso():
                                    for row in cursor.execute(sql_av):
                                        print(row[1])
                                aviso()


                    avisos_turma()

                elif opcao_a == 3:
                    print(' ')
                    print('-----Avisos Gerais-----')


                    def avisos_turma():
                        for row in cursor.execute(sql_aluno, (email_log, senha_log)):
                            sql_dt_prov = 'SELECT * FROM avisos_s WHERE cod_turma = 100'
                            def dt_prv():
                                for row in cursor.execute(sql_dt_prov):
                                    print(row[1])
                            dt_prv()
                    avisos_turma()


                elif opcao_a == 4:
                    print(' ')
                    print('-----Data(s) de Prova(s)-----')
                    def avisos_turma():
                        for row in cursor.execute(sql_aluno, (email_log, senha_log)):
                            if row[4] == 1:
                                sql_dt_prov = 'SELECT * FROM datas_provas WHERE cod_turma = 1'
                                def dt_prv():
                                    for row in cursor.execute(sql_dt_prov):
                                        print(row[1])
                                dt_prv()
                            elif row[4] == 2:
                                sql_dt_prov = 'SELECT * FROM datas_provas WHERE cod_turma = 2'
                                def dt_prv():
                                    for row in cursor.execute(sql_dt_prov):
                                        print(row[1])
                                dt_prv()
                            elif row[4] == 3:
                                sql_dt_prov = 'SELECT * FROM datas_provas WHERE cod_turma = 3'
                                def dt_prv():
                                    for row in cursor.execute(sql_dt_prov):
                                        print(row[1])
                                dt_prv()
                            elif row[4] == 4:
                                sql_dt_prov = 'SELECT * FROM datas_provas WHERE cod_turma = 4'
                                def dt_prv():
                                    for row in cursor.execute(sql_dt_prov):
                                        print(row[1])
                                dt_prv()
                            elif row[4] == 5:
                                sql_dt_prov = 'SELECT * FROM datas_provas WHERE cod_turma = 5'
                                def dt_prv():
                                    for row in cursor.execute(sql_dt_prov):
                                        print(row[1])
                                dt_prv()
                            elif row[4] == 6:
                                sql_dt_prov = 'SELECT * FROM datas_provas WHERE cod_turma = 6'
                                def dt_prv():
                                    for row in cursor.execute(sql_dt_prov):
                                        print(row[1])
                                dt_prv()
                            elif row[4] == 7:
                                sql_dt_prov = 'SELECT * FROM datas_provas WHERE cod_turma = 7'
                                def dt_prv():
                                    for row in cursor.execute(sql_dt_prov):
                                        print(row[1])
                                dt_prv()
                            elif row[4] == 8:
                                sql_dt_prov = 'SELECT * FROM datas_provas WHERE cod_turma = 8'
                                def dt_prv():
                                    for row in cursor.execute(sql_dt_prov):
                                        print(row[1])
                                dt_prv()
                            elif row[4] == 9:
                                sql_dt_prov = 'SELECT * FROM datas_provas WHERE cod_turma = 9'
                                def dt_prv():
                                    for row in cursor.execute(sql_dt_prov):
                                        print(row[1])
                                dt_prv()
                            elif row[4] == 10:
                                sql_dt_prov = 'SELECT * FROM datas_provas WHERE cod_turma = 10'
                                def dt_prv():
                                    for row in cursor.execute(sql_dt_prov):
                                        print(row[1])
                                dt_prv()
                            elif row[4] == 11:
                                sql_dt_prov = 'SELECT * FROM datas_provas WHERE cod_turma = 11'
                                def dt_prv():
                                    for row in cursor.execute(sql_dt_prov):
                                        print(row[1])
                                dt_prv()
                            elif row[4] == 12:
                                sql_dt_prov = 'SELECT * FROM datas_provas WHERE cod_turma = 12'
                                def dt_prv():
                                    for row in cursor.execute(sql_dt_prov):
                                        print(row[1])
                                dt_prv()
                    avisos_turma()

                elif opcao_a == 5:
                    def perfil_aluno():
                        for row in cursor.execute(sql_aluno, (email_log, senha_log)):
                            print(' ')
                            print('-----Opções de editar-----')
                            print('1- Editar opção de estágio')
                            print('2- Editar opção de eventos')
                            edit_pref = int(input('Digite a sua escolha para de editar: '))
                            if edit_pref == 1:
                                print(' ')
                                print('-----Preferências de Notîcias de estágio-----')
                                if row[5] == 1:
                                    print("Sua preferências atual de Notîcias estãgio: Sim")
                                elif row[5] == 0:
                                    print("Sua preferências atual de Notîcias estãgio: Não")
                                nova_op_edit = int(input('Digite sua nova preferência 1-Sim ou 0-Não: '))
                                def db_update(opcao_esta, email):
                                    return """
                                    UPDATE alunos SET opcao_esta = '{}' WHERE email = '{}'
                                    """.format(opcao_esta, email)
                                cursor.execute(db_update(nova_op_edit, row[2]))
                                banco.commit()
                                print('Edição concluída com sucesso!!!')

                            if edit_pref == 2:
                                print(' ')
                                print('-----Preferências de Notîcias de eventos-----')
                                if row[7] == 1:
                                    print("Sua preferências atual de Notîcias de eventos: Sim")
                                elif row[7] == 0:
                                    print("Sua preferências atual de Notîcias de eventos: Não")
                                nova_op_edit = int(input('Digite sua nova preferência 1-Sim ou 0-Não: '))
                                def db_update(opcao_even, email):
                                    return """
                                    UPDATE alunos SET opcao_even = '{}' WHERE email = '{}'
                                    """.format(opcao_even, email)
                                cursor.execute(db_update(nova_op_edit, row[2]))
                                banco.commit()
                                print('Edição concluída com sucesso!!!')


                    perfil_aluno()

                elif opcao_a > 6 or opcao_a == 0:
                    print('Função não indentificada')
            opcao_a = 0



        elif key_master != 10:
            print('E-mail ou Senha digitados estão incorretos')
