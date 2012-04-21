/*
    Vote
*/
function vote(video_id){
    if(ytplayer.getCurrentTime()>30 && getPlayerState()==1){
        $.post('/dev/perfis/votar/', { video_id: video_id }, function (result) {
          WinId=window.open('/dev/perfis/votar/', 'Votar', 'width=485,height=390');
          WinId.document.open();
          WinId.document.write(result);
          WinId.document.close();
        });
        $('span#vote_result').replaceWith("<span id='vote_result'>Voto aceito</span>");
    }
    else{
        $('span#vote_result').replaceWith("<span id='vote_result'>Assista pelo menos 30 segundos do vídeo antes de votar</span>");
    }
}
/*
$('button#index').click(function() {
  $('input#index_result').val(ytplayer.getPlaylistIndex());
  $('input#video_id_result').val(jsPlaylist[ytplayer.getPlaylistIndex()]);
});
*/
