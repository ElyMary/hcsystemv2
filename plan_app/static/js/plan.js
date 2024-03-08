$(function(){
    //Auto creation of Plan Type Name
    function concat_for_plantype(){
        var roomcode = $('#roomcode').find(":selected").html(), premiumamount = $('#premiumamount').val();

        //Value will be reflected to the textbox that is hidden
        $('#plantype').val(roomcode + '-' + premiumamount);
        //Value will also be reflected to the textbox that is shown as well
        $('#plantype1').val(roomcode + '-' + premiumamount);

    }
    $('#roomcode').on('change', concat_for_plantype);
    $('#premiumamount').on('keyup', concat_for_plantype);
    //End of Function: Auto creation of Plan Type

});

$( document ).ready(function() {
    //Get checkbox value
    ischecked = 0;
    $('#withtophospital').val(ischecked);
    
    function get_checkbox_value(){
        ischecked = this.checked ? 1 : 0
        $('#withtophospital').val(ischecked);
    }
    $('#withtophospital1').on('change', get_checkbox_value);
    //End of Function: Get checkbox value
});