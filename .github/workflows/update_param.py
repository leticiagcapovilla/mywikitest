import os
import re

#---------------------------------------------------------------------------
# DEFINIÇÃO DAS FUNÇÕES
#---------------------------------------------------------------------------

# [ ]: Arrumar o mix de português e inglês que está esse código

# Procura as páginas que possuem o parâmetro (através do link) recursivamente
# a partir da raíz das páginas
def find_pages(folder, param_link):
    """
    Procura recursivamente na pasta e em suas subpastas por arquivos que contêm o termo especificado.
    
    Args:
        folder (str): Caminho da pasta principal.
        param_link (str): Termo a ser procurado no conteúdo dos arquivos.
    
    Returns:
        pages_with_param (list): Lista de caminhos dos arquivos que contêm o termo.
    """
    pages_with_param = []

    for root, _, filenames in os.walk(folder):
        for page in filenames:
            page_path = os.path.join(root, page)
            if os.path.isfile(page_path):
                try:
                    with open(page_path, 'r', encoding='utf-8') as f:
                        if param_link in f.read():
                            pages_with_param.append(page_path)
                except (UnicodeDecodeError, PermissionError) as e:
                    print(f"Não foi possível ler o arquivo: {page_path}. Erro: {e}")

    return pages_with_param


# Procura o parâmetro recursivamente a partir da pasta raiz dos parâmetros
def find_param(folder, param_link):
    """
    Procura recursivamente na pasta e em suas subpastas por um arquivo com o nome especificado.
    
    Args:
        folder (str): Caminho da pasta principal.
        param_link (str): Nome exato do arquivo a ser procurado.
    
    Returns:
        str: Conteúdo do arquivo, se encontrado. Caso contrário, retorna None.
    """
    for root, _, filenames in os.walk(folder):
        for param in filenames:
            if param == param_link:
                param_path = os.path.join(root, param)
                try:
                    with open(param_path, 'r', encoding='utf-8') as f:
                        return f.read()
                except (UnicodeDecodeError, PermissionError) as e:
                    print(f"Não foi possível ler o arquivo: {param_path}. Erro: {e}")
                    return None
    return None


# [ ]: Função para extrair valores do parâmetro
# [ ]: Documentar fetch_param_values
def fetch_param_values(param_link):
    try:
        with open(param_link, 'r', encoding='utf-8') as f:
            param_info = f.read()
        
        # Extração de "Valor: " e "Unidade: "
        val_start = param_info.find("Valor: ") + len("Valor: ")
        val_end = param_info.find("\n", val_start)
        val = param_info[val_start:val_end].strip()

        unit_start = param_info.find("Unidade: ") + len("Unidade: ")
        unit_end = param_info.find("\n", unit_start)
        unit = param_info[unit_start:unit_end].strip()

        # Retorna o valor e a unidade separadamente
        return val, unit
    except Exception as e:
        return None, f"Erro ao processar o arquivo: {e}"
    

# [ ]: Extrair valor numérico e unidade do parâmetro
# [ ]: Documentar param_val_unit
def param_val_unit(param_dir, param_link):
    param_path = os.path.join(param_dir, param_link)
    val, unit = fetch_param_values(param_path)

    return val + " " + unit


# [ ]: Substituir valor do parâmetro no texto
# [ ]: Documentar replace_param_val_unit
def replace_param_val_unit(pages_with_param, param_link, p_val_unit):
    for page in pages_with_param:
        try:
            # Abrir o arquivo e ler o conteúdo
            with open(page, 'r', encoding='utf-8') as f:
                conteudo = f.read()
            
            # Procurar por todas as ocorrências de param_link entre parênteses
            identifier = "(" + param_link + ")"
            pattern = re.compile(r'(\[.*?\])\s*' + re.escape(identifier))
            conteudo_modificado = re.sub(pattern, lambda m: m.group(1).replace(m.group(1)[1:-1], p_val_unit) + identifier, conteudo)
            
            # Se houver modificações, reescrever o arquivo com as alterações
            if conteudo != conteudo_modificado:
                with open(page, 'w', encoding='utf-8') as f:
                    f.write(conteudo_modificado)
                print(f"Arquivo '{page}' modificado com sucesso.")
            else:
                print(f"Nenhuma alteração necessária em '{page}'.")

        except Exception as e:
            print(f"Erro ao processar o arquivo '{page}': {e}")


#---------------------------------------------------------------------------
# EXECUÇÃO
#---------------------------------------------------------------------------

# Exemplo de uso
pages_dir = "param_sync/Paginas"
param_dir = "param/sync/Parametros"
param_link = "parametro_1.txt"

# Encontra arquivos que contêm o termo
pages_with_param = find_pages(pages_dir, param_link)
print("Arquivos que contêm o termo:")
print(pages_with_param)

# Procura o conteúdo do arquivo de parâmetro
conteudo_parametro = find_param(param_dir, param_link)
if conteudo_parametro:
    print("\nConteúdo do arquivo de parâmetro:")
    print(conteudo_parametro)
else:
    print("\nArquivo de parâmetro não encontrado.")

# Extrai valor e unidade do parâmetro
p_val_unit = param_val_unit(param_dir, param_link)
print(p_val_unit)

# Realiza a substituição do parâmetro nas páginas que contém o parâmetro
replace_param_val_unit(pages_with_param, param_link, p_val_unit)