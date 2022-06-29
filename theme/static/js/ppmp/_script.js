$(document).ready(function(e){
    var base_url = window.location.origin;

    $(".cost_center_row").on('click', function(e){
        e.preventDefault();
        var cost_center_id = $(this).attr("data-cost-center-id");
        
        window.location.href = base_url + "/home/ppmp/costcenter?cc_id=" + cost_center_id;
    });
});