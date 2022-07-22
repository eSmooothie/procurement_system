$(document).ready(function(e){
    var base_url = window.location.origin;

    $(".cost_center_list").on('click', function(e){
        e.preventDefault();
        var cost_center_id = $(this).attr("data-cost-center-id");
        
        window.location.href = base_url + "/home/ppmp/costcenter/" + cost_center_id + "/";
    });

    $(".cost_center_ppmp_list").on('click', function(e){
        e.preventDefault();

        // select all child that is not the selected and remove the class bg-gray-200
        $("#ppmp_list_tbody").children().not(this).removeClass("bg-gray-200");

        var cc_ppmp_id = $(this).attr("data-ppmp-id");

        $(this).addClass("bg-gray-200");

        $("#edit_selected_ppmp_btn").removeAttr('disabled');
        $("#edit_selected_ppmp_btn").removeClass("bg-gray-300 hover:bg-gray-400").addClass("hover:bg-blue-400 bg-blue-300");
        $("#edit_selected_ppmp_btn").attr("data-selected-ppmp-id",cc_ppmp_id);

        console.log($("#edit_selected_ppmp_btn"));

        alert("The PPMP ID is: " + cc_ppmp_id);
    });

    $("#id_cc_ppmp_year").on("change", function(e){
        e.preventDefault();
        var selected_year = $(this).find(":selected").val();
        
        var cc_id = getUrlParameter('cc_id');
        
        window.location.href = base_url + window.location.pathname + "?ppmp_year=" + selected_year;
    });

    $("#edit_selected_ppmp_btn").on("click", function(e){
        e.preventDefault();

        var selected_ppmp_id = $(this).attr("data-selected-ppmp-id");

        alert("Edit Selected PPMP id: "+ selected_ppmp_id);
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