var $input = $('.datepicker').pickadate();
var picker = $input.pickadate('picker');
picker.set('select', new Date(2018, 5, 4));

this.instanceDatepicker = new M.Datepicker(this.elDatepicker.nativeElement, {
        defaultDate: new Date(2018,5,4),
        setDefaultDate: true,
        selectMonths: true,
        selectYears: 200, 
        format: "dd/mm/yyyy"
    });