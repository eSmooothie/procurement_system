
function paging(page_no){
    let url = new URL(window.location.href);
    let search_params = url.searchParams;
    search_params.set('page', page_no);

    url.search = search_params.toString();

    window.location.href = url.toString();
}

var sendRequest = function send_request({method = "GET", url="",data={}, done=function(data){console.log(data);}, fail=function(xhr){console.log(xhr);}}){

    $.ajax({
        headers: {'X-CSRFToken': csrftoken},
        url: base_url + url,
        method: method,
        data:data,
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
    const targetEl = document.getElementById('edit-item-modal');
    const options = {
        backdropClasses: 'bg-gray-900 bg-opacity-50 dark:bg-opacity-80 fixed inset-0 z-40',
    };
    const edit_item_modal = new Modal(targetEl, options);

    $(".pagination").on('click', function(){
        const page_no = $(this).attr('page-number');
        paging(page_no);
    });
    
    $(".edit_req_btn").on("click", function(){

        const item_id = $(this).attr('id');

        $("#category-checkbox-container").empty();

        sendRequest({
            method:'GET',
            data:{'item_id':item_id},
            url: '/api/item/get_request',
            done: function(data){
                let item_id = data['id'];
                let item_name = data['name'];
                let item_unit = data['unit'];
                let item_price = data['price'];

                $("#edit-item-form input[name=item_id]").val(item_id);
                $("#edit-item-form textarea[name=item_name]").val(item_name);
                $("#edit-item-form input[name=item_unit]").val(item_unit);
                $("#edit-item-form input[name=item_price]").val(item_price);

                let categories = data['categories'];
                for (const index in categories) {
                    if (Object.hasOwnProperty.call(categories, index)) {
                        const cat = categories[index];
                        const checkbox = categoryCheckbox(cat['code'], cat['name']);         

                        $("#category-checkbox-container").append(checkbox);
                    }
                }
            }
        })
        

        edit_item_modal.toggle();
    });

    $(".close_req_modal").on("click", function(){
        edit_item_modal.toggle();
    });

    $("#clear_search").on('click', function(){
        let url = new URL(window.location.href);
        let search_params = url.searchParams;
        search_params.delete('keyword');
        url.search = search_params.toString();
        window.location.href = url.toString();
    });

    $("#edit-item-form input[name=search_category]").autocomplete({
        autoFocus: true,
        minLength:2,
        source: base_url + "/api/categories",
        select: function(event, ui){
            var category_selected = ui.item;
            
            var checkbox = categoryCheckbox(category_selected['code'], category_selected['value']);         

            $("#category-checkbox-container").append(checkbox);
            
        }
    });

    $("#edit-item-form").submit(function(e){
        e.preventDefault();
        var data = $(this).serializeArray();
        console.log(data);
        
        sendRequest({
            method: 'POST',
            url:"/api/item/request/update",
            data:data,
            done : function(data){
                window.location.reload();
            },
        });
    });
});