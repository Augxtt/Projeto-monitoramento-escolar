"""
Projeto: Sistema de Monitoramento de Alunos e Evasão Escolar
Disciplina: Seminário Integrador - Talento Tech
Desenvolvido por: Mateus Augusto Adão Rocha
Data: 05/12/2024
Descrição:
    Este projeto simula um sistema básico para Monitorar um sistema escolar e alertar sobre possíveis evasões(reprovas).
    O sistema inclui funcionalidades como:
    - Registrar frequência.
    - Registrar notas.
    - Calcular a média da notas e a porcertagem de presença.
    - Alerta se o risco de evasão está alto ou não.

Objetivo:
    Este sistema foi desenvolvido para aplicar conceitos de Programação Orientada a Objetos (POO)
    e Engenharia de Software em um contexto prático, alinhado aos objetivos do projeto Talento Tech.
"""
#Importa as classes Aluno e SistemaMonitoramento de seus arquivos
from aluno import Aluno #type: ignore
from sistemaMonitoramento import SistemaMonitoramento # type: ignore

#Exemplo de uso
sistema = SistemaMonitoramento()

# Registro dos alunos
aluno1 = Aluno("Mateus Augusto", 1)
aluno2 = Aluno("Gabriella da Cunha", 2)
aluno3 = Aluno("Leonardo Silva", 3)
aluno4 = Aluno("Pablo Costa", 4)
aluno5 = Aluno("Mia Couto", 5)
sistema.adicionar_aluno(aluno1)
sistema.adicionar_aluno(aluno2)
sistema.adicionar_aluno(aluno3)
sistema.adicionar_aluno(aluno4)
sistema.adicionar_aluno(aluno5)

# Registro de presença
sistema.registrar_presenca(1, "01/12/2024")
sistema.registrar_presenca(1, "02/12/2024")
sistema.registrar_falta(1, "03/12/2024")
sistema.registrar_presenca(2, "01/12/2024")
sistema.registrar_falta(2, "02/12/2024")
sistema.registrar_presenca(2, "03/12/2024")
sistema.registrar_presenca(3, "01/12/2024")
sistema.registrar_presenca(3, "02/12/2024")
sistema.registrar_falta(3, "03/12/2024")
sistema.registrar_presenca(4, "01/12/2024")
sistema.registrar_falta(4, "02/12/2024")
sistema.registrar_falta(4, "03/12/2024")
sistema.registrar_presenca(5, "01/12/2024")
sistema.registrar_presenca(5, "02/12/2024")
sistema.registrar_falta(5, "03/12/2024")

# Registro de notas
sistema.adicionar_nota(1,"Matemática", 7.5)
sistema.adicionar_nota(1,"Português", 8.0)
sistema.adicionar_nota(2,"Matemática", 6.0)
sistema.adicionar_nota(2,"Português", 7.8)
sistema.adicionar_nota(3,"Matemática", 5.0)
sistema.adicionar_nota(3,"Português", 8.0)
sistema.adicionar_nota(4,"Matemática", 2.0)
sistema.adicionar_nota(4,"Português", 5.0)
sistema.adicionar_nota(5,"Matemática", 5.8)
sistema.adicionar_nota(5,"Português", 4.0)

# Gerando alerta de evasão
alertas = sistema.gerar_alerta()

print("Alerta de risco de evasão:")
for alerta in alertas:
    print(f"Aluno: {alerta['aluno']}")
    print(f"Frequência: {alerta['frequencia']:.2f}%")
    print(f"Média Geral: {alerta['media_geral']:.2f}")
    print(f"Alerta de evasão: {alerta['risco']}")
    print("---")
