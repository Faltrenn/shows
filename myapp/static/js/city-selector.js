stateSelector = document.getElementById("estado");
citySelector = document.getElementById("cidade");
if(stateSelector && citySelector){
    stateSelector.addEventListener("change", (event) => {
        httpRequest = new XMLHttpRequest();
        httpRequest.open("POST", "/getCities/", true);
        httpRequest.setRequestHeader("X-CSRFToken", csrftoken); 
        httpRequest.setRequestHeader("Content-Type", 'application/x-www-form-urlencoded');
        httpRequest.onload = function (){
            let data = JSON.parse(this.responseText);
            citySelector.innerHTML = "";
            data["cidades"].forEach(city => {
                option = document.createElement("option");
                option.value = option.text = city;
                citySelector.add(option);
            });
        }
        httpRequest.send("estado=" + stateSelector.value);
    });
}
