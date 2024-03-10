// Script for pop-up functionality

$(document).ready(function() {
    $('.project-link').click(function() {
        var modalId = $(this).data('target');
        $(modalId).css('display', 'block');
    });

    $('.close').click(function() {
        $('.modal').css('display', 'none');
    });

    $(window).click(function(event) {
        if ($(event.target).hasClass('modal')) {
            $('.modal').css('display', 'none');
        }
    });
});

