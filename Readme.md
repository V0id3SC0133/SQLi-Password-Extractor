## 🛡️ SQLi Password Extractor 

O SQLi Password Extractor é uma ferramenta automatizada projetada para explorar vulnerabilidades de SQL Injection Blind em aplicações web. Esta ferramenta permite a extração precisa de hashes de senhas, o que a torna muito útil em ambientes de laboratórios controlados e em treinamentos de segurança. O foco principal do SQLi Password Extractor é facilitar a identificação e exploração de falhas de segurança, permitindo que profissionais de segurança testem a robustez das aplicações contra ataques de injeção SQL. 

## Características:

✅ Compatível com Windows, Linux e macOS

✅ Configuração simples e intuitiva

✅ Interface interativa no terminal

✅ Suporte para exploração manual e automatizada

✅ Extração passo a passo de hashes de senhas


⚙️ Como funciona?

O script implementa uma técnica de SQL Injection Blind para realizar a extração da hash da senha armazenada no banco de dados, caractere por caractere. Esse processo ocorre através da análise das respostas do servidor, permitindo determinar cada caractere da hash de forma iterativa. No entanto, para a execução bem-sucedida dessa abordagem, é necessário que a vulnerabilidade de injeção de SQL tenha sido previamente identificada, bem como o caminho exato para a injeção (endpoint ou parâmetro vulnerável).

## Requisitos

Certifique-se de que os seguintes requisitos estão instalados no seu sistema:

Python 3.x

Bibliotecas Python necessárias:

pip install requests

## Como usar?
Clone este repositório:

git clone https://github.com/ESC0133/sqli-password-extractor.git
cd sqli-password-extractor
Instale as dependências:

pip install -r requirements.txt
Execute o script:

python3 sqli_extractor.py
Exemplo de uso:

![image](https://github.com/user-attachments/assets/02d3430d-8dbf-4621-807f-9daba3fafad1)


## Exemplo de Saída

![image](https://github.com/user-attachments/assets/6af82b1d-b373-46e4-b763-c4930da2c02a)


## Dependências Automáticas

Se algum módulo estiver faltando, o script tentará instalá-lo automaticamente ao ser executado com permissões adequadas. Caso isso falhe, você pode instalar manualmente usando:

pip install requests
Importante: Execute o script com permissões adequadas na primeira vez:

## ⚠️ Isenção de responsabilidade
Este script é fornecido apenas para fins educacionais e deve ser usado em ambientes controlados com autorização prévia. O uso indevido é de total responsabilidade do usuário.

## Autor
## 👨‍💻 Autor
- **Ernani S. C.**
- **Nickname:** 3SC0133



