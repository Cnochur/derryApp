const map = L.map('map').setView([54.9966, -7.3086], 14);

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; OpenStreetMap contributors'
}).addTo(map);

let selectedStopId = null;

function selectStop(stopId) {
    selectedStopId = stopId;
    console.log("Selected stop ID:", stopId);
}

function renderStopsOnMap(stops) {
    map.eachLayer(layer => {
        if (layer instanceof L.Marker) map.removeLayer(layer);
    });

    stops.forEach(stop => {
        const marker = L.marker([stop.latitude, stop.longitude]).addTo(map);
        marker.bindPopup(`
            <div>
                <b>${stop.name}</b><br>
                <button type="button" onclick="selectStop(${stop.id})">Choose</button>
            </div>
        `, { maxWidth: 250 });
    });
}

renderStopsOnMap(stops)

document.getElementById("searchStops").addEventListener("click", () => {
    const area = document.getElementById("area").value;
    const direction = document.getElementById("direction").value;

    fetch(`/buschecker/stops/?area=${area}&direction=${direction}`)
        .then(response => response.json())
        .then(stops => {
            const sortedStops = stops.sort((a, b) => a.position - b.position);
            renderStopsOnMap(sortedStops);
        })
        .catch(error => console.error("Error fetching stops:", error));
});
