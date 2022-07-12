const nav = document.querySelector(".nav");

// window.addEventListener("scroll", fixNav);

// function fixNav() {
//     if(window.scrollY > nav.offsetHeight + 150) {
//         nav.classList.add("active");
//     } else {
//         nav.classList.remove("active");
//     }
// }


const buttons = document. querySelectorAll(".ripple");

buttons.forEach(button => {
    button.addEventListener("click", function (e)  {
        const x = e.clientX;
        const y = e.clientY;

        const buttonTop = e.target.offsetTop;
        const buttonLeft = e.target.offsetLeft;

        const xInside = x - buttonLeft;
        const yInside = y - buttonTop;

        const circle = document.createElement("span");
        circle.classList.add("circle");
        circle.style.top = yInside + "px";
        circle.style.left = xInside + "px";

        this.appendChild(circle);

        setTimeOut(() => circle.remove(), 500);
    });
});