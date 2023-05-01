function showImage(num) {
    var images = document.getElementsByTagName("img");
    for (var i = 0; i < images.length; i++) {
      images[i].style.display = "none";
    }
    document.getElementById("image" + num).style.display = "block";
  }