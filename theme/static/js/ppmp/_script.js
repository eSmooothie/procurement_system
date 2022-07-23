var base_url = window.location.origin;

$(document).ready(function(e){

    $(".cost_center_list").on('click', function(e){
        e.preventDefault();
        var cost_center_id = $(this).attr("data-cost-center-id");
        
        window.location.href = base_url + "/home/ppmp/costcenter/" + cost_center_id + "/";
    });

    $(".cost_center_ppmp_list").on('click', function(e){
        e.preventDefault();

        var cc_ppmp_id = $(this).attr("data-ppmp-id");

        var selected_year = getUrlParameter('ppmp_year');

        if(!selected_year){
            selected_year = $("#id_cc_ppmp_year option:selected").val();
        }
        
        window.location.href = base_url + window.location.pathname + "?ppmp_year=" + selected_year + "&ppmp_id=" + cc_ppmp_id;
    });

    $("#id_cc_ppmp_year").on("change", function(e){
        e.preventDefault();
        var selected_year = $(this).find(":selected").val();
        
        window.location.href = base_url + window.location.pathname + "?ppmp_year=" + selected_year;
    });

    $("#edit_selected_ppmp_btn").on("click", function(e){
        e.preventDefault();

        var selected_ppmp_id = $(this).attr("data-selected-ppmp-id");

        alert("Edit Selected PPMP id: "+ selected_ppmp_id);
    });


});

