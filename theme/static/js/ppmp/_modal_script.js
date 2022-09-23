var base_url = window.location.origin;

function create_ppmp_modal_activity(){
    const _target = document.getElementById('create-ppmp-modal');
    const _opt = {
        backdropClasses: 'bg-gray-900 bg-opacity-50 dark:bg-opacity-80 fixed inset-0 z-40',
        onToggle: () => {
            
        },
    };
    const _modal = new Modal(_target, _opt);

    var is_up = getUrlParameter("toogle_ppmp_modal");

    if(Boolean(is_up)){
        _modal.toggle();
    }

    $("#create_selected_ppmp_btn").on('click', function(e){
        _modal.toggle();
    });

    $(".close-create-ppmp-modal").on('click', function(e){
        _modal.toggle();
    });
}

function toggle_print_btn(){
    let is_active = ($("#print_btn_selected_ppmp").attr("data-is-active") === "true");

    if(is_active){
        $("#print_btn_selected_ppmp").addClass("bg-gray-400 hover:bg-gray-400 focus:ring-gray-300");
        $("#print_btn_selected_ppmp").removeClass("bg-blue-700 hover:bg-blue-800 focus:ring-blue-300");
        $("#print_btn_selected_ppmp").attr("data-is-active", false);
    }else{
        $("#print_btn_selected_ppmp").removeClass("bg-gray-400 hover:bg-gray-400 focus:ring-gray-300");
        $("#print_btn_selected_ppmp").addClass("bg-blue-700 hover:bg-blue-800 focus:ring-blue-300");
        $("#print_btn_selected_ppmp").attr("data-is-active", true);
    }
}

$(document).ready(function(){
    // toggle_create_modal();
    create_ppmp_modal_activity();
    
    if($("#select-category-input").val() !== ""){
        var cat_id = getUrlParameter("cat_id");
        var cc_id = $("#modal_cost_center_paragraph").attr("data-cc-id");
        var ppmp_id = $("#modal_cost_center_paragraph").attr("data-ppmp-id");
        var sof_id = $("#modal_sof_p").attr("data-sof-id"); 
        getCostCenterPPMPDetails(sof_id, cc_id, cat_id, ppmp_id);
    }

    $("#select-category-input").autocomplete({
        autoFocus: true,
        minLength:2,
        source: base_url + "/api/categories",
        select: function(event, ui){
            var category_selected = ui.item;
            
            window.location.href = window.location.href + "&cat_id=" + category_selected.id + "&toogle_ppmp_modal="+1;
        }
    });

    $("#edit_btn_selected_ppmp").on("click", function(e){
        e.preventDefault();
        var is_active = ($(this).attr("data-is-active") === "true");

        if(is_active){
            $(".delete_item_container").removeClass("hidden");
            $("#tfoot_tr").removeClass("hidden");
            $("#save_btn_selected_ppmp").removeClass("hidden");
            $("#cancel_btn_selected_ppmp").removeClass("hidden");

            $("#edit_btn_selected_ppmp").addClass("hidden");
            $("#suggest_item_btn_selected_ppmp").addClass("hidden");
            $("#print_btn_selected_ppmp").addClass("hidden");
            // parent > selector > selector
            $("#order_details_tbody").children('tr').children('.editable').each(function(){
                const curr_val = $(this).text();
                $(this).empty();
                const input_elem = $("<input />").addClass("w-full border border-b p-1 update_quant_val").attr({type:"number",min:"0", value:curr_val});
                $(this).append(input_elem);
            });
        }
    });

    $("#order_details_tbody").on("input", ".update_quant_val", function(){
        const item_node = $(this).parents()[1];
        const quant = $(this).parent().attr("data-quant");
        const val = $(this).val();
        $(item_node).attr(quant, val);
    });

    $("#cancel_btn_selected_ppmp").on("click", function(){
        $("#edit_btn_selected_ppmp").removeClass("hidden");
        $("#suggest_item_btn_selected_ppmp").removeClass("hidden");
        $("#print_btn_selected_ppmp").removeClass("hidden");

        $(".delete_item_container").addClass("hidden");
        $("#tfoot_tr").addClass("hidden");
        $("#save_btn_selected_ppmp").addClass("hidden");
        $("#cancel_btn_selected_ppmp").addClass("hidden");

        $("#order_details_tbody").children('tr').children('.editable').each(function(){
            const curr_val = $(this).children().first().val();
            $(this).empty();
            $(this).text(curr_val);
        });
    });

    $("#save_btn_selected_ppmp").on("click", function(){
        const updated_orderitem = $("#order_details_tbody").children("tr");
        
        var updated_orderitem_list = [];
        
        $("#order_details_tbody").children("tr").each(function(){
            const item_id = $(this).attr("id");
            const first = $(this).attr("data-first-quant");
            const second = $(this).attr("data-second-quant");
            const third = $(this).attr("data-third-quant");
            const fourth = $(this).attr("data-fourth-quant");

            const data = {
                'item_id' : item_id,
                'first' : first,
                'second' : second,
                'third' : third,
                'fourth' : fourth
            }

            updated_orderitem_list.push(data);
        });
        send_post_request({
            url:"/api/orderitem/update",
            data: {
                "item_list" : updated_orderitem_list,
                "ppmp_id" : getUrlParameter("ppmp_id"),
                "cat_id" : getUrlParameter("cat_id"),
            },
            done: function(data){window.location.reload();}
        });
    });

    $("#print_btn_selected_ppmp").on("click", function(e){
        e.preventDefault();
        var is_active = ($(this).attr("data-is-active") === "true");

        if(is_active){
            console.log("PRINT ME");
        }
    });
});



var getCostCenterPPMPDetails  = function getCostCenterPPMPDetails(sof_id, cc_id, cat_id, ppmp_id){
    $("#ppmp_item_list").removeClass("hidden");

    window.sessionStorage.setItem("selected_ppmp_sof_id", sof_id);
    window.sessionStorage.setItem("selected_ppmp_cc_id", cc_id);
    window.sessionStorage.setItem("selected_ppmp_cat_id", cat_id);
    window.sessionStorage.setItem("selected_ppmp_ppmp_id", ppmp_id);

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
        const cc_curr_budget = (data.budget.length !== 0)? data.budget[0].curr_budget : 0;
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
                const first_quant = $("<td></td>").addClass("px-3 py-2 editable").attr("data-quant","data-first-quant").text(order_detail.first_quart_quant);
                const first_ammt = $("<td></td>").addClass("px-3 py-2").text(moneyParser(ammount));
                
                ammount = parseFloat(order_detail.second_quart_quant) * parseFloat(order_detail.price.price);
                const second_quant = $("<td></td>").addClass("px-3 py-2 editable").attr("data-quant","data-second-quant").text(order_detail.second_quart_quant);
                const second_ammt = $("<td></td>").addClass("px-3 py-2").text(moneyParser(ammount));
                
                ammount = parseFloat(order_detail.third_quart_quant) * parseFloat(order_detail.price.price);
                const third_quant = $("<td></td>").addClass("px-3 py-2 editable").attr("data-quant","data-third-quant").text(order_detail.third_quart_quant);
                const third_ammt = $("<td></td>").addClass("px-3 py-2").text(moneyParser(ammount));
                
                ammount = parseFloat(order_detail.fourth_quart_quant) * parseFloat(order_detail.price.price);
                const fourth_quant = $("<td></td>").addClass("px-3 py-2 editable").attr("data-quant","data-fourth-quant").text(order_detail.fourth_quart_quant);
                const fourth_ammt = $("<td></td>").addClass("px-3 py-2").text(moneyParser(ammount));
                
                const delete_opt = $("<td></td>").addClass("px-3 py-2 hidden delete_item_container").append(
                    $("<button></button>").addClass("delete_item hover:underline text-red-500").text("Remove")
                    );

                const tr = $("<tr></tr>").addClass("bg-white border-b hover:cursor-pointer text-xs order_item_details").attr("id",order_detail.item_desc.id).append(item_code,
                    item_s, item_desc, unit, price, first_quant, first_ammt, second_quant, second_ammt, third_quant, third_ammt,
                    fourth_quant, fourth_ammt,delete_opt);
                
                tr.attr({
                    "data-first-quant":order_detail.first_quart_quant,
                    "data-second-quant":order_detail.second_quart_quant,
                    "data-third-quant":order_detail.third_quart_quant,
                    "data-fourth-quant":order_detail.fourth_quart_quant
                });

                $("#order_details_tbody").append(tr);
            }
        }
        
        $("#edit_btn_selected_ppmp").removeClass("bg-gray-400 hover:bg-gray-400 focus:ring-gray-300");
        $("#edit_btn_selected_ppmp").addClass("bg-blue-700 hover:bg-blue-800 focus:ring-blue-300");
        $("#edit_btn_selected_ppmp").attr("data-is-active", true);

        toggle_print_btn();

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

function send_post_request({url="",data={}, done=function(data){console.log(data);}, fail=function(xhr){console.log(xhr);}}){
    data_to_send = JSON.stringify(data);
    $.ajax({
        headers: {'X-CSRFToken': csrftoken},
        url: base_url + url,
        method: "POST",
        data:{"data":data_to_send},
        dataType: 'html',
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