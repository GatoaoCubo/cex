---
id: landing_page_pet-shop-crm
kind: landing_page
8f: F6_produce
pillar: P05
title: Pet Shop CRM - Manage Your Business Effortlessly
version: 1.0.0
created: 2023-10-15
author: landing-page-builder
quality: null
tags: [landing-page, pet-shop-crm, html+tailwind, responsive, dark-mode]
stack: html+tailwind
sections_count: 6
responsive: true
dark_mode: true
a11y: AA
seo:
  title: Pet Shop CRM | Manage Customers, Inventory & Appointments
  description: Streamline your pet shop operations with our all-in-one CRM solution. Track customers, schedule appointments, manage inventory, and boost sales with ease.
  og_image: https://example.com/og-image.jpg
---

# Landing Page: Pet Shop CRM

## Design Tokens
| Token | Value |
|-------|-------|
| Primary | #3B82F6 |
| Secondary | #60A5FA |
| Font Heading | 'Inter', sans-serif |
| Font Body | 'Inter', sans-serif |

## Sections
- [Hero](#hero)
- [Features](#features)
- [Testimonials](#testimonials)
- [Pricing](#pricing)
- [FAQ](#faq)
- [CTA](#cta)

## Code

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Pet Shop CRM | Manage Customers, Inventory & Appointments</title>
  <meta name="description" content="Streamline your pet shop operations with our all-in-one CRM solution. Track customers, schedule appointments, manage inventory, and boost sales with ease." />
  <meta property="og:title" content="Pet Shop CRM | Manage Customers, Inventory & Appointments" />
  <meta property="og:description" content="Streamline your pet shop operations with our all-in-one CRM solution. Track customers, schedule appointments, manage inventory, and boost sales with ease." />
  <meta property="og:image" content="https://example.com/og-image.jpg" />
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600&display=swap" rel="stylesheet">
  <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-white text-gray-900 dark:bg-gray-900 dark:text-white">
  <section id="hero" class="min-h-screen flex items-center justify-center bg-gradient-to-r from-blue-500 to-indigo-600 text-white">
    <div class="container px-6 py-12 mx-auto">
      <div class="max-w-3xl">
        <h1 class="text-4xl md:text-5xl font-bold mb-6">Pet Shop CRM</h1>
        <p class="text-xl mb-8">Streamline your pet shop operations with our all-in-one CRM solution.</p>
        <a href="#cta" class="inline-block bg-white text-blue-600 font-semibold py-3 px-8 rounded-md hover:bg-blue-50 transition">Get Started</a>
      </div>
    </div>
  </section>

  <section id="features" class="py-16 bg-gray-50 dark:bg-gray-800">
    <div class="container px-6 mx-auto">
      <h2 class="text-3xl font-bold text-center mb-12">Key Features</h2>
      <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
        <div class="bg-white dark:bg-gray-700 p-6 rounded-lg shadow-md">
          <h3 class="text-xl font-semibold mb-3">Customer Management</h3>
          <p>Track customer preferences, purchase history, and communication history in one place.</p>
        </div>
        <div class="bg-white dark:bg-gray-700 p-6 rounded-lg shadow-md">
          <h3 class="text-xl font-semibold mb-3">Appointment Scheduling</h3>
          <p>Automate appointment reminders and manage your schedule efficiently.</p>
        </div>
        <div class="bg-white dark:bg-gray-700 p-6 rounded-lg shadow-md">
          <h3 class="text-xl font-semibold mb-3">Inventory Tracking</h3>
          <p>Monitor stock levels, set reorder alerts, and manage product details effortlessly.</p>
        </div>
      </div>
    </div>
  </section>

  <section id="testimonials" class="py-16 bg-white dark:bg-gray-900">
    <div class="container px-6 mx-auto">
      <h2 class="text-3xl font-bold text-center mb-12">What Our Customers Say</h2>
      <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
        <div class="bg-gray-50 dark:bg-gray-800 p-6 rounded-lg shadow-md">
          <p class="italic mb-4">"This CRM has transformed how we manage our pet shop. Everything is organized and easy to use!"</p>
          <p class="font-semibold">- Sarah, Pet Shop Owner</p>
        </div>
        <div class="bg-gray-50 dark:bg-gray-800 p-6 rounded-lg shadow-md">
          <p class="italic mb-4">"The inventory tracking feature alone saves us hours every week. Highly recommend!"</p>
          <p class="font-semibold">- James, Pet Shop Manager</p>
        </div>
      </div>
    </div>
  </section>

  <section id="pricing" class="py-16 bg-gray-50 dark:bg-gray-800">
    <div class="container px-6 mx-auto">
      <h2 class="text-3xl font-bold text-center mb-12">Pricing</h2>
      <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
        <div class="bg-white dark:bg-gray-700 p-6 rounded-lg shadow-md text-center">
          <h3 class="text-xl font-semibold mb-4">Basic</h3>
          <p class="text-2xl font-bold mb-4">$29/month</p>
          <ul class="space-y-2 mb-6">
            <li>✅ Customer Management</li>
            <li>✅ Appointment Scheduling</li>
            <li>❌ Limited Inventory Tracking</li>
          </ul>
          <a href="#cta" class="inline-block bg-blue-600 text-white font-semibold py-2 px-4 rounded-md hover:bg-blue-700 transition">Get Started</a>
        </div>
        <div class="bg-white dark:bg-gray-700 p-6 rounded-lg shadow-md text-center">
          <h3 class="text-xl font-semibold mb-4">Pro</h3>
          <p class="text-2xl font-bold mb-4">$59/month</p>
          <ul class="space-y-2 mb-6">
            <li>✅ Customer Management</li>
            <li>✅ Appointment Scheduling</li>
            <li>✅ Full Inventory Tracking</li>
          </ul>
          <a href="#cta" class="inline-block bg-blue-600 text-white font-semibold py-2 px-4 rounded-md hover:bg-blue-700 transition">Get Started</a>
        </div>
        <div class="bg-white dark:bg-gray-700 p-6 rounded-lg shadow-md text-center">
          <h3 class="text-xl font-semibold mb-4">Enterprise</h3>
          <p class="text-2xl font-bold mb-4">Custom Pricing</p>
          <ul class="space-y-2 mb-6">
            <li>✅ Customer Management</li>
            <li>✅ Appointment Scheduling</li>
            <li>✅ Full Inventory Tracking</li>
            <li>✅ Dedicated Support</li>
          </ul>
          <a href="#cta" class="inline-block bg-blue-600 text-white font-semibold py-2 px-4 rounded-md hover:bg-blue-700 transition">Contact Us</a>
        </div>
      </div>
    </div>
  </section>

  <section id="faq" class="py-16 bg-white dark:bg-gray-900">
    <div class="container px-6 mx-auto">
      <h2 class="text-3xl font-bold text-center mb-12">FAQ</h2>
      <div class="max-w-2xl mx-auto">
        <div class="mb-6">
          <h3 class="text-xl font-semibold mb-2">What payment methods do you accept?</h3>
          <p class="text-gray-600 dark:text-gray-300">We accept credit cards, PayPal, and bank transfers.</p>
        </div>
        <div class="mb-6">
          <h3 class="text-xl font-semibold mb-2">Can I try the CRM before purchasing?</h3>
          <p class="text-gray-600 dark:text-gray-300">Yes! Sign up for a free 14-day trial to experience all features.</p>
        </div>
        <div class="mb-6">
          <h3 class="text-xl font-semibold mb-2">Is there a mobile app?</h3>
          <p class="text-gray-600 dark:text-gray-300">Currently, we offer a web-based interface, but our mobile app is in development.</p>
        </div>
      </div>
    </div>
  </section>

  <section id="cta" class="py-16 bg-gradient-to-r from-blue-500 to-indigo-600 text-white">
    <div class="container px-6 mx-auto">
      <div class="max-w-3xl mx-auto text-center">
        <h2 class="text-3xl font-bold mb-4">Ready to Transform Your Pet Shop?</h2>
        <p class="text-xl mb-8">Join thousands of pet shop owners who have already streamlined their operations with our CRM.</p>
        <a href="#" class="inline-block bg-white text-blue-600 font-semibold py-3 px-8 rounded-md hover:bg-blue-50 transition">Start Free Trial</a>
      </div>
    </div>
  </section>
</body>
</html>
```

## Deploy Instructions
1. Save the code as `index.html`
2. Host on a web server or static site hosting platform
3. Replace placeholder URLs with your actual content
4. Customize colors, fonts, and text to match your brand
5. Add your Google Analytics tracking code if needed