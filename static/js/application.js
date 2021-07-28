const statusMsg = function(msg) {
  $('#audio-log').text(msg);
}

$("#input-form").on("submit", function(event) {
  event.preventDefault();
  const text = $("#input-text")[0].value;
  statusMsg('Carregando...');
  $.ajax({
    data: {
      text: text
    },
    type: 'POST',
    url: '/tts'
  }).done(function(data) {
    statusMsg('Tocando áudio...');
    const audio = new Audio(data.audio_url);
    audio.play();
    audio.onended = function() {
      statusMsg('');
    };
  });
});
