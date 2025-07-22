async function fetchLogs() {
    const response = await fetch("/logs");
    const logs = await response.json();
    const tbody = document.querySelector("#logTable tbody");
    tbody.innerHTML = "";
    logs.forEach(log => {
        const row = `<tr>
            <td>${log.timestamp}</td>
            <td>${log.type}</td>
            <td>${log.message}</td>
        </tr>`;
        tbody.innerHTML += row;
    });
}
window.onload = fetchLogs;
setInterval(fetchLogs, 5000);
