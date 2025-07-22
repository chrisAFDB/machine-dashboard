function showSection(id) {
  document.querySelectorAll('.section').forEach(section => {
    section.classList.add('hidden');
  });
  document.getElementById(id).classList.remove('hidden');
}

// ==== Chargement des données ====

async function fetchLogs() {
  const res = await fetch('/logs');
  const data = await res.json();
  return data;
}

function updateDashboard(logs) {
  const summary = document.getElementById("summary-cards");
  summary.innerHTML = "";

  const totalLogs = logs.length;
  const lastLog = logs[logs.length - 1] || { timestamp: '-', type: '-', message: '-' };

  const cards = [
    { title: "Total logs", value: totalLogs },
    { title: "Dernier log", value: lastLog.timestamp },
    { title: "Type", value: lastLog.type },
    { title: "Message", value: lastLog.message }
  ];

  cards.forEach(card => {
    summary.innerHTML += `
      <div class="card">
        <h3>${card.title}</h3>
        <div class="value">${card.value}</div>
      </div>
    `;
  });
}

function updateLogs(logs) {
  const container = document.getElementById("logs-container");
  container.innerHTML = "<table><thead><tr><th>Date</th><th>Type</th><th>Message</th></tr></thead><tbody></tbody></table>";
  const tbody = container.querySelector("tbody");

  logs.slice().reverse().forEach(log => {
    const row = `<tr><td>${log.timestamp}</td><td>${log.type}</td><td>${log.message}</td></tr>`;
    tbody.innerHTML += row;
  });
}

async function init() {
  const logs = await fetchLogs();
  updateDashboard(logs);
  updateLogs(logs);
}

init();
setInterval(init, 10000); // Rafraîchit toutes les 10 secondes
