// Smooth scrolling for navigation (if needed in future)
document.addEventListener('DOMContentLoaded', function() {
    // Add smooth scrolling to all links
    const links = document.querySelectorAll('a[href^="#"]');
    
    links.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            
            const targetId = this.getAttribute('href');
            const targetSection = document.querySelector(targetId);
            
            if (targetSection) {
                targetSection.scrollIntoView({
                    behavior: 'smooth'
                });
            }
        });
    });

    // Simple fade-in animation for cards
    const cards = document.querySelectorAll('.feature-card, .metric-card');
    cards.forEach((card, index) => {
        setTimeout(() => {
            card.style.opacity = '1';
            card.style.transform = 'translateY(0)';
        }, index * 100);
    });

    // Add loading animation for video
    const iframe = document.querySelector('iframe');
    if (iframe) {
        iframe.addEventListener('load', function() {
            this.style.opacity = '1';
        });
    }

    // Add hover effect for badges
    const badges = document.querySelectorAll('.badge');
    badges.forEach(badge => {
        badge.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-2px) scale(1.05)';
        });
        
        badge.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0) scale(1)';
        });
    });

    // Performance metrics counter animation
    const metricNumbers = document.querySelectorAll('.metric-number');
    
    function animateMetrics() {
        metricNumbers.forEach(metric => {
            const finalValue = metric.textContent;
            const numericValue = parseInt(finalValue.replace(/[^\d]/g, ''));
            
            if (!isNaN(numericValue)) {
                let currentValue = 0;
                const increment = numericValue / 50;
                const timer = setInterval(() => {
                    currentValue += increment;
                    if (currentValue >= numericValue) {
                        metric.textContent = finalValue;
                        clearInterval(timer);
                    } else {
                        metric.textContent = Math.floor(currentValue) + finalValue.replace(/\d/g, '').replace(/^\d/, '');
                    }
                }, 30);
            }
        });
    }

    // Trigger metric animation when results section is visible
    const resultsSection = document.querySelector('.results');
    if (resultsSection) {
        const resultsObserver = new IntersectionObserver(function(entries) {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    animateMetrics();
                    resultsObserver.unobserve(entry.target);
                }
            });
        }, { threshold: 0.3 });
        
        resultsObserver.observe(resultsSection);
    }

    console.log('Robot Challenge presentation loaded successfully! 🤖');
});