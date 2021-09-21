// first slider
$('.slider-one')
.not(".slick-intialized")
.slick({
 autoplay:true,
 autoplaySpeed:3000,
 dots:true,
 prevArrow:'.site-slider .slider-btn .prev',
 nextArrow:'.site-slider .slider-btn .next',
}); 

// scond slider
$('.slider-two')
.not(".slick-intialized")
.slick({

 prevArrow:'.site-slider-two .prev',
 nextArrow:'.site-slider-two .next',
 slidesToShow:4,
 slidesToScroll:1,
 autoplay:3000,
}); 

function sendMail() {
    
    var name=document.getElementById('conName')
    console.log('name'+name)
    // Email.send({
    //     Host : "smtp.gmail.com",
    //     Username : "barnaghosh19@gmail.com",
    //     Password : "roposi34@99",
    //     To : 'barnag119@gmail.com',
    //     From : "you@isp.com",
    //     Subject : "This is the subject",
    //     Body : "And this is the body"
    // }).then(
    //   message => alert(message)
    // );
}