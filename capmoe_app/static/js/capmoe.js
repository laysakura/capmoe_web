////////////////////////////////////////
// upload_capimg.html
////////////////////////////////////////
function upload_capimg(){
  // page local variables
  var img;
  var scale;
  var canvas;
  var ctx;
  $(function(){
    img    = document.getElementById('capimg-preview-img')
    scale  = img.width / img.naturalWidth;
    canvas = document.getElementById('capimg-preview-canvas');
    ctx    = canvas.getContext("2d");
  });

  // Canvas size by CSS
  // See http://stackoverflow.com/questions/2588181/canvas-is-stretched-when-using-css-but-normal-with-width-height-properties#comment-2614029
  $(function(){
    var canvas = $('#capimg-preview-canvas');
    canvas.attr('width',  parseInt(canvas.css('width')));
    canvas.attr('height', parseInt(canvas.css('height')));
  });

  // Select a candidate and fill its (x, y, r) into hidden input box
  $(function(){
    $('.candidates').mousedown(function(e){
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
  });

  // Draw a circle on #capimg-preview-canvas
  $(function(){
    ctx.strokeStyle = '#00F';
    $('#id_cap_x, #id_cap_y, #id_cap_r').change(function(e){
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      ctx.beginPath();
      ctx.arc($('#id_cap_x').val() * scale, $('#id_cap_y').val() * scale, $('#id_cap_r').val() * scale,
              0, Math.PI*2, false)
      ctx.stroke();
    });
  });

  // Draw a circle with mouse on #capimg-preview-canvas
  $(function(){
    $('#capimg-preview-canvas').mousedown(function(e){
      var railhead = e.target.getBoundingClientRect();
      var center_x = e.clientX-railhead.left;
      var center_y = e.clientY-railhead.top;
      var r = 0;

      $('#capimg-preview-canvas').bind('mousemove',function(e){
        var railhead = e.target.getBoundingClientRect();
        var x = e.clientX - railhead.left;
        var y = e.clientY - railhead.top;
        r = Math.sqrt(Math.pow(x - center_x, 2) + Math.pow(y - center_y, 2));

        ctx.clearRect(0, 0, canvas.width, canvas.height);
        ctx.beginPath();
        ctx.arc(center_x, center_y, Math.sqrt(Math.pow(x - center_x, 2) + Math.pow(y - center_y, 2)),
                0, Math.PI*2, false)
        ctx.stroke();
      });

      $('#capimg-preview-canvas').mouseup(function(){
        $('#capimg-preview-canvas').unbind('mousemove');
        $('#id_cap_x').val(Math.round(center_x / scale)).trigger('change');
        $('#id_cap_y').val(Math.round(center_y / scale)).trigger('change');
        $('#id_cap_r').val(Math.round(r        / scale)).trigger('change');
      });
    });
  });
};
