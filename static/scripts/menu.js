const button = document.querySelector('.navbar-toggler');
const menu = document.querySelector('.collapse');

button.onclick = () => {
    menu.classList.toggle('show');
}