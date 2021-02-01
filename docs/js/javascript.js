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
let parallax2=document.getElementById('parallax2');
let parallax3=document.getElementById('parallax3');
if(parallax){
parallax.style.backgroundPositionY=String(-0.5*window.pageYOffset-160)+'px';
}
if(parallax2){
parallax2.style.backgroundPositionY=String(-0.5*window.pageYOffset+370-100)+'px';
}
if(parallax3){
parallax3.style.backgroundPositionY=String(-0.5*window.pageYOffset+760-100)+'px';
}
});
