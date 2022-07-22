$(document).ready(function(e){
    var base_url = window.location.origin;

    $(".cost_center_list").on('click', function(e){
        e.preventDefault();
        var cost_center_id = $(this).attr("data-cost-center-id");
        
        window.location.href = base_url + "/home/ppmp/costcenter/" + cost_center_id + "/";
    });

    $(".cost_center_ppmp_list").on('click', function(e){
        e.preventDefault();

        var cc_ppmp_id = $(this).attr("data-ppmp-id");

        alert("The PPMP ID is: " + cc_ppmp_id);
    });

    $("#id_cc_ppmp_year").on("change", function(e){
        e.preventDefault();
        var selected_year = $(this).find(":selected").val();
        
        var cc_id = getUrlParameter('cc_id');
        
        window.location.href = base_url + window.location.pathname + "?ppmp_year=" + selected_year;
    });
});

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