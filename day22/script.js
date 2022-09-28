function hide_tv(){
    var tv_tv = document.getElementsByClassName("tv");
    console.log(tv_tv);

for (var i = 0; i < tv_tv.length; i++) {
    var x = tv_tv[i]
    if (x.style.display == "none"){
        x.style.display = "block"
    }    
    else {
        tv_tv[i].style.display = "none";}   
    
   
}
}