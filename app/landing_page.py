from nicegui import ui
import logging

logger = logging.getLogger(__name__)


def apply_theme() -> None:
    """Apply black and blue color scheme with modern design"""
    ui.colors(
        primary="#2563eb",  # Professional blue
        secondary="#1e293b",  # Dark slate
        accent="#3b82f6",  # Bright blue
        positive="#10b981",  # Success green
        negative="#ef4444",  # Error red
        warning="#f59e0b",  # Warning amber
        info="#06b6d4",  # Info cyan
    )

    # Add custom CSS for enhanced styling and security
    ui.add_head_html("""
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="Professional IT Smart Home Solutions - Transform your home with cutting-edge technology">
    <meta name="keywords" content="smart home, IT solutions, home automation, security systems, energy management">
    <meta name="robots" content="index, follow">
    <meta http-equiv="X-Content-Type-Options" content="nosniff">
    <meta http-equiv="X-Frame-Options" content="DENY">
    <meta http-equiv="X-XSS-Protection" content="1; mode=block">
    <meta http-equiv="Referrer-Policy" content="strict-origin-when-cross-origin">
    
    <style>
        :root {
            --primary-blue: #2563eb;
            --dark-bg: #0f172a;
            --darker-bg: #020617;
            --light-blue: #3b82f6;
            --text-light: #e2e8f0;
            --text-gray: #64748b;
        }
        
        .hero-gradient {
            background: linear-gradient(135deg, var(--darker-bg) 0%, var(--dark-bg) 50%, var(--primary-blue) 100%);
        }
        
        .glass-card {
            background: rgba(15, 23, 42, 0.8);
            backdrop-filter: blur(10px);
            border: 1px solid rgba(59, 130, 246, 0.2);
        }
        
        .service-card {
            background: var(--dark-bg);
            border: 1px solid rgba(59, 130, 246, 0.1);
            transition: all 0.3s ease;
        }
        
        .service-card:hover {
            border-color: var(--primary-blue);
            transform: translateY(-4px);
            box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.3);
        }
        
        .benefit-item {
            background: rgba(15, 23, 42, 0.6);
            border-left: 4px solid var(--primary-blue);
        }
        
        .cta-button {
            background: linear-gradient(45deg, var(--primary-blue), var(--light-blue));
            transition: all 0.3s ease;
        }
        
        .cta-button:hover {
            transform: translateY(-2px);
            box-shadow: 0 10px 20px rgba(37, 99, 235, 0.3);
        }
        
        .whatsapp-btn {
            background: linear-gradient(45deg, #25d366, #128c7e);
        }
        
        .email-btn {
            background: linear-gradient(45deg, var(--primary-blue), #1d4ed8);
        }
        
        body {
            background-color: var(--darker-bg);
            color: var(--text-light);
        }
        
        /* Responsive design */
        @media (max-width: 768px) {
            .hero-content {
                padding: 2rem 1rem;
            }
            .service-grid {
                grid-template-columns: 1fr;
            }
        }
        
        /* Accessibility improvements */
        .btn-focus:focus {
            outline: 2px solid var(--primary-blue);
            outline-offset: 2px;
        }
        
        /* Security: Hide potential info leakage */
        .no-select {
            -webkit-user-select: none;
            -moz-user-select: none;
            -ms-user-select: none;
            user-select: none;
        }
    </style>
    """)


def create_hero_section() -> None:
    """Create the hero section with prominent headline and description"""
    with ui.element("section").classes("hero-gradient min-h-screen flex items-center justify-center px-4"):
        with ui.column().classes("max-w-6xl mx-auto text-center hero-content"):
            # Hero headline
            ui.label("Transform Your Home with Smart IT Solutions").classes(
                "text-5xl md:text-7xl font-bold text-white mb-6 leading-tight"
            )

            # Hero description
            ui.label(
                "Experience the future of home automation with our cutting-edge IT solutions. "
                "From intelligent lighting systems to advanced security networks, we bring "
                "technology and comfort together seamlessly."
            ).classes("text-xl md:text-2xl text-slate-300 mb-12 max-w-4xl mx-auto leading-relaxed")

            # Hero CTA buttons
            with ui.row().classes("gap-6 justify-center flex-wrap"):
                ui.button("Get Free Consultation", on_click=lambda: scroll_to_cta()).classes(
                    "cta-button text-white px-8 py-4 text-lg font-semibold rounded-xl btn-focus"
                ).props("no-caps")

                ui.button("View Our Services", on_click=lambda: scroll_to_services()).classes(
                    "border-2 border-blue-500 text-blue-400 hover:bg-blue-500 hover:text-white px-8 py-4 text-lg font-semibold rounded-xl btn-focus"
                ).props("outline no-caps")


def create_services_section() -> None:
    """Create the services section with key offerings"""
    with ui.element("section").classes("py-20 px-4").add_slot("services"):
        with ui.column().classes("max-w-6xl mx-auto"):
            # Section header
            ui.label("Our Smart Home Services").classes("text-4xl md:text-5xl font-bold text-center mb-4 text-white")
            ui.label("Comprehensive IT solutions tailored for modern smart homes").classes(
                "text-xl text-slate-400 text-center mb-16 max-w-3xl mx-auto"
            )

            # Services grid
            services_data = [
                {
                    "icon": "lightbulb",
                    "title": "Smart Lighting Systems",
                    "description": "Intelligent lighting solutions that adapt to your lifestyle. Control brightness, color, and scheduling from anywhere with energy-efficient LED technology and automated sensors.",
                },
                {
                    "icon": "security",
                    "title": "Advanced Security Networks",
                    "description": "Comprehensive security systems with HD cameras, smart locks, motion sensors, and 24/7 monitoring. Protect your home with enterprise-grade cybersecurity protocols.",
                },
                {
                    "icon": "power",
                    "title": "Energy Management",
                    "description": "Optimize your home's energy consumption with smart meters, automated HVAC control, and renewable energy integration. Reduce costs while maintaining comfort.",
                },
                {
                    "icon": "wifi",
                    "title": "Network Infrastructure",
                    "description": "High-performance Wi-Fi networks, mesh systems, and IoT device management. Ensure seamless connectivity throughout your smart home ecosystem.",
                },
                {
                    "icon": "home",
                    "title": "Home Automation Hub",
                    "description": "Centralized control systems that integrate all your smart devices. Voice control, mobile apps, and automated routines for ultimate convenience.",
                },
                {
                    "icon": "support_agent",
                    "title": "Technical Support",
                    "description": "24/7 technical support and maintenance services. Regular updates, troubleshooting, and system optimization to keep your smart home running perfectly.",
                },
            ]

            with ui.element("div").classes("grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8"):
                for service in services_data:
                    with ui.card().classes("service-card p-8 rounded-2xl"):
                        ui.icon(service["icon"]).classes("text-5xl text-blue-400 mb-6")
                        ui.label(service["title"]).classes("text-2xl font-bold text-white mb-4")
                        ui.label(service["description"]).classes("text-slate-300 leading-relaxed")


def create_benefits_section() -> None:
    """Create the benefits section detailing why to choose the company"""
    with ui.element("section").classes("py-20 px-4 bg-slate-900/50"):
        with ui.column().classes("max-w-6xl mx-auto"):
            # Section header
            ui.label("Why Choose Our Smart Home Solutions").classes(
                "text-4xl md:text-5xl font-bold text-center mb-4 text-white"
            )
            ui.label("Experience the advantages of working with industry-leading professionals").classes(
                "text-xl text-slate-400 text-center mb-16 max-w-3xl mx-auto"
            )

            benefits_data = [
                {
                    "icon": "verified",
                    "title": "Certified IT Professionals",
                    "description": "Our team consists of certified network engineers, cybersecurity specialists, and smart home technology experts with years of industry experience.",
                },
                {
                    "icon": "speed",
                    "title": "Rapid Implementation",
                    "description": "Quick and efficient installation processes with minimal disruption to your daily routine. Most systems are operational within 24-48 hours.",
                },
                {
                    "icon": "security",
                    "title": "Enterprise-Grade Security",
                    "description": "Military-level encryption, secure protocols, and regular security audits ensure your smart home data remains private and protected.",
                },
                {
                    "icon": "savings",
                    "title": "Cost-Effective Solutions",
                    "description": "Reduce energy bills by up to 30% with intelligent automation. Our solutions pay for themselves through energy savings and increased home value.",
                },
                {
                    "icon": "update",
                    "title": "Future-Proof Technology",
                    "description": "Scalable systems designed to grow with advancing technology. Regular firmware updates and hardware upgrade paths included.",
                },
                {
                    "icon": "support",
                    "title": "Lifetime Support",
                    "description": "Comprehensive warranty coverage, 24/7 technical support, and free system health monitoring to ensure optimal performance.",
                },
            ]

            with ui.element("div").classes("grid grid-cols-1 md:grid-cols-2 gap-8"):
                for benefit in benefits_data:
                    with ui.element("div").classes("benefit-item p-6 rounded-xl"):
                        with ui.row().classes("items-start gap-4"):
                            ui.icon(benefit["icon"]).classes("text-3xl text-blue-400 mt-1")
                            with ui.column().classes("flex-1"):
                                ui.label(benefit["title"]).classes("text-xl font-bold text-white mb-2")
                                ui.label(benefit["description"]).classes("text-slate-300 leading-relaxed")


def create_cta_section() -> None:
    """Create the call-to-action section with WhatsApp and Email buttons"""
    with ui.element("section").classes("py-20 px-4").add_slot("cta"):
        with ui.column().classes("max-w-4xl mx-auto text-center"):
            # CTA header
            ui.label("Ready to Transform Your Home?").classes("text-4xl md:text-5xl font-bold mb-6 text-white")
            ui.label(
                "Get in touch with our experts today for a free consultation and personalized smart home solution."
            ).classes("text-xl text-slate-300 mb-12 max-w-3xl mx-auto leading-relaxed")

            # Contact statistics
            with ui.row().classes("justify-center gap-8 mb-12 flex-wrap"):
                with ui.element("div").classes("text-center"):
                    ui.label("500+").classes("text-3xl font-bold text-blue-400")
                    ui.label("Homes Automated").classes("text-slate-400")

                with ui.element("div").classes("text-center"):
                    ui.label("24/7").classes("text-3xl font-bold text-blue-400")
                    ui.label("Support Available").classes("text-slate-400")

                with ui.element("div").classes("text-center"):
                    ui.label("98%").classes("text-3xl font-bold text-blue-400")
                    ui.label("Customer Satisfaction").classes("text-slate-400")

            # CTA buttons
            with ui.row().classes("gap-6 justify-center flex-wrap"):
                ui.button("Contact via WhatsApp", icon="chat", on_click=lambda: open_whatsapp()).classes(
                    "whatsapp-btn text-white px-8 py-4 text-lg font-semibold rounded-xl btn-focus"
                ).props("no-caps")

                ui.button("Send us an Email", icon="email", on_click=lambda: open_email()).classes(
                    "email-btn text-white px-8 py-4 text-lg font-semibold rounded-xl btn-focus"
                ).props("no-caps")

            # Additional contact info
            with ui.element("div").classes("mt-12 p-6 glass-card rounded-xl"):
                ui.label("Prefer a Phone Call?").classes("text-lg font-semibold text-white mb-2")
                ui.label("Call us at: +1 (555) 123-SMART").classes("text-blue-400 text-xl font-mono")
                ui.label("Available Monday-Friday, 9AM-6PM EST").classes("text-slate-400 text-sm mt-2")


def create_footer() -> None:
    """Create a simple footer section"""
    with ui.element("footer").classes("bg-slate-950 py-12 px-4 border-t border-slate-800"):
        with ui.column().classes("max-w-6xl mx-auto"):
            with ui.row().classes("justify-between items-start gap-8 flex-wrap"):
                # Company info
                with ui.column().classes("flex-1 min-w-64"):
                    ui.label("SmartHome IT Solutions").classes("text-2xl font-bold text-white mb-4")
                    ui.label(
                        "Transforming homes with cutting-edge technology solutions. "
                        "Your trusted partner for smart home automation and IT infrastructure."
                    ).classes("text-slate-400 leading-relaxed mb-4")

                    # Social links placeholder
                    with ui.row().classes("gap-4"):
                        ui.icon("facebook").classes("text-2xl text-slate-500 hover:text-blue-400 cursor-pointer")
                        ui.icon("twitter").classes("text-2xl text-slate-500 hover:text-blue-400 cursor-pointer")
                        ui.icon("linkedin").classes("text-2xl text-slate-500 hover:text-blue-400 cursor-pointer")
                        ui.icon("instagram").classes("text-2xl text-slate-500 hover:text-blue-400 cursor-pointer")

                # Quick links
                with ui.column().classes("min-w-48"):
                    ui.label("Quick Links").classes("text-lg font-semibold text-white mb-4")
                    for link in ["Services", "About Us", "Case Studies", "Support", "Contact"]:
                        ui.label(link).classes("text-slate-400 hover:text-blue-400 cursor-pointer mb-2")

                # Contact info
                with ui.column().classes("min-w-64"):
                    ui.label("Contact Information").classes("text-lg font-semibold text-white mb-4")
                    ui.label("📧 info@smarthome-it.com").classes("text-slate-400 mb-2")
                    ui.label("📞 +1 (555) 123-SMART").classes("text-slate-400 mb-2")
                    ui.label("📍 123 Technology Drive, Smart City, SC 12345").classes("text-slate-400 mb-2")

            # Copyright
            with ui.element("div").classes("border-t border-slate-800 pt-8 mt-8 text-center"):
                ui.label(
                    "© 2024 SmartHome IT Solutions. All rights reserved. | Privacy Policy | Terms of Service"
                ).classes("text-slate-500 no-select")


def scroll_to_services() -> None:
    """Scroll to services section"""
    ui.run_javascript("document.querySelector('[slot=\"services\"]')?.scrollIntoView({ behavior: 'smooth' })")


def scroll_to_cta() -> None:
    """Scroll to CTA section"""
    ui.run_javascript("document.querySelector('[slot=\"cta\"]')?.scrollIntoView({ behavior: 'smooth' })")


def open_whatsapp() -> None:
    """Open WhatsApp with pre-filled message"""
    # OWASP compliant - using client-side redirect with sanitized data
    message = "Hello! I'm interested in your smart home IT solutions. Could you provide more information?"
    phone = "1234567890"  # Replace with actual WhatsApp business number

    try:
        ui.run_javascript(f'''
            const message = encodeURIComponent("{message}");
            const phone = "{phone}";
            const url = `https://wa.me/${{phone}}?text=${{message}}`;
            window.open(url, '_blank', 'noopener,noreferrer');
        ''')
        ui.notify("Opening WhatsApp...", type="info")
    except Exception as e:
        logger.error(f"Error opening WhatsApp: {e}")
        ui.notify("Error opening WhatsApp. Please try again.", type="negative")


def open_email() -> None:
    """Open email client with pre-filled message"""
    # OWASP compliant - using client-side mailto with sanitized data
    try:
        ui.run_javascript("""
            const subject = encodeURIComponent("Smart Home IT Solutions Inquiry");
            const body = encodeURIComponent("Hello,\\n\\nI am interested in learning more about your smart home IT solutions. Please provide information about:\\n\\n- Available services\\n- Pricing options\\n- Installation timeline\\n- Free consultation\\n\\nThank you!");
            const email = "info@smarthome-it.com";
            const mailtoUrl = `mailto:${email}?subject=${subject}&body=${body}`;
            window.location.href = mailtoUrl;
        """)
        ui.notify("Opening email client...", type="info")
    except Exception as e:
        logger.error(f"Error opening email: {e}")
        ui.notify("Error opening email client. Please try again.", type="negative")


def create() -> None:
    """Create the landing page with all sections"""
    apply_theme()

    @ui.page("/")
    def landing_page():
        # Security headers and tracking (OWASP compliant)
        try:
            # Log page view for analytics (anonymized)
            client_ip = getattr(ui.context.client, "environ", {}).get("REMOTE_ADDR", "unknown")
            if client_ip and client_ip != "unknown":
                # In production, implement proper IP anonymization
                logger.info(f"Landing page view from IP: {client_ip[:8]}...")
        except Exception as e:
            logger.error(f"Error logging page view: {e}")

        # Build the page sections
        create_hero_section()
        create_services_section()
        create_benefits_section()
        create_cta_section()
        create_footer()

        # Add smooth scrolling behavior
        ui.add_head_html("<style>html { scroll-behavior: smooth; }</style>")
