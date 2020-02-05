function canvasAnimation() {
    var t = document.querySelector("canvas"),
        o = t.getContext("2d");
    t.width = window.innerWidth, t.height = window.innerHeight, o.lineWidth = .5, o.strokeStyle = new y(150).style;
    var n = {
            x: t.width / 2,
            y: t.height / 2
        },
        a = !1;
    "undefined" != typeof homeCanvas && !0 === homeCanvas && (a = homeCanvas);
    var r = 350;
    t.width < 1400 && (r = 200);
    var d = {
        nb: r,
        distance: 100,
        d_radius: 150,
        array: []
    };

    function e(i) {
        return Math.floor(255 * Math.random() + i)
    }

    function h(i, t, o) {
        return !0 === a ? "#8DA9D0" : "rgba(28,114,184, 0.8)"
    }

    function s(i, t, o, n) {
        return (i * t + o * n) / (t + n)
    }

    function y(i) {
        i = i || 0, this.r = e(i), this.g = e(i), this.b = e(i), this.style = h(this.r, this.g, this.b)
    }

    function u() {
        this.x = Math.random() * t.width, this.y = Math.random() * t.height, this.vx = -.5 + Math.random(), this.vy = -.5 + Math.random(), this.radius = 2 * Math.random(), this.color = new y
    }
    u.prototype = {
            draw: function() {
                o.beginPath(), o.fillStyle = this.color.style, o.arc(this.x, this.y, this.radius, 0, 2 * Math.PI, !1), o.fill()
            }
        }, $("body").on("mousemove", function(i) {
            n.x = i.pageX, n.y = i.pageY
        }),
        function() {
            for (i = 0; i < d.nb; i++) d.array.push(new u)
        }(), requestAnimationFrame(function a() {
            o.clearRect(0, 0, t.width, t.height),
                function() {
                    for (i = 0; i < d.nb; i++) {
                        var o = d.array[i];
                        o.y < 0 || o.y > t.height ? (o.vx = o.vx, o.vy = -o.vy) : (o.x < 0 || o.x > t.width) && (o.vx = -o.vx, o.vy = o.vy), o.x += o.vx, o.y += o.vy
                    }
                }(),
                function() {
                    for (i = 0; i < d.nb; i++)
                        for (j = 0; j < d.nb; j++) i_dot = d.array[i], j_dot = d.array[j], i_dot.x - j_dot.x < d.distance && i_dot.y - j_dot.y < d.distance && i_dot.x - j_dot.x > -d.distance && i_dot.y - j_dot.y > -d.distance && i_dot.x - n.x < d.d_radius && i_dot.y - n.y < d.d_radius && i_dot.x - n.x > -d.d_radius && i_dot.y - n.y > -d.d_radius && (o.beginPath(), o.strokeStyle = (t = i_dot, a = j_dot, r = void 0, e = void 0, y = void 0, u = void 0, c = void 0, r = t.color, e = a.color, y = s(r.r, t.radius, e.r, a.radius), u = s(r.g, t.radius, e.g, a.radius), c = s(r.b, t.radius, e.b, a.radius), h(Math.floor(y), Math.floor(u), Math.floor(c))), o.moveTo(i_dot.x, i_dot.y), o.lineTo(j_dot.x, j_dot.y), o.stroke(), o.closePath());
                    var t, a, r, e, y, u, c
                }(),
                function() {
                    for (i = 0; i < d.nb; i++) d.array[i].draw()
                }(), requestAnimationFrame(a)
        })
}
$(document).ready(function() {
    canvasAnimation()
}), $(window).resize(function() {
    canvasAnimation()
});

let letters = document.getElementsByClassName('title-letter');

setTimeout(() => {
    for (let i = 0; i < letters.length; i++) {
        anime({
            targets: letters[i],
            easing: 'easeInQuad',
            translateX: ['5px', '0'],
            delay: 50 * i
        });

        anime({
            targets: letters[i],
            easing: 'easeInQuad',
            opacity: 1,
            delay: 60 * i,
            complete: function(anim) {
                if (i === letters.length - 1) {
                    showSubTitle()
                }
            }
        });
    }
}, 500);


function showSubTitle() {
    anime({
        targets: '#sub-title',
        easing: 'easeInQuad',
        opacity: 1,
        duration: 300,
        delay: 1
    });
}