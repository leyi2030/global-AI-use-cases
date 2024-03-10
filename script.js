/* Add your JavaScript code here */
document.addEventListener('DOMContentLoaded', function () {
    var modalLinks = document.querySelectorAll('.project-link');
    modalLinks.forEach(function (link) {
        link.addEventListener('click', function (event) {
            event.preventDefault();
            var modalId = this.getAttribute('data-target').replace('#', '');
            var modal = document.getElementById(modalId);
            modal.style.display = 'block';
        });
    });

    var closeButtons = document.querySelectorAll('.close');
    closeButtons.forEach(function (button) {
        button.addEventListener('click', function () {
            var modal = this.closest('.modal');
            modal.style.display = 'none';
        });
    });

    window.addEventListener('click', function (event) {
        var modals = document.querySelectorAll('.modal');
        modals.forEach(function (modal) {
            if (event.target == modal) {
                modal.style.display = 'none';
            }
        });
    });
});
