function cleanUp(map){
    map.svg.remove();
    delete map.svg;
    delete map;
}     
            
function mapCreate(type) {
    var countries = Datamap.prototype.fraTopo.objects.fra.geometries;
    var series = [];
    var map; // Déclarer la variable map en dehors de loadCSVData

    function loadCSVData() {
        return new Promise((resolve, reject) => {
            d3.csv("../static/blog/data.csv", function(data) {
                resolve(data);
            });
        });
    }

    return loadCSVData().then(data => {
        for (var i = 0, j = countries.length; i < j; i++) {
            var a = countries[i].id;
            var b = countries[i].properties.name;
            var c = 0;

            for (var k = 0; k < data.length; k++) {
                if (data[k].DEP == b) {
                    if (type == 1) {
                        c = data[k].NBCOM;
                    } else {
                        c = data[k].PTOT;
                    }
                }
            }

            series[i] = [a, c];
        }

        var dataset = {};
        var onlyValues = series.map(function(obj) { return obj[1]; });
        var minValue = Math.min.apply(null, onlyValues),
            maxValue = Math.max.apply(null, onlyValues);

        var paletteScale = d3.scale.linear()
            .domain([minValue, maxValue])
            .range(["#f8efff", "#7C4EE4"]);

        series.forEach(function(item) {
            var iso = item[0],
                value = item[1];
            dataset[iso] = { numberOfThings: value, fillColor: paletteScale(value) };
        });

        map = new Datamap({
            element: document.getElementById('container'),
            responsive: true,
            geographyConfig: {
                dataUrl: null,
                popupOnHover: true,
                highlightOnHover: true,
                borderColor: '#444',
                borderWidth: 0.5,
            },
            scope: 'fra',
            data: dataset,
            setProjection: function(element) {
                var projection = d3.geo.mercator()
                    .center([3.0, 48.5])
                    .scale(3500);
                var path = d3.geo.path().projection(projection);
                return {
                    path: path,
                    projection: projection
                };
            },
            geographyConfig: {
                popupTemplate: function(geo, data) {
                    if (type == 1) {
                        return ['<div class="hoverinfo"><strong>',
                            'Nombre de commune dans le département ' + geo.properties.name,
                            ': ' + data.numberOfThings,
                            '</strong></div>'
                        ].join('');
                    } else {
                        return ['<div class="hoverinfo"><strong>',
                            'Population dans le département ' + geo.properties.name,
                            ': ' + data.numberOfThings,
                            '</strong></div>'
                        ].join('');
                    }
                }
            }
        });
        return map; // Retourner l'objet map
    }).catch(error => {
        console.error("Erreur lors du chargement des données CSV :", error);
    });
}
    var data_x = data_get_x
    var data_y = data_get_y 


    const ctx = document.getElementById('myChart');
    chart = new Chart(ctx, {
    type: 'line',
    data: {
      labels: data_x,
      datasets: [{
        label: 'Nombre de naissance',
        data: data_y,
        borderWidth: 1,
        borderColor: "#7C4EE4"
      }]
    },
    options: {
      scales: {
        y: {
          beginAtZero: true
        }
      },
      pointStyle: false,
    },
  });

  var val = document.getElementById("steps-range").value
        document.getElementById("steps-range").oninput = function(){
            update()
            send_data()
        }
        document.getElementById("steps-range-debut").oninput=function(){
            update()
            send_data()
        }

        function update(){
           var val = document.getElementById("steps-range").value
           var val_debut = document.getElementById("steps-range-debut").value
           data_x = []
           data_y = []


           for (var i = 0, j = val; i < j; i++) {
            data_x[i] = data_get_x[i]
            data_y[i] = data_get_y[i]
        }
            for(var i=0, j= val_debut;i<j;i++){
                data_x.shift()
                data_y.shift()
            }
        
        chart.data.datasets = [{
            label: 'Nombre de naissance',
            data: data_y,
            borderWidth: 1,
            borderColor: "#7C4EE4"
        }]
        val = document.getElementById("output-range")
        val.innerHTML = "Donnée sélectionnée de " + data_x[0] +" jusqu'à " + data_x[data_x.length-1]
        chart.data.labels = data_x
        chart.update()
        }

        function send_data(){
            var val_fin = document.getElementById("steps-range").value
            var val_debut_r = document.getElementById("steps-range-debut").value
            $.ajax({
                url: url_stat,
                data:{
                    'csrfmiddlewaretoken':csrf_tok,
                    'valeur_debut':data_x[0],
                    'valeur_fin':data_x[data_x.length-1],
                    'int_debut':val_debut_r,
                    'int_fin':val_fin
                },
                method:'POST'
            })
        }
        tab = document.getElementById("tab")

        bouton_com = document.getElementById("bt-com")
        bouton_com.addEventListener("click",(event) => {
            send_data_map(0)
            cleanUp(carte)
            mapCreate(0).then(map=>{
                carte = map
            })
        });

        bouton_pop = document.getElementById("bt-pop")
        bouton_pop.addEventListener("click",(event) => {
            send_data_map(1)
            cleanUp(carte)
            mapCreate(1).then(map=>{
                carte = map
            })
        });

        function send_data_map(val){
            console.log("OK")
            console.log(val)
            if(val==1){
            $.ajax({
                url:url_com,
                data:{
                    'csrfmiddlewaretoken':csrf_tok,
                    'type':val
                },
                method:'POST',
                success: function(data){
                    $("#tab").load(url_com);
                }   
            })
            } else{
            $.ajax({
                url:url_pop,
                data:{
                    'csrfmiddlewaretoken':csrf_tok,
                    'type':val
                },
                method:'POST',
                success: function(data){
                    $("#tab").load(url_pop);
                }   
            })}
           
        }
    
            