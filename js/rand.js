const pages = [
    "index.html",
    "b1.html"
];

// Fungsi untuk memilih halaman acak
function redirectToRandomPage() {
    const randomPage = pages[Math.floor(Math.random() * pages.length)];
    window.location.href = randomPage;  // Redirect ke halaman acak
}

// Mengatur waktu mundur acak antara 30 hingga 60 detik
let countdown = Math.floor(Math.random() * (30 - 20 + 1)) + 20;

function startCountdown() {
    const countdownElement = document.getElementById('countdown');
    const interval = setInterval(function() {
        countdownElement.innerText = `Halaman akan dialihkan dalam ${countdown} detik...`;

        // Setelah waktu mencapai 0, lakukan redirect
        if (countdown <= 0) {
            clearInterval(interval);  // Hentikan interval
            redirectToRandomPage();  // Redirect ke halaman acak
        }

        countdown--;
    }, 1000); // Update setiap detik
}

// Mulai hitung mundur setelah halaman dimuat
window.onload = startCountdown;