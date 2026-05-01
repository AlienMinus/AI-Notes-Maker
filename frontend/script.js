const BASE_URL = "http://127.0.0.1:8000";

async function callAPI(endpoint) {
    const text = document.getElementById("inputText").value;
    const output = document.getElementById("outputText");
    const loading = document.getElementById("loading");

    if (!text.trim()) {
        alert("Enter text!");
        return;
    }

    loading.classList.remove("hidden");
    output.innerText = "";

    try {
        const res = await fetch(`${BASE_URL}/${endpoint}`, {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify({ text })
        });

        const data = await res.json();

        output.innerText = formatOutput(endpoint, data);

    } catch (err) {
        output.innerText = "Error connecting to API";
    }

    loading.classList.add("hidden");
}

function formatOutput(type, data) {
    if (data.error) return data.error;

    switch (type) {
        case "summarize":
            return data.summary;

        case "notes":
            return data.notes;

        case "keywords":
            return data.keywords.join(", ");

        case "mindmap":
            let text = `Central Topic: ${data.central_topic}\n\n`;
            data.branches.forEach(b => {
                text += `• ${b.topic}\n`;
            });
            return text;

        default:
            return JSON.stringify(data, null, 2);
    }
}

function clearText() {
    document.getElementById("inputText").value = "";
    document.getElementById("outputText").innerText = "Output will appear here...";
}