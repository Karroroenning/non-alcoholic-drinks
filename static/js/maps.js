// Initialize and add the map
let map;

async function initMap() {
  // The location of Nonalco4me
  const position = { lat: 56.87573696215281, lng: 16.654649106896684 };

  const { Map } = await google.maps.importLibrary("maps");
  const { AdvancedMarkerElement } = await google.maps.importLibrary("marker");

  // The map, centered at Borgholm
  map = new Map(document.getElementById("map"), {
    zoom: 6,
    center: position,
    mapId: "DEMO_MAP_ID",
  });

  // The marker, positioned at Borgholm
  const marker = new AdvancedMarkerElement({
    map: map,
    position: position,
    title: "NonAlco4Me",
  });
}

initMap();