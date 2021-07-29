# IBM Watson Text to Speech (TTS) e Speech to Text (STT)
Uma aplicação simples que utiliza os serviços de Texto para Fala (TTS) e Fala para Texto (STT) da IBM Watson.

## Trabalho de reconhecimento e sintetização de voz
O objetivo é fazer uma interface fácil para o usuário interagir com a aplicação e conseguir sintetizar um texto em fala e transcrever uma fala em texto usando os serviços de inteligência artificial da IBM Watson.

A aplicação pronta está disponível no endereço: https://evening-reef-56487.herokuapp.com/

## Arquitetura da aplicação
A aplicação foi desenvolvida em interface HTML no modelo de arquitetura cliente/servidor. O servidor possuí interface REST HTTP e se comunica com a API de serviços de Cloud IBM Watson.

A funcionalidade STT usa os recursos de reconhecimento de fala da IBM para converter a fala em texto. Primeiramente é solicitada a permissão do usuário para utilizar o microfone no navegador. A transcrição do áudio de entrada é gravada e enviada ao servidor de aplicação para que este possa acessar os recursos de WebServices da IBM Watson e fazer uso da chamada _recognize_ da classe _SpeechToTextV1_. Como resultado a aplicação devolve o texto transcrito e este é apresentado ao usuário. O serviço da IBM é acessado por meio de uma interface REST HTTP.

A funcionalidade TTS recebe por formulário um texto do usuário e este é recebido no servidor de aplicação e enviado para o WebService da IBM Watson para fazer a síntese de áudio. O áudio é gravado no servidor e um link é enviado como resposta para que possa ser tocado no navegador. Para este processo é chamado o método _synthesize_ da classe _TextToSpeechV1_.

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

## Deploy no Heroku

Implante o código com `git push heroku`.

## Referências

- https://cloud.ibm.com/apidocs/speech-to-text?code=python
- https://cloud.ibm.com/apidocs/text-to-speech?code=python
- https://github.com/judytraj007/IBM-Watson-TTS-App/blob/master/flask_app.py
- https://devcenter.heroku.com/articles/getting-started-with-python
- https://stackabuse.com/deploying-a-flask-application-to-heroku
- https://developers.google.com/web/fundamentals/media/recording-audio
- https://blog.addpipe.com/using-recorder-js-to-capture-wav-audio-in-your-html5-web-site/