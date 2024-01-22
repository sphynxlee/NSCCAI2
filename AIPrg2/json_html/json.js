const data = `[{
    "id": "0001",
    "type": "donut",
    "name": "Cake",
    "ppu": 0.55,
    "batters": {
        "batter": [{
                "id": "1001",
                "type": "Regular"
            },
            {
                "id": "1002",
                "type": "Chocolate"
            },
            {
                "id": "1003",
                "type": "Blueberry"
            },
            {
                "id": "1004",
                "type": "Devil's Food"
            }
        ]
    },
    "topping": [{
            "id": "5001",
            "type": "None"
        },
        {
            "id": "5002",
            "type": "Glazed"
        },
        {
            "id": "5005",
            "type": "Sugar"
        },
        {
            "id": "5007",
            "type": "Powdered Sugar"
        },
        {
            "id": "5006",
            "type": "Chocolate with Sprinkles"
        },
        {
            "id": "5003",
            "type": "Chocolate"
        },
        {
            "id": "5004",
            "type": "Maple"
        }
    ]
}]`;

// console.log(JSON.parse(data)[0]);

arrData = JSON.parse(data);


// for (let i = 0; i < arrData.length; i++) {
    //     console.log(`Name: ${arrData[i].name}`);
    //     console.log(`Type: ${arrData[i].type}`);
    //     // the Template Literal syntax does not let you use the dot notation
    //     // console.log(`Toppings: ${arrData[i].topping}`);
    //     console.log("TTTopping: ", arrData[i].topping);
    // }
    // console.log(arrData);


    const output = document.getElementById('results');
    let strHTML = "";
    // output.innerText = data;
    for (let i = 0; i < arrData.length; i++) {
        strHTML = strHTML +  `<h2>${arrData[i].id}</h2>`;
        strHTML = strHTML +  `<h2>${arrData[i].name}</h2>`;
        strHTML = strHTML + `<ul>`;
        for (let j = 0; j < arrData[i].topping.length; j++) {
            console.log(arrData[i].topping[j].type);
            strHTML = strHTML + `<li>${arrData[i].topping[j].type}</li>`;
        }
        strHTML = strHTML + `</ul>`;
    }
    output.innerHTML = strHTML;

    const data2 = fetch('https://jsonplaceholder.typicode.com/users')
    .then(response => response.json())
    .then(data => console.log(data));