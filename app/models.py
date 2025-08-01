from sqlmodel import SQLModel, Field, JSON, Column
from datetime import datetime
from typing import Optional, Dict


# Hero Section Model
class HeroSection(SQLModel, table=True):
    __tablename__ = "hero_sections"  # type: ignore[assignment]

    id: Optional[int] = Field(default=None, primary_key=True)
    headline: str = Field(max_length=200, description="Main hero headline")
    description: str = Field(max_length=500, description="Hero section description")
    background_image_url: Optional[str] = Field(default=None, max_length=500)
    is_active: bool = Field(default=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


# Services Model
class Service(SQLModel, table=True):
    __tablename__ = "services"  # type: ignore[assignment]

    id: Optional[int] = Field(default=None, primary_key=True)
    title: str = Field(max_length=100, description="Service title")
    description: str = Field(max_length=1000, description="Service description")
    icon_class: Optional[str] = Field(default=None, max_length=50, description="CSS icon class")
    display_order: int = Field(default=0, description="Order for displaying services")
    is_active: bool = Field(default=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


# Benefits Model
class Benefit(SQLModel, table=True):
    __tablename__ = "benefits"  # type: ignore[assignment]

    id: Optional[int] = Field(default=None, primary_key=True)
    title: str = Field(max_length=100, description="Benefit title")
    description: str = Field(max_length=800, description="Benefit description")
    icon_class: Optional[str] = Field(default=None, max_length=50, description="CSS icon class")
    display_order: int = Field(default=0, description="Order for displaying benefits")
    is_active: bool = Field(default=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


# Call to Action Model
class CallToAction(SQLModel, table=True):
    __tablename__ = "call_to_actions"  # type: ignore[assignment]

    id: Optional[int] = Field(default=None, primary_key=True)
    button_text: str = Field(max_length=50, description="CTA button text")
    action_type: str = Field(max_length=20, description="Type: 'whatsapp', 'email', 'phone'")
    action_value: str = Field(max_length=200, description="Contact value (phone, email, etc.)")
    button_style: str = Field(default="primary", max_length=20, description="Button styling class")
    display_order: int = Field(default=0, description="Order for displaying CTAs")
    is_active: bool = Field(default=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


# Footer Content Model
class FooterContent(SQLModel, table=True):
    __tablename__ = "footer_contents"  # type: ignore[assignment]

    id: Optional[int] = Field(default=None, primary_key=True)
    company_name: str = Field(max_length=100, description="Company name")
    address: Optional[str] = Field(default=None, max_length=300, description="Company address")
    phone: Optional[str] = Field(default=None, max_length=20, description="Company phone")
    email: Optional[str] = Field(default=None, max_length=100, description="Company email")
    copyright_text: str = Field(max_length=200, description="Copyright text")
    social_links: Dict[str, str] = Field(default={}, sa_column=Column(JSON), description="Social media links")
    is_active: bool = Field(default=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


# Contact Form Submissions (for security and data handling)
class ContactSubmission(SQLModel, table=True):
    __tablename__ = "contact_submissions"  # type: ignore[assignment]

    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(max_length=100, description="Contact name")
    email: str = Field(max_length=255, regex=r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")
    phone: Optional[str] = Field(default=None, max_length=20)
    message: str = Field(max_length=2000, description="Contact message")
    ip_address: Optional[str] = Field(default=None, max_length=45, description="Client IP for security")
    user_agent: Optional[str] = Field(default=None, max_length=500, description="Client user agent")
    status: str = Field(default="new", max_length=20, description="Status: new, contacted, resolved")
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


# Site Configuration Model (for theme colors, settings)
class SiteConfiguration(SQLModel, table=True):
    __tablename__ = "site_configurations"  # type: ignore[assignment]

    id: Optional[int] = Field(default=None, primary_key=True)
    config_key: str = Field(max_length=50, unique=True, description="Configuration key")
    config_value: str = Field(max_length=1000, description="Configuration value")
    config_type: str = Field(default="string", max_length=20, description="Value type: string, json, boolean")
    description: Optional[str] = Field(default=None, max_length=200, description="Configuration description")
    is_active: bool = Field(default=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)


# Security and Analytics Model
class PageView(SQLModel, table=True):
    __tablename__ = "page_views"  # type: ignore[assignment]

    id: Optional[int] = Field(default=None, primary_key=True)
    page_path: str = Field(max_length=200, description="Page path viewed")
    ip_address: Optional[str] = Field(default=None, max_length=45, description="Visitor IP")
    user_agent: Optional[str] = Field(default=None, max_length=500, description="Visitor user agent")
    referrer: Optional[str] = Field(default=None, max_length=500, description="Referrer URL")
    session_id: Optional[str] = Field(default=None, max_length=100, description="Session identifier")
    created_at: datetime = Field(default_factory=datetime.utcnow)


# Non-persistent schemas for validation and forms


class HeroSectionCreate(SQLModel, table=False):
    headline: str = Field(max_length=200)
    description: str = Field(max_length=500)
    background_image_url: Optional[str] = Field(default=None, max_length=500)


class HeroSectionUpdate(SQLModel, table=False):
    headline: Optional[str] = Field(default=None, max_length=200)
    description: Optional[str] = Field(default=None, max_length=500)
    background_image_url: Optional[str] = Field(default=None, max_length=500)
    is_active: Optional[bool] = Field(default=None)


class ServiceCreate(SQLModel, table=False):
    title: str = Field(max_length=100)
    description: str = Field(max_length=1000)
    icon_class: Optional[str] = Field(default=None, max_length=50)
    display_order: int = Field(default=0)


class ServiceUpdate(SQLModel, table=False):
    title: Optional[str] = Field(default=None, max_length=100)
    description: Optional[str] = Field(default=None, max_length=1000)
    icon_class: Optional[str] = Field(default=None, max_length=50)
    display_order: Optional[int] = Field(default=None)
    is_active: Optional[bool] = Field(default=None)


class BenefitCreate(SQLModel, table=False):
    title: str = Field(max_length=100)
    description: str = Field(max_length=800)
    icon_class: Optional[str] = Field(default=None, max_length=50)
    display_order: int = Field(default=0)


class BenefitUpdate(SQLModel, table=False):
    title: Optional[str] = Field(default=None, max_length=100)
    description: Optional[str] = Field(default=None, max_length=800)
    icon_class: Optional[str] = Field(default=None, max_length=50)
    display_order: Optional[int] = Field(default=None)
    is_active: Optional[bool] = Field(default=None)


class CallToActionCreate(SQLModel, table=False):
    button_text: str = Field(max_length=50)
    action_type: str = Field(max_length=20)
    action_value: str = Field(max_length=200)
    button_style: str = Field(default="primary", max_length=20)
    display_order: int = Field(default=0)


class CallToActionUpdate(SQLModel, table=False):
    button_text: Optional[str] = Field(default=None, max_length=50)
    action_type: Optional[str] = Field(default=None, max_length=20)
    action_value: Optional[str] = Field(default=None, max_length=200)
    button_style: Optional[str] = Field(default=None, max_length=20)
    display_order: Optional[int] = Field(default=None)
    is_active: Optional[bool] = Field(default=None)


class ContactSubmissionCreate(SQLModel, table=False):
    name: str = Field(max_length=100)
    email: str = Field(max_length=255, regex=r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")
    phone: Optional[str] = Field(default=None, max_length=20)
    message: str = Field(max_length=2000)


class FooterContentCreate(SQLModel, table=False):
    company_name: str = Field(max_length=100)
    address: Optional[str] = Field(default=None, max_length=300)
    phone: Optional[str] = Field(default=None, max_length=20)
    email: Optional[str] = Field(default=None, max_length=100)
    copyright_text: str = Field(max_length=200)
    social_links: Dict[str, str] = Field(default={})


class FooterContentUpdate(SQLModel, table=False):
    company_name: Optional[str] = Field(default=None, max_length=100)
    address: Optional[str] = Field(default=None, max_length=300)
    phone: Optional[str] = Field(default=None, max_length=20)
    email: Optional[str] = Field(default=None, max_length=100)
    copyright_text: Optional[str] = Field(default=None, max_length=200)
    social_links: Optional[Dict[str, str]] = Field(default=None)
    is_active: Optional[bool] = Field(default=None)


class SiteConfigurationCreate(SQLModel, table=False):
    config_key: str = Field(max_length=50)
    config_value: str = Field(max_length=1000)
    config_type: str = Field(default="string", max_length=20)
    description: Optional[str] = Field(default=None, max_length=200)


class SiteConfigurationUpdate(SQLModel, table=False):
    config_value: Optional[str] = Field(default=None, max_length=1000)
    config_type: Optional[str] = Field(default=None, max_length=20)
    description: Optional[str] = Field(default=None, max_length=200)
    is_active: Optional[bool] = Field(default=None)
