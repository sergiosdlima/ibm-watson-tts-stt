// UTILS
const printMsg = function(el, msg) {
  el.text(msg);
}

// TEXT TO SPEECH
$("#input-form").on("submit", function(event) {
  event.preventDefault();
  const text = $("#input-text")[0].value;
  const textLog = $('#text-log');
  if (text) {
    printMsg(textLog, 'Enviando texto...');
    $.ajax({
      data: {
        text: text
      },
      type: 'POST',
      url: '/tts'
    }).done(function(data) {
      printMsg(textLog, 'Tocando áudio...');
      const audio = new Audio(data.audio_url);
      audio.play();
      audio.onended = function() {
        printMsg(textLog, '');
      };
    });
  }
});

// SPEECH TO TEXT
let log = console.log.bind(console);
let mediaRecorder;
const startButton = document.getElementById('start-speech');
const stopButton = document.getElementById('stop-speech');
const audioLog = $('#audio-log');

startButton.addEventListener('click', function() {
  audioLog.val('Escutando...');
  mediaRecorder.start();
});

stopButton.addEventListener('click', function() {
  mediaRecorder.stop();
});

const handleSuccess = function(stream) {
  const options = {mimeType: 'audio/webm'};
  let recordedChunks = [];
  mediaRecorder = new MediaRecorder(stream, options);

  mediaRecorder.addEventListener('start', function() {
    if (recordedChunks.length) {
      recordedChunks = [];
    }
  });

  mediaRecorder.addEventListener('dataavailable', function(e) {
    audioLog.val('Processando...');
    if (e.data.size > 0) {
      recordedChunks.push(e.data);
    }
  });

  mediaRecorder.addEventListener('stop', function() {
    const audioBlob = new Blob(recordedChunks);
    let fd = new FormData();
    fd.append('blob', audioBlob);
    $.ajax({
      method: 'POST',
      url: '/stt',
      data: fd,
      processData: false,
      contentType: false
    }).done((data) => {
      audioLog.val('');
      textResult = '';
      for (let i = 0; i < data.result.results.length; i++) {
        textResult += data.result.results[i].alternatives[0].transcript + ' ';
      }
      audioLog.val(textResult);
    });
  });
};
// Acessa o microfone de forma interativa
navigator.mediaDevices.getUserMedia({ audio: true, video: false })
  .then(handleSuccess)
  .catch(log);
