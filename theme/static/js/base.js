var $loading = $('#display_loading_div').hide();

$(document).on("ajaxSend", function(){
  $loading.show();
}).on("ajaxComplete", function(){
  $loading.hide();
});

var sendRequest = function send_request({
  method = "GET", 
  url="",
  data={}, 
  done=function(data){console.log(data);}, 
  fail=function(xhr){window.location.reload();}
}){
  $.ajax({
      headers: {'X-CSRFToken': csrftoken},
      url: base_url + url,
      method: method,
      data:data
  })
  .done(done)
  .fail(fail);
}
