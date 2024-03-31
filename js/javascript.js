// (c) 2021 Mineyuki Iwasaki

// Scroll
window.addEventListener('scroll', function () {
    // Change header color
    let header = document.getElementById('header');
    if (header) {
        if (window.scrollY < 50) {
            header.style.backgroundColor = 'rgba(0, 0, 0, 0)';
        } else {
            header.style.backgroundColor = 'rgba(0, 0, 0, 0.75)';
        }
    }

    // Scroll parallax
    let user_agent = window.navigator.userAgent.toLowerCase();
    let parallax = document.getElementById('parallax');
    let parallax2 = document.getElementById('parallax2');
    let parallax3 = document.getElementById('parallax3');
    if (user_agent.indexOf('android') !== -1 || user_agent.indexOf('ipad') !== -1 || user_agent.indexOf('iphone') !== -1) {
        // Phone
        if (parallax) {
            parallax.style.backgroundPositionY = String(0.5 * window.scrollY) + 'px';
        }
        if (parallax2) {
            parallax2.style.backgroundPositionY = String(0.5 * window.scrollY - 500) + 'px';
        }
        if (parallax3) {
            parallax3.style.backgroundPositionY = String(0.5 * window.scrollY - 900) + 'px';
        }
    } else {
        // PC
        if (parallax) {
            parallax.style.backgroundAttachment = 'fixed';
            parallax.style.backgroundPositionY = String(-0.5 * window.scrollY) + 'px';
        }
        if (parallax2) {
            parallax2.style.backgroundAttachment = 'fixed';
            parallax2.style.backgroundPositionY = String(-0.5 * window.scrollY + 500) + 'px';
        }
        if (parallax3) {
            parallax3.style.backgroundAttachment = 'fixed';
            parallax3.style.backgroundPositionY = String(-0.5 * window.scrollY + 900) + 'px';
        }
    }
});
