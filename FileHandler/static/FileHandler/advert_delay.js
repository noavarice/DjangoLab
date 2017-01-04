{% load staticfiles %}
document.addEventListener('DOMContentLoaded', function() {
    $('#content').load('{% static "advertising/advert.html" %}');
});

setTimeout(function() {
    $('#content').load('{% static "download.html" %}');
}, 2000);
