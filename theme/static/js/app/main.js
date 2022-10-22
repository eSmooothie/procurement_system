var base_url = window.location.origin;

var sendRequest = function send_request({method = "GET", url="",data={}, done=function(data){console.log(data);}, fail=function(xhr){console.log(xhr);}}){

    $.ajax({
        headers: {'X-CSRFToken': csrftoken},
        url: base_url + url,
        method: method,
        data:data,
    }).done(done).fail(fail);
}

var moneyParser = function moneyParser(money_string, currency = "PHP"){
    return new Intl.NumberFormat('en-US', {
        style : 'currency',
        currency : currency,
    }).format(money_string);
}

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

$(document).ready(function(){
    $("input[name=search_category]").autocomplete({
        autoFocus: true,
        minLength:2,
        source: base_url + "/api/categories",
        select: function(event, ui){
            var category_selected = ui.item;
            $("input[name=cat_id]").attr('value',category_selected.id);
        }
    });

    $('#filter_app').on('submit', function(e){
        e.preventDefault();
        let data = $(this).serializeArray();

        sendRequest({
            method: "GET",
            url: "/api/app/get/consolidated/ppmps",
            data: data,
            done: function(data){
                console.log(data);
            },
            fail: function(xhr){
                console.log(xhr);
            }
        });
    });

});