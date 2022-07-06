document.addEventListener("DOMContentLoaded", function() {
    console.log("test datefields");
    
    
   





function DateControl(){
    var id_date2 = document.getElementById('id_date2').type="date";
    id_date2.type="date";
    var id_bt_date = document.getElementById('id_badanietechniczne_data_konc');
    id_bt_date.type="date";
  //  <input type="text" name="badanietechniczne_data_konc" value="2022-09-23" required="" id="id_badanietechniczne_data_konc">
    
   console.log(id_bt_date);
};  
    
    DateControl();

var control = document.getElementsByClassName("form-control");

console.log(control);
});