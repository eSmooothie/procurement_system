var base_url = window.location.origin;

function create_ppmp_modal_activity(){
    const _target = document.getElementById('create-ppmp-modal');
    const _opt = {
        backdropClasses: 'bg-gray-900 bg-opacity-50 dark:bg-opacity-80 fixed inset-0 z-40',
        onHide: () => {
            let ppmp_year = getUrlParameter("ppmp_year");
            let ppmp_id = getUrlParameter("ppmp_id");
            let path = window.location.pathname;
            window.location.href = base_url + path + "?ppmp_year="+ ppmp_year +"&ppmp_id=" + ppmp_id; 
        },
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

function orderdetail_item_log_message_modal(){
    const _target = document.getElementById('view_log_modal');
    const _opt = {
        backdropClasses: 'bg-gray-900 bg-opacity-50 dark:bg-opacity-80 fixed inset-0 z-[44]',
    };

    const _modal = new Modal(_target, _opt);

    $("#order_details_tbody").on("click", ".view_item_log", function(){
        let tr_dom = $(this).parent().parent();
        // do something
        
        $.ajax({
            headers: {'X-CSRFToken': csrftoken},
            url: base_url + '/api/orderitem/logs',
            method: "GET",
            data:{"orderitem_id":$(tr_dom).attr("data-order-detail-id")},
        }).done(function(data){
            $("#log_item_name").text(data['item_name']);
            log_records = data['log_records'];
            orderitem_status = data['status'];

            $("#app_status").text(orderitem_status['app']);
            $("#received_quotation_status").text(orderitem_status['received_quotation']);
            $("#award_winning_bidder_status").text(orderitem_status['award_winning']);
            $("#obligate_po_status").text(orderitem_status['obligate_po']);
            $("#served_status").text(orderitem_status['served']);

            $("#log_records").empty();
            for (const key in log_records) {
                if (Object.hasOwnProperty.call(log_records, key)) {
                    const record = log_records[key];
                    const log_msg = $("<p></p>").append(
                        $("<span></span>").addClass("font-semibold mr-1").text("["+record['datetime']+"] : "),
                        $("<span></span>").text("logged at " + record['cc_name'])
                    );

                    $("#log_records").append(log_msg);
                }
            }

        }).fail(function(err){
            console.log(err);
        });

        _modal.toggle();
    });

    $(".close-view-log-modal").on("click", function(){
        
        _modal.toggle();
    });
}

$(document).ready(function(){
    // toggle_create_modal();
    create_ppmp_modal_activity();
    
    orderdetail_item_log_message_modal();

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
            
            let ppmp_year = getUrlParameter("ppmp_year");
            let ppmp_id = getUrlParameter("ppmp_id");
            let path = window.location.pathname;
            window.location.href = base_url + path + "?ppmp_year="+ ppmp_year +"&ppmp_id=" + ppmp_id + "&cat_id=" + category_selected.id + "&toogle_ppmp_modal="+1;
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
            $("#add_new_data_btn_selected_ppmp").removeClass("hidden");

            $("#edit_btn_selected_ppmp").addClass("hidden");
            $("#suggest_item_btn_selected_ppmp").addClass("hidden");
            $("#print_btn_selected_ppmp").addClass("hidden");
            $(".view_log_container").addClass("hidden");
            // parent > selector > selector
            $("#order_details_tbody").children('tr').children('.editable').each(function(){
                const curr_val = $(this).text();
                $(this).empty();
                const input_elem = $("<input />").addClass("w-full border border-b p-1 update_quant_val").attr({type:"number",min:"0", value:curr_val});
                $(this).append(input_elem);
            });
        }
    });

    // update quantity
    $("#order_details_tbody").on("input", ".update_quant_val", function(){
        const item_node = $(this).parents()[1];
        const quant = $(this).parent().attr("data-quant");
        const val = $(this).val();
        $(item_node).attr(quant, val);
    });

    //cancel
    $("#cancel_btn_selected_ppmp").on("click", function(){
        $("#edit_btn_selected_ppmp").removeClass("hidden");
        $("#suggest_item_btn_selected_ppmp").removeClass("hidden");
        $("#print_btn_selected_ppmp").removeClass("hidden");
        $(".view_log_container").removeClass("hidden");

        $(".delete_item_container").addClass("hidden");
        $("#tfoot_tr").addClass("hidden");
        $("#save_btn_selected_ppmp").addClass("hidden");
        $("#cancel_btn_selected_ppmp").addClass("hidden");
        $("#add_new_data_btn_selected_ppmp").addClass("hidden");

        $("#order_details_tbody").children('tr').children('.editable').each(function(){
            const curr_val = $(this).children().first().val();
            $(this).empty();
            $(this).text(curr_val);
        });

        $("#order_details_tbody").children('tr.new_order_item_data').each(function(){
            $(this).remove();
        });
    });

    //save
    $("#save_btn_selected_ppmp").on("click", function(){
        const updated_orderitem = $("#order_details_tbody").children("tr");
        
        var updated_orderitem_list = [];
        
        $("#order_details_tbody").children("tr").each(function(){
            const item_id = $(this).attr("id");
            const first = $(this).attr("data-first-quant");
            const second = $(this).attr("data-second-quant");
            const third = $(this).attr("data-third-quant");
            const fourth = $(this).attr("data-fourth-quant");
            const price_id = $(this).attr("data-price-id");

            const data = {
                'item_id' : item_id,
                'first' : first,
                'second' : second,
                'third' : third,
                'fourth' : fourth,
                'price_id': price_id,
            }

            updated_orderitem_list.push(data);
        });
        // console.log(updated_orderitem_list);
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

    //remove
    $("#order_details_tbody").on("click", ".delete_item", function(){
        var item_node = $(this).parents()[1];
        $(item_node).remove();
    });

    $("#add_new_data_btn_selected_ppmp").on("click", function(e){
        const order_detail_node = $("#order_details_tbody");

        const input_label = $("<label></label>").attr({for:"add_btn_search_item"}).text("Search Item");
        const input_field = $("<input />").attr({type:"text",placeholder:"Search item"}).addClass("w-full add_btn_search_item")

        const td = $("<td></td>").addClass("px-3 py-2").attr({colspan:"5"}).append(input_label, input_field);
        const tr = $("<tr></tr>").addClass("bg-white border-b hover:cursor-pointer text-xs order_item_details new_order_item_data").append(td);

        order_detail_node.append(tr);

        $("#ppmp_item_list").animate({scrollTop: $(tr).offset().top}, 1000);
    });

    $("#order_details_tbody").on("input", ".add_btn_search_item", function(){
        $(this).autocomplete({
            autoFocus: true,
            minLength:2,
            source: base_url + "/api/items?cat_id=" + getUrlParameter("cat_id"),
            select: function(event, ui){
                var selected_item = ui.item;
                
                // console.log(selected_item);

                const tr = generateTableRowOrderItemDetails({
                    item_id:selected_item.item_id,
                    item_name:selected_item.value,
                    price:selected_item.price,
                    price_unit:selected_item.unit,
                    generic_item_id:selected_item.general_item_id,
                    price_id:selected_item.price_id,
                    is_new:true,
                });

                $(tr).insertBefore($(this).parents()[1]);
                $(this).parents()[1].remove();
                
            }
        });
    });


    $("#print_btn_selected_ppmp").on("click", function(e){
        e.preventDefault();
        var is_active = ($(this).attr("data-is-active") === "true");

        if(is_active){
            data = {
                cc_id : $("#modal_cost_center_paragraph").attr("data-cc-id"),
                ppmp_yr : getUrlParameter("ppmp_year"),
                ppmp_id : getUrlParameter("ppmp_id"),
                cat_id : getUrlParameter("cat_id")
            }
        
            $.ajax({
                headers: {'X-CSRFToken': csrftoken},
                url: base_url + "/pdf/download/ppmp",
                method: "POST",
                data:data,
                xhrFields: {
                    responseType: 'blob'
                },
            }).done(function(data){
                var a = document.createElement('a');
                var url = window.URL.createObjectURL(data);
                a.href = url;
                a.download = "ppmp_report.pdf";
                document.body.append(a);
                a.click();
                a.remove();
                window.URL.revokeObjectURL(url);
            }).fail(function(xhr){
                console.log(xhr);
            });
        }
    });


});


var generateTableRowOrderItemDetails = function generateTableRowOrderItemDetails({orderdetail_id="", item_id="",item_name="",price_unit="",generic_item_id="",
price="", price_id="", first_quant="0",second_quant="0",third_quant="0",fourth_quant="0",is_new=false}){
    
    const item_code_td = $("<th></th>").addClass("px-3 py-2 font-medium text-gray-900 dark:text-white whitespace-nowrap").attr("scope","row").text(generic_item_id);
    
    const item_desc_td = $("<td></td>").addClass("px-3 py-2").attr("colspan","2").text(item_name);
    const unit_td = $("<td></td>").addClass("px-3 py-2").text(price_unit);
    const price_td = $("<td></td>").addClass("px-3 py-2").text(moneyParser(price));
    
    let ammount = parseFloat(first_quant) * parseFloat(price);
    const first_quant_td = $("<td></td>").addClass("px-3 py-2 editable").attr("data-quant","data-first-quant").text(first_quant);
    const first_ammt_td = $("<td></td>").addClass("px-3 py-2").text(moneyParser(ammount));
    
    ammount = parseFloat(second_quant) * parseFloat(price);
    const second_quant_td = $("<td></td>").addClass("px-3 py-2 editable").attr("data-quant","data-second-quant").text(second_quant);
    const second_ammt_td = $("<td></td>").addClass("px-3 py-2").text(moneyParser(ammount));
    
    ammount = parseFloat(third_quant) * parseFloat(price);
    const third_quant_td = $("<td></td>").addClass("px-3 py-2 editable").attr("data-quant","data-third-quant").text(third_quant);
    const third_ammt_td = $("<td></td>").addClass("px-3 py-2").text(moneyParser(ammount));
    
    ammount = parseFloat(fourth_quant) * parseFloat(price);
    const fourth_quant_td = $("<td></td>").addClass("px-3 py-2 editable").attr("data-quant","data-fourth-quant").text(fourth_quant);
    const fourth_ammt_td = $("<td></td>").addClass("px-3 py-2").text(moneyParser(ammount));
    
    const log_opt_td = $("<td></td>").addClass("px-3 py-2 view_log_container").append(
        $("<button></button>").addClass("view_item_log text-blue-500 hover:underline").text("logs")
    ).attr({
        'ppmp_id': getUrlParameter("ppmp_id"),
        'item_id' : item_id
    });

    if(is_new){
        $(log_opt_td).addClass("hidden");
    }

    const delete_opt_td = $("<td></td>").addClass("px-3 py-2 hidden delete_item_container").append(
        $("<button></button>").addClass("delete_item hover:underline text-red-500").text("Remove")
    );

    const tr = $("<tr></tr>").addClass("bg-white border-b hover:cursor-pointer text-xs order_item_details").attr("id",item_id).append(
        item_code_td, item_desc_td, unit_td, price_td, first_quant_td, first_ammt_td, second_quant_td, 
        second_ammt_td, third_quant_td, third_ammt_td, fourth_quant_td, fourth_ammt_td, delete_opt_td, log_opt_td);
    
    tr.attr({
        "data-order-detail-id":orderdetail_id,
        "data-first-quant":first_quant,
        "data-second-quant":second_quant,
        "data-third-quant":third_quant,
        "data-fourth-quant":fourth_quant,
        "data-price-id":price_id,
    });

    if(is_new){
        delete_opt_td.removeClass("hidden");

        $(tr).addClass("new_order_item_data");

        $(tr).children('.editable').each(function(){
            const curr_val = $(this).text();
            $(this).empty();
            const input_elem = $("<input />").addClass("w-full border border-b p-1 update_quant_val").attr({type:"number",min:"0", value:curr_val});
            $(this).append(input_elem);
        });
    }

    return tr
}


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
        // console.log(data);

        // console.log(data.budget);
       

        // display current budget for that ppmp
        const cc_curr_budget = (data.budget.length !== 0)? data.budget[0].curr_budget : 0;
        $("#cc_ppmp_budget").text(moneyParser(cc_curr_budget));

        if (data.order_details.length == 0){
            $("#order_details_no_data").removeClass("hidden");
        }else{
            $("#order_details_tbody").empty();
        }

        $("#order_details_thead").removeClass("hidden");
        // display ppmp items to table
        for (const key in data.order_details) {
            if (Object.hasOwnProperty.call(data.order_details, key)) {
                const order_detail = data.order_details[key];
                
                let item_name = order_detail.item_desc.item.general_name;

                if(order_detail.item_desc.spec_1 !== "None"){
                    item_name += "-" + order_detail.item_desc.spec_1;
                }
                if(order_detail.item_desc.spec_2 !== "None"){
                    item_name += "-" + order_detail.item_desc.spec_2;
                }
                if(order_detail.item_desc.spec_3 !== "None"){
                    item_name += "-" + order_detail.item_desc.spec_3;
                }
                if(order_detail.item_desc.spec_4 !== "None"){
                    item_name += "-" + order_detail.item_desc.spec_4;
                }
                if(order_detail.item_desc.spec_5 !== "None"){
                    item_name += "-" + order_detail.item_desc.spec_5;
                }

                const tr = generateTableRowOrderItemDetails({
                    orderdetail_id:order_detail.id,
                    item_id:order_detail.item_desc.id,
                    item_name:item_name,
                    price_unit:order_detail.price.unit,
                    price:order_detail.price.price,
                    generic_item_id:order_detail.item_desc.item.id,
                    first_quant:order_detail.first_quart_quant,
                    second_quant:order_detail.second_quart_quant,
                    third_quant:order_detail.third_quart_quant,
                    fourth_quant:order_detail.fourth_quart_quant,
                    price_id:order_detail.price.id,
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