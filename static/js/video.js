const myVideoElement = $('#myVideo');

function pauseVideo() {
    myVideoElement.html(`
    <video autoplay muted loop>
      <source src="{% static 'images/stars.mp4' %}" type="video/mp4">
      Your browser does not support HTML5 video.
    </video>
    `);
    
};
