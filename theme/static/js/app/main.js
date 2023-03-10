var base_url = window.location.origin;

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
    $("input[name=search_category]").autocomplete({
        autoFocus: true,
        minLength:2,
        source: base_url + "/api/categories",
        select: function(event, ui){
            var category_selected = ui.item;
            
            var checkbox = categoryCheckbox(category_selected['code'], category_selected['value']);   
            $("#search-category").val("");
            $("#category-checkbox-container").append(checkbox);
            
        }
    });

    $("#create-app-form").submit(function (e){
        e.preventDefault();

        var data = $(this).serializeArray();   

        sendRequest({
            method:"POST",
            url:"/api/app/consolidate",
            data:data,
            done:function(data){
                window.location.reload();
            },
            fail:function(err){
                console.log(err);
            }
        })
    });

    $("input[name=consolidate]","#create-app-form").change(function(){
        var val = $(this).val();
        // console.log(val);
        if(val == 1){
            $("#search-category").attr({
                disabled: true
            }).addClass("hidden").removeClass("block").val("");
            $("#category-checkbox-container").empty();
        }else{
            $("#search-category").attr({
                disabled: false
            }).addClass("block").removeClass("hidden");
        }
    });
});