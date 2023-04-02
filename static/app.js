const hamburg = document.getElementById('hamburger');
const menu = document.getElementById('menu');

hamburg.addEventListener("click", () => {
    menu.classList.toggle("hidden")
    hamburg.classList.toggle("text-white")
})