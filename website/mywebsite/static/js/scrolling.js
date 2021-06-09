$(window).scroll(function(){
  var scroll = $(window).scrollTop();

  document.getElementById("myBody").style.marginTop = (-100 - scroll*0.5) + "px";

  if (scroll>=150) {
    $("#myNav").addClass("bg-dark");
  }else {
    $("#myNav").removeClass("bg-dark");
  }
});
