$(function(){

  // Select a candidate and fill its (x, y, r) into hidden input box
  $('.candidates').mousedown(function(e) {
    var cand_id = e.currentTarget.id;
    var x = $('#' + cand_id + '>' + '.x').text();
    var y = $('#' + cand_id + '>' + '.y').text();
    var r = $('#' + cand_id + '>' + '.r').text();
    $('#id_cap_x').val($('#' + cand_id + '>' + '.x').text());
    $('#id_cap_y').val($('#' + cand_id + '>' + '.y').text());
    $('#id_cap_r').val($('#' + cand_id + '>' + '.r').text());
  });

});
