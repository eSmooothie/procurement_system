$(document).ready(function(e){
    
    $(".cost_center_row").on('click', function(e){
        e.preventDefault();
        var cost_center_id = $(this).attr("data-cost-center-id");

        console.log(cost_center_id);
                
    });
});