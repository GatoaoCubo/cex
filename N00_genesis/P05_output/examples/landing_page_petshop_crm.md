---
id: landing_page_petshop_crm
kind: landing_page
8f: F6_produce
pillar: P05
title: PetShop CRM - Manage Your Pet Business
version: 1.0.0
created: 2023-10-15
author: landing-page-builder
quality: null
tags: [landing-page, petshop-crm, html, responsive, dark-mode]
stack: HTML + Tailwind CDN
sections_count: 6
responsive: true
dark_mode: true
a11y: AA
seo:
  title: PetShop CRM - Manage Your Pet Business
  description: Streamline pet shop operations with our CRM solution. Track customers, pets, sales, and appointments in one place.
  og_image: https://example.com/og-image.jpg
---

# Landing Page: PetShop CRM

## Design Tokens
| Token | Value |
|-------|-------|
| Primary | #4F46E5 |
| Secondary | #6D28D9 |
| Font Heading | 'Inter', sans-serif |
| Font Body | 'Inter', sans-serif |

## Sections
- [Hero](#hero) - Introduce PetShop CRM and its value proposition
- [Features](#features) - Highlight key CRM functionalities
- [How It Works](#how-it-works) - Demonstrate the CRM workflow
- [Testimonials](#testimonials) - Showcase customer feedback
- [Pricing](#pricing) - Outline subscription plans
- [CTA](#cta) - Encourage sign-ups and demos

## Code
```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <meta property="og:title" content="PetShop CRM - Manage Your Pet Business" />
  <meta property="og:description" content="Streamline pet shop operations with our CRM solution. Track customers, pets, sales, and appointments in one place." />
  <meta property="og:image" content="https://example.com/og-image.jpg" />
  <title>PetShop CRM - Manage Your Pet Business</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <style>
    @layer utilities {
      .dark-mode {
        @apply bg-gray-900 text-white;
      }
    }
  </style>
</head>
<body class="dark-mode">
  <header class="bg-primary text-white py-6">
    <div class="container mx-auto px-4">
      <h1 class="text-3xl font-bold">PetShop CRM</h1>
      <p class="text-lg mt-2">Manage your pet business with ease</p>
    </div>
  </header>

  <section id="hero" class="py-12">
    <div class="container mx-auto px-4">
      <h2 class="text-4xl font-bold mb-4">Streamline Your Pet Shop Operations</h2>
      <p class="text-xl mb-6">Track customers, pets, sales, and appointments in one centralized platform.</p>
      <a href="#cta" class="bg-secondary text-white px-6 py-3 rounded hover:bg-purple-700 transition">Get Started</a>
    </div>
  </section>

  <section id="features" class="py-12 bg-gray-100 dark:bg-gray-800">
    <div class="container mx-auto px-4">
      <h2 class="text-3xl font-bold mb-8">Key Features</h2>
      <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
        <div class="bg-white p-6 rounded shadow dark:bg-gray-700">
          <h3 class="text-xl font-semibold mb-2">Customer Management</h3>
          <p>Organize and track customer information, preferences, and purchase history.</p>
        </div>
        <div class="bg-white p-6 rounded shadow dark:bg-gray-700">
          <h3 class="text-xl font-semibold mb-2">Pet Records</h3>
          <p>Keep detailed records of each pet, including medical history, vaccinations, and more.</p>
        </div>
        <div class="bg-white p-6 rounded shadow dark:bg-gray-700">
          <h3 class="text-xl font-semibold mb-2">Sales Tracking</h3>
          <p>Monitor sales performance, inventory levels, and generate reports for better decision-making.</p>
        </div>
      </div>
    </div>
  </section>

  <section id="how-it-works" class="py-12">
    <div class="container mx-auto px-4">
      <h2 class="text-3xl font-bold mb-8">How It Works</h2>
      <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
        <div class="bg-white p-6 rounded shadow dark:bg-gray-700">
          <h3 class="text-xl font-semibold mb-2">Step 1</h3>
          <p>Sign up for your free account and customize your CRM settings.</p>
        </div>
        <div class="bg-white p-6 rounded shadow dark:bg-gray-700">
          <h3 class="text-xl font-semibold mb-2">Step 2</h3>
          <p>Start managing your customers, pets, and sales with intuitive tools.</p>
        </div>
        <div class="bg-white p-6 rounded shadow dark:bg-gray-700">
          <h3 class="text-xl font-semibold mb-2">Step 3</h3>
          <p>Access real-time analytics and reports to optimize your pet shop operations.</p>
        </div>
      </div>
    </div>
  </section>

  <section id="testimonials" class="py-12 bg-gray-100 dark:bg-gray-800">
    <div class="container mx-auto px-4">
      <h2 class="text-3xl font-bold mb-8">What Our Customers Say</h2>
      <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
        <div class="bg-white p-6 rounded shadow dark:bg-gray-700">
          <p>"PetShop CRM has transformed how we manage our business. It's a game-changer!"</p>
          <p class="mt-2 font-semibold">- Sarah, Pet Shop Owner</p>
        </div>
        <div class="bg-white p-6 rounded shadow dark:bg-gray-700">
          <p>"The pet records feature alone saves us hours every week. Highly recommend!"</p>
          <p class="mt-2 font-semibold">- James, Pet Shop Manager</p>
        </div>
      </div>
    </div>
  </section>

  <section id="pricing" class="py-12">
    <div class="container mx-auto px-4">
      <h2 class="text-3xl font-bold mb-8">Pricing</h2>
      <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
        <div class="bg-white p-6 rounded shadow dark:bg-gray-700">
          <h3 class="text-xl font-semibold mb-2">Basic</h3>
          <p class="text-2xl font-bold mb-4">$29/month</p>
          <ul class="list-disc pl-5 mb-4">
            <li>Up to 100 customers</li>
            <li>Basic reporting</li>
            <li>Email support</li>
          </ul>
          <a href="#cta" class="bg-secondary text-white px-4 py-2 rounded hover:bg-purple-700 transition">Choose Plan</a>
        </div>
        <div class="bg-white p-6 rounded shadow dark:bg-gray-700">
          <h3 class="text-xl font-semibold mb-2">Pro</h3>
          <p class="text-2xl font-bold mb-4">$59/month</p>
          <ul class="list-disc pl-5 mb-4">
            <li>Unlimited customers</li>
            <li>Advanced analytics</li>
            <li>Priority support</li>
          </ul>
          <a href="#cta" class="bg-secondary text-white px-4 py-2 rounded hover:bg-purple-700 transition">Choose Plan</a>
        </div>
        <div class="bg-white p-6 rounded shadow dark:bg-gray-700">
          <h3 class="text-xl font-semibold mb-2">Enterprise</h3>
          <p class="text-2xl font-bold mb-4">Custom Pricing</p>
          <ul class="list-disc pl-5 mb-4">
            <li>Custom features</li>
            <li>24/7 support</li>
            <li>On-premise deployment</li>
          </ul>
          <a href="#cta" class="bg-secondary text-white px-4 py-2 rounded hover:bg-purple-700 transition">Contact Sales</a>
        </div>
      </div>
    </div>
  </section>

  <section id="cta" class="py-12 bg-primary text-white">
    <div class="container mx-auto px-4">
      <h2 class="text-4xl font-bold mb-4">Ready to Transform Your Pet Shop?</h2>
      <p class="text-xl mb-6">Join thousands of pet shop owners who have already streamlined their operations with PetShop CRM.</p>
      <a href="#" class="bg-secondary text-white px-6 py-3 rounded hover:bg-purple-700 transition">Start Free Trial</a>
    </div>
  </section>

  <footer class="bg-gray-800 text-white py-6 mt-12">
    <div class="container mx-auto px-4">
      <p>&copy; 2023 PetShop CRM. All rights reserved.</p>
    </div>
  </footer>
</body>
</html>
```