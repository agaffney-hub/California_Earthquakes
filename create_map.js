// Create a map centered on California
const map = L.map('map').setView([36.7783, -119.4179], 6);

// Load and display tile layers
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
}).addTo(map);

// Load earthquake data from the CSV file
fetch('data/earthquake_data.csv')
    .then(response => response.text())
    .then(data => {
        const rows = data.split('\n').slice(1); // Skip header row
        rows.forEach(row => {
            const [magnitude, location, time, latitude, longitude] = row.split(',');

            // Create a marker for each earthquake
            const marker = L.marker([latitude, longitude]).addTo(map);
            marker.bindPopup(`<b>Magnitude:</b> ${magnitude}<br><b>Location:</b> ${location}<br><b>Time:</b> ${time}`);
        });
    })
    .catch(error => console.error('Error loading earthquake data:', error));
