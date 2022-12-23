$(document).ready(function(){
   $("#create_ppmp_form").on('submit', function(e){
        e.preventDefault();
        let data = $(this).serializeArray();

        console.log(data);
        
        sendRequest({
         path : "/api/add/ppmp",
         method : "POST",
         data : data,
         done : function (data){
            // console.log(data);
            window.location.reload();
         }
        });
   });

   $(".cost_center_list").on('click', function(e){
      e.preventDefault();
      let cost_center_id = $(this).attr("data-cost-center-code");
      
      window.location.href = base_url + "/home/ppmp/costcenter/" + cost_center_id + "/";
   });

   $(".cost_center_ppmp_list").on('click', function(){
      let ppmp = $(this).attr("data-ppmp-id");

      window.location.href = base_url + "/home/ppmp/costcenter/ppmp/" + ppmp;
   });

   $("#id_cc_ppmp_year").on("change", function(e){
      e.preventDefault();
      let selected_year = $(this).find(":selected").val();
      
      window.location.href = base_url + window.location.pathname + "?year=" + selected_year;
   });
});