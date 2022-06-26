document.addEventListener("DOMContentLoaded", function() {


var rows = document.querySelectorAll(".rows");

var detail = document.querySelectorAll(".detail");


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

function TurnOnSmoke(){
    for(var i = 0; i < detail.length; i++) {
        detail[i].addEventListener("mouseover", function(event) {
        this.style.backgroundColor = "whitesmoke";
        });
        }
};  

function TurnOffSmoke(){
    for(var i = 0; i < detail.length; i++) {
        detail[i].addEventListener("mouseout", function(event) {
        this.style.backgroundColor = "White";
        });
        }
};  



TurnOnLightRows();
TurnOffLightRows();
TurnOnSmoke();
TurnOffSmoke();

    
    });



    
