var getUrlParameter = function getUrlParameter(sParam) {
   var sPageURL = window.location.search.substring(1),
       sURLVariables = sPageURL.split('&'),
       sParameterName,
       i;

   for (i = 0; i < sURLVariables.length; i++) {
       sParameterName = sURLVariables[i].split('=');

       if (sParameterName[0] === sParam) {
           return sParameterName[1] === undefined ? true : decodeURIComponent(sParameterName[1]);
       }
   }
   return false;
};

var sendRequest = function sendRequest({
    path = "",
    method = "",
    data = {},
    done = function(data){},
    fail = function(msg){}
 }){
 
    $.ajax({
       headers: {'X-CSRFToken': csrftoken},
       url: base_url + path,
       method: method,
       data: data,
   }).done(done).fail(fail);
 }

$(document).ready(function(){
    // set the modal menu element
    const targetEl = document.getElementById('item_logs_modal');
        // options with default values
    const options = {
        backdropClasses: 'bg-gray-900 bg-opacity-50 dark:bg-opacity-80 fixed inset-0 z-40',
    };

    const modal = new Modal(targetEl, options);

    $(".more_log_btn").on('click', function(){
        const order_id = $(this).parent().parent().attr("data-order-id");
       
        sendRequest({
            path : "/api/orderitem/logs",
            method: "GET",
            data: {
                'orderitem_id' : order_id
            },
            done: function(data){
                console.log(data);
                log_records = data['log_records'];
                $("#item_name").text(data['item_name']);
                const log_elem = $("#logs");

                if(log_records.length > 0){
                    for (const i in log_records) {
                        if (Object.hasOwnProperty.call(log_records, i)) {
                            const log = log_records[i];
                            const cc = log['cc_name'];
                            const timestamp = log['datetime'];
                            const desc = "Logged at " + cc;
    
                            $(log_elem).append(
                                $("<p></p>").addClass("text-gray-500").append(
                                    $("<span></span>").addClass("font-medium").text(timestamp), 
                                    $("<span></span>").text(desc)
                                    )
                                );
                        }
                    }
                }else{
                    $(log_elem).append(
                        $("<p></p>").addClass("text-gray-500").append(
                            $("<span></span>").addClass("font-medium").text("NO LOG")
                            )
                        );
                }
                
            }          
        })
        modal.toggle();
    });

   
    $(".close_modal_btn").on('click', function(){
        modal.toggle();
    });

});
