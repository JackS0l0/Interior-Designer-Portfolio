$('.headerCarusel').slick({
    slidesToShow: 1,
    slidesToScroll: 1,
    autoplay: true,
    autoplaySpeed: 2000,
    speed: 19000,
    infinite: true,
    dots: false,
    arrows: false,
    pauseOnHover:false,
});
$('.advantages').slick({
    slidesToShow: 5,
    slidesToScroll: 1,
    autoplay: true,
    autoplaySpeed: 2000,
    speed: 19000,
    infinite: true,
    dots: false,
    arrows: false,
    pauseOnHover:false,
    responsive: [
        {
            breakpoint: 1000,
            settings: {
                slidesToShow: 1,
                slidesToScroll: 1,
            }
        },
    ]
});
// dark-mode
document.addEventListener("DOMContentLoaded", () => {
    const toggleButtons = document.querySelectorAll(".theme-toggle"); // Bütün butonları seç
    const body = document.body;
    toggleButtons.forEach((button) => {
        const icon = button.querySelector("i"); // Hər buton üçün ikon tap
        if (localStorage.getItem("theme") === "dark") {
            body.classList.add("dark-mode");
            icon.classList.replace("bi-moon-stars", "bi-brightness-high");
        }
        button.addEventListener("click", () => {
            body.classList.toggle("dark-mode");
            const isDarkMode = body.classList.contains("dark-mode");
            localStorage.setItem("theme", isDarkMode ? "dark" : "light");
            toggleButtons.forEach((btn) => {
                const btnIcon = btn.querySelector("i");
                if (isDarkMode) {
                    btnIcon.classList.replace("bi-moon-stars", "bi-brightness-high");
                } else {
                    btnIcon.classList.replace("bi-brightness-high", "bi-moon-stars");
                }
            });
        });
    });
});
