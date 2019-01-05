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
      center: { lng: 20.262038, lat: 49.819856 }
    });

    var group = new H.map.Group();
    map.addObject(group);

  // add 'tap' event listener, that opens info bubble, to the group
    group.addEventListener('tap', function (evt) {
    // event target is the marker itself, group is a parent event target
    // for all objects that it contains
    var bubble =  new H.ui.InfoBubble(evt.target.getPosition(), {
      // read custom data
      content: evt.target.getData()
    });
    // show info bubble
    ui.addBubble(bubble);
     }, false);


const behavior = new H.mapevents.Behavior(new H.mapevents.MapEvents(map));
// console.log("geo!" + sLat + "," + sLng);
function my_cool_js_function(param1, param2, colourt, client, name){
    let routingParameters1 = {
        // The routing mode:
        mode: "fastest;car",
        // The start point of the route:
        waypoint0: param1,
        // The end point of the route:
        waypoint1: param2,
        // To retrieve the shape of the route we choose the route
        // representation mode 'display'
        representation: "display"
    };
var svgMarkup = '<svg width="24" height="24" ' +
  'xmlns="http://www.w3.org/2000/svg">' +
  '<rect stroke="white" fill="#1b468d" x="1" y="1" width="22" ' +
  'height="22" /><text x="12" y="18" font-size="12pt" ' +
  'font-family="Arial" font-weight="bold" text-anchor="middle" ' +
  'fill="white">H</text></svg>';
var svgMarkupClient = '<svg width="24" height="24" ' +
  'xmlns="http://www.w3.org/2000/svg">' +
  '<rect stroke="white" fill="#1b468d" x="1" y="1" width="22" ' +
  'height="22" /><text x="12" y="18" font-size="12pt" ' +
  'font-family="Arial" font-weight="bold" text-anchor="middle" ' +
  'fill="white">K</text></svg>';
// Add the marker to the map:
// Define a callback function to process the routing response:
    let onResult = function (result) {
        let route, routeShape, startPoint, endPoint, linestring;
        if (result.response.route) {
            console.log("Success");
            // Pick the first route from the response:
            route = result.response.route[0];
            // Pick the route's shape:sudo fuser -k 8000/tcp
            routeShape = route.shape;
            // Create a linestring to use as a point source for the route line
            linestring = new H.geo.LineString();
            // Push all the points in the shape into the linestring:
            routeShape.forEach(function (point) {
                let parts = point.split(",");
                linestring.pushLatLngAlt(parts[0], parts[1]);
            });
            // Retrieve the mapped positions of the requested waypoints:
            startPoint = route.waypoint[0].mappedPosition;
            endPoint = route.waypoint[1].mappedPosition;
            // Create a polyline to display the route:
            let routeLine = new H.map.Polyline(linestring, {
                style: {strokeColor: colourt, lineWidth: 5}
            });
            // Create a marker for the start point:
            let startMarker;
            console.log(startPoint.latitude, startPoint.longitude);
            if(startPoint.latitude===49.8192871 && startPoint.longitude===20.2598438) {
                startMarker = new H.map.Marker({
                lat: startPoint.latitude,
                lng: startPoint.longitude,
            },{icon: new H.map.Icon(svgMarkup)});
            }
            else if(!(startPoint.latitude===49.8192871 && startPoint.longitude===20.2598438) && client) {
                startMarker = new H.map.Marker({
                lat: startPoint.latitude,
                lng: startPoint.longitude,
            },{icon: new H.map.Icon(svgMarkupClient)});
            }
            else{
                startMarker = new H.map.Marker({
                lat: startPoint.latitude,
                lng: startPoint.longitude,
            });}

            // Define a letiable holding SVG mark-up that defines an icon image:
            // Create a marker for the end point:
            // noinspection JSAnnotator
            let endMarker;
            if(endPoint.latitude===49.8192871 && endPoint.longitude===20.2598438) {
                endMarker = new H.map.Marker({
                lat: endPoint.latitude,
                lng: endPoint.longitude,
            },{icon: new H.map.Icon(svgMarkup)});
            }
            else if((endPoint.latitude===49.8192871 && endPoint.longitude===20.2598438) && client) {
                endMarker = new H.map.Marker({
                lat: endPoint.latitude,
                lng: endPoint.longitude,
            },{icon: new H.map.Icon(svgMarkupClient)});
            }
            else{
                endMarker = new H.map.Marker({
                lat: endPoint.latitude,
                lng: endPoint.longitude,
            });}
            // Add the route polyline and the two markers to the map:
            // language=HTML


            startMarker.setData('<div><a href=\'http://www.mcfc.co.uk\' ><div id="name">name</div></a>' +
    '                           </div><div >City of Manchester Stadium<br><div id="param1">lol</div></div>');

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
                document.getElementById("param1").innerHTML = "param1";
                document.getElementById("name").innerHTML = "name";

                }, false);


            startMarker.setData('<div><a href=\'http://www.mcfc.co.uk\' ><div id="nameContainer">name</div></a>' +
    '                           </div><div >City of Manchester Stadium<br><div id="paramContainer">lol</div></div>');

                //document.getElementById("param1").innerHTML = param1;
                //document.getElementById("name").innerHTML = name;

        //     startMarker.addEventListener('tap', function (evt) {
        //         let bubble =  new H.ui.InfoBubble(evt.target.getPosition(), {
        //                         content: evt.target.getData()});
        //
        //         let pixelRatio = window.devicePixelRatio || 1;
        //         let defaultLayers = platform.createDefaultLayers({
        //                             tileSize: pixelRatio === 1 ? 256 : 512,
        //                             ppi: pixelRatio === 1 ? undefined : 320
        //         });
        //         var ui = H.ui.UI.createDefault(map, defaultLayers);
        //         ui.addBubble(bubble);
		// let tmpContainer = "";
		// if(document.getElementById("nameContainer")==="name"){
		// 	tmpContainer = "eloziomek";
		// 	document.getElementById("nameContainer").innerHTML = tmpContainer;
		// }
        //
        //         }, false);
                map.addObjects([routeLine, startMarker, endMarker]);
            // Set the map's viewport to make the whole route visible:
                map.setViewBounds(routeLine.getBounds());

        }
    };



// Get an instance of the routing service:
    let router = platform.getRoutingService();
// Call calculateRoute() with the routing parameters,
// the callback and an error callback function (called if a
// communication error occurs):
    router.calculateRoute(routingParameters1, onResult, function (error) {
        alert(error.message);
    });
}
