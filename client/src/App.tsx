import './App.css';
import { useState } from 'react';

function App() {
  const [isMenuOpen, setIsMenuOpen] = useState(false);

  const handleWhatsAppContact = () => {
    // OWASP-compliant external link handling with validation
    const phoneNumber = "+1234567890"; // Placeholder number
    const message = encodeURIComponent("Hi! I'm interested in your IT smart home solutions.");
    const whatsappUrl = `https://wa.me/${phoneNumber.replace(/[^\d]/g, '')}?text=${message}`;
    window.open(whatsappUrl, '_blank', 'noopener,noreferrer');
  };

  const handleEmailContact = () => {
    // OWASP-compliant email handling
    const email = "contact@smarthomeit.com"; // Placeholder email
    const subject = encodeURIComponent("Inquiry about IT Smart Home Solutions");
    const body = encodeURIComponent("Hello,\n\nI'm interested in learning more about your smart home IT solutions.\n\nBest regards");
    const mailtoUrl = `mailto:${email}?subject=${subject}&body=${body}`;
    window.location.href = mailtoUrl;
  };

  return (
    <div className="app">
      {/* Navigation Header */}
      <nav className="nav">
        <div className="nav-container">
          <div className="nav-brand">
            <span className="brand-text">SmartHome IT</span>
          </div>
          <button 
            className={`nav-toggle ${isMenuOpen ? 'active' : ''}`}
            onClick={() => setIsMenuOpen(!isMenuOpen)}
            aria-label="Toggle navigation menu"
          >
            <span></span>
            <span></span>
            <span></span>
          </button>
          <div className={`nav-menu ${isMenuOpen ? 'active' : ''}`}>
            <a href="#home" className="nav-link">Home</a>
            <a href="#services" className="nav-link">Services</a>
            <a href="#benefits" className="nav-link">Benefits</a>
            <a href="#contact" className="nav-link">Contact</a>
          </div>
        </div>
      </nav>

      {/* Hero Section */}
      <section id="home" className="hero">
        <div className="hero-container">
          <div className="hero-content">
            <h1 className="hero-title">
              Transform Your Home with
              <span className="hero-highlight"> Smart IT Solutions</span>
            </h1>
            <p className="hero-description">
              Experience the future of home automation with our cutting-edge IT solutions. 
              From intelligent lighting to advanced security systems, we bring technology 
              and comfort together seamlessly.
            </p>
            <div className="hero-actions">
              <button 
                className="btn btn-primary"
                onClick={handleWhatsAppContact}
                aria-label="Contact us via WhatsApp"
              >
                <span className="btn-icon">📱</span>
                WhatsApp Us
              </button>
              <button 
                className="btn btn-secondary"
                onClick={handleEmailContact}
                aria-label="Contact us via email"
              >
                <span className="btn-icon">✉️</span>
                Email Us
              </button>
            </div>
          </div>
          <div className="hero-visual">
            <div className="hero-graphic">
              <div className="smart-grid">
                <div className="grid-item">🏠</div>
                <div className="grid-item">💡</div>
                <div className="grid-item">🔒</div>
                <div className="grid-item">📱</div>
                <div className="grid-item">🌡️</div>
                <div className="grid-item">📊</div>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* Services Section */}
      <section id="services" className="services">
        <div className="container">
          <div className="section-header">
            <h2 className="section-title">Our Services</h2>
            <p className="section-description">
              Comprehensive smart home solutions tailored to your needs
            </p>
          </div>
          <div className="services-grid">
            <div className="service-card">
              <div className="service-icon">💡</div>
              <h3 className="service-title">Smart Lighting</h3>
              <p className="service-description">
                Intelligent lighting systems that adapt to your lifestyle. 
                Control brightness, color, and schedules from anywhere.
              </p>
              <ul className="service-features">
                <li>Voice control integration</li>
                <li>Energy-efficient LED systems</li>
                <li>Automated scheduling</li>
                <li>Remote access control</li>
              </ul>
            </div>
            
            <div className="service-card">
              <div className="service-icon">🔒</div>
              <h3 className="service-title">Security Systems</h3>
              <p className="service-description">
                Advanced security solutions with real-time monitoring 
                and instant alerts for complete peace of mind.
              </p>
              <ul className="service-features">
                <li>24/7 monitoring systems</li>
                <li>Smart door locks</li>
                <li>HD security cameras</li>
                <li>Motion detection alerts</li>
              </ul>
            </div>
            
            <div className="service-card">
              <div className="service-icon">⚡</div>
              <h3 className="service-title">Energy Management</h3>
              <p className="service-description">
                Optimize your home's energy consumption with smart 
                monitoring and automated efficiency controls.
              </p>
              <ul className="service-features">
                <li>Real-time energy tracking</li>
                <li>Smart thermostat integration</li>
                <li>Automated power management</li>
                <li>Cost optimization reports</li>
              </ul>
            </div>
            
            <div className="service-card">
              <div className="service-icon">🏠</div>
              <h3 className="service-title">Home Automation</h3>
              <p className="service-description">
                Complete home automation systems that integrate all 
                your smart devices into one seamless experience.
              </p>
              <ul className="service-features">
                <li>Centralized control hub</li>
                <li>Multi-device integration</li>
                <li>Custom automation rules</li>
                <li>Voice assistant compatibility</li>
              </ul>
            </div>
            
            <div className="service-card">
              <div className="service-icon">📡</div>
              <h3 className="service-title">Network Infrastructure</h3>
              <p className="service-description">
                Robust networking solutions to ensure all your smart 
                devices stay connected and perform optimally.
              </p>
              <ul className="service-features">
                <li>High-speed Wi-Fi coverage</li>
                <li>Network security protocols</li>
                <li>IoT device management</li>
                <li>24/7 technical support</li>
              </ul>
            </div>
            
            <div className="service-card">
              <div className="service-icon">🎵</div>
              <h3 className="service-title">Entertainment Systems</h3>
              <p className="service-description">
                Immersive audio-visual experiences with integrated 
                smart entertainment solutions throughout your home.
              </p>
              <ul className="service-features">
                <li>Multi-room audio systems</li>
                <li>Smart TV integration</li>
                <li>Streaming optimization</li>
                <li>Theater room setups</li>
              </ul>
            </div>
          </div>
        </div>
      </section>

      {/* Benefits Section */}
      <section id="benefits" className="benefits">
        <div className="container">
          <div className="section-header">
            <h2 className="section-title">Why Choose Us</h2>
            <p className="section-description">
              Experience the advantages of professional smart home IT solutions
            </p>
          </div>
          <div className="benefits-grid">
            <div className="benefit-item">
              <div className="benefit-icon">🎯</div>
              <h3 className="benefit-title">Expert Installation</h3>
              <p className="benefit-description">
                Our certified technicians ensure seamless installation and 
                configuration of all smart home systems with minimal disruption.
              </p>
            </div>
            
            <div className="benefit-item">
              <div className="benefit-icon">🛡️</div>
              <h3 className="benefit-title">Enhanced Security</h3>
              <p className="benefit-description">
                Advanced cybersecurity measures protect your smart home network 
                and personal data from potential threats.
              </p>
            </div>
            
            <div className="benefit-item">
              <div className="benefit-icon">💰</div>
              <h3 className="benefit-title">Cost Savings</h3>
              <p className="benefit-description">
                Smart energy management and automation reduce utility bills 
                while increasing your home's value and efficiency.
              </p>
            </div>
            
            <div className="benefit-item">
              <div className="benefit-icon">🚀</div>
              <h3 className="benefit-title">Future-Ready Technology</h3>
              <p className="benefit-description">
                Stay ahead with cutting-edge solutions that adapt and scale 
                with emerging smart home technologies.
              </p>
            </div>
            
            <div className="benefit-item">
              <div className="benefit-icon">🔧</div>
              <h3 className="benefit-title">24/7 Support</h3>
              <p className="benefit-description">
                Round-the-clock technical support ensures your smart home 
                systems operate smoothly without interruption.
              </p>
            </div>
            
            <div className="benefit-item">
              <div className="benefit-icon">📱</div>
              <h3 className="benefit-title">Easy Control</h3>
              <p className="benefit-description">
                Intuitive mobile apps and voice controls make managing 
                your smart home simple and convenient.
              </p>
            </div>
          </div>
        </div>
      </section>

      {/* Call to Action Section */}
      <section id="contact" className="cta">
        <div className="container">
          <div className="cta-content">
            <h2 className="cta-title">Ready to Transform Your Home?</h2>
            <p className="cta-description">
              Get started with a free consultation and discover how our IT smart home 
              solutions can enhance your lifestyle, security, and energy efficiency.
            </p>
            <div className="cta-actions">
              <button 
                className="btn btn-primary btn-large"
                onClick={handleWhatsAppContact}
                aria-label="Start consultation via WhatsApp"
              >
                <span className="btn-icon">📱</span>
                Start WhatsApp Chat
              </button>
              <button 
                className="btn btn-secondary btn-large"
                onClick={handleEmailContact}
                aria-label="Send consultation request via email"
              >
                <span className="btn-icon">✉️</span>
                Send Email Inquiry
              </button>
            </div>
            <div className="cta-info">
              <p className="cta-note">
                ✨ Free consultation • 🏆 5+ years experience • 🛡️ Fully insured
              </p>
            </div>
          </div>
        </div>
      </section>

      {/* Footer */}
      <footer className="footer">
        <div className="container">
          <div className="footer-content">
            <div className="footer-section">
              <h3 className="footer-title">SmartHome IT</h3>
              <p className="footer-description">
                Leading provider of intelligent home automation and IT solutions. 
                Transforming homes with cutting-edge technology since 2018.
              </p>
            </div>
            
            <div className="footer-section">
              <h4 className="footer-heading">Services</h4>
              <ul className="footer-links">
                <li><a href="#services">Smart Lighting</a></li>
                <li><a href="#services">Security Systems</a></li>
                <li><a href="#services">Energy Management</a></li>
                <li><a href="#services">Home Automation</a></li>
              </ul>
            </div>
            
            <div className="footer-section">
              <h4 className="footer-heading">Contact</h4>
              <div className="footer-contact">
                <p>📧 contact@smarthomeit.com</p>
                <p>📱 +1 (555) 123-4567</p>
                <p>📍 123 Tech Street, Smart City, SC 12345</p>
              </div>
            </div>
            
            <div className="footer-section">
              <h4 className="footer-heading">Follow Us</h4>
              <div className="footer-social">
                <a href="#" aria-label="Facebook">📘</a>
                <a href="#" aria-label="Twitter">🐦</a>
                <a href="#" aria-label="LinkedIn">💼</a>
                <a href="#" aria-label="Instagram">📷</a>
              </div>
            </div>
          </div>
          
          <div className="footer-bottom">
            <div className="footer-bottom-content">
              <p>&copy; 2024 SmartHome IT Solutions. All rights reserved.</p>
              <div className="footer-legal">
                <a href="#" className="footer-legal-link">Privacy Policy</a>
                <a href="#" className="footer-legal-link">Terms of Service</a>
                <a href="#" className="footer-legal-link">Cookie Policy</a>
              </div>
            </div>
          </div>
        </div>
      </footer>
    </div>
  );
}

export default App;