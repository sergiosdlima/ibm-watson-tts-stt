# IBM Watson Texto para Fala (TTS) e Fala para Texto (STT)
Uma aplicação simples que utiliza as APIs de Texto para Fala (TTS) e Fala para Texto (STT) da IBM Watson.

## Trabalho de reconhecimento e sintetização de voz
O objetivo é fazer uma interface fácil para o usuário interagir com a aplicação.

## Configurando o ambiente local

No diretório do seu projeto, vamos começar criando um virtualenv

`python -m venv venv/` ou `virtualenv venv`

E vamos ativá-lo com o comando source:

`source venv/bin/activate`

Então, vamos usar o pip para instalar as bibliotecas que vamos usar:

`pip install -r requirements.txt`

Agora, sempre que você executar um script Python, o executável, as configurações e os pacotes do ambiente virtual Python serão usados em vez do executável Python global.

Crie um arquivo .env com as variáveis de ambiente `API_KEY` e `TTS_SERVICE_URL`.

Para parar de usar o ambiente virtual, basta desativá-lo executando:

`deactivate`

## Configurando o Heroku CLI para deploy

Faça a instalação padrão:

`curl https://cli-assets.heroku.com/install.sh | sh`

Verifique se ocorreu tudo bem:

`heroku --version`

Inicie uma sessão:

`heroku login`

Configure as variáveis de ambiente `API_KEY` e `TTS_SERVICE_URL`.

## Referências

- https://devcenter.heroku.com/articles/getting-started-with-python
- https://stackabuse.com/deploying-a-flask-application-to-heroku
- https://github.com/judytraj007/IBM-Watson-TTS-App/blob/master/flask_app.py