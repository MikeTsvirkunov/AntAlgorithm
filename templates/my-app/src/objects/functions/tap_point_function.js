function tap_point_on_canvas(canvas, event){
    var ctx = canvas.getContext('2d');
    var x = event.offsetX;
    var y = event.offsetY;

    ctx.beginPath();
    ctx.arc(x, y, 50, 0, 2 * Math.PI);
    ctx.fillStyle = 'red';
    ctx.fill();
}