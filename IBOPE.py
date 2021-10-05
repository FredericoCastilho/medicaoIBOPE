print("-------------")
print("|   IBOPE   |")
print("-------------")
ponto_pnt=int(716007)
ponto_grande_sp=int(205377)
ponto_grande_rj=int(125721)
ponto_grande_bh=int(55610)
ponto_grande_portoAlegre=int(40332)
ponto_grande_recife=int(37569)
ponto_grande_salvador=int(36627)
ponto_grande_fortaleza=int(36088)
ponto_grande_curitiba=int(32449)
ponto_distrito_federal=int(27337)
ponto_grande_goiania=int(24317)
ponto_grande_belem=int(23001)
ponto_grande_campinas=int(22289)
ponto_grande_manaus=int(19774)
ponto_grande_vitoria=int(18578)
ponto_grande_floripa=int(10936)
tot_pessoas_pnt=int(0)
lista_regiao=[]
regiao=["PAINEL NACIONAL DE TELEVISÃO",
        "SÃO PAULO",
        "RIO DE JANEIRO",
        "BELO HORIZONTE",
        "PORTO ALEGRE",
        "RECIFE",
        "SALVADOR",
        "FORTALEZA",
        "CURITIBA",
        "DISTRITO FEDERAL",
        "GOIÂNIA",
        "BELÉM",
        "CAMPINAS",
        "MANAUS",
        "VITÓRIA",
        "FLORIANÓPOLIS"]
resp=str("N")
resp_menu_audiencia=int(0)

while (resp=="N"):
    while ((resp_menu_audiencia!=1) or (resp_menu_audiencia!=2)):
        print("""MENU CADASTRO DE AUDIÊNCIA
[ 1 ] AUDIÊNCIA NACIONAL(PNT)
[ 2 ] AUDIÊNCIA DE UMA REGIÃO METROPOLINATA
[ 3 ] AUDIÊNCIA DE TODAS AS 15 REGIÕES METROPOLITANAS
[ 4 ] SAIR""")
        resp_menu_audiencia = int(input("QUAL A ESCOLHA?"))
        if resp_menu_audiencia==1:
            nome_programa=str(input("NOME DA ATRAÇÃO:")).strip()
            nome_programa=nome_programa.upper()
            tot_pontos_pnt=int((input("DIGITE OS PONTOS DA AUDIÊNCIA NACIONAL(PNT) DA ATRAÇÃO:")))
            tot_pessoas_pnt = tot_pontos_pnt*ponto_pnt
            print("-=" * 20)
            print("""
            ATRAÇÃO:{}
            PAINEL NACIONAL DE TELEVISÃO
            AUDIÊNCIA:{} PONTOS 
            UM(1) PONTO NO PNT EQUIVALE:{} PESSOAS
            """.format(nome_programa, tot_pontos_pnt, ponto_pnt))
            print("O TOTAL DE PESSOAS QUE ASSITIRAM A ATRAÇÃO {} NO PNT FOI DE {}\n".format(nome_programa, tot_pessoas_pnt))
            print("-=" * 20)

        elif resp_menu_audiencia==2:
            print("CADASTRANDO AUDIÊNCIA POR REGIÃO...")
            nome_programa = str(input("NOME DA ATRAÇÃO:")).strip()
            nome_programa=nome_programa.upper()
            print("""ESCOLHA A REGIÃO METROPOLITANA:
            [ 1 ] SÃO PAULO
            [ 2 ] RIO DE JANEIRO
            [ 3 ] BELO HORIZONTE
            [ 4 ] PORTO ALEGRE
            [ 5 ] RECIFE
            [ 6 ] SALVADOR
            [ 7 ] FORTALEZA
            [ 8 ] CURITIBA
            [ 9 ] DISTRITO FEDERAL
            [ 10] GOIÂNIA
            [ 11] BELÉM
            [ 12] CAMPINAS
            [ 13] MANAUS
            [ 14] VITÓRIA
            [ 15] FLORIANÓPOLIS
            """)
            escolha_regiao=int(input("QUAL A OPÇÃO?"))

            if (escolha_regiao==1):
                nome_regiao=str("SÃO PAULO")
                tot_pontos_sp=int(input("DIGITE A AUDIÊNCIA EM PONTOS DA ATRAÇÃO {}:".format(nome_programa)))
                tot_pessoas_sp=(tot_pontos_sp*ponto_grande_sp)
                print("-="*20)
                print("""
                ATRAÇÃO:{}
                REGIÃO METROPOLITANA:{}
                AUDIÊNCIA:{} PONTOS 
                UM(1) PONTO EQUIVALE:{} PESSOAS
                """.format(nome_programa, nome_regiao, tot_pontos_sp, ponto_grande_sp))
                print("O TOTAL DE PESSOAS QUE ASSITIRAM A ATRAÇÃO {} EM {} FOI DE {} PESSOAS".format(nome_programa, nome_regiao, tot_pessoas_sp))
                print("-=" * 20)
            elif (escolha_regiao==2):
                nome_regiao=str("RIO DE JANEIRO")
                tot_pontos_rj = int(input("DIGITE A AUDIÊNCIA EM PONTOS DA ATRAÇÃO {}:".format(nome_programa)))
                tot_pessoas_rj=(tot_pontos_rj*ponto_grande_rj)
                print("-=" * 20)
                print("""
                ATRAÇÃO:{}
                REGIÃO METROPOLITANA:{}
                AUDIÊNCIA:{} PONTOS 
                UM(1) PONTO EQUIVALE:{} PESSOAS
                """.format(nome_programa, nome_regiao, tot_pontos_rj, ponto_grande_rj))
                print("O TOTAL DE PESSOAS QUE ASSITIRAM A ATRAÇÃO {} EM {} FOI DE {} PESSOAS".format(nome_programa, nome_regiao, tot_pessoas_rj))
                print("-=" * 20)
            elif (escolha_regiao==3):
                nome_regiao=str("BELO HORIZONTE")
                tot_pontos_bh = int(input("DIGITE A AUDIÊNCIA EM PONTOS DA ATRAÇÃO {}:".format(nome_programa)))
                tot_pessoas_bh=(tot_pontos_bh*ponto_grande_bh)
                print("-=" * 20)
                print("""
                ATRAÇÃO:{}
                REGIÃO METROPOLITANA:{}
                AUDIÊNCIA:{} PONTOS 
                UM(1) PONTO EQUIVALE:{} PESSOAS
                """.format(nome_programa, nome_regiao, tot_pontos_bh, ponto_grande_bh))
                print("O TOTAL DE PESSOAS QUE ASSITIRAM A ATRAÇÃO {} EM {} FOI DE {} PESSOAS".format(nome_programa, nome_regiao, tot_pessoas_bh))
                print("-=" * 20)
            elif (escolha_regiao==4):
                nome_regiao=str("PORTO ALEGRE")
                tot_pontos_portoalegre = int(input("DIGITE A AUDIÊNCIA EM PONTOS DA ATRAÇÃO {}:".format(nome_programa)))
                tot_pessoas_portoalegre=(tot_pontos_portoalegre*ponto_grande_portoAlegre)
                print("-=" * 20)
                print("""
                ATRAÇÃO:{}
                REGIÃO METROPOLITANA:{}
                AUDIÊNCIA:{} PONTOS 
                UM(1) PONTO EQUIVALE:{} PESSOAS
                """.format(nome_programa, nome_regiao, tot_pontos_portoalegre, ponto_grande_portoAlegre))
                print("O TOTAL DE PESSOAS QUE ASSITIRAM A ATRAÇÃO  EM {} FOI DE {} PESSOAS".format(nome_programa, nome_regiao, tot_pessoas_portoalegre))
                print("-=" * 20)
            elif (escolha_regiao==5):
                nome_regiao=str("RECIFE")
                tot_pontos_recife = int(input("DIGITE A AUDIÊNCIA EM PONTOS DA ATRAÇÃO {}:".format(nome_programa)))
                tot_pessoas_recife=(tot_pontos_recife*ponto_grande_recife)
                print("-=" * 20)
                print("""
                ATRAÇÃO:{}
                REGIÃO METROPOLITANA:{}
                AUDIÊNCIA:{} PONTOS 
                UM(1) PONTO EQUIVALE:{} PESSOAS
                """.format(nome_programa, nome_regiao, tot_pontos_recife, ponto_grande_recife))
                print("O TOTAL DE PESSOAS QUE ASSITIRAM A ATRAÇÃO  EM {} FOI DE {} PESSOAS".format(nome_programa, nome_regiao, tot_pessoas_recife))
                print("-=" * 20)
            elif (escolha_regiao==6):
                nome_regiao=str("SALVADOR")
                tot_pontos_salvador = int(input("DIGITE A AUDIÊNCIA EM PONTOS DO PROGRAMA {}:".format(nome_programa)))
                tot_pessoas_salvador=(tot_pontos_salvador*ponto_grande_salvador)
                print("-=" * 20)
                print("""
                ATRAÇÃO:{}
                REGIÃO METROPOLITANA:{}
                AUDIÊNCIA:{} PONTOS 
                UM(1) PONTO EQUIVALE:{} PESSOAS
                """.format(nome_programa, nome_regiao, tot_pontos_salvador, ponto_grande_salvador))
                print("O TOTAL DE PESSOAS QUE ASSITIRAM A ATRAÇÃO {} EM {} FOI DE {} PESSOAS".format(nome_programa, nome_regiao, tot_pessoas_salvador))
                print("-=" * 20)
            elif (escolha_regiao==7):
                nome_regiao=str("FORTALEZA")
                tot_pontos_fortaleza = int(input("DIGITE A AUDIÊNCIA EM PONTOS DO PROGRAMA {}:".format(nome_programa)))
                tot_pessoas_fortaleza=(tot_pontos_fortaleza*ponto_grande_fortaleza)
                print("-=" * 20)
                print("""
                ATRAÇÃO:{}
                REGIÃO METROPOLITANA:{}
                AUDIÊNCIA:{} PONTOS 
                UM(1) PONTO EQUIVALE:{} PESSOAS
                """.format(nome_programa, nome_regiao, tot_pontos_fortaleza, ponto_grande_fortaleza))
                print("O TOTAL DE PESSOAS QUE ASSITIRAM A ATRAÇÃO {} EM {}  DE {} PESSOAS".format(nome_programa, nome_regiao, tot_pessoas_fortaleza))
                print("-=" * 20)
            elif (escolha_regiao==8):
                nome_regiao=str("CURITIBA")
                tot_pontos_curitiba = int(input("DIGITE A AUDIÊNCIA EM PONTOS DO PROGRAMA {}:".format(nome_programa)))
                tot_pessoas_curitiba=(tot_pontos_curitiba*ponto_grande_curitiba)
                print("-=" * 20)
                print("""
                ATRAÇÃO:{}
                REGIÃO METROPOLITANA:{}
                AUDIÊNCIA:{} PONTOS 
                UM(1) PONTO EQUIVALE:{} PESSOAS
                """.format(nome_programa, nome_regiao, tot_pontos_curitiba, ponto_grande_curitiba))
                print("O TOTAL DE PESSOAS QUE ASSITIRAM A ATRAÇÃO {} EM {} FOI DE {} PESSOAS".format(nome_programa, nome_regiao, tot_pessoas_curitiba))
                print("-=" * 20)
            elif (escolha_regiao==9):
                nome_regiao=str("DISTRITO FEDERAL")
                tot_pontos_df = int(input("DIGITE A AUDIÊNCIA EM PONTOS DO PROGRAMA {}:".format(nome_programa)))
                tot_pessoas_df=(tot_pontos_df*ponto_distrito_federal)
                print("-=" * 20)
                print("""
                ATRAÇÃO:{}
                REGIÃO METROPOLITANA:{}
                AUDIÊNCIA:{} PONTOS 
                UM(1) PONTO EQUIVALE:{} PESSOAS
                """.format(nome_programa, nome_regiao, tot_pontos_df, ponto_distrito_federal))
                print("O TOTAL DE PESSOAS QUE ASSITIRAM A ATRAÇÃO {} EM {} FOI DE {} PESSOAS".format(nome_programa, nome_regiao, tot_pessoas_df))
            elif (escolha_regiao==10):
                nome_regiao=str("GOIÂNIA")
                tot_pontos_goiania = int(input("DIGITE A AUDIÊNCIA EM PONTOS DO PROGRAMA {}:".format(nome_programa)))
                tot_pessoas_goiania=(tot_pontos_goiania*ponto_grande_goiania)
                print("-=" * 20)
                print("""
                ATRAÇÃO:{}
                REGIÃO METROPOLITANA:{}
                AUDIÊNCIA:{} PONTOS 
                UM(1) PONTO EQUIVALE:{} PESSOAS
                """.format(nome_programa, nome_regiao, tot_pontos_goiania, ponto_grande_goiania))
                print("O TOTAL DE PESSOAS QUE ASSITIRAM A ATRAÇÃO {} EM {} FOI DE {} PESSOAS".format(nome_programa, nome_regiao, tot_pessoas_goiania))
                print("-=" * 20)
            elif (escolha_regiao==11):
                nome_regiao=str("BELÉM")
                tot_pontos_belem = int(input("DIGITE A AUDIÊNCIA EM PONTOS DO PROGRAMA {}:".format(nome_programa)))
                tot_pessoas_belem=(tot_pontos_belem*ponto_grande_belem)
                print("-=" * 20)
                print("""
                ATRAÇÃO:{}
                REGIÃO METROPOLITANA:{}
                AUDIÊNCIA:{} PONTOS 
                UM(1) PONTO EQUIVALE:{} PESSOAS
                """.format(nome_programa, nome_regiao, tot_pontos_belem, ponto_grande_belem))
                print("O TOTAL DE PESSOAS QUE ASSITIRAM A ATRAÇÃO {} EM {} FOI DE {} PESSOAS".format(nome_programa, nome_regiao, tot_pessoas_belem))
                print("-=" * 20)
            elif (escolha_regiao==12):
                nome_regiao=str("CAMPINAS")
                tot_pontos_campinas = int(input("DIGITE A AUDIÊNCIA EM PONTOS DO PROGRAMA {}:".format(nome_programa)))
                tot_pessoas_campinas=(tot_pontos_campinas*ponto_grande_campinas)
                print("-=" * 20)
                print("""
                ATRAÇÃO:{}
                REGIÃO METROPOLITANA:{}
                AUDIÊNCIA:{} PONTOS 
                UM(1) PONTO EQUIVALE:{} PESSOAS
                """.format(nome_programa, nome_regiao, tot_pontos_campinas, ponto_grande_campinas))
                print("O TOTAL DE PESSOAS QUE ASSITIRAM A ATRAÇÃO {} EM {} FOI DE {} PESSOAS".format(nome_programa, nome_regiao, tot_pessoas_campinas))
                print("-=" * 20)
            elif (escolha_regiao==13):
                nome_regiao=str("MANAUS")
                tot_pontos_manaus = int(input("DIGITE A AUDIÊNCIA EM PONTOS DO PROGRAMA {}:".format(nome_programa)))
                tot_pessoas_manaus=(tot_pontos_manaus*ponto_grande_manaus)
                print("-=" * 20)
                print("""
                ATRAÇÃO:{}
                REGIÃO METROPOLITANA:{}
                AUDIÊNCIA:{} PONTOS 
                UM(1) PONTO EQUIVALE:{} PESSOAS
                """.format(nome_programa, nome_regiao, tot_pontos_manaus, ponto_grande_manaus))
                print("O TOTAL DE PESSOAS QUE ASSITIRAM A ATRAÇÃO {} EM {} FOI DE {} PESSOAS".format(nome_programa, nome_regiao, tot_pessoas_manaus))
                print("-=" * 20)
            elif (escolha_regiao==14):
                nome_regiao=str("VITÓRIA")
                tot_pontos_vitoria = int(input("DIGITE A AUDIÊNCIA EM PONTOS DO PROGRAMA {}:".format(nome_programa)))
                tot_pessoas_vitoria=(tot_pontos_vitoria*ponto_grande_vitoria)
                print("-=" * 20)
                print("""
                ATRAÇÃO:{}
                REGIÃO METROPOLITANA:{}
                AUDIÊNCIA:{} PONTOS 
                UM(1) PONTO EQUIVALE:{} PESSOAS
                """.format(nome_programa, nome_regiao, tot_pontos_vitoria, ponto_grande_vitoria))
                print("O TOTAL DE PESSOAS QUE ASSITIRAM A ATRAÇÃO {} EM {} FOI DE {} PESSOAS".format(nome_programa, nome_regiao, tot_pessoas_vitoria))
                print("-=" * 20)
            elif (escolha_regiao==15):
                nome_regiao=str("FLORIANÓPOLIS")
                tot_pontos_floripa = int(input("DIGITE A AUDIÊNCIA EM PONTOS DO PROGRAMA {}:".format(nome_programa)))
                tot_pessoas_floripa=(tot_pontos_floripa*ponto_grande_floripa)
                print("-=" * 20)
                print("""
                ATRAÇÃO:{}
                REGIÃO METROPOLITANA:{}
                AUDIÊNCIA:{} PONTOS 
                UM(1) PONTO EQUIVALE:{} PESSOAS
                """.format(nome_programa, nome_regiao, tot_pontos_floripa, ponto_grande_floripa))
                print("O TOTAL DE PESSOAS QUE ASSITIRAM A ATRAÇÃO {} EM {} FOI DE {} PESSOAS".format(nome_programa, nome_regiao, tot_pessoas_floripa))
                print("-=" * 20)
        elif resp_menu_audiencia==3:
            nome_programa = str(input("NOME DA ATRAÇÃO:")).strip()
            nome_programa=nome_programa.upper()
            nome_regiao1=str("SÃO PAULO")
            escolha_regiao = 1
            tot_pontos_sp=int(input("DIGITE A AUDIÊNCIA EM PONTOS DA ATRAÇÃO {} EM {}:".format(nome_programa, nome_regiao1)))
            tot_pessoas_sp=(tot_pontos_sp*ponto_grande_sp)
            print("-="*20)
            print("""
            ATRAÇÃO:{}
            REGIÃO METROPOLITANA:{}
            AUDIÊNCIA:{} PONTOS 
            UM(1)PONTO EQUIVALE:{} PESSOAS
            """.format(nome_programa, nome_regiao1, tot_pontos_sp, ponto_grande_sp))
            print("O TOTAL DE PESSOAS QUE ASSITIRAM A ATRAÇÃO {} EM {} FOI DE {} PESSOAS".format(nome_programa, nome_regiao1, tot_pessoas_sp))
            print("-=" * 20)

            nome_regiao2=str("RIO DE JANEIRO")
            escolha_regiao = 2
            tot_pontos_rj = int(input("DIGITE A AUDIÊNCIA EM PONTOS DA ATRAÇÃO {} EM {}:".format(nome_programa, nome_regiao2)))
            tot_pessoas_rj=(tot_pontos_rj*ponto_grande_rj)
            print("-=" * 20)
            print("""
            ATRAÇÃO:{}
            REGIÃO METROPOLITANA:{}
            AUDIÊNCIA:{} PONTOS 
            UM(1) PONTO EQUIVALE:{} PESSOAS
            """.format(nome_programa, nome_regiao2, tot_pontos_rj, ponto_grande_rj))
            print("O TOTAL DE PESSOAS QUE ASSITIRAM A ATRAÇÃO {} EM {} FOI DE {} PESSOAS".format(nome_programa, nome_regiao2, tot_pessoas_rj))
            print("-=" * 20)

            nome_regiao3=str("BELO HORIZONTE")
            escolha_regiao = 3
            tot_pontos_bh = int(input("DIGITE A AUDIÊNCIA EM PONTOS DA ATRAÇÃO {} EM {} :".format(nome_programa, nome_regiao3)))
            tot_pessoas_bh=(tot_pontos_bh*ponto_grande_bh)
            print("-=" * 20)
            print("""
            ATRAÇÃO:{}
            REGIÃO METROPOLITANA:{}
            AUDIÊNCIA:{} PONTOS 
            UM(1) PONTO EQUIVALE:{} PESSOAS
            """.format(nome_programa, nome_regiao3, tot_pontos_bh, ponto_grande_bh))
            print("O TOTAL DE PESSOAS QUE ASSITIRAM A ATRAÇÃO {} EM {} FOI DE {} PESSOAS".format(nome_programa, nome_regiao3, tot_pessoas_bh))
            print("-=" * 20)

            nome_regiao4=str("PORTO ALEGRE")
            escolha_regiao = 4
            tot_pontos_portoalegre = int(input("DIGITE A AUDIÊNCIA EM PONTOS DA ATRAÇÃO {} EM {}:".format(nome_programa, nome_regiao4)))
            tot_pessoas_portoalegre=(tot_pontos_portoalegre*ponto_grande_portoAlegre)
            print("-=" * 20)
            print("""
            ATRAÇÃO:{}
            REGIÃO METROPOLITANA:{}
            AUDIÊNCIA:{} PONTOS 
            UM(1) PONTO EQUIVALE:{} PESSOAS
            """.format(nome_programa, nome_regiao4, tot_pontos_portoalegre, ponto_grande_portoAlegre))
            print("O TOTAL DE PESSOAS QUE ASSITIRAM A ATRAÇÃO {} EM {} FOI DE {} PESSOAS".format(nome_programa, nome_regiao4, tot_pessoas_portoalegre))
            print("-=" * 20)

            nome_regiao5=str("RECIFE")
            escolha_regiao = 5
            tot_pontos_recife = int(input("DIGITE A AUDIÊNCIA EM PONTOS DA ATRAÇÃO {} EM {}:".format(nome_programa, nome_regiao5)))
            tot_pessoas_recife=(tot_pontos_recife*ponto_grande_recife)
            print("-=" * 20)
            print("""
            ATRAÇÃO:{}
            REGIÃO METROPOLITANA:{}
            AUDIÊNCIA:{} PONTOS 
            UM(1) PONTO EQUIVALE:{} PESSOAS
            """.format(nome_programa, nome_regiao5, tot_pontos_recife, ponto_grande_recife))
            print("O TOTAL DE PESSOAS QUE ASSITIRAM A ATRAÇÃO  EM {} FOI DE {} PESSOAS".format(nome_programa, nome_regiao5, tot_pessoas_recife))
            print("-=" * 20)

            nome_regiao6=str("SALVADOR")
            escolha_regiao = 6
            tot_pontos_salvador = int(input("DIGITE A AUDIÊNCIA EM PONTOS DO PROGRAMA {} EM {}:".format(nome_programa, nome_regiao6)))
            tot_pessoas_salvador=(tot_pontos_salvador*ponto_grande_salvador)
            print("-=" * 20)
            print("""
            ATRAÇÃO:{}
            REGIÃO METROPOLITANA:{}
            AUDIÊNCIA:{} PONTOS 
            UM(1) PONTO EQUIVALE:{} PESSOAS
            """.format(nome_programa, nome_regiao6, tot_pontos_salvador, ponto_grande_salvador))
            print("O TOTAL DE PESSOAS QUE ASSITIRAM A ATRAÇÃO {} EM {} FOI DE {} PESSOAS".format(nome_programa, nome_regiao6, tot_pessoas_salvador))
            print("-=" * 20)

            nome_regiao7=str("FORTALEZA")
            escolha_regiao = 7
            tot_pontos_fortaleza = int(input("DIGITE A AUDIÊNCIA EM PONTOS DO PROGRAMA {} EM {}:".format(nome_programa, nome_regiao7)))
            tot_pessoas_fortaleza=(tot_pontos_fortaleza*ponto_grande_fortaleza)
            print("-=" * 20)
            print("""
            ATRAÇÃO:{}
            REGIÃO METROPOLITANA:{}
            AUDIÊNCIA:{} PONTOS 
            UM(1) PONTO EQUIVALE:{} PESSOAS
            """.format(nome_programa, nome_regiao7, tot_pontos_fortaleza, ponto_grande_fortaleza))
            print("O TOTAL DE PESSOAS QUE ASSITIRAM A ATRAÇÃO {} EM {}  DE {} PESSOAS".format(nome_programa, nome_regiao7, tot_pessoas_fortaleza))
            print("-=" * 20)

            nome_regiao8=str("CURITIBA")
            escolha_regiao = 8
            tot_pontos_curitiba = int(input("DIGITE A AUDIÊNCIA EM PONTOS DO PROGRAMA {} EM {}:".format(nome_programa, nome_regiao8)))
            tot_pessoas_curitiba=(tot_pontos_curitiba*ponto_grande_curitiba)
            print("-=" * 20)
            print("""
            ATRAÇÃO:{}
            REGIÃO METROPOLITANA:{}
            AUDIÊNCIA:{} PONTOS 
            UM(1) PONTO EQUIVALE:{} PESSOAS
            """.format(nome_programa, nome_regiao8, tot_pontos_curitiba, ponto_grande_curitiba))
            print("O TOTAL DE PESSOAS QUE ASSITIRAM A ATRAÇÃO {} EM {} FOI DE {} PESSOAS".format(nome_programa, nome_regiao8, tot_pessoas_curitiba))
            print("-=" * 20)

            nome_regiao9=str("DISTRITO FEDERAL")
            escolha_regiao = 9
            tot_pontos_df = int(input("DIGITE A AUDIÊNCIA EM PONTOS DO PROGRAMA {} EM {}:".format(nome_programa, nome_regiao9)))
            tot_pessoas_df=(tot_pontos_df*ponto_distrito_federal)
            print("-=" * 20)
            print("""
            ATRAÇÃO:{}
            REGIÃO METROPOLITANA:{}
            AUDIÊNCIA:{} PONTOS 
            UM(1) PONTO EQUIVALE:{} PESSOAS
            """.format(nome_programa, nome_regiao9, tot_pontos_df, ponto_distrito_federal))
            print("O TOTAL DE PESSOAS QUE ASSITIRAM A ATRAÇÃO {} EM {} FOI DE {} PESSOAS".format(nome_programa, nome_regiao9, tot_pessoas_df))

            nome_regiao10=str("GOIÂNIA")
            escolha_regiao = 10
            tot_pontos_goiania = int(input("DIGITE A AUDIÊNCIA EM PONTOS DO PROGRAMA {} EM {}:".format(nome_programa, nome_regiao10)))
            tot_pessoas_goiania=(tot_pontos_goiania*ponto_grande_goiania)
            print("-=" * 20)
            print("""
            ATRAÇÃO:{}
            REGIÃO METROPOLITANA:{}
            AUDIÊNCIA:{} PONTOS 
            UM(1) PONTO EQUIVALE:{} PESSOAS
            """.format(nome_programa, nome_regiao10, tot_pontos_goiania, ponto_grande_goiania))
            print("O TOTAL DE PESSOAS QUE ASSITIRAM A ATRAÇÃO {} EM {} FOI DE {} PESSOAS".format(nome_programa, nome_regiao10, tot_pessoas_goiania))
            print("-=" * 20)

            nome_regiao11=str("BELÉM")
            escolha_regiao = 11
            tot_pontos_belem = int(input("DIGITE A AUDIÊNCIA EM PONTOS DO PROGRAMA {} EM {}:".format(nome_programa, nome_regiao11)))
            tot_pessoas_belem=(tot_pontos_belem*ponto_grande_belem)
            print("-=" * 20)
            print("""
            ATRAÇÃO:{}
            REGIÃO METROPOLITANA:{}
            AUDIÊNCIA:{} PONTOS 
            UM(1) PONTO EQUIVALE:{} PESSOAS
            """.format(nome_programa, nome_regiao11, tot_pontos_belem, ponto_grande_belem))
            print("O TOTAL DE PESSOAS QUE ASSITIRAM A ATRAÇÃO {} EM {} FOI DE {} PESSOAS".format(nome_programa, nome_regiao11, tot_pessoas_belem))
            print("-=" * 20)

            nome_regiao12=str("CAMPINAS")
            escolha_regiao = 12
            tot_pontos_campinas = int(input("DIGITE A AUDIÊNCIA EM PONTOS DO PROGRAMA {} EM {}:".format(nome_programa, nome_regiao12)))
            tot_pessoas_campinas=(tot_pontos_campinas*ponto_grande_campinas)
            print("-=" * 20)
            print("""
            ATRAÇÃO:{}
            REGIÃO METROPOLITANA:{}
            AUDIÊNCIA:{} PONTOS 
            UM(1) PONTO EQUIVALE:{} PESSOAS
            """.format(nome_programa, nome_regiao12, tot_pontos_campinas, ponto_grande_campinas))
            print("O TOTAL DE PESSOAS QUE ASSITIRAM A ATRAÇÃO {} EM {} FOI DE {} PESSOAS".format(nome_programa, nome_regiao12, tot_pessoas_campinas))
            print("-=" * 20)

            nome_regiao13=str("MANAUS")
            escolha_regiao = 13
            tot_pontos_manaus = int(input("DIGITE A AUDIÊNCIA EM PONTOS DO PROGRAMA {} EM {}:".format(nome_programa, nome_regiao13)))
            tot_pessoas_manaus=(tot_pontos_manaus*ponto_grande_manaus)
            print("-=" * 20)
            print("""
            ATRAÇÃO:{}
            REGIÃO METROPOLITANA:{}
            AUDIÊNCIA:{} PONTOS 
            UM(1) PONTO EQUIVALE:{} PESSOAS
            """.format(nome_programa, nome_regiao13, tot_pontos_manaus, ponto_grande_manaus))
            print("O TOTAL DE PESSOAS QUE ASSITIRAM A ATRAÇÃO {} EM {} FOI DE {} PESSOAS".format(nome_programa, nome_regiao13, tot_pessoas_manaus))
            print("-=" * 20)

            nome_regiao14=str("VITÓRIA")
            escolha_regiao = 14
            tot_pontos_vitoria = int(input("DIGITE A AUDIÊNCIA EM PONTOS DO PROGRAMA {} EM {}:".format(nome_programa, nome_regiao14)))
            tot_pessoas_vitoria=(tot_pontos_vitoria*ponto_grande_vitoria)
            print("-=" * 20)
            print("""
            ATRAÇÃO:{}
            REGIÃO METROPOLITANA:{}
            AUDIÊNCIA:{} PONTOS 
            UM(1) PONTO EQUIVALE:{} PESSOAS
            """.format(nome_programa, nome_regiao14, tot_pontos_vitoria, ponto_grande_vitoria))
            print("O TOTAL DE PESSOAS QUE ASSITIRAM A ATRAÇÃO {} EM {} FOI DE {} PESSOAS".format(nome_programa, nome_regiao14, tot_pessoas_vitoria))
            print("-=" * 20)

            nome_regiao15=str("FLORIANÓPOLIS")
            escolha_regiao = 15
            tot_pontos_floripa = int(input("DIGITE A AUDIÊNCIA EM PONTOS DO PROGRAMA {} EM {}:".format(nome_programa, nome_regiao15)))
            tot_pessoas_floripa=(tot_pontos_floripa*ponto_grande_floripa)
            print("-=" * 20)
            print("""
            ATRAÇÃO:{}
            REGIÃO METROPOLITANA:{}
            AUDIÊNCIA:{} PONTOS 
            UM(1) PONTO EQUIVALE:{} PESSOAS
            """.format(nome_programa, nome_regiao15, tot_pontos_floripa, ponto_grande_floripa))
            print("O TOTAL DE PESSOAS QUE ASSITIRAM A ATRAÇÃO {} EM {} FOI DE {} PESSOAS".format(nome_programa, nome_regiao15, tot_pessoas_floripa))
            print("-=" * 20)

        elif resp_menu_audiencia==4:
            break
    resp=str(input("DESEJA SAIR?[S/N]")).strip()
    resp=resp.upper()
    print("SAINDO DO PROGRAMA...")
    

