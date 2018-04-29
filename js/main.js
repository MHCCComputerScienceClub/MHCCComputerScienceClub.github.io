$(document).ready(()=> {
    $(".slide-up")
        .css('opacity', 0)
        .animate(
                {opacity: 1},
                {queue: false, duration: 'slow'}
                );
});
