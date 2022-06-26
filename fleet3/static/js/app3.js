document.addEventListener("DOMContentLoaded", function() {


var rows = document.querySelectorAll(".rows");




function TurnOnLightRows(){
    for(var i = 0; i < rows.length; i++) {
        rows[i].addEventListener("mouseover", function(event) {
        this.style.backgroundColor = "cadetblue";
        });
        }
};  
    
function TurnOffLightRows(){
    for(var i = 0; i < rows.length; i++) {
        rows[i].addEventListener("mouseout", function(event) {
        this.style.backgroundColor = "white";
        });
        }
};  
       
TurnOnLightRows();
TurnOffLightRows();

    
    });



    

