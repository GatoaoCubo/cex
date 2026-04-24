---
id: p05_output_email_template
kind: output_validator
8f: F6_produce
pillar: P05
title: Responsive Email HTML Template with Outlook Compatibility
tldr: Production-ready responsive email templates with Outlook compatibility, dark mode support, and mobile optimization
version: 1.0.0
created: 2026-04-01
author: n02_visual_frontend
domain: frontend
quality: 9.1
density_score: 1.0
tags: [email-template, responsive, html, marketing, n02]
related:
  - n02_kc_email_html_responsive
  - p01_kc_email_html_responsive
  - spec_n02_part2
  - p05_output_social_card
  - p10_hos_html_output_visual_frontend
  - p03_pt_visual_frontend_marketing
  - landing_page_petshop_crm
  - p01_kc_brand_propagation_arch
  - bld_examples_landing_page
  - n02_kc_color_theory_applied
---

# Responsive Email HTML Template

## Purpose

Provides production-ready responsive email templates with comprehensive Outlook compatibility, dark mode support, and web-safe typography. Ensures consistent rendering across all major email clients including Outlook 2007-2019, Gmail, Apple Mail, and mobile clients.

## Template Structure

### Core Architecture
- **Table-based layout**: Ensures Outlook 2007+ compatibility
- **Max-width 600px**: Standard email client viewport
- **Inline CSS**: Required for email client parsing
- **MSO conditionals**: Outlook-specific styling
- **Dark mode media queries**: Modern email client support
- **Web-safe font stack**: Fallback typography system

### Required Components
1. DOCTYPE and MSO compatibility headers
2. Container table with max-width constraint
3. Header section with logo and navigation
4. Content sections with responsive spacing
5. Footer with unsubscribe and social links
6. Dark mode color schemes
7. Mobile breakpoint optimizations

## Complete HTML Example

### Welcome Email Template

```html
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <meta name="color-scheme" content="light dark" />
    <meta name="supported-color-schemes" content="light dark" />
    <title>Welcome to Our Platform</title>
    
    <!-- MSO Outlook Compatibility -->
    <!--[if gte mso 9]>
    <xml>
        <o:OfficeDocumentSettings>
            <o:AllowPNG/>
            <o:PixelsPerInch>96</o:PixelsPerInch>
        </o:OfficeDocumentSettings>
    </xml>
    <![endif]-->
    
    <!-- Dark Mode Support -->
    <style type="text/css">
        /* Client-specific Styles */
        #outlook a { padding: 0; }
        .ReadMsgBody { width: 100%; }
        .ExternalClass { width: 100%; }
        .ExternalClass * { line-height: 100%; }
        
        /* Dark Mode Styles */
        @media (prefers-color-scheme: dark) {
            .dark-mode-bg { background-color: #1a1a1a !important; }
            .dark-mode-text { color: #ffffff !important; }
            .dark-mode-secondary { color: #cccccc !important; }
            .dark-mode-border { border-color: #333333 !important; }
        }
        
        /* Mobile Responsive */
        @media only screen and (max-width: 600px) {
            .mobile-full { width: 100% !important; }
            .mobile-center { text-align: center !important; }
            .mobile-padding { padding: 20px 15px !important; }
            .mobile-hide { display: none !important; }
        }
    </style>
</head>

<body style="margin: 0; padding: 0; background-color: #f5f5f5; font-family: Arial, Helvetica, sans-serif;">
    <!-- Preheader Text (hidden but shows in inbox preview) -->
    <div style="display: none; font-size: 1px; line-height: 1px; max-height: 0; max-width: 0; opacity: 0; overflow: hidden; mso-hide: all;">
        Welcome! Get started with your new account and explore our features.
    </div>
    
    <!-- Main Container Table -->
    <table role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%" style="background-color: #f5f5f5;" class="dark-mode-bg">
        <tr>
            <td align="center" style="padding: 40px 0;">
                
                <!-- Email Container -->
                <table role="presentation" cellspacing="0" cellpadding="0" border="0" width="600" style="max-width: 600px; background-color: #ffffff; border-radius: 8px; box-shadow: 0 2px 8px rgba(0,0,0,0.1);" class="mobile-full dark-mode-bg">
                    
                    <!-- Header Section -->
                    <tr>
                        <td style="padding: 40px 40px 20px 40px; text-align: center; border-bottom: 1px solid #e5e5e5;" class="mobile-padding dark-mode-border">
                            <!-- Logo -->
                            <img src="https://example.com/logo.png" alt="Company Logo" width="120" height="40" style="display: block; margin: 0 auto 20px auto;" />
                            <h1 style="margin: 0; font-size: 28px; font-weight: 600; color: #1f2937; line-height: 1.2;" class="dark-mode-text">
                                Welcome to Our Platform!
                            </h1>
                        </td>
                    </tr>
                    
                    <!-- Main Content Section -->
                    <tr>
                        <td style="padding: 40px;" class="mobile-padding">
                            <p style="margin: 0 0 20px 0; font-size: 16px; line-height: 1.6; color: #374151;" class="dark-mode-secondary">
                                Hi <strong>{{first_name}}</strong>,
                            </p>
                            <p style="margin: 0 0 20px 0; font-size: 16px; line-height: 1.6; color: #374151;" class="dark-mode-secondary">
                                Thank you for joining our platform! We're excited to have you on board and can't wait for you to explore all the amazing features we've built.
                            </p>
                            <p style="margin: 0 0 30px 0; font-size: 16px; line-height: 1.6; color: #374151;" class="dark-mode-secondary">
                                To get started, please verify your email address by clicking the button below:
                            </p>
                            
                            <!-- CTA Button -->
                            <table role="presentation" cellspacing="0" cellpadding="0" border="0" align="center">
                                <tr>
                                    <td style="border-radius: 6px; background-color: #3b82f6;">
                                        <!--[if mso]>
                                        <v:roundrect xmlns:v="urn:schemas-microsoft-com:vml" xmlns:w="urn:schemas-microsoft-com:office:word" href="{{verification_link}}" style="height: 50px; v-text-anchor: middle; width: 200px;" arcsize="12%" stroke="f" fillcolor="#3b82f6">
                                            <w:anchorlock/>
                                            <center style="color: #ffffff; font-family: Arial, sans-serif; font-size: 16px; font-weight: 600;">Verify Email Address</center>
                                        </v:roundrect>
                                        <![endif]-->
                                        <!--[if !mso]><!-- -->
                                        <a href="{{verification_link}}" style="display: inline-block; padding: 15px 30px; background-color: #3b82f6; color: #ffffff; text-decoration: none; font-size: 16px; font-weight: 600; border-radius: 6px;">
                                            Verify Email Address
                                        </a>
                                        <!--<![endif]-->
                                    </td>
                                </tr>
                            </table>
                            
                            <p style="margin: 30px 0 0 0; font-size: 14px; line-height: 1.6; color: #6b7280;" class="dark-mode-secondary">
                                If the button doesn't work, you can copy and paste this link into your browser:<br>
                                <a href="{{verification_link}}" style="color: #3b82f6; word-break: break-all;">{{verification_link}}</a>
                            </p>
                        </td>
                    </tr>
                    
                    <!-- Feature Highlights Section -->
                    <tr>
                        <td style="padding: 0 40px 40px 40px;" class="mobile-padding">
                            <h2 style="margin: 0 0 20px 0; font-size: 20px; font-weight: 600; color: #1f2937;" class="dark-mode-text">
                                What's Next?
                            </h2>
                            
                            <!-- Feature List -->
                            <table role="presentation" cellspacing="0" cellpadding="0" border="0" width="100%">
                                <tr>
                                    <td width="40" style="padding-right: 15px; vertical-align: top;">
                                        <div style="width: 30px; height: 30px; background-color: #dbeafe; border-radius: 6px; display: flex; align-items: center; justify-content: center;">
                                            <span style="color: #3b82f6; font-size: 16px;">✓</span>
                                        </div>
                                    </td>
                                    <td>
                                        <p style="margin: 0 0 15px 0; font-size: 16px; line-height: 1.6; color: #374151;" class="dark-mode-secondary">
                                            <strong>Complete your profile</strong> to personalize your experience
                                        </p>
                                    </td>
                                </tr>
                                <tr>
                                    <td width="40" style="padding-right: 15px; vertical-align: top;">
                                        <div style="width: 30px; height: 30px; background-color: #dbeafe; border-radius: 6px; display: flex; align-items: center; justify-content: center;">
                                            <span style="color: #3b82f6; font-size: 16px;">✓</span>
                                        </div>
                                    </td>
                                    <td>
                                        <p style="margin: 0 0 15px 0; font-size: 16px; line-height: 1.6; color: #374151;" class="dark-mode-secondary">
                                            <strong>Explore our dashboard</strong> and discover powerful tools
                                        </p>
                                    </td>
                                </tr>
                                <tr>
                                    <td width="40" style="padding-right: 15px; vertical-align: top;">
                                        <div style="width: 30px; height: 30px; background-color: #dbeafe; border-radius: 6px; display: flex; align-items: center; justify-content: center;">
                                            <span style="color: #3b82f6; font-size: 16px;">✓</span>
                                        </div>
                                    </td>
                                    <td>
                                        <p style="margin: 0; font-size: 16px; line-height: 1.6; color: #374151;" class="dark-mode-secondary">
                                            <strong>Join our community</strong> and connect with other users
                                        </p>
                                    </td>
                                </tr>
                            </table>
                        </td>
                    </tr>
                    
                    <!-- Footer Section -->
                    <tr>
                        <td style="padding: 30px 40px; background-color: #f9fafb; border-top: 1px solid #e5e5e5;" class="mobile-padding dark-mode-bg dark-mode-border">
                            <!-- Social Links -->
                            <table role="presentation" cellspacing="0" cellpadding="0" border="0" align="center" style="margin-bottom: 20px;">
                                <tr>
                                    <td style="padding-right: 15px;">
                                        <a href="{{twitter_url}}" style="text-decoration: none;">
                                            <img src="https://example.com/twitter-icon.png" alt="Twitter" width="24" height="24" />
                                        </a>
                                    </td>
                                    <td style="padding-right: 15px;">
                                        <a href="{{linkedin_url}}" style="text-decoration: none;">
                                            <img src="https://example.com/linkedin-icon.png" alt="LinkedIn" width="24" height="24" />
                                        </a>
                                    </td>
                                    <td>
                                        <a href="{{facebook_url}}" style="text-decoration: none;">
                                            <img src="https://example.com/facebook-icon.png" alt="Facebook" width="24" height="24" />
                                        </a>
                                    </td>
                                </tr>
                            </table>
                            
                            <!-- Footer Text -->
                            <p style="margin: 0 0 10px 0; font-size: 14px; line-height: 1.5; color: #6b7280; text-align: center;" class="dark-mode-secondary">
                                © 2026 Your Company Name. All rights reserved.
                            </p>
                            <p style="margin: 0 0 10px 0; font-size: 14px; line-height: 1.5; color: #6b7280; text-align: center;" class="dark-mode-secondary">
                                123 Main Street, City, State 12345
                            </p>
                            <p style="margin: 0; font-size: 14px; line-height: 1.5; color: #6b7280; text-align: center;" class="dark-mode-secondary">
                                <a href="{{unsubscribe_url}}" style="color: #3b82f6; text-decoration: underline;">Unsubscribe</a> | 
                                <a href="{{preferences_url}}" style="color: #3b82f6; text-decoration: underline;">Email Preferences</a> |
                                <a href="{{privacy_url}}" style="color: #3b82f6; text-decoration: underline;">Privacy Policy</a>
                            </p>
                        </td>
                    </tr>
                    
                </table>
                
            </td>
        </tr>
    </table>
</body>
</html>
```

## Variants

### 1. Welcome Email
- **Purpose**: New user onboarding
- **Key Elements**: Email verification CTA, feature highlights, next steps
- **Tone**: Friendly, encouraging, informative

### 2. Transactional Email
- **Purpose**: Order confirmations, receipts, notifications
- **Key Elements**: Clear subject line, transaction details, support contact
- **Tone**: Professional, clear, reassuring

### 3. Marketing Email
- **Purpose**: Promotional campaigns, feature announcements
- **Key Elements**: Compelling headlines, product showcases, strong CTAs
- **Tone**: Persuasive, benefit-focused, action-oriented

### 4. Cart Abandonment Email
- **Purpose**: Recover abandoned purchases
- **Key Elements**: Product reminders, urgency indicators, easy checkout links
- **Tone**: Helpful, non-pushy, value-focused

## Usage Notes

### Implementation Guidelines
- **Variable Replacement**: Use `{{variable_name}}` for dynamic content
- **Image Hosting**: Host images on reliable CDN with HTTPS
- **Link Tracking**: Implement UTM parameters for analytics
- **Testing**: Use tools like Litmus or Email on Acid for client testing

### Outlook Compatibility
- **MSO Conditionals**: Essential for Outlook 2007-2019
- **VML Buttons**: Required for proper button rendering
- **Table Structure**: Mandatory for consistent layout

### Dark Mode Support
- **Color Scheme Meta**: Enable automatic dark mode detection
- **CSS Classes**: Use conditional classes for dark mode styling
- **Fallbacks**: Ensure readability when dark mode isn't supported

### Mobile Optimization
- **Viewport Meta**: Essential for mobile rendering
- **Responsive Tables**: Use width percentages and min-widths
- **Touch Targets**: Ensure buttons are at least 44px tall
- **Font Sizes**: Minimum 14px for body text on mobile

### Performance Considerations
- **Inline CSS**: Required for maximum compatibility
- **Image Optimization**: Use compressed, web-optimized formats
- **HTML Size**: Keep total email under 102KB for Gmail
- **Load Times**: Optimize for slow mobile connections

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[n02_kc_email_html_responsive]] | upstream | 0.69 |
| [[p01_kc_email_html_responsive]] | upstream | 0.68 |
| [[spec_n02_part2]] | downstream | 0.36 |
| [[p05_output_social_card]] | sibling | 0.35 |
| [[p10_hos_html_output_visual_frontend]] | downstream | 0.33 |
| [[p03_pt_visual_frontend_marketing]] | upstream | 0.28 |
| [[landing_page_petshop_crm]] | related | 0.28 |
| [[p01_kc_brand_propagation_arch]] | upstream | 0.28 |
| [[bld_examples_landing_page]] | upstream | 0.27 |
| [[n02_kc_color_theory_applied]] | upstream | 0.26 |
