window.addEventListener("scroll",function(){
let header=document.getElementById('header');
if(header){
if(window.pageYOffset<50){
header.style.backgroundColor='rgba(0,0,0,0)';
}else{
header.style.backgroundColor='rgba(0,0,0,0.75)';
}
}
let parallax=document.getElementById('parallax');
if(parallax){
parallax.style.backgroundPositionY=String(0.5*window.pageYOffset)+'px';
}
});
