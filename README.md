<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Mohsan | Cybersecurity Portfolio</title>
<style>
    :root {
        --primary: #2563eb;
        --dark: #1e293b;
        --light: #f8fafc;
        --gray: #64748b;
        --transition: all 0.3s ease;
    }
    * { margin:0; padding:0; box-sizing:border-box; }
    body { font-family: sans-serif; background: var(--light); color: var(--dark); line-height: 1.6; scroll-behavior: smooth; }
    a { text-decoration: none; color: inherit; }
    header { position: fixed; top:0; width:100%; background: var(--light); padding: 15px 20px; box-shadow: 0 2px 5px rgba(0,0,0,0.1); z-index:100; display:flex; justify-content:space-between; align-items:center; }
    header .logo { font-weight:bold; color: var(--primary); font-size:1.5rem; }
    nav ul { display:flex; list-style:none; gap:20px; }
    nav ul li a:hover { color: var(--primary); }
    section { padding: 100px 20px 60px 20px; max-width: 900px; margin: auto; }
    h2 { font-size:2rem; margin-bottom:20px; text-align:center; color: var(--dark); }
    .btn { display:inline-block; padding:10px 20px; background: var(--primary); color:white; border-radius:5px; transition: var(--transition); }
    .btn:hover { background: #1d4ed8; }
    .hero { text-align:center; padding-top:150px; padding-bottom:100px; }
    .hero h1 { font-size:2.5rem; margin-bottom:20px; }
    .hero p { margin-bottom:20px; color: var(--gray); }
    .about, .skills, .projects, .education, .contact { background:white; margin-top:50px; border-radius:10px; padding:30px; box-shadow:0 5px 15px rgba(0,0,0,0.05); }
    .skills-list, .projects-list { display:grid; gap:15px; }
    .skill { display:flex; justify-content:space-between; }
    .skill-bar { width:70%; height:10px; background:#e2e8f0; border-radius:5px; overflow:hidden; }
    .skill-progress { height:100%; background:var(--primary); width:0; transition: width 1.5s ease; }
    .project, .education-item { border:1px solid #e2e8f0; border-radius:5px; padding:15px; }
    .contact form { display:flex; flex-direction:column; gap:15px; }
    input, textarea { padding:10px; border-radius:5px; border:1px solid #ccc; width:100%; }
    footer { text-align:center; padding:20px; margin-top:50px; color: var(--gray); }
    @media(max-width:600px){ nav ul{flex-direction:column; gap:10px;} }
</style>
</head>
<body>

<header>
    <div class="logo">Mohsan</div>
    <nav>
        <ul>
            <li><a href="#hero">Home</a></li>
            <li><a href="#about">About</a></li>
            <li><a href="#skills">Skills</a></li>
            <li><a href="#projects">Projects</a></li>
            <li><a href="#education">Education</a></li>
            <li><a href="#contact">Contact</a></li>
        </ul>
    </nav>
</header>

<section id="hero" class="hero">
    <h1>Hi, I'm Mohsan</h1>
    <p>Cybersecurity Student | Ethical Hacking Enthusiast</p>
    <a href="#projects" class="btn">View My Projects</a>
</section>

<section id="about" class="about">
    <h2>About Me</h2>
    <p>Hello! I'm Mohsan, a cybersecurity student at UMT, 3rd semester. I am passionate about learning penetration testing, network security, and ethical hacking. My goal is to secure systems and understand how digital threats work.</p>
</section>

<section id="skills" class="skills">
    <h2>My Skills</h2>
    <div class="skills-list">
        <div class="skill">
            <span>Python</span>
            <div class="skill-bar"><div class="skill-progress" data-width="60%"></div></div>
        </div>
        <div class="skill">
            <span>Linux</span>
            <div class="skill-bar"><div class="skill-progress" data-width="50%"></div></div>
        </div>
        <div class="skill">
            <span>Networking</span>
            <div class="skill-bar"><div class="skill-progress" data-width="55%"></div></div>
        </div>
        <div class="skill">
            <span>Git/GitHub</span>
            <div class="skill-bar"><div class="skill-progress" data-width="70%"></div></div>
        </div>
    </div>
</section>

<section id="projects" class="projects">
    <h2>Mini Projects / Labs</h2>
    <div class="projects-list">
        <div class="project">
            <h3>Password Strength Checker</h3>
            <p>Python script to validate password strength.</p>
            <a href="#">View on GitHub</a>
        </div>
        <div class="project">
            <h3>Simple Port Scanner</h3>
            <p>Python-based network scanner to detect open ports.</p>
            <a href="#">View on GitHub</a>
        </div>
        <div class="project">
            <h3>Basic Website Analysis</h3>
            <p>HTML/CSS/JS project to check website headers and security info.</p>
            <a href="#">View on GitHub</a>
        </div>
    </div>
</section>

<section id="education" class="education">
    <h2>Education</h2>
    <div class="education-item">
        <h3>Bachelor in Cybersecurity, UMT</h3>
        <p>3rd Semester | 2025</p>
        <p>Courses: Networking, Python, Ethical Hacking Labs</p>
    </div>
</section>

<section id="contact" class="contact">
    <h2>Contact Me</h2>
    <form id="contactForm">
        <input type="text" placeholder="Your Name" required>
        <input type="email" placeholder="Your Email" required>
        <textarea placeholder="Your Message" required></textarea>
        <button type="submit" class="btn">Send Message</button>
    </form>
</section>

<footer>
    <p>© 2025 Mohsan | Cybersecurity Student</p>
</footer>

<script>
// Animate skill bars
window.addEventListener('scroll', () => {
    document.querySelectorAll('.skill-progress').forEach(bar => {
        const rect = bar.getBoundingClientRect();
        if(rect.top < window.innerHeight){
            bar.style.width = bar.getAttribute('data-width');
        }
    });
});

// Contact form simple alert
document.getElementById('contactForm').addEventListener('submit', e => {
    e.preventDefault();
    alert('Thanks! I will contact you soon.');
    e.target.reset();
});
</script>

</body>
</html>
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Mohsan | Cybersecurity Portfolio</title>
<style>
    :root {
        --primary: #2563eb;
        --dark: #1e293b;
        --light: #f8fafc;
        --gray: #64748b;
        --transition: all 0.3s ease;
    }
    * { margin:0; padding:0; box-sizing:border-box; }
    body { font-family: sans-serif; background: var(--light); color: var(--dark); line-height: 1.6; scroll-behavior: smooth; }
    a { text-decoration: none; color: inherit; }
    header { position: fixed; top:0; width:100%; background: var(--light); padding: 15px 20px; box-shadow: 0 2px 5px rgba(0,0,0,0.1); z-index:100; display:flex; justify-content:space-between; align-items:center; }
    header .logo { font-weight:bold; color: var(--primary); font-size:1.5rem; }
    nav ul { display:flex; list-style:none; gap:20px; }
    nav ul li a:hover { color: var(--primary); }
    section { padding: 100px 20px 60px 20px; max-width: 900px; margin: auto; }
    h2 { font-size:2rem; margin-bottom:20px; text-align:center; color: var(--dark); }
    .btn { display:inline-block; padding:10px 20px; background: var(--primary); color:white; border-radius:5px; transition: var(--transition); }
    .btn:hover { background: #1d4ed8; }
    .hero { text-align:center; padding-top:150px; padding-bottom:100px; }
    .hero h1 { font-size:2.5rem; margin-bottom:20px; }
    .hero p { margin-bottom:20px; color: var(--gray); }
    .about, .skills, .projects, .education, .contact { background:white; margin-top:50px; border-radius:10px; padding:30px; box-shadow:0 5px 15px rgba(0,0,0,0.05); }
    .skills-list, .projects-list { display:grid; gap:15px; }
    .skill { display:flex; justify-content:space-between; }
    .skill-bar { width:70%; height:10px; background:#e2e8f0; border-radius:5px; overflow:hidden; }
    .skill-progress { height:100%; background:var(--primary); width:0; transition: width 1.5s ease; }
    .project, .education-item { border:1px solid #e2e8f0; border-radius:5px; padding:15px; }
    .contact form { display:flex; flex-direction:column; gap:15px; }
    input, textarea { padding:10px; border-radius:5px; border:1px solid #ccc; width:100%; }
    footer { text-align:center; padding:20px; margin-top:50px; color: var(--gray); }
    @media(max-width:600px){ nav ul{flex-direction:column; gap:10px;} }
</style>
</head>
<body>

<header>
    <div class="logo">Mohsan</div>
    <nav>
        <ul>
            <li><a href="#hero">Home</a></li>
            <li><a href="#about">About</a></li>
            <li><a href="#skills">Skills</a></li>
            <li><a href="#projects">Projects</a></li>
            <li><a href="#education">Education</a></li>
            <li><a href="#contact">Contact</a></li>
        </ul>
    </nav>
</header>

<section id="hero" class="hero">
    <h1>Hi, I'm Mohsan</h1>
    <p>Cybersecurity Student | Ethical Hacking Enthusiast</p>
    <a href="#projects" class="btn">View My Projects</a>
</section>

<section id="about" class="about">
    <h2>About Me</h2>
    <p>Hello! I'm Mohsan, a cybersecurity student at UMT, 3rd semester. I am passionate about learning penetration testing, network security, and ethical hacking. My goal is to secure systems and understand how digital threats work.</p>
</section>

<section id="skills" class="skills">
    <h2>My Skills</h2>
    <div class="skills-list">
        <div class="skill">
            <span>Python</span>
            <div class="skill-bar"><div class="skill-progress" data-width="60%"></div></div>
        </div>
        <div class="skill">
            <span>Linux</span>
            <div class="skill-bar"><div class="skill-progress" data-width="50%"></div></div>
        </div>
        <div class="skill">
            <span>Networking</span>
            <div class="skill-bar"><div class="skill-progress" data-width="55%"></div></div>
        </div>
        <div class="skill">
            <span>Git/GitHub</span>
            <div class="skill-bar"><div class="skill-progress" data-width="70%"></div></div>
        </div>
    </div>
</section>

<section id="projects" class="projects">
    <h2>Mini Projects / Labs</h2>
    <div class="projects-list">
        <div class="project">
            <h3>Password Strength Checker</h3>
            <p>Python script to validate password strength.</p>
            <a href="#">View on GitHub</a>
        </div>
        <div class="project">
            <h3>Simple Port Scanner</h3>
            <p>Python-based network scanner to detect open ports.</p>
            <a href="#">View on GitHub</a>
        </div>
        <div class="project">
            <h3>Basic Website Analysis</h3>
            <p>HTML/CSS/JS project to check website headers and security info.</p>
            <a href="#">View on GitHub</a>
        </div>
    </div>
</section>

<section id="education" class="education">
    <h2>Education</h2>
    <div class="education-item">
        <h3>Bachelor in Cybersecurity, UMT</h3>
        <p>3rd Semester | 2025</p>
        <p>Courses: Networking, Python, Ethical Hacking Labs</p>
    </div>
</section>

<section id="contact" class="contact">
    <h2>Contact Me</h2>
    <form id="contactForm">
        <input type="text" placeholder="Your Name" required>
        <input type="email" placeholder="Your Email" required>
        <textarea placeholder="Your Message" required></textarea>
        <button type="submit" class="btn">Send Message</button>
    </form>
</section>

<footer>
    <p>© 2025 Mohsan | Cybersecurity Student</p>
</footer>

<script>
// Animate skill bars
window.addEventListener('scroll', () => {
    document.querySelectorAll('.skill-progress').forEach(bar => {
        const rect = bar.getBoundingClientRect();
        if(rect.top < window.innerHeight){
            bar.style.width = bar.getAttribute('data-width');
        }
    });
});

// Contact form simple alert
document.getElementById('contactForm').addEventListener('submit', e => {
    e.preventDefault();
    alert('Thanks! I will contact you soon.');
    e.target.reset();
});
</script>

</body>
</html>
