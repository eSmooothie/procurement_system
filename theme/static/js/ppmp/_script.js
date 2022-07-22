$(document).ready(function(e){
    toggle_create_modal();

    var base_url = window.location.origin;

    $(".cost_center_list").on('click', function(e){
        e.preventDefault();
        var cost_center_id = $(this).attr("data-cost-center-id");
        
        window.location.href = base_url + "/home/ppmp/costcenter/" + cost_center_id + "/";
    });

    $(".cost_center_ppmp_list").on('click', function(e){
        e.preventDefault();

        var cc_ppmp_id = $(this).attr("data-ppmp-id");

        var selected_year = getUrlParameter('ppmp_year');

        if(!selected_year){
            selected_year = $("#id_cc_ppmp_year option:selected").val();
        }
        
        window.location.href = base_url + window.location.pathname + "?ppmp_year=" + selected_year + "&ppmp_id=" + cc_ppmp_id;
    });

    $("#id_cc_ppmp_year").on("change", function(e){
        e.preventDefault();
        var selected_year = $(this).find(":selected").val();
        
        var cc_id = getUrlParameter('cc_id');
        
        window.location.href = base_url + window.location.pathname + "?ppmp_year=" + selected_year;
    });

    $("#edit_selected_ppmp_btn").on("click", function(e){
        e.preventDefault();

        var selected_ppmp_id = $(this).attr("data-selected-ppmp-id");

        alert("Edit Selected PPMP id: "+ selected_ppmp_id);
    });

    $("#select-category-input").autocomplete({
        autoFocus: true,
        minLength:2,
        source: base_url + "/api/categories/search",
        select: function(event, ui){
            var category_selected = ui.item;
            console.log(category_selected);

            $("#ppmp_item_list").removeClass("hidden");
            
        }
    });
});

function toggle_create_modal(){
    // set the modal menu element
    var target = document.getElementById('create-ppmp-modal');

    // options with default values
    var options = {
    placement: 'top-center',
        onHide: () => {
            console.log('modal is hidden');
        },
        onShow: () => {
            console.log('modal is shown');
        },
        onToggle: () => {
            console.log('modal has been toggled');
        }
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