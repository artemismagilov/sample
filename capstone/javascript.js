function upDate(previewPic){
    var image = document.getElementById("image");
    document.getElementById("body").style.background = "url(" + previewPic.src + ") white";
}
function unDo(){
    var image = document.getElementById("image");
    document.getElementById("body").style.background = "white";
}
