var is_edit=false;

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

var sendRequest = function sendRequest({
    method = "GET",
    path = "",
    data = {},
    done = function(data){},
    fail = function(msg){}
 }){
 
    $.ajax({
       headers: {'X-CSRFToken': csrftoken},
       url: base_url + path,
       method: method,
       data: data,
   }).done(done).fail(fail);
 }

 var categoryCheckbox = function categoryCheckbox(cat_code, cat_name){
   // console.log(cat_name)
   const li = $("<li></li>").addClass("w-full rounded-t-lg border-b border-gray-200");
   const div = $("<div></div>").addClass("flex items-center pl-3");
   const checkbox = $("<input />").attr({
       name:'categories[]',
       id:cat_code+"-checkbox",
       type:'checkbox',
       checked:true,
       value:cat_code
   }).addClass("w-4 h-4 text-blue-600 bg-gray-100 rounded border-gray-300 focus:ring-blue-500");
   const label = $("<label></label>").attr({
       for:cat_code+"-checkbox",
   }).addClass("py-3 ml-2 w-full text-sm font-medium text-gray-900").text(cat_name);

   div.append(checkbox, label);
   li.append(div)

   return li
}

$(document).ready(function(){
   $("#search-category").autocomplete({
      autoFocus: true,
      minLength:2,
      source: base_url + "/api/categories",
      select: function(event, ui){
         let category_selected = ui.item;

         $("input[name=category_selected]").attr("value", category_selected.code);
         $("#search-category-form").submit();
      }
   });

   $("#req-item-form input[name=search_category]").autocomplete({
      autoFocus: true,
      minLength:2,
      source: base_url + "/api/categories",
      select: function(event, ui){
          var category_selected = ui.item;
          
          var checkbox = categoryCheckbox(category_selected['code'], category_selected['value']);         

          $("#category-checkbox-container").append(checkbox);
          
      }
  });

   $("#search-category-form").on('submit', function(e){
      let data = $(this).serializeArray();
   });

   $("#edit_ppmp_btn").on('click', function(){
      is_edit = true;
      $("#add_item_ppmp_btn").removeClass("hidden");
      $("#cancel_edit_ppmp_btn").removeClass("hidden");
      $("#save_edit_ppmp_btn").removeClass("hidden");
      $(".edit_mode").removeClass("hidden");
      $(".edit_mod").addClass("flex flex-col items-left")

      $(this).addClass("hidden");
      $("#print_ppmp_btn").addClass("hidden");
      $("#item_logs_btn").addClass("hidden");
      $(".pr_td").addClass('hidden');

      $("#orderdetails_container_tbody").children("tr").children(".editable").each(function() {
         const curr_val = $(this).text().trim();
         $(this).empty();
         const input_elem = $("<input />").addClass(" w-9 border border-b p-1 update_quant_val").attr({
            type:"number",
            min:"0",
            'data-curr-val':curr_val,
            value:curr_val
         });
         $(this).append(input_elem);
      });
   });

   add_item_ppmp_modal();
   
   $("#orderdetails_container_tbody").on('click', ".remove_item_btn", function(){
      let btn = $(this);
      let parent_node = $(this).parent().parent()[0];
      
      $(parent_node).remove();
   });

   $("#cancel_edit_ppmp_btn").on('click', function(){
      if(is_edit){
         window.location.reload();
      }
   });

   $("#save_edit_ppmp_btn").on('click', function(){
      let _data = {};
      let updated_items = [];
      let is_valid = true;

      _data['ppmp_id'] = $("#ppmp_info").attr('data-ppmp-id');
      _data['cat_code'] =  getUrlParameter("category_selected");

      $("#orderdetails_container_tbody").children("tr").each(function(){
         const is_new = $(this).hasClass("new_item");
         const quarts_elements = $(this).children(".editable");
         
         let data = {};

         data['order_id'] = $(this).attr('data-order-id');
         data['item_id'] = $(this).attr('id');

         let quant_ttl = 0;
         for (let index = 0; index < 4; index++) {
            const element = quarts_elements[index];
            let quart = $(element).attr('data-quart');
            let input_elem = $(element).children()[0];
            let updt_val = $(input_elem).val();
            
            quant_ttl += parseInt(updt_val)

            data[quart] = updt_val;
         }
         
         if(quant_ttl <= 0){
            is_valid = false;
            alert("Invalid value.");
         }
         updated_items.push(data);
      });

      if(is_valid){
    
         _data['items'] = updated_items
         // to do submit to data so server
         data_to_send = JSON.stringify(_data);

         $.ajax({
            headers: {'X-CSRFToken': csrftoken},
            url: base_url + "/api/orderitem/update",
            method: "POST",
            data:{"data":data_to_send},
            dataType: 'html',
         }).done(function(data){
            window.location.reload();
         }).fail(function(xhr){
            console.log(xhr);
         });

      }else{
         console.log("Invalid value.");
      }
   });

   $("#req-item-form").submit(function(e){
      e.preventDefault();
      var data = $(this).serializeArray();

      // console.log(data);
      sendRequest({
          method: 'POST',
          path:"/api/item/add/request",
          data:data,
          done : function(data){
            // console.log(data);
            window.location.reload();
          },
      });
  });

});

function add_item_ppmp_modal(){
   var new_item;
   const order_detail_node = $("#orderdetails_container_tbody");
   const targetEl = document.getElementById('add_item_ppmp_modal');
   const options = {
      backdropClasses: 'bg-gray-900 bg-opacity-50 dark:bg-opacity-80 fixed inset-0 z-40',
   };
   
   const modal = new Modal(targetEl, options);

   $(".close_add_item_ppmp_modal").on('click', function(){
      modal.hide();
   });

   $("#add_item_ppmp_btn").on('click', function(){
      if(!is_edit){
         return false;
      }

      modal.show();
   });

   $("#search_item").autocomplete({
      autoFocus: true,
      minLength:2,
      source: base_url + "/api/item/autocomplete_search?cat_code=" + getUrlParameter("category_selected"),
      select: function(event, ui){
         new_item = ui.item;
        
         $("#search_item_form").submit();
      }
   });

   $("#search_item_form").on('submit', function(e){
      e.preventDefault();
      
      let is_exist = false;
      order_detail_node.children('tr').each(function(){
         let id = $(this).attr('id');
   
         if(id == new_item['id']){
            is_exist = true;
            alert("Item already exist.");
         }
      });

      
      if(!is_exist){
         const new_item_tr = newOrderDetail(new_item['id'], new_item['name'], new_item['price'], new_item['unit']);

         order_detail_node.append(new_item_tr);
         
      }
   });
}

var newOrderDetail = function newOrderDetail(item_id, item_name, item_price, item_unit){
   const tr = $("<tr></tr>").addClass("bg-white border-b text-xs new_item").attr({id:item_id});
   const item_code_td = $("<th></th>").addClass("py-4 px-6 font-medium text-gray-900 whitespace-nowrap dark:text-white").attr({scope:"row"}).text(item_id);
   const item_name_td = $("<td></td>").addClass("py-4 px-6 break-words w-28").attr({colspan:"2"}).text(item_name);
   const item_unit_td = $("<td></td>").addClass("py-4 px-6").text(item_unit);
   const item_price_td = $("<td></td>").addClass("py-4 px-6").text(item_price);

   const quant = $("<td></td>").addClass("py-4 px-6 editable");
   const quant_ammount = $("<td></td>").addClass("py-4 px-6").text(0);

   const input_elem = $("<input />").addClass(" w-9 border border-b p-1 update_quant_val").attr({
      type:"number",
      min:"0",
      'data-curr-val':0,
      value:0
   });

   tr.append(item_code_td, item_name_td, item_unit_td, item_price_td);

   let quart_counter = 1;
   for (let index = 0; index < 4; index++) {
      const clone_0 = quant.clone();
      const clone_1 = quant_ammount.clone();
      const clone_2 = input_elem.clone();

      clone_0.append(clone_2)
      clone_0.attr('data-quart', quart_counter)
      quart_counter += 1;

      tr.append(clone_0, clone_1);
   }

   const rmv_btn = $("<button></button>").addClass("font-medium text-red-600 dark:text-red-500 hover:underline remove_item_btn").attr({type:"button"}).text("Remove");
   const option_td = $("<td></td>").addClass("items-center py-4 px-6 space-x-3 edit_mode");
   option_td.append(rmv_btn);

   tr.append(option_td);

   return tr
}

