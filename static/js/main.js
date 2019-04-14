document.getElementById('navbartoggler').onclick = function(event) {
   document.getElementById('mobilenav').className = "show";
}

document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('.datepicker');
    var instances = M.Datepicker.init(elems, open);
  });
