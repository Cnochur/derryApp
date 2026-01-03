const map = L.map('map').setView([54.9966, -7.3086], 14)

const wallPath = stops
    .sort((a, b) => a.position - b.position) // ensure correct order
    .map(stop => [stop.latitude, stop.longitude]);

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; OpenStreetMap contributors'
}).addTo(map);


stops.forEach(stop => {
    const marker = L.marker([stop.latitude, stop.longitude]).addTo(map);
    marker.bindPopup(`
        <b>${stop.position}. ${stop.name}</b><br>
        ${stop.description}
    `, { maxWidth:250 });
});

const polyline = L.polyline(wallPath, {
    color: 'red',       // line color
    weight: 4,          // thickness
    opacity: 0.7,       // semi-transparent
    smoothFactor: 1     // makes the line look smooth
}).addTo(map);