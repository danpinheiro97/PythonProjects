cariotipo = list()
nmet = 0
cont = 0
while True:
    metafases = dict()
    metafases["ID"] = int(input("Qual é o ID da metáfase?"))
    metafases["Braço Longo"] = float(input("Qual é o tamanho do braço longo?"))
    metafases["Braço Curto"] = float(input("Qual é o tamanho do braço curto"))
    metafases["Razão"] = metafases["Braço Longo"]/metafases["Braço Curto"]
    metafases["Altura do Cromossomo"] = metafases["Braço Longo"] + metafases["Braço Curto"]
    if metafases["Razão"] >= 0 and metafases["Razão"] <= 1.70:
        metafases["Tipo de cromossomo"] = "Metacêntrico"
    if metafases["Razão"] >= 1.71 and metafases["Razão"] <= 3.0:
        metafases["Tipo de cromossomo"] = "Sub-Metacêntrico"
    if metafases["Razão"] >= 3.01 and metafases["Razão"] <= 7.0:
        metafases["Tipo de cromossomo"] = "Sub-Telocêntrico"
    if metafases["Razão"] >= 7.01:
        metafases["Tipo de cromossomo"] = "Acrocêntrico"
    cariotipo.append(metafases)
    qst = str(input("Você deseja adicionar mais metafáses?"))
    if qst != "Nn":
        nmet += 1
    if qst in "Nn":
        break
    print(cariotipo)
arquivo = open("C:\\Users\\dagol\\Desktop\\Citogenetica\\H.motuchae\\11085\\11085.csv", "w")
while nmet > cont:
    valores = f'{"ID"};{"Razão"};{"Altura do Cromossomo"};{"Tipo de Cromossomo"}\n{cariotipo[cont]["ID"]}; {cariotipo[cont]["Razão"]:.2f}; {cariotipo[cont]["Altura do Cromossomo"]};{cariotipo[cont]["Tipo de cromossomo"]}\n'
    arquivo.write(valores)
    cont += 1
    if nmet == cont:
        break




