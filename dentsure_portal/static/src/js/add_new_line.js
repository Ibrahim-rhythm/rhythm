odoo.define('dentsure_portal.add_new_line', function(require){
    'use strict';

    $(document).ready(function () {
        $('#add_line_button').click(function () {
            var $rowLines = $('#row-line');
            var $newLine = $('<div>').addClass('row-line');
            $newLine.append('<select name="mouth_sector"><option value="">Quadrant</option><option value="upper_right">Upper Right</option><option value="upper_left">Upper Left</option><option value="lower_right">Lower Right</option><option value="lower_left">Lower Left</option></select>');
            $newLine.append('<select name="tooth_number"><option value="">Tooth Num</option><option value="A">A</option><option value="B">B</option><option value="C">C</option><option value="D">D</option><option value="E">E</option><option value="F">F</option><option value="H">H</option></select>');
            $newLine.append('<input type="text" id="notes"name="notes" placeholder="Description"class="field-size"/>');
            $rowLines.append($newLine);
        });
    });
});
//    function myCreateFunction() {
//      var table = document.getElementById("myTable");
//      var row = table.insertRow(0);
//      var cell1 = row.insertCell(0);
//      var cell2 = row.insertCell(1);
//      cell1.innerHTML = "NEW CELL1";
//      cell2.innerHTML = "NEW CELL2";
//}
//insertCell
//function myDeleteFunction() {
//  document.getElementById("myTable").deleteRow(0);
//}

    //
//    var current_page = window.location.href
//
//    if (current_page.includes('/dentsure/clinic')){
//
//        const ajax = require('web.ajax');
//        const core = require('web.core');
//        const selection = document.getElementById('service_selection');
//        const service_form_group = document.getElementById('service_form_group');
//        const add_line_button = document.getElementById('add_line_button');
//
//        // add line code
//        var row_id = 1
//        add_line_button.addEventListener('click', function() {
//            row_id = row_id + 1
//            console.log("line added in: ",service_form_group)
//            // row
//            var row = document.createElement('div');
//            row.setAttribute('class','row');
//            row.setAttribute('style','margin-top:5px;')
//            row.setAttribute('id',row_id)
//            // col-6
//            var col6 = document.createElement('div');
//            col6.setAttribute('class','col-5');
//            var added_selection = document.createElement('select');
//            added_selection.setAttribute('class','form-control service_selection custom-select')
//            // add options to selection
//            quadrants.forEach(quadrant => {
//                // create option
//                var option = document.createElement('option');
//                option.setAttribute('value',quadrant['id']);
//                option.setAttribute('name' ,'quadrant_id_' + quadrant['id'])
//                added_selection.setAttribute('name' ,'quadrant_id_' + quadrant['id'])
//                var code = ''
//                    if (quadrant['default_code'] != false){
//                        code = quadrant['default_code']
//                    }
//                var option_text = document.createTextNode(quadrant['name'] + ' [' + code + ']')
//                option.appendChild(option_text)
//                // append option to added_selection
//                added_selection.appendChild(option)
//            });
//            added_selection.setAttribute('name' ,'quadrant_id_' + quadrants[0]['id'])
//            col6.appendChild(added_selection);
//
//
//            // col-1 ( the delete button )
//            var col1 = document.createElement('div')
//            col1.setAttribute('class','col-1 text-center')
//            col1.setAttribute('style','background:#ff0303; border-radius:10px')
//            // delete row
//            var delete_row = document.createElement('i');
//            delete_row.setAttribute('class','fa fa-trash')
//            delete_row.setAttribute('style','color:white');
//            // var delete_text = document.createTextNode("delete");
//            // delete_row.appendChild(delete_text);
//
//
//            col1.addEventListener('click',function(){
//                col1.parentNode.remove();
//            })
//            col1.appendChild(delete_row);
//            // append the two cols i nrow
//            row.appendChild(col6);
//            // append row to form gorup
//            service_form_group.appendChild(row);
//
//        });
//    }
//});