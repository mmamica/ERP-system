// Initialize the platform object:
    var platform = new H.service.Platform({
    app_id: "Z7uukAiQbHvHZ43KIBKW",
    app_code: "nadFSh5EHBHkTdUQ3YnTEg"
    });
    // Obtain the default map types from the platform object
    var maptypes = platform.createDefaultLayers();
    // Instantiate (and display) a map object:
    var map = new H.Map(
    document.getElementById('mapContainer'),
    maptypes.normal.map,
    {
      zoom: 10,
      center: { lng: 20.085053, lat: 49.882387 }
    });


const behavior = new H.mapevents.Behavior(new H.mapevents.MapEvents(map));
// console.log("geo!" + sLat + "," + sLng);



function marker(latitude, longitude, name){



    var coords = {lat: latitude, lng: longitude};

    var startMarker = new H.map.Marker({
                lat: latitude,
                lng: longitude,
            });


    startMarker.setData('<div><div id="name">'+String(name)+'</div>' +
                                        '</div><div >'+ String(latitude) +'<br><div id="param1">'+String(longitude)+'</div></div>');
    startMarker.addEventListener('tap', function (evt) {

        let bubble =  new H.ui.InfoBubble(evt.target.getPosition(), {
                                content: evt.target.getData()});

        let pixelRatio = window.devicePixelRatio || 1;
        let defaultLayers = platform.createDefaultLayers({
                                    tileSize: pixelRatio === 1 ? 256 : 512,
                                    ppi: pixelRatio === 1 ? undefined : 320
                });
        var ui = H.ui.UI.createDefault(map, defaultLayers);
        ui.addBubble(bubble);

        }, false);

    map.addObjects([startMarker]);
                          //      map.addObjects(startMarker);


            // Set the map's viewport to make the whole route visible:

}



