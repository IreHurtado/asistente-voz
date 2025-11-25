console.log("🔥 Script cargado correctamente");

// ELEMENTOS DEL DOM
const chat = document.getElementById("chat");
const avatar = document.getElementById("avatar");
const audio = document.getElementById("audio");

// VERIFICAR EXISTENCIA DE ELEMENTOS
if (!chat) console.error("❌ ERROR: No existe el div #chat");
if (!avatar) console.error("❌ ERROR: No existe #avatar");
if (!audio) console.error("❌ ERROR: No existe #audio");

// ANIMACIÓN DEL AVATAR
let talkingInterval = null;

function startTalking() {
    console.log("▶️ Inicia animación hablar...");
    const frames = ["assets/talk1.png", "assets/talk2.png"];
    let i = 0;

    talkingInterval = setInterval(() => {
        avatar.src = frames[i % 2];
        i++;
    }, 150);
}

function stopTalking() {
    console.log("⏹ Detiene animación hablar");
    clearInterval(talkingInterval);
    avatar.src = "assets/smile.png";
}

// AÑADE MENSAJE DEL USUARIO A LA INTERFAZ
function addUserMessage(text) {
    console.log("💬 Añadiendo mensaje de usuario:", text);

    const div = document.createElement("div");
    div.className = "msg user-msg";
    div.textContent = text;

    chat.appendChild(div);
    chat.scrollTop = chat.scrollHeight;
}

// AÑADE MENSAJE DEL BOT (CON AUDIO BASE64)
function addBotMessage(texto, audio_b64) {
    console.log("🤖 Añadiendo mensaje del bot:", texto);

    const div = document.createElement("div");
    div.className = "msg bot-msg";
    div.innerHTML = `<p>${texto}</p>`;

    // Botón reproducir nuevamente
    const btn = document.createElement("button");
    btn.className = "audio-btn";
    btn.textContent = "▶️ Escuchar audio otra vez";

    // Convertir base64 → Blob (lo hacemos una sola vez)
    const byteCharacters = atob(audio_b64);
    const byteNumbers = Array.from(byteCharacters).map(c => c.charCodeAt(0));
    const byteArray = new Uint8Array(byteNumbers);
    const blob = new Blob([byteArray], { type: "audio/mpeg" });

    // FUNCIÓN REPRODUCIR
    function reproducirAudio() {
        console.log("🎧 Reproduciendo audio...");
        audio.src = URL.createObjectURL(blob);

        audio.play()
            .then(() => startTalking())
            .catch(e => console.error("❌ Error al reproducir audio:", e));

        audio.onended = stopTalking;
    }

    // CLICK EN EL BOTÓN → reproducir de nuevo
    btn.onclick = reproducirAudio;

    // Agregar elementos al chat
    div.appendChild(btn);
    chat.appendChild(div);
    chat.scrollTop = chat.scrollHeight;

    // 🔥 Reproducción automática apenas llega la respuesta
    reproducirAudio();
}

// FUNCIÓN PRINCIPAL DE ENVÍO
async function enviar() {
    try {
        console.log("🔵 Enviando...");

        const input = document.getElementById("preg");
        if (!input) {
            console.error("❌ ERROR: No existe el input #preg");
            return;
        }

        const q = input.value.trim();
        console.log("Pregunta capturada:", q);

        if (!q) {
            console.warn("⚠️ Pregunta vacía");
            return;
        }

        addUserMessage(q);
        input.value = "";

        avatar.src = "assets/smile.png";

        console.log("🌍 Llamando al backend...");

        const res = await fetch(
            `http://127.0.0.1:8000/preguntar?q=${encodeURIComponent(q)}`
        );

        console.log("📥 Respuesta recibida:", res);

        const data = await res.json();
        console.log("📥 JSON recibido:", data);

        addBotMessage(data.texto, data.audio_b64);

    } catch (err) {
        console.error("🔥 ERROR FATAL EN enviar():", err);
    }
}

// CAPTURAR ERRORES GLOBALES
window.onerror = function (msg, url, line) {
    console.error("🔥 ERROR GLOBAL:", msg, "en", url, "línea", line);
};
