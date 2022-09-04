var base_url = window.location.origin;

$(document).ready(function(){
    // toggle_create_modal();

    $("#select-category-input").autocomplete({
        autoFocus: true,
        minLength:2,
        source: base_url + "/api/categories",
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

        // console.log(data.budget);
        $("#order_details_tbody").empty();

        // display current budget for that ppmp
        const cc_curr_budget = (data.budget.length !== 0)? data.budget[0].curr_budget : "NO BUDGET SET";
        $("#cc_ppmp_budget").text(moneyParser(cc_curr_budget));

        // display ppmp items to table
        for (const key in data.order_details) {
            if (Object.hasOwnProperty.call(data.order_details, key)) {
                const order_detail = data.order_details[key];

                const item_code = $("<th></th>").addClass("px-3 py-2 font-medium text-gray-900 dark:text-white whitespace-nowrap").attr("scope","row").text(order_detail.item_desc.item.id);
                const item_s = $("<td></td>").addClass("px-3 py-2").text("x");
                const item_name = order_detail.item_desc.item.general_name + "-" + order_detail.item_desc.spec_1
                const item_desc = $("<td></td>").addClass("px-3 py-2").text(item_name);
                const unit = $("<td></td>").addClass("px-3 py-2").text(order_detail.price.unit);
                const price = $("<td></td>").addClass("px-3 py-2").text(moneyParser(order_detail.price.price));
                let ammount = parseFloat(order_detail.first_quart_quant) * parseFloat(order_detail.price.price);
                const first_quant = $("<td></td>").addClass("px-3 py-2").text(order_detail.first_quart_quant);
                const first_ammt = $("<td></td>").addClass("px-3 py-2").text(moneyParser(ammount));
                ammount = parseFloat(order_detail.second_quart_quant) * parseFloat(order_detail.price.price);
                const second_quant = $("<td></td>").addClass("px-3 py-2").text(order_detail.second_quart_quant);
                const second_ammt = $("<td></td>").addClass("px-3 py-2").text(moneyParser(ammount));
                ammount = parseFloat(order_detail.third_quart_quant) * parseFloat(order_detail.price.price);
                const third_quant = $("<td></td>").addClass("px-3 py-2").text(order_detail.third_quart_quant);
                const third_ammt = $("<td></td>").addClass("px-3 py-2").text(moneyParser(ammount));
                ammount = parseFloat(order_detail.fourth_quart_quant) * parseFloat(order_detail.price.price);
                const fourth_quant = $("<td></td>").addClass("px-3 py-2").text(order_detail.fourth_quart_quant);
                const fourth_ammt = $("<td></td>").addClass("px-3 py-2").text(moneyParser(ammount));

                const tr = $("<tr></tr>").addClass("bg-white border-b hover:cursor-pointer").attr("id",1).append(item_code,
                    item_s, item_desc, unit, price, first_quant, first_ammt, second_quant, second_ammt, third_quant, third_ammt,
                    fourth_quant, fourth_ammt);

                $("#order_details_tbody").append(tr);
            }
        }
        
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