"""
Script auxiliar para coletar resultados de todos os cenários
"""

import subprocess
import re
import os
import sys

def executar_script_sem_plots(caminho):
    try:
        if not os.path.exists(caminho):
            return None, f"Arquivo não encontrado: {caminho}"
        
        with open(caminho, 'r', encoding='utf-8') as f:
            conteudo_original = f.read()
        
        conteudo_modificado = conteudo_original.replace('plt.show()', '# plt.show()  # Desabilitado para coleta')
        
        if 'import matplotlib' in conteudo_modificado or 'import matplotlib.pyplot' in conteudo_modificado:
            if 'matplotlib.use' not in conteudo_modificado:
                import_match = re.search(r'(import matplotlib[^\n]*)', conteudo_modificado)
                if import_match:
                    pos = import_match.end()
                    conteudo_modificado = conteudo_modificado[:pos] + '\nimport matplotlib\nmatplotlib.use(\'Agg\')' + conteudo_modificado[pos:]
        else:
            pass
        
        temp_script = os.path.join(os.path.dirname(caminho) or '.', 'temp_coleta.py')
        with open(temp_script, 'w', encoding='utf-8') as f:
            f.write(conteudo_modificado)
        
        cwd = os.path.dirname(caminho) if os.path.dirname(caminho) else '.'
        resultado = subprocess.run(
            [sys.executable, 'temp_coleta.py'],
            capture_output=True,
            text=True,
            timeout=120,
            cwd=cwd
        )
        
        try:
            os.remove(temp_script)
        except:
            pass
        
        if resultado.returncode != 0:
            return None, f"Erro (código {resultado.returncode}):\n{resultado.stderr[:500]}"
        
        return resultado.stdout, None
        
    except subprocess.TimeoutExpired:
        return None, "Timeout ao executar"
    except Exception as e:
        return None, f"Exceção: {str(e)}"


def extrair_resultados(saida):
    resultados = {}
    
    # Padrões mais flexíveis
    padroes = {
        'tempo_1_agente': [
            r'Tempo total se apenas 1 agente trabalhar:\s*([\d.]+)',
            r'1 agente trabalhar[:\s]+([\d.]+)',
        ],
        'tempo_A': [
            r'Tempo Agente A:\s*([\d.]+)',
            r'Agente A[:\s]+([\d.]+)',
        ],
        'tempo_B': [
            r'Tempo Agente B:\s*([\d.]+)',
            r'Agente B[:\s]+([\d.]+)',
        ],
        'tempo_equipe': [
            r'Tempo total da equipe \(2 agentes\):\s*([\d.]+)',
            r'equipe \(2 agentes\)[:\s]+([\d.]+)',
            r'Tempo total da equipe[:\s]+([\d.]+)',
        ],
        'economia': [
            r'Economia\s*=\s*([\d.]+)',
        ],
        'reducao': [
            r'Redução percentual\s*=\s*([\d.]+)',
            r'Redução[:\s]+([\d.]+)\s*%',
        ]
    }
    
    for chave, lista_padroes in padroes.items():
        valor_encontrado = None
        for padrao in lista_padroes:
            match = re.search(padrao, saida, re.IGNORECASE)
            if match:
                try:
                    valor_encontrado = float(match.group(1))
                    break
                except:
                    continue
        resultados[chave] = valor_encontrado
    
    return resultados


def main():  
    cenarios = {
        'Casa': 'Casa/div2ag.py',
        'Rua': 'Rua/div2ag.py',
        'RuaCasa': 'RuaCasa/div2ag.py'
    }
    
    todos_resultados = {}
        
    for nome, caminho in cenarios.items():
        print(f"Executando {nome} ({caminho})...")
        
        saida, erro = executar_script_sem_plots(caminho)
        
        if erro:
            print(f"  ✗ Erro: {erro}")
            todos_resultados[nome] = {k: None for k in ['tempo_1_agente', 'tempo_A', 'tempo_B', 'tempo_equipe', 'economia', 'reducao']}
            print()
            continue
        
        if not saida:
            print(f"  ✗ Nenhuma saída gerada")
            todos_resultados[nome] = {k: None for k in ['tempo_1_agente', 'tempo_A', 'tempo_B', 'tempo_equipe', 'economia', 'reducao']}
            print()
            continue
        
        resultados = extrair_resultados(saida)
        todos_resultados[nome] = resultados
        
        if resultados['tempo_1_agente']:
            print(f"  ✓ Resultados coletados:")
            print(f"     • Tempo 1 agente: {resultados['tempo_1_agente']:.2f} min")
            print(f"     • Tempo Agente A: {resultados['tempo_A']:.2f} min")
            print(f"     • Tempo Agente B: {resultados['tempo_B']:.2f} min")
            print(f"     • Makespan: {resultados['tempo_equipe']:.2f} min")
            print(f"     • Redução: {resultados['reducao']:.2f}%")
        else:
            print(f"  ✗ Não foi possível extrair resultados")
            # Mostrar linhas relevantes da saída
            linhas = saida.split('\n')
            linhas_relevantes = [l for l in linhas if any(palavra in l.lower() for palavra in ['tempo', 'resultado', 'redução', 'economia'])]
            if linhas_relevantes:
                print(f"     Linhas relevantes encontradas:")
                for linha in linhas_relevantes[:5]:
                    print(f"     {linha[:70]}")
        print()
    
    metricas = [
        ('Tempo 1 agente (min)', 'tempo_1_agente'),
        ('Tempo Agente A (min)', 'tempo_A'),
        ('Tempo Agente B (min)', 'tempo_B'),
        ('Tempo equipe (min)', 'tempo_equipe'),
        ('Economia (min)', 'economia'),
        ('Redução (\\%)', 'reducao')
    ]
    
    
    print("| Métrica | Casas | Distância | Combinado |")
    print("|---------|-------|-----------|-----------|")
    
    for nome_metrica, chave in metricas:
        linha = f"| {nome_metrica} |"
        for cenario in ['Casa', 'Rua', 'RuaCasa']:
            valor = todos_resultados[cenario].get(chave)
            if valor is not None:
                linha += f" {valor:.2f} |"
            else:
                linha += " -- |"
        print(linha)
    


if __name__ == '__main__':
    main()

