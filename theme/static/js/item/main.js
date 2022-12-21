
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

    $(".pagination").on('click', function(){
        const page_no = $(this).attr('page-number');
        paging(page_no);
    });

    $("#clear_search").on('click', function(){
        let url = new URL(window.location.href);
        let search_params = url.searchParams;
        search_params.delete('keyword');
        url.search = search_params.toString();
        window.location.href = url.toString();
    });

    $(".modal_close").on('click', function(){
        $("#category-checkbox-container").empty();
    });

    $("#new-item-form input[name=search_category]").autocomplete({
        autoFocus: true,
        minLength:2,
        source: base_url + "/api/categories",
        select: function(event, ui){
            var category_selected = ui.item;
            
            var checkbox = categoryCheckbox(category_selected['code'], category_selected['value']);         

            $("#category-checkbox-container").append(checkbox);
            
        }
    });

    $("#new-item-form").submit(function(e){
        e.preventDefault();
        var data = $(this).serializeArray();

        
        sendRequest({
            method: 'POST',
            url:"/api/item/add",
            data:data,
            done : function(data){
                window.location.reload();
            },
        })
    });
});