
const stars =  document.querySelectorAll(".star");

const rate = document.getElementById("ratings")
console.log(parseInt (rate.textContent[0]))
stars.forEach((s,i)=>{
if (i<parseInt (rate.textContent[0])){
  s.classList.add("active");
}
else{
  s.remove()
}

  
})

