// const url_string = window.location.href; //window.location.href
// const url = new URL(url_string);
// const sLng = url.searchParams.get("sLng");
// const sLat = url.searchParams.get("sLat");
// const dLng = url.searchParams.get("dLng");
// const dLat = url.searchParams.get("dLat");

// Initialize the platform object:
const platform = new H.service.Platform({
  app_id: "Z7uukAiQbHvHZ43KIBKW",
  app_code: "nadFSh5EHBHkTdUQ3YnTEg"
  // useHTTPS: true
});
// Obtain the default map types from the platform object
const maptypes = platform.createDefaultLayers();
// Instantiate (and display) a map object:
const map = new H.Map(
  document.getElementById("mapContainer"),
  maptypes.normal.map,
  {
    zoom: 10,
    center: { lng: 13.4, lat: 52.51 }
  }
);
const behavior = new H.mapevents.Behavior(new H.mapevents.MapEvents(map));
// console.log("geo!" + sLat + "," + sLng);

let routingParameters = {
  // The routing mode:
  mode: "fastest;car",
  // The start point of the route:
  waypoint0: "geo!50.1120423728813,8.68340740740811",
  // The end point of the route:
  waypoint1: "geo!52.5309916298853,13.3846220493377",
  // To retrieve the shape of the route we choose the route
  // representation mode 'display'
  representation: "display"
};
// Define a callback function to process the routing response:
let onResult = function(result) {
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
    routeShape.forEach(function(point) {
      let parts = point.split(",");
      linestring.pushLatLngAlt(parts[0], parts[1]);
    });
    // Retrieve the mapped positions of the requested waypoints:
    startPoint = route.waypoint[0].mappedPosition;
    endPoint = route.waypoint[1].mappedPosition;
    // Create a polyline to display the route:
    let routeLine = new H.map.Polyline(linestring, {
      style: { strokeColor: "blue", lineWidth: 5 }
    });
    // Create a marker for the start point:
    let startMarker = new H.map.Marker({
      lat: startPoint.latitude,
      lng: startPoint.longitude
    });
    // Define a letiable holding SVG mark-up that defines an icon image:
    // Create a marker for the end point:
    const endMarker = new H.map.Marker({
      lat: endPoint.latitude,
      lng: endPoint.longitude
    });
    // Add the route polyline and the two markers to the map:
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
router.calculateRoute(routingParameters, onResult, function(error) {
  alert(error.message);
});
