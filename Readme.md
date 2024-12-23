🛡️ SQLi Password Extractor 

O SQLi Password Extractor é uma ferramenta automatizada desenvolvida para explorar vulnerabilidades de SQL Injection Blind em aplicações web. Ela permite extrair hashes de senhas com precisão, sendo especialmente útil para laboratórios controlados e treinamentos de segurança.

🚀 Características:

✅ Compatível com Windows, Linux e macOS

✅ Configuração simples e intuitiva

✅ Interface interativa no terminal

✅ Suporte para exploração manual e automatizada

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

![image](https://github.com/user-attachments/assets/02d3430d-8dbf-4621-807f-9daba3fafad1)


📊 Exemplo de Saída

![image](https://github.com/user-attachments/assets/6af82b1d-b373-46e4-b763-c4930da2c02a)


🐍 Dependências Automáticas

Se algum módulo estiver faltando, o script tentará instalá-lo automaticamente ao ser executado com permissões adequadas. Caso isso falhe, você pode instalar manualmente usando:

pip install requests
Importante: Execute o script com permissões adequadas na primeira vez:


sudo python3 sqli_extractor.py

⚠️ Isenção de responsabilidade
Este script é fornecido apenas para fins educacionais e deve ser usado em ambientes controlados com autorização prévia. O uso indevido é de total responsabilidade do usuário.
