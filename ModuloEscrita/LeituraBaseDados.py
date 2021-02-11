
# é possivel criar dois for sendo um para percorrer a pasta e outro para caminhar no arquivo
def leituraArquivo(path):
    with open(path, 'r') as file:
        return file.read()

def leituraYaml(path):
    import yaml
    with open(path, 'r') as yml:
        try:
            return yml.read()
        except yaml.YAMLError as exc:
            print(exc)

def escreveYaml(path, escrita):
    import yaml
    with open(path, 'a+') as yml:
        try:
            return yml.write(escrita)
        except yaml.YAMLError as exc:
            print(exc)

'''-> retorna uma lista com todo o conteudo do arquivo'''
def arquivoEmLista(path):
    valor = leituraArquivo(path)
    linha = valor.split('\n')
    return linha

''' -> Separa a linha do titulo para criar a intent'''
def identificadoIntent(path):
    linha0 = arquivoEmLista(path)
    valor = linha0[0].split(' - ')
    return valor

def textIntent(path_read):
    intencao = identificadoIntent(path_read)
    lista = []
    texto = '    - Preciso do chamado '  + intencao[2]
    texto1 = '    - Quero abrir o chamado ' + intencao[2]
    texto2 = '    - Preciso abrir o chamado '+ intencao[2]
    texto3 = '    - quero o chamado '+ intencao[0] + '-' + intencao[1]
    texto4 = '    - quero a ocorrencia '+ intencao[0] + '-' + intencao[1]
    lista.append(texto)
    lista.append(texto1)
    lista.append(texto2)
    lista.append(texto3)
    lista.append(texto4)
    return lista

def criaIntent(path_write, path_read):
    cria = identificadoIntent(path_read)
    texto = textIntent(path_read)
    variavelFinal = "- intent: " + cria[2].replace(' ', '_')+'\n'+'  examples: |\n'
    for i in range(len(texto)):
        variavelFinal += texto[i]+'\n'
    escreveYaml(path_write, variavelFinal)

leitura = '/home/erickson/PP_IFPB/chamados/CA1 - Cadastro/CA1 - MC1 - Mudança de local para cobrança'
escrita = '/home/erickson/PP_IFPB/rasa/data/nlu.yml'
valor = criaIntent(escrita, leitura)
# print(textIntent(leitura))




# o nome da ocorrencia se tornará a intent ( intenção de fala ) -> NLU
#selecionando intent a ser gravada
# os exemplos são nome, referencia do chamado e conjunto de frases com o nome do chamado
# Quero abrir [x], preciso do [x] e etc
# inserir lógica de pergunta "Quando abrir?" -> Intent -> Quando+Chamado
# Resposta -> Utter_Qd+Chamado -> Motivo
# motivo de geração vai se tornar a respostar (utter_intent) -> Domain
# texto padrão será (utter_padrao_chamado) -> Domain
# será criado uma regra onde para cada intent há uma utter -> Rules