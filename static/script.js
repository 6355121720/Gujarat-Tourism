function scrollLeft() {
    document.querySelector('.spots-wrapper').scrollBy({ left: -305, behavior: 'smooth' });
}

function scrollRight() {
    document.querySelector('.spots-wrapper').scrollBy({ left: 305, behavior: 'smooth' });
}
let left=document.querySelector(".arrow-left");
let right=document.querySelector(".arrow-right");





let slider=document.querySelector("#slider")
let allimages=document.querySelectorAll("img")

allimages.forEach((image)=>{
    image.loading="lazy"
})

let count=1;


right.addEventListener('click',() => {
    if(count==13){
        right.style.opacity="0.3"
    }else{
        left.style.opacity="1"
        scrollRight()
        count++;
    }
})

left.addEventListener('click',() => {
    if(count==1){
        left.style.opacity='0.3'
    }else{
        scrollLeft()
        right.style.opacity='1'
        count--;
    }
})