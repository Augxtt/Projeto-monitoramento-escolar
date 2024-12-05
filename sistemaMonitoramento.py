# Define a classe SistemaMonitoramento
class SistemaMonitoramento:
    def __init__(self):
        self.alunos = {}#inicia um dicionário vazio que será usado para armazenar os alunos cadastrados
        #a chave do dicionário será o RA e o valor um objeto represantando o aluno
    
    # Método para adicionar um aluno
    def adicionar_aluno(self, aluno):
        self.alunos[aluno.ra] = aluno
    
    # Método para registrar presença e faltas
    def registrar_presenca(self, ra_aluno, data):
        if ra_aluno in self.alunos:
            self.alunos[ra_aluno].registrar_presenca(data)
    
    def registrar_falta(self, ra_aluno, data):
        if ra_aluno in self.alunos:
            self.alunos[ra_aluno].registrar_falta(data)
    
    # Método para adionar notas
    def adicionar_nota(self, ra_aluno, disciplina, nota):
        # Verefica se o RA existe no dicionário
        if ra_aluno in self.alunos:
            self.alunos[ra_aluno].adicionar_nota(disciplina, nota)
        # Se existir, chama o método adicionar_nota(disciplina, nota) no objeto do aluno correspondente.
    
    # Define um método para gerar alertas
    def gerar_alerta(self, limiteFrequencia = 75, limiteMedia=6):
        alertas = [] # Lista para armzarnar os dados de alunos em risco
        for aluno in self.alunos.values():
            frequencia = aluno.calcular_frequencia()
            media_geral = sum(aluno.calcular_media(d) for d in aluno.notas) / len(aluno.notas) if aluno.notas else 0

            # Verifica se a frequência ou as notas estão de acordo com os parâmetros estabelecidos
            if frequencia < limiteFrequencia or media_geral < limiteMedia:
                alertas.append({
                    "aluno":aluno.nome,
                    "frequencia": frequencia,
                    "media_geral": media_geral,
                    "risco": "Alto" if frequencia < 50 or media_geral < 5 else "Baixo"
                })

        return alertas # Retorna a lista de alertas gerada