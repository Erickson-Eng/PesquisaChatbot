from rasa_sdk.interfaces import Action

def leituraArquivo(path):
    with open(path, 'r') as file:
        return file.read()

def nomeOcorrencia(path):
    arquivo = leituraArquivo(path)
    linha = arquivo.split('\n')
    return linha[0]

def motivoOcorrencia(path):
    arquivo = leituraArquivo(path)
    linha = arquivo.split('\n')
    motivo = linha[1].split(":")
    return motivo[1]

def listaArquivos(path):
    import os
    return os.listdir(path)

valores = listaArquivos('/home/cellash/Área de Trabalho/PP_IFPB/chamados')

print('Diretorios')

for i in range(len(valores)):
    novoCaminho = '/home/erickson/PP_IFPB/chamados' + "/" + valores[i]
    # print(novoCaminho)
    final = listaArquivos(novoCaminho)
    for j in range(len(final)):
        caminhoFinal = novoCaminho + "/" + final[j]
        print(final[j])
        print(motivoOcorrencia(caminhoFinal))
        print()
