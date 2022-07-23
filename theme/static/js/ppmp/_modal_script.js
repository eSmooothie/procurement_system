var base_url = window.location.origin;

$(document).ready(function(){
    toggle_create_modal();

    $("#select-category-input").autocomplete({
        autoFocus: true,
        minLength:2,
        source: base_url + "/api/categories/search",
        select: function(event, ui){
            var category_selected = ui.item;
            var cc_id = $("#modal_cost_center_paragraph").attr("data-cc-id");
            var ppmp_id = $("#modal_cost_center_paragraph").attr("data-ppmp-id");
            var sof_id = $("#modal_sof_p").attr("data-sof-id");
            
            getCostCenterPPMPDetails(sof_id, cc_id, category_selected.id, ppmp_id);
        }
    });
});

var getCostCenterPPMPDetails  = function getCostCenterPPMPDetails(sof_id, cc_id, cat_id, ppmp_id){
    $("#ppmp_item_list").removeClass("hidden");

    $.ajax({
        url: base_url + "/api/cost_center/ppmp_detail",
        method: "GET",
        data:{
            cat_id : cat_id,
            cc_id : cc_id,
            sof_id : sof_id,
            ppmp_id : ppmp_id
        },
    }).done(function(data){
        console.log(data);

        
        var th = $("<th></th>").addClass("px-3 py-2 font-medium text-gray-900 dark:text-white whitespace-nowrap").attr("scope","row").text("TEST");
        var td = $("<td></td>").addClass("px-3 py-2");
        var tr = $("<tr></tr>").addClass("bg-white border-b hover:cursor-pointer").attr("id",1).append(th,td);
        $("#order_details_tbody").append(tr)
    }).fail(function(xhr, text_status, error_code){
        console.log(xhr);
    })
}

function toggle_create_modal(){
    // set the modal menu element
    var target = document.getElementById('create-ppmp-modal');

    // options with default values
    var options = {
        placement: 'top-center',
    };

    const modal = new Modal(target, options);

    modal.show();
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