/* Diagnose add line button behavior */
$(document).ready(function(){
    $(document).on('click', '.btn-copy', function() {
        var $lastDiv = $('div[id^="div-0"]:last');
        var count = parseInt( $lastDiv.prop("id").match(/\d+/g), 10 ) + 1;

        var $newDiv = $lastDiv.clone(true).prop('id', 'div-0'+count );
        $lastDiv.after( $newDiv );

        $newDiv.find("input").each(function() {
            if ($(this).is("input")) {
              $(this).val("");
            }
        });
        $newDiv.find("a").each(function() {
            var newId = $(this).prop('id', "div-btn-0"+count);
            var newName = $(this).prop('name', "div-btn-0"+count);
            var newClass = $(this).prop('class', "fa fa-trash btn-remove");
            var newStyle = $(this).prop('style', "float:right; width:5%; height:20px; margin-right:10px; margin-top:10px;");
        });
    });

    $(document).on('click', '.btn-remove', function() {
        $(this).parent().parent().remove();
    });
});