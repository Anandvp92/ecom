var swiper = new Swiper(".swiper", {
  grabCursor: true,
  speed: 500,
  effect: "slide",
  loop: true,
  autoplay: {
    delay: 5000
  }
});

swiper.enable();
const loginform = document.getElementById("login-form");
const signupform = document.getElementById("signup-form");
const loginlink = document.getElementById("login-link");
const signuplink = document.getElementById("signup-link");

loginlink.addEventListener("click", (event) => {
  event.preventDefault();
  signupform.style.display = "none";
  loginform.style.display = "block";

  setTimeout(() => {
    signupform.style.opacity = 0;
    loginform.style.opacity = 1;
  }, 10);
});
signuplink.addEventListener("click", (event) => {
  event.preventDefault();
  signupform.style.display = "block";
  loginform.style.display = "none";

  setTimeout(() => {
    signupform.style.opacity = 1;
    loginform.style.opacity = 0;
  }, 10);
});


