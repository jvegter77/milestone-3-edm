document.getElementById('navbartoggler').onclick = function(event) {
   document.getElementById('mobilenav').className = "show";
};

$(document).ready(function(){
    $('.datepicker').datepicker({
        firstDay: 1,
        format: 'dd/mm/yyyy'
    });
    
  });

 $(document).ready(function(){
    $('select').formSelect();
  });