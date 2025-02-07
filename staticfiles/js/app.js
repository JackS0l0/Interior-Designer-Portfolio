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
});
// dark-mode
document.addEventListener("DOMContentLoaded", () => {
    const toggleButton = document.getElementById("theme-toggle");
    const body = document.body;
    const icon = toggleButton.querySelector("i");
    if (localStorage.getItem("theme") === "dark") {
        body.classList.add("dark-mode");
        icon.classList.replace("bi-moon-stars", "bi-brightness-high");
    }
    toggleButton.addEventListener("click", () => {
        body.classList.toggle("dark-mode");
        if (body.classList.contains("dark-mode")) {
            localStorage.setItem("theme", "dark");
            icon.classList.replace("bi-moon-stars", "bi-brightness-high");
        } else {
            localStorage.setItem("theme", "light");
            icon.classList.replace("bi-brightness-high", "bi-moon-stars");
        }
    });
});