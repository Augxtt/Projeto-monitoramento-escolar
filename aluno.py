# Define a classe "Aluno"
class Aluno:
    def __init__(self, nome, ra):
        self.nome = nome # Atributo nome
        self.ra = ra # Atributo registro acadêmico
        self.frequencia = {} # Dicionário vazio para armazernar presença
        self.notas = {} # Dicionário vazio para armazernar nota

    # Método de Registro de presença e falta
    def registrar_presenca(self, data):
        if data not in self.frequencia:
            self.frequencia[data] = True

    def registrar_falta(self, data):
        if data not in self.frequencia:
            self.frequencia[data] = False
    # Verifica sempre se a data já existe no dicionário antes de adiconar, o que evita sobrecarga de registros já existentes

    # Calculo da média
    def calcular_media(self, disciplina):
        # Verifica se a disciplina existe no dicionário 'notas'
        if disciplina in self.notas and len(self.notas[disciplina]) > 0:
            return sum(self.notas[disciplina]) / len(self.notas[disciplina])
        return 0 #se houve notas, calcula a média; caso contrário retorna 0

    # Adiciona notas
    def adicionar_nota(self, disciplina, nota):
        # Verefica se a disciplina não existe no dicionário 'notas'
        if disciplina not in self.notas:
            self.notas[disciplina] = []# Cria uma nova lista pra ela
        self.notas[disciplina].append(nota)# Adiciona a nota à lista de notas da disciplina

    #Calcula a frequência
    def calcular_frequencia(self):
        #Calcula a porcentagem de frequencia do aluno
        if len(self.frequencia) == 0:
            return 0# se não houver presença retorna 0
        presencas = sum(1 for presenca in self.frequencia.values() if presenca)
        return (presencas / len(self.frequencia)) * 100
        #Calcula a porcentagem dividindo o número de presenças pelo total de registros e multiplicando por 100