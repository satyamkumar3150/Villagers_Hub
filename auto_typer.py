import sys
import time
import random
import subprocess
import os

index_html = """<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title> Villager's Hub - Services </title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/7.0.1/css/all.min.css"
        integrity="sha512-2SwdPD6INVrV/lHTZbO2nodKhrnDdJK9/kg2XD1r9uGqPo1cUbujc+IYdlYdEErWNu69gVcYgdxlmVmzTWnetw=="
        crossorigin="anonymous" referrerpolicy="no-referrer" />
    <link rel="stylesheet" href="main.css">
</head>

<body>
    <header>
        <nav class="navbar flex between wrapper">
            <a href="index.html" class="logo">Villager's Hub</a>
            <ul class="navlist flex gap-3">
                <li><a href="index.html">Home</a></li>
                <li><a href="services.html">Services</a></li>
                <li><a href="about.html">About Us</a></li>
                <li><a href="menu.html">Menu</a></li>
                <li><a href="contact.html">Contact</a></li>
            </ul>
            <div class="desktop-action flex gap-2">
                <a href="#" class="cart-icon"><i class="fa-solid fa-bag-shopping"></i><span
                        class="cart-value">0</span></a>
                <a href="#" class="btn">Sign in &nbsp;<i class="fa-solid fa-arrow-right-from-bracket"></i></a>
                <label for="nav-toggle" class="hamburger"><i class="fa-solid fa-bars"></i></label>
            </div>
            <input type="checkbox" id="nav-toggle">
            <ul class="mobile-menu">
                <li><a href="index.html">Home</a></li>
                <li><a href="services.html">Services</a></li>
                <li><a href="about.html">About Us</a></li>
                <li><a href="menu.html">Menu</a></li>
                <li><a href="contact.html">Contact</a></li>
                <li><a href="#" class="btn">Sign in &nbsp;<i class="fa-solid fa-arrow-right-from-bracket"></i></a></li>
            </ul>
        </nav>
    </header>

    <main>
        <section class="wrapper" style="padding: 4rem 0;">
            <div style="text-align: center;">
                <h1>Our <span>Services</span></h1>
                <p class="para" style="margin: 1rem auto;">We provide top-notch services for all your needs.</p>
            </div>

            <div class="services-grid">
                <div class="service-card">
                    <div class="service-icon"><i class="fa-solid fa-truck-fast"></i></div>
                    <h3>Fast Delivery</h3>
                    <p style="color: gray; margin-top: 1rem;">We ensure your food reaches you hot and fresh within 30
                        minutes.</p>
                </div>
                <div class="service-card">
                    <div class="service-icon"><i class="fa-solid fa-utensils"></i></div>
                    <h3>Quality Food</h3>
                    <p style="color: gray; margin-top: 1rem;">Prepared by expert chefs using the finest ingredients from
                        the village.</p>
                </div>
                <div class="service-card">
                    <div class="service-icon"><i class="fa-solid fa-headset"></i></div>
                    <h3>24/7 Support</h3>
                    <p style="color: gray; margin-top: 1rem;">Our team is always available to assist you with your
                        orders.</p>
                </div>
            </div>
        </section>
    </main>

    <footer style="text-align: center; padding: 2rem; background-color: var(--hint-yellow); margin-top: 2rem;">
        <p>&copy; 2025 Villager's Hub. All rights reserved.</p>
    </footer>
</body>

</html>"""

style_css = """@import url('https://fonts.googleapis.com/css2?family=Roboto+Condensed:ital,wght@0,100..900;1,100..900&display=swap');


* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    font-family: "Roboto Condensed", sans-serif;
    /* border: .1rem solid red; */
}

:root {
    --lead: #212121;
    --gold-finger: #F2BD12;
    --eye-ball: #FFFDF7;
    --hint-yellow: #FCF1CC;
    --pure-white: #FFF;
}

body {
    background: var(--eye-ball);
}


/* Basic Styling */
a {
    font-size: 1.1rem;
    text-decoration: none;
    color: var(--lead)
}

.flex {
    display: flex;
    align-items: center;
}

li {
    list-style: none;
}

.between {
    justify-content: space-between;
}

.gap-2 {
    gap: 2rem;
}

.gap-3 {
    gap: 3rem;
}

.wrapper {
    max-width: 1400px;
    /* background-color: gold; */
    margin: auto;
    padding-inline: 1.5rem;
}

img {
    max-width: 100%;
    height: auto;
    margin: auto;
    display: block;
}

.p-top {}



/* header Styling */
.navbar {
    min-height: 14vh;
    position: relative;
}

.logo {
    font-size: 2rem;
    font-weight: bold;
    color: var(--gold-finger)
}

.btn {
    display: inline-block;
    padding: .9rem 2rem;
    background: var(--gold-finger);
    border-radius: 1rem;
    font-size: 1.1rem;
    color: var(--pure-white);
    box-shadow: rgba(0, 0, 0, 0.1) 0 2px 1px;
    transition: .3s ease-in-out;
}

.btn:hover {
    background: var(--lead);
}

.cart-icon {
    /* color: var(--lead); */
    font-size: 1.3rem;
    position: relative;
}

.cart-icon .cart-value {
    position: absolute;
    top: 50%;
    right: -10px;
    font-size: .85rem;
    width: 20px;
    aspect-ratio: 1;
    border-radius: 100vw;
    background: var(--gold-finger);
    color: var(--lead);
    text-align: center;
    line-height: 20px;
}

.desktop-action .hamburger {
    font-size: 1.5rem;
    display: none;
}

.mobile-menu {
    display: none;
}




/* Sections Styling */
.hero-section {
    /* background: gold; */
    min-height: calc(100vh - 14vh);
}

.content,
.image-container {
    flex: 1;
}

h1 {
    font-size: 5.6vw;
    color: var(--lead);
}

#nav-toggle {
    opacity: 0;
    position: fixed;
    width: 0;
    height: 0;
    pointer-events: none;
}

h1 span {
    color: var(--gold-finger);
}

p {
    font-size: 1.25rem;
    color: gray;
    line-height: 1.8rem;
}

.para {
    margin-block: 2rem;
    max-width: 550px;
}

.social-icon {
    background: var(--hint-yellow);
    width: 3rem;
    aspect-ratio: 1;
    border-radius: 1rem;
    font-size: 1.2rem;
    text-align: center;
    line-height: 3rem;
    box-shadow: rgba(0, 0, 0, 0.1) 0 2px 1px;
    transition: .3s ease-in-out;
}

.social-icon:hover {
    background: var(--lead);
    color: var(--pure-white);
}




/* Footer Styling */






















/* Media Queries */

/* HEADER STYLING */
@media screen and (max-width: 780px) {

    .navlist,
    .desktop-action .btn {
        display: none;
    }

    .desktop-action .hamburger {
        display: block;
        cursor: pointer;
    }



    .mobile-menu {
        display: none;
        /* Hidden by default */
        flex-direction: column;
        justify-content: center;
        align-items: center;
        gap: 2rem;
        position: absolute;
        top: 100%;
        /* Below header */
        right: 1.5rem;
        /* Align to right edge with some padding */
        left: auto;
        transform: none;
        width: 20rem;
        padding: 2rem;
        background: var(--pure-white);
        border: .1rem solid var(--gold-finger);
        border-radius: 2rem;
        box-shadow:
            rgba(0, 0, 0, 0.05) 8px 8px 8px,
            rgba(0, 0, 0, 0.05) 8px 8px 8px inset;
        transition: all .5s ease-in-out;
        z-index: 1000;
    }

    /* Show menu when checkbox is checked */
    #nav-toggle:checked~.mobile-menu {
        display: flex;
    }


    /* SECTIONS STYLING */
    h1 {
        font-size: 3.6rem;
    }

    .content {
        padding-top: 3rem;
    }

    .gap-2 {
        gap: 1.4rem;
    }

    gap-4 {
        gap: 4rem;
    }




}

/* About Page Styling */
.about-content {
    padding: 4rem 0;
    text-align: center;
}

/* Services Page Styling */
.services-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 2rem;
    margin-top: 4rem;
}

.service-card {
    background: white;
    padding: 2rem;
    border-radius: 1rem;
    text-align: center;
    box-shadow: rgba(0, 0, 0, 0.1) 0 4px 6px;
    transition: .3s ease;
}

.service-card:hover {
    transform: translateY(-5px);
}

.service-icon {
    font-size: 3rem;
    color: var(--gold-finger);
    margin-bottom: 1rem;
}

/* Contact Page Styling */
.contact-form {
    max-width: 600px;
    margin: 4rem auto;
    background: white;
    padding: 3rem;
    border-radius: 2rem;
    box-shadow: rgba(0, 0, 0, 0.1) 0 4px 6px;
}

.form-group {
    margin-bottom: 1.5rem;
}

.form-label {
    display: block;
    margin-bottom: 0.5rem;
    color: var(--lead);
    font-weight: bold;
}

.form-input,
.form-textarea {
    width: 100%;
    padding: 1rem;
    border: 1px solid #ddd;
    border-radius: 0.5rem;
    font-size: 1rem;
}

.form-textarea {
    height: 150px;
    resize: vertical;
}

/* Menu Page Styling */
.menu-section {
    padding: 2rem 0;
}

.menu-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 2rem;
    padding-bottom: 2rem;
}

.menu-card {
    background: white;
    border-radius: 1.5rem;
    overflow: hidden;
    box-shadow: rgba(0, 0, 0, 0.1) 0 4px 6px;
    transition: transform 0.3s ease;
    display: flex;
    flex-direction: column;
}

.menu-card:hover {
    transform: translateY(-5px);
}

.menu-img {
    width: 100%;
    height: 200px;
    object-fit: cover;
}

.menu-info {
    padding: 1.5rem;
    flex-grow: 1;
    display: flex;
    flex-direction: column;
}

.menu-info h3 {
    font-size: 1.5rem;
    color: var(--lead);
    margin-bottom: 0.5rem;
}

.menu-desc {
    color: gray;
    margin-bottom: 1rem;
    flex-grow: 1;
}

.menu-options {
    margin-bottom: 1rem;
}

.price-select {
    width: 100%;
    padding: 0.5rem;
    border: 1px solid #ddd;
    border-radius: 0.5rem;
    font-size: 1rem;
    color: var(--lead);
    background-color: var(--pure-white);
}

.menu-action {
    text-align: center;
}"""

script_js = """document.addEventListener('DOMContentLoaded', () => {
    const canvas = document.getElementById('particle-canvas');
    if (!canvas) return;
    
    const ctx = canvas.getContext('2d');

    let width, height;
    let mouseX = 0;
    let mouseY = 0;
    let targetMouseX = 0;
    let targetMouseY = 0;
    
    let exactMouseX = -1000;
    let exactMouseY = -1000;
    const MOUSE_RADIUS = 150;

    let isMouseOverCard = false;
    let gravityEnabled = false;

    class Spark {
        constructor() {
            this.x = Math.random() * window.innerWidth;
            this.y = Math.random() * window.innerHeight;
            this.size = Math.random() * 2 + 1;
            
            this.vx = (Math.random() - 0.5) * 1.5;
            this.vy = (Math.random() - 0.5) * 1.5;
            this.speedX = this.vx;
            this.speedY = this.vy;
            
            const fireColors = ['#ff3300', '#ff6600', '#ffaa00'];
            this.color = fireColors[Math.floor(Math.random() * fireColors.length)];
        }

        update() {
            if (gravityEnabled) {
                this.speedY += 0.15;
            } else {
                this.speedY -= 0.02;
            }

            this.x += this.speedX;
            this.y += this.speedY;

            if (this.x < 0) { this.x = 0; this.speedX *= -0.8; this.vx *= -1; }
            if (this.x > width) { this.x = width; this.speedX *= -0.8; this.vx *= -1; }
            
            if (this.y < 0) { 
                if (gravityEnabled) {
                    this.y = 0; this.speedY *= -0.8; this.vy *= -1;
                } else {
                    this.y = height;
                }
            }
            if (this.y > height) {
                if (gravityEnabled) {
                    this.y = height;
                    this.speedY *= -0.6;
                    this.vy *= -1;
                } else {
                    this.y = 0;
                }
            }

            const parallaxX = mouseX * -20;
            const parallaxY = mouseY * -20;
            const shiftedMouseX = exactMouseX - parallaxX;
            const shiftedMouseY = exactMouseY - parallaxY;

            const dx = shiftedMouseX - this.x;
            const dy = shiftedMouseY - this.y;
            const distance = Math.sqrt(dx * dx + dy * dy);
            
            if (!isMouseOverCard && distance < MOUSE_RADIUS) {
                const force = (MOUSE_RADIUS - distance) / MOUSE_RADIUS;
                const fx = dx / distance;
                const fy = dy / distance;
                
                this.speedX -= fx * force * 5;
                this.speedY -= fy * force * 5;
            } else {
                if (!gravityEnabled) {
                    this.speedX -= (this.speedX - this.vx) * 0.05;
                    this.speedY -= (this.speedY - this.vy) * 0.05;
                } else {
                    this.speedX *= 0.99;
                }
            }
            
            this.speedX = Math.max(-10, Math.min(this.speedX, 10));
            this.speedY = Math.max(-10, Math.min(this.speedY, 10));
        }

        draw() {
            ctx.fillStyle = this.color; 
            ctx.shadowBlur = 10;        
            ctx.shadowColor = this.color;
            ctx.beginPath();
            ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
            ctx.fill();
            ctx.shadowBlur = 0; 
        }
    }

    class BurstFlame {
        constructor(x, y) {
            this.x = x;
            this.y = y;
            
            const angle = Math.random() * Math.PI * 2;
            const speed = Math.random() * 10 + 2; 
            this.vx = Math.cos(angle) * speed;
            this.vy = Math.sin(angle) * speed;
            this.size = Math.random() * 3 + 1;
            
            const colors = ['#ff0000', '#ff6600', '#ffff00'];
            this.color = colors[Math.floor(Math.random() * colors.length)];
            
            this.life = 1.0;
            this.decay = Math.random() * 0.03 + 0.01; 
        }
        
        update() {
            if (gravityEnabled) {
                this.vy += 0.3; 
            } else {
                this.vy -= 0.1;
            }

            this.x += this.vx;
            this.y += this.vy;
            
            this.vx *= 0.92;
            this.vy *= 0.92;
            
            if (this.y > height) {
                this.y = height;
                this.vy *= -0.5;
            }
            this.life -= this.decay;
        }
        
        draw() {
            ctx.globalAlpha = Math.max(0, this.life);
            ctx.strokeStyle = this.color;
            ctx.lineWidth = this.size;
            ctx.lineCap = 'round';
            ctx.shadowBlur = 15;
            ctx.shadowColor = this.color;
            
            ctx.beginPath();
            ctx.moveTo(this.x - this.vx * 2, this.y - this.vy * 2);
            ctx.lineTo(this.x, this.y);
            ctx.stroke();
            
            ctx.shadowBlur = 0;
            ctx.globalAlpha = 1.0;
        }
    }

    let sparksArray = [];
    let burstsArray = [];

    function initParticles() {
        sparksArray = [];
        for (let i = 0; i < 150; i++) {
            sparksArray.push(new Spark());
        }
    }

    function resizeCanvas() {
        width = canvas.width = window.innerWidth;
        height = canvas.height = window.innerHeight;
        initParticles();
    }

    resizeCanvas();
    window.addEventListener('resize', resizeCanvas);

    window.addEventListener('mousemove', (e) => {
        targetMouseX = (e.clientX - width / 2) / (width / 2);
        targetMouseY = (e.clientY - height / 2) / (height / 2);
        exactMouseX = e.clientX;
        exactMouseY = e.clientY;
    });

    const uiCard = document.getElementById('ui-card');
    uiCard.addEventListener('mouseenter', () => isMouseOverCard = true);
    uiCard.addEventListener('mouseleave', () => isMouseOverCard = false);

    document.getElementById('btn-reset').addEventListener('click', () => {
        initParticles();
    });

    const btnGravity = document.getElementById('btn-gravity');
    btnGravity.addEventListener('click', () => {
        gravityEnabled = !gravityEnabled;
        if (gravityEnabled) {
            btnGravity.classList.add('active');
            btnGravity.innerText = "Gravity: ON";
        } else {
            btnGravity.classList.remove('active');
            btnGravity.innerText = "Gravity: OFF";
        }
    });

    window.addEventListener('click', (e) => {
        if (isMouseOverCard) return; 
        
        const parallaxX = mouseX * -20;
        const parallaxY = mouseY * -20;
        const startX = e.clientX - parallaxX;
        const startY = e.clientY - parallaxY;

        const count = 30 + Math.random() * 20;
        for (let i = 0; i < count; i++) {
            burstsArray.push(new BurstFlame(startX, startY));
        }
    });

    let time = 0;
    const focalLength = 300; 
    
    function project(x, y, z) {
        if (z < 0.1) z = 0.1; 
        return {
            x: width / 2 + x * (focalLength / z),
            y: (height * 0.4) + y * (focalLength / z) 
        };
    }

    function animate() {
        ctx.fillStyle = '#0f0200';
        ctx.fillRect(0, 0, width, height);

        time += 2; 
        mouseX += (targetMouseX - mouseX) * 0.05;
        mouseY += (targetMouseY - mouseY) * 0.05;

        const gridSpacing = 60;
        const offsetZ = time % gridSpacing;
        const camX = mouseX * 200;
        const camY = 120 + mouseY * 60; 
        
        ctx.beginPath();
        for (let i = 1; i < 40; i++) {
            const z = i * gridSpacing - offsetZ;
            if (z < 1) continue;
            const start = project(-2000 - camX, camY, z);
            const end = project(2000 - camX, camY, z);
            ctx.moveTo(start.x, start.y);
            ctx.lineTo(end.x, end.y);
        }
        
        for (let i = -30; i <= 30; i++) {
            const x = i * gridSpacing - camX;
            const start = project(x, camY, gridSpacing - offsetZ);
            const end = project(x, camY, 40 * gridSpacing - offsetZ);
            ctx.moveTo(start.x, start.y);
            ctx.lineTo(end.x, end.y);
        }
        
        const horizonY = height * 0.4;
        const gradient = ctx.createLinearGradient(0, horizonY, 0, height);
        gradient.addColorStop(0, 'rgba(255, 50, 0, 0)');     
        gradient.addColorStop(0.1, 'rgba(255, 50, 0, 0.1)'); 
        gradient.addColorStop(0.5, 'rgba(255, 100, 0, 0.4)'); 
        gradient.addColorStop(1, 'rgba(255, 150, 0, 0.8)');   
        ctx.strokeStyle = gradient;
        ctx.lineWidth = 1.5;
        ctx.stroke();

        ctx.save();
        ctx.translate(mouseX * -20, mouseY * -20);

        ctx.strokeStyle = 'rgba(255, 100, 0, 0.15)';
        ctx.lineWidth = 1;
        ctx.beginPath();
        for (let i = 0; i < sparksArray.length; i++) {
            for (let j = i + 1; j < sparksArray.length; j++) {
                const dx = sparksArray[i].x - sparksArray[j].x;
                const dy = sparksArray[i].y - sparksArray[j].y;
                if (dx * dx + dy * dy < 10000) { 
                    ctx.moveTo(sparksArray[i].x, sparksArray[i].y);
                    ctx.lineTo(sparksArray[j].x, sparksArray[j].y);
                }
            }
        }
        ctx.stroke();

        for (let i = 0; i < sparksArray.length; i++) {
            sparksArray[i].update();
            sparksArray[i].draw();
        }

        for (let i = burstsArray.length - 1; i >= 0; i--) {
            let p = burstsArray[i];
            p.update();
            p.draw();
            if (p.life <= 0) {
                burstsArray.splice(i, 1);
            }
        }

        ctx.restore(); 

        if (!isMouseOverCard && exactMouseX !== -1000) {
            ctx.beginPath();
            ctx.arc(exactMouseX, exactMouseY, 60, 0, Math.PI * 2);
            ctx.fillStyle = 'rgba(255, 100, 0, 0.05)';
            ctx.shadowBlur = 50;
            ctx.shadowColor = '#ff6600';
            ctx.fill();
            ctx.shadowBlur = 0; 
        }

        requestAnimationFrame(animate);
    }
    
    animate();
});"""

files = {
    "index.html": index_html,
    "style.css": style_css,
    "script.js": script_js
}

def type_chunk_via_clipboard(chunk):
    # Put text chunk directly onto clipboard
    p = subprocess.Popen(['pbcopy'], stdin=subprocess.PIPE)
    p.communicate(input=chunk.encode('utf-8'))
    # Trigger Cmd+V to paste the chunk
    subprocess.run(["osascript", "-e", 'tell application "System Events" to keystroke "v" using command down'])

def type_text(text):
    start_time = time.time()
    
    # Save the user's original clipboard safely
    try:
        orig_clip = subprocess.check_output(['pbpaste']).decode('utf-8')
    except Exception:
        orig_clip = ""
        
    idx = 0
    while idx < len(text):
        if time.time() - start_time > 13:
            pause = random.uniform(3.0, 5.0)
            print(f"\\n[Taking a {pause:.1f}s human-like break...]", flush=True)
            time.sleep(pause)
            start_time = time.time()
            
        # Burst typing: chunks of characters
        chunk_size = random.randint(2, 6)
        chunk = text[idx : idx + chunk_size]
        idx += chunk_size
        
        type_chunk_via_clipboard(chunk)
        
        # We need ~35-40 WPM. That is ~200 chars/min => ~3.33 char/sec.
        delay = chunk_size / random.uniform(4.5, 5.5)
        time.sleep(delay)

    # Restore the user's clipboard
    p = subprocess.Popen(['pbcopy'], stdin=subprocess.PIPE)
    p.communicate(input=orig_clip.encode('utf-8'))


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('file', choices=['index.html', 'style.css', 'script.js'], help='File to type')
    args = parser.parse_args()

    print(f"\\n--- Get ready to type {args.file} ---")
    print("1. Please switch to VS Code immediately and EMPTY the file.")
    print("2. You have 5 seconds to place your cursor inside the empty file.")
    print("3. DO NOT CLICK AWAY!\\n")

    for i in range(5, 0, -1):
        print(f"Starting in {i}...")
        time.sleep(1)
        
    print("Typing started! To cancel, press Ctrl+C in this terminal window.")
    try:
        type_text(files[args.file])
        print(f"\\nFinished typing {args.file}!")
    except KeyboardInterrupt:
        print("\\n[ABORTED] Type script cancelled.")