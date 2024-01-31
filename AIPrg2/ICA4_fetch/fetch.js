"use strict";

// https://restcountries.com/v3.1/all
(() => {

    const countryInfo = document.querySelector("#country_info");
    const getDataBtn = document.querySelector("#get_data_btn");

    function renderData(data) {
        console.log("data[0] is: ", data[0]);
        getDataBtn.style.display = "none";
        for (const [index, obj] of data.entries()) {
            if (index > 10) {
                return;
            }
            countryInfo.innerHTML += "<br><br>";
            console.log("index is: ", index);
            console.log("obj is: ", obj);
            console.log("\n");
            for (const [key, value] of Object.entries(obj)) {
                if (key === "name" || key === "capital" || key === "region" || key === "subregion" || key === "population" || key === "area" || key === "flag") {
                    countryInfo.innerText += `${key}: ${JSON.stringify(value)}`;
                }
                // console.log("key is: ", key);
                // console.log("value is: ", value);
            }
        }
    }

    function getAllCountryData () {
        fetch("https://restcountries.com/v3.1/all")
        .then(res => res.json())
        .then(data => renderData(data))
        .catch(err => console.error("Error: ", err));
    }


    window.addEventListener("load", () => {
        getDataBtn.addEventListener("click", getAllCountryData);
    });

})();
