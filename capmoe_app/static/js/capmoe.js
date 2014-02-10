$(function(){

  ////////////////////////////////////////
  // upload_capimg.html
  ////////////////////////////////////////

  // Select a candidate and fill its (x, y, r) into hidden input box
  $('.candidates').mousedown(function(e) {
    var cand_id = e.currentTarget.id;
    var x = $('#' + cand_id + '>' + '.x').text();
    var y = $('#' + cand_id + '>' + '.y').text();
    var r = $('#' + cand_id + '>' + '.r').text();

    // trigger('change') hack
    // See http://stackoverflow.com/questions/12580761/hidden-input-change-event#answer-14834895
    $('#id_cap_x').val($('#' + cand_id + '>' + '.x').text()).trigger('change');
    $('#id_cap_y').val($('#' + cand_id + '>' + '.y').text()).trigger('change');
    $('#id_cap_r').val($('#' + cand_id + '>' + '.r').text()).trigger('change');
  });

  // Canvas size by CSS
  // See http://stackoverflow.com/questions/2588181/canvas-is-stretched-when-using-css-but-normal-with-width-height-properties#comment-2614029
  var canvas = $('#capimg-preview-canvas');
  canvas.attr('width',  parseInt(canvas.css('width')));
  canvas.attr('height', parseInt(canvas.css('height')));

  // Draw a circle on img#capimg-preview
  var img    = document.getElementById('capimg-preview-img')
  var scale  = img.width / img.naturalWidth;
  var canvas = document.getElementById('capimg-preview-canvas');
  var ctx    = canvas.getContext("2d");
  ctx.strokeStyle = '#00F';
  $('#id_cap_x, #id_cap_y, #id_cap_r').change(function(e) {
    ctx.clearRect(0,0,canvas.width,canvas.height);
    ctx.beginPath();
    ctx.arc($('#id_cap_x').val() * scale, $('#id_cap_y').val() * scale, $('#id_cap_r').val() * scale,
            0, Math.PI*2, false)
    ctx.stroke();
  });

});
