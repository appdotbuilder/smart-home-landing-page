from sqlmodel import select, asc
from app.database import get_session
from app.models import (
    HeroSection,
    Service,
    Benefit,
    CallToAction,
    FooterContent,
    ContactSubmission,
    PageView,
    SiteConfiguration,
    HeroSectionCreate,
    ServiceCreate,
    BenefitCreate,
    ContactSubmissionCreate,
)
from typing import List, Optional
from datetime import datetime
import logging
import re

logger = logging.getLogger(__name__)


class LandingPageService:
    """Service layer for landing page operations"""

    @staticmethod
    def get_hero_section() -> Optional[HeroSection]:
        """Get the active hero section"""
        try:
            with get_session() as session:
                statement = select(HeroSection).where(HeroSection.is_active)
                return session.exec(statement).first()
        except Exception as e:
            logger.error(f"Error fetching hero section: {e}")
            return None

    @staticmethod
    def get_services() -> List[Service]:
        """Get all active services ordered by display_order"""
        try:
            with get_session() as session:
                statement = select(Service).where(Service.is_active).order_by(asc(Service.display_order))
                return list(session.exec(statement))
        except Exception as e:
            logger.error(f"Error fetching services: {e}")
            return []

    @staticmethod
    def get_benefits() -> List[Benefit]:
        """Get all active benefits ordered by display_order"""
        try:
            with get_session() as session:
                statement = select(Benefit).where(Benefit.is_active).order_by(asc(Benefit.display_order))
                return list(session.exec(statement))
        except Exception as e:
            logger.error(f"Error fetching benefits: {e}")
            return []

    @staticmethod
    def get_cta_buttons() -> List[CallToAction]:
        """Get all active call-to-action buttons ordered by display_order"""
        try:
            with get_session() as session:
                statement = select(CallToAction).where(CallToAction.is_active).order_by(asc(CallToAction.display_order))
                return list(session.exec(statement))
        except Exception as e:
            logger.error(f"Error fetching CTA buttons: {e}")
            return []

    @staticmethod
    def get_footer_content() -> Optional[FooterContent]:
        """Get the active footer content"""
        try:
            with get_session() as session:
                statement = select(FooterContent).where(FooterContent.is_active)
                return session.exec(statement).first()
        except Exception as e:
            logger.error(f"Error fetching footer content: {e}")
            return None

    @staticmethod
    def create_hero_section(hero_data: HeroSectionCreate) -> Optional[HeroSection]:
        """Create a new hero section"""
        try:
            with get_session() as session:
                # Deactivate existing hero sections
                existing_heroes = session.exec(select(HeroSection).where(HeroSection.is_active))
                for hero in existing_heroes:
                    hero.is_active = False

                # Create new hero section
                hero = HeroSection(
                    headline=hero_data.headline,
                    description=hero_data.description,
                    background_image_url=hero_data.background_image_url,
                    is_active=True,
                )
                session.add(hero)
                session.commit()
                session.refresh(hero)
                return hero
        except Exception as e:
            logger.error(f"Error creating hero section: {e}")
            return None

    @staticmethod
    def create_service(service_data: ServiceCreate) -> Optional[Service]:
        """Create a new service"""
        try:
            with get_session() as session:
                service = Service(
                    title=service_data.title,
                    description=service_data.description,
                    icon_class=service_data.icon_class,
                    display_order=service_data.display_order,
                    is_active=True,
                )
                session.add(service)
                session.commit()
                session.refresh(service)
                return service
        except Exception as e:
            logger.error(f"Error creating service: {e}")
            return None

    @staticmethod
    def create_benefit(benefit_data: BenefitCreate) -> Optional[Benefit]:
        """Create a new benefit"""
        try:
            with get_session() as session:
                benefit = Benefit(
                    title=benefit_data.title,
                    description=benefit_data.description,
                    icon_class=benefit_data.icon_class,
                    display_order=benefit_data.display_order,
                    is_active=True,
                )
                session.add(benefit)
                session.commit()
                session.refresh(benefit)
                return benefit
        except Exception as e:
            logger.error(f"Error creating benefit: {e}")
            return None

    @staticmethod
    def submit_contact_form(
        contact_data: ContactSubmissionCreate, ip_address: Optional[str] = None, user_agent: Optional[str] = None
    ) -> Optional[ContactSubmission]:
        """Submit a contact form with security validations"""
        try:
            # Input validation and sanitization
            if not LandingPageService._validate_email(contact_data.email):
                logger.warning(f"Invalid email format submitted: {contact_data.email}")
                return None

            if not LandingPageService._validate_phone(contact_data.phone):
                logger.warning(f"Invalid phone format submitted: {contact_data.phone}")
                return None

            # Rate limiting check (basic implementation)
            if ip_address and LandingPageService._check_rate_limit(ip_address):
                logger.warning(f"Rate limit exceeded for IP: {ip_address}")
                return None

            with get_session() as session:
                contact = ContactSubmission(
                    name=contact_data.name.strip()[:100],  # Sanitize and limit length
                    email=contact_data.email.strip().lower()[:255],
                    phone=contact_data.phone.strip()[:20] if contact_data.phone else None,
                    message=contact_data.message.strip()[:2000],
                    ip_address=LandingPageService._anonymize_ip(ip_address) if ip_address else None,
                    user_agent=user_agent[:500] if user_agent else None,
                    status="new",
                )
                session.add(contact)
                session.commit()
                session.refresh(contact)
                return contact
        except Exception as e:
            logger.error(f"Error submitting contact form: {e}")
            return None

    @staticmethod
    def log_page_view(
        page_path: str,
        ip_address: Optional[str] = None,
        user_agent: Optional[str] = None,
        referrer: Optional[str] = None,
        session_id: Optional[str] = None,
    ) -> Optional[PageView]:
        """Log a page view for analytics"""
        try:
            with get_session() as session:
                page_view = PageView(
                    page_path=page_path[:200],
                    ip_address=LandingPageService._anonymize_ip(ip_address) if ip_address else None,
                    user_agent=user_agent[:500] if user_agent else None,
                    referrer=referrer[:500] if referrer else None,
                    session_id=session_id[:100] if session_id else None,
                )
                session.add(page_view)
                session.commit()
                session.refresh(page_view)
                return page_view
        except Exception as e:
            logger.error(f"Error logging page view: {e}")
            return None

    @staticmethod
    def get_site_config(key: str) -> Optional[str]:
        """Get a site configuration value"""
        try:
            with get_session() as session:
                statement = select(SiteConfiguration).where(
                    SiteConfiguration.config_key == key, SiteConfiguration.is_active
                )
                config = session.exec(statement).first()
                return config.config_value if config else None
        except Exception as e:
            logger.error(f"Error fetching site config for key {key}: {e}")
            return None

    @staticmethod
    def _validate_email(email: str) -> bool:
        """Validate email format"""
        if not email or len(email) > 255:
            return False
        pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        return re.match(pattern, email) is not None

    @staticmethod
    def _validate_phone(phone: Optional[str]) -> bool:
        """Validate phone format (if provided)"""
        if not phone:
            return True  # Phone is optional
        if len(phone) > 20:
            return False
        # Basic phone validation - digits, spaces, dashes, parentheses, plus
        pattern = r"^[\d\s\-\(\)\+]+$"
        return re.match(pattern, phone) is not None

    @staticmethod
    def _check_rate_limit(ip_address: str) -> bool:
        """Check if IP address has exceeded rate limit"""
        try:
            with get_session() as session:
                # Check submissions in the last hour
                from datetime import timedelta

                hour_ago = datetime.utcnow() - timedelta(hours=1)

                # Use anonymized IP for rate limiting
                anonymized_ip = LandingPageService._anonymize_ip(ip_address)

                statement = select(ContactSubmission).where(
                    ContactSubmission.ip_address == anonymized_ip, ContactSubmission.created_at >= hour_ago
                )
                recent_submissions = session.exec(statement).all()

                # Allow max 3 submissions per hour per IP
                return len(recent_submissions) >= 3
        except Exception as e:
            logger.error(f"Error checking rate limit: {e}")
            return False  # Allow submission if check fails

    @staticmethod
    def _anonymize_ip(ip_address: str) -> str:
        """Anonymize IP address for privacy compliance"""
        try:
            if ":" in ip_address:  # IPv6
                parts = ip_address.split(":")
                if len(parts) >= 4:
                    return ":".join(parts[:4]) + ":0000:0000:0000:0000"
                else:
                    return "anonymized"
            else:  # IPv4
                parts = ip_address.split(".")
                if len(parts) == 4:
                    return ".".join(parts[:3]) + ".0"
                else:
                    return "anonymized"
        except Exception as e:
            logger.error(f"Error anonymizing IP address: {e}")
            return "anonymized"


# Initialize default data for landing page
def initialize_default_data() -> None:
    """Initialize default landing page data if none exists"""
    try:
        service = LandingPageService()

        # Check if hero section exists
        if not service.get_hero_section():
            logger.info("Creating default hero section")
            hero_data = HeroSectionCreate(
                headline="Transform Your Home with Smart IT Solutions",
                description="Experience the future of home automation with our cutting-edge IT solutions.",
            )
            service.create_hero_section(hero_data)

        # Check if services exist
        existing_services = service.get_services()
        if not existing_services:
            logger.info("Creating default services")
            default_services = [
                ServiceCreate(
                    title="Smart Lighting Systems",
                    description="Intelligent lighting solutions that adapt to your lifestyle.",
                    icon_class="lightbulb",
                    display_order=1,
                ),
                ServiceCreate(
                    title="Advanced Security Networks",
                    description="Comprehensive security systems with HD cameras and smart locks.",
                    icon_class="security",
                    display_order=2,
                ),
                ServiceCreate(
                    title="Energy Management",
                    description="Optimize your home's energy consumption with smart automation.",
                    icon_class="power",
                    display_order=3,
                ),
            ]

            for service_data in default_services:
                service.create_service(service_data)

        logger.info("Default landing page data initialization completed")

    except Exception as e:
        logger.error(f"Error initializing default data: {e}")
