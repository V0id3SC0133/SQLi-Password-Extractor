🛡️ SQLi Password Extractor 

O SQLi Password Extractor é uma ferramenta automatizada desenvolvida para explorar vulnerabilidades de SQL Injection Blind em aplicações web. Ela permite extrair hashes de senhas com precisão, sendo especialmente útil para laboratórios controlados e treinamentos de segurança.

🚀 Características:

✅ Compatível com Windows, Linux e macOS

✅ Configuração simples e intuitiva

✅ Interface interativa no terminal

✅ Suporte para exploração manual e automatizada

✅ Pausa visual para monitoramento de progresso

✅ Extração passo a passo de hashes de senhas


⚙️ Como funciona?

O script utiliza SQL Injection Blind para testar caractere por caractere da senha armazenada no banco de dados, verificando cada caractere com base nas respostas recebidas do servidor.

📚 Requisitos

Certifique-se de que os seguintes requisitos estão instalados no seu sistema:

Python 3.x
Bibliotecas Python necessárias:

pip install requests

💻 Como usar?
Clone este repositório:

git clone https://github.com/ESC0133/sqli-password-extractor.git
cd sqli-password-extractor
Instale as dependências:

pip install -r requirements.txt
Execute o script:

python3 sqli_extractor.py
Exemplo de uso:

Qual é a URL vulnerável a SQLi? http://exemplo.com
Qual é o path vulnerável a SQLi? /forgot_password.php
Qual é o nome do usuário válido? admin

📊 Exemplo de Saída

=== SQL Injection Blind - Extrator de Senha ===

Iniciando extração de senha para o usuário: admin
Testando caracteres para o usuário válido: admin
[+] Testando posição 1 com caractere: a - Caractere encontrado: a
[+] Testando posição 2 com caractere: b - Caractere encontrado: b

A hash da senha do usuário é: abcd1234

🐍 Dependências Automáticas

Se algum módulo estiver faltando, o script tentará instalá-lo automaticamente ao ser executado com permissões adequadas. Caso isso falhe, você pode instalar manualmente usando:

pip install requests
Importante: Execute o script com permissões adequadas na primeira vez:


sudo python3 sqli_extractor.py

⚠️ Isenção de responsabilidade
Este script é fornecido apenas para fins educacionais e deve ser usado em ambientes controlados com autorização prévia. O uso indevido é de total responsabilidade do usuário.
