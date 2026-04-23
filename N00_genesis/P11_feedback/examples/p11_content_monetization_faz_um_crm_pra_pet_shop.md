---  
id: petshop-crm  
kind: content_monetization  
pillar: P11  
title: "Pet Shop CRM"  
version: "1.0.0"  
created: "2023-10-15"  
author: "content-monetization-builder"  
domain: petshop-crm  
quality: null  
tags: [content-monetization, pricing, petshop-crm]  
---  
# Pet Shop CRM  
## Pipeline (9 stages)  
### Pricing Strategy  
- **Strategy**: tiered  
- **Floor Margin**: 0.35  
- **Trial Days**: 7  
- **Tiers**:  
  - Free: 0 centavos, 100 credits/month, basic contact management  
  - Pro: 9900 centavos/month, 500 credits/month, advanced analytics, team access  
  - Enterprise: 29900 centavos/month, 1500 credits/month, custom workflows, API access  

### Credit System  
- **Unit Name**: CRM Credit  
- **Pipeline Costs**:  
  - Contact Sync: 10  
  - Appointment Booking: 15  
  - Report Generation: 25  
  - Team Collaboration: 30  
- **Packs**:  
  - - name: "Monthly Pro", credits: 500, price: 9900  
  - - name: "Annual Pro", credits: 6000, price: 118800  
- **Overdraft Policy**: block  
- **Rollover**: false  

### Checkout Integration  
- **Provider**: stripe  
- **Webhook URL**: https://api.petshopcrm.com/webhooks  
- **Webhook Secret Env**: STRIPE_WEBHOOK_SECRET  
- **Success Redirect**: https://petshopcrm.com/thank-you  
- **Cancel Redirect**: https://petshopcrm.com/upgrade  
- **Mock Mode**: true  

### Courses  
- **Enabled**: true  
- **Modules**:  
  - - title: "CRM Basics", lessons: [ { title: "Getting Started", type: "video", duration_min: 15 }, { title: "Contact Management", type: "text", duration_min: 20 } ], drip_days: 3  
  - - title: "Advanced Features", lessons: [ { title: "Analytics Dashboard", type: "quiz", duration_min: 10 }, { title: "Custom Workflows", type: "assignment", duration_min: 30 } ], drip_days: 7  
- **Certification**: true  
- **Completion Threshold**: 0.85  

### Ads  
- **Enabled**: true  
- **Platforms**: [meta, google]  
- **Monthly Budget**: 50000 centavos  
- **Target CPA**: 2000 centavos  
- **Pixel Env**: PETSHOP_PIXEL  

### Emails  
- **Provider**: resend  
- **API Key Env**: RESEND_API_KEY  
- **Sequences**:  
  - - name: "Onboarding", trigger: "signup", emails: [ { delay_hours: 1, template: "welcome" }, { delay_hours: 24, template: "setup-guide" } ]  
  - - name: "Upsell", trigger: "trial-end", emails: [ { delay_hours: 2, template: "upgrade-offer" } ]  
  - - name: "Churn Prevention", trigger: "credit-low", emails: [ { delay_hours: 12, template: "renewal-reminder" } ]  

### Validation  
- **Margin Check**: true  
- **Webhook Test**: true  
- **Mock Before Live**: true