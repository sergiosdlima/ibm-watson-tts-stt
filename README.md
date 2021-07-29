# IBM Watson Texto para Fala (TTS) e Fala para Texto (STT)
Uma aplicação simples que utiliza as APIs de Texto para Fala (TTS) e Fala para Texto (STT) da IBM Watson.

## Trabalho de reconhecimento e sintetização de voz
O objetivo é fazer uma interface fácil para o usuário interagir com a aplicação.

A aplicação pronta está disponível no endereço: https://evening-reef-56487.herokuapp.com/

## Configurando o ambiente local

No diretório do seu projeto, vamos começar criando um virtualenv

`python -m venv venv/` ou `virtualenv venv`

E vamos ativá-lo com o comando source:

`source venv/bin/activate`

Então, vamos usar o pip para instalar as bibliotecas que vamos usar:

`pip install -r requirements.txt`

Agora, sempre que você executar um script Python, o executável, as configurações e os pacotes do ambiente virtual Python serão usados em vez do executável Python global.

Crie um arquivo `.env` com as variáveis de ambiente `TTS_API_KEY`, `TTS_SERVICE_URL`, `STT_API_KEY` e `STT_SERVICE_URL`.

Para parar de usar o ambiente virtual, basta desativá-lo executando:

`deactivate`

## Configurando o Heroku CLI para deploy

Faça a instalação padrão:

`curl https://cli-assets.heroku.com/install.sh | sh`

Verifique se ocorreu tudo bem:

`heroku --version`

Inicie uma sessão:

`heroku login`

Configure as variáveis de ambiente `TTS_API_KEY`, `TTS_SERVICE_URL`, `STT_API_KEY` e `STT_SERVICE_URL` na aba Settings no painel da sua aplicação.

Crie o aplicativo Heroku para implantar:

`heroku create`

Implante o código com `git push`.

## Referências

- https://cloud.ibm.com/apidocs/speech-to-text?code=python
- https://cloud.ibm.com/apidocs/text-to-speech?code=python
- https://github.com/judytraj007/IBM-Watson-TTS-App/blob/master/flask_app.py
- https://devcenter.heroku.com/articles/getting-started-with-python
- https://stackabuse.com/deploying-a-flask-application-to-heroku
- https://developers.google.com/web/fundamentals/media/recording-audio
- https://blog.addpipe.com/using-recorder-js-to-capture-wav-audio-in-your-html5-web-site/