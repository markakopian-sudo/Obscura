const addressBar = document.getElementById('address-bar');
const goBtn = document.getElementById('go-btn');
const viewport = document.getElementById('viewport');
const backBtn = document.getElementById('back-btn');
const forwardBtn = document.getElementById('forward-btn');
const refreshBtn = document.getElementById('refresh-btn');

// Base proxy URL to bypass X-Frame-Options/CORS blocks on major sites
const proxyUrl = "https://api.allorigins.win/raw?url=";

function navigateToUrl() {
    let url = addressBar.value.trim();
    
    if (!url) return;

    // If it doesn't look like a URL, turn it into a Google Search
    if (!url.includes('.') || url.includes(' ')) {
        url = `https://www.google.com/search?q=${encodeURIComponent(url)}`;
    } else {
        // Ensure protocol exists
        if (!url.startsWith('http://') && !url.startsWith('https://')) {
            url = 'https://' + url;
        }
    }

    // Load via proxy to bypass iframe security blocks
    viewport.src = proxyUrl + encodeURIComponent(url);
}

// Event Listeners
goBtn.addEventListener('click', navigateToUrl);
addressBar.addEventListener('keypress', (e) => {
    if (e.key === 'Enter') {
        navigateToUrl();
    }
});

// Navigation buttons (Simulated)
refreshBtn.addEventListener('click', () => {
    viewport.src = viewport.src;
});

backBtn.addEventListener('click', () => {
    try {
        window.history.back();
    } catch (e) {
        alert("Cannot go back due to browser safety limits.");
    }
});

forwardBtn.addEventListener('click', () => {
    try {
        window.history.forward();
    } catch (e) {
        alert("Cannot go forward due to browser safety limits.");
    }
});
