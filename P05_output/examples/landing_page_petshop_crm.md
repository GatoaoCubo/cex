---
id: landing_page_petshop_crm
kind: landing_page
pillar: P05
title: "Pet Shop CRM - Manage Your Pets with Ease!"
version: 1.0.0
created: 2023-10-15
author: landing-page-builder
quality: null
tags: [landing-page, petshop-crm, html, responsive, dark-mode]
stack: html
sections_count: 6
responsive: true
dark_mode: true
a11y: AA
seo:
  title: "Pet Shop CRM - Transform Your Pet Shop with AI-Powered CRM"
  description: "Automate bookings, track inventory, and boost customer loyalty with our AI-powered CRM tailored for pet shops. Start your free trial today!"
  og_image: "https://example.com/og-image.jpg"
---

# Landing Page: Pet Shop CRM

## Design Tokens
| Token | Value |
|-------|-------|
| Primary | #3B82F6 |
| Secondary | #60A5FA |
| Font Heading | 'Poppins', sans-serif |
| Font Body | 'Inter', sans-serif |

## Sections
- [Hero Section](#hero-section)
- [Problem/Solution](#problem-solution)
- [Features](#features)
- [Testimonials](#testimonials)
- [Call-to-Action](#call-to-action)
- [Footer](#footer)

## Code

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <meta property="og:title" content="Pet Shop CRM - Transform Your Pet Shop with AI-Powered CRM" />
  <meta property="og:description" content="Automate bookings, track inventory, and boost customer loyalty with our AI-powered CRM tailored for pet shops. Start your free trial today!" />
  <meta property="og:image" content="https://example.com/og-image.jpg" />
  <meta property="og:url" content="https://example.com/pet-shop-crm" />
  <title>Pet Shop CRM - Transform Your Pet Shop with AI-Powered CRM</title>
  <script src="https://cdn.tailwindcss.com"></script>
  <style>
    @media (prefers-color-scheme: dark) {
      :root {
        --bg-color: #0f172a;
        --text-color: #f3f4f6;
        --accent-color: #3b82f6;
      }
    }
  </style>
</head>
<body class="bg-white text-gray-900 dark:bg-gray-900 dark:text-white transition-colors duration-300">
  <header class="sticky top-0 z-10 bg-white dark:bg-gray-800 shadow-md">
    <div class="container mx-auto px-4 py-4 flex justify-between items-center">
      <h1 class="text-2xl font-bold">Pet Shop CRM</h1>
      <nav class="hidden md:flex space-x-6">
        <a href="#hero-section" class="hover:text-blue-500">Home</a>
        <a href="#features" class="hover:text-blue-500">Features</a>
        <a href="#testimonials" class="hover:text-blue-500">Testimonials</a>
      </nav>
    </div>
  </header>

  <section id="hero-section" class="py-20 bg-gradient-to-r from-blue-500 to-purple-600 text-white">
    <div class="container mx-auto px-4 text-center">
      <h2 class="text-4xl md:text-5xl font-extrabold mb-6">Transform Your Pet Shop with AI-Powered CRM</h2>
      <p class="text-xl mb-8">Automate bookings, track inventory, and boost customer loyalty with our AI-powered CRM tailored for pet shops.</p>
      <a href="#call-to-action" class="bg-white text-blue-600 px-8 py-3 rounded-md hover:bg-blue-50 transition-colors duration-300">Start Free Trial</a>
    </div>
  </section>

  <section id="problem-solution" class="py-20 bg-gray-50 dark:bg-gray-800">
    <div class="container mx-auto px-4">
      <div class="max-w-3xl mx-auto text-center">
        <h3 class="text-3xl font-bold mb-6">The Problem</h3>
        <p class="text-lg mb-6">Lost customers, manual bookings, and inventory chaos are common challenges for pet shop owners. Our CRM streamlines operations and delivers 3x more bookings.</p>
        <h3 class="text-3xl font-bold mb-6">The Solution</h3>
        <p class="text-lg">Our AI-powered CRM automates bookings, tracks inventory, and provides customer insights to help you grow your business.</p>
      </div>
    </div>
  </section>

  <section id="features" class="py-20">
    <div class="container mx-auto px-4">
      <h2 class="text-3xl font-bold text-center mb-12">Key Features</h2>
      <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
        <div class="bg-white dark:bg-gray-700 p-6 rounded-lg shadow-md">
          <h3 class="text-xl font-bold mb-2">AI-Powered Booking</h3>
          <p>Automate pet grooming, boarding, and playdate bookings with our intelligent scheduling system.</p>
        </div>
        <div class="bg-white dark:bg-gray-700 p-6 rounded-lg shadow-md">
          <h3 class="text-xl font-bold mb-2">Inventory Management</h3>
          <p>Track pet supplies, food, and toys with real-time inventory alerts to prevent stockouts.</p>
        </div>
        <div class="bg-white dark:bg-gray-700 p-6 rounded-lg shadow-md">
          <h3 class="text-xl font-bold mb-2">Customer Insights</h3>
          <p>Gain valuable insights into customer preferences and behavior to improve your services.</p>
        </div>
      </div>
    </div>
  </section>

  <section id="testimonials" class="py-20 bg-gray-50 dark:bg-gray-800">
    <div class="container mx-auto px-4">
      <h2 class="text-3xl font-bold text-center mb-12">What Our Customers Say</h2>
      <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
        <div class="bg-white dark:bg-gray-700 p-6 rounded-lg shadow-md">
          <p class="italic">"Pet Shop CRM has transformed how we manage our business. The inventory tracking alone has saved us hours each week!"</p>
          <p class="mt-4 font-bold">- Sarah M., Pet Shop Owner</p>
        </div>
        <div class="bg-white dark:bg-gray-700 p-6 rounded-lg shadow-md">
          <p class="italic">"The AI booking system has reduced our no-shows by 40%. Highly recommend!"</p>
          <p class="mt-4 font-bold">- James L., Pet Shop Owner</p>
        </div>
      </div>
    </div>
  </section>

  <section id="call-to-action" class="py-20 bg-gradient-to-r from-blue-500 to-purple-600 text-white">
    <div class="container mx-auto px-4 text-center">
      <h2 class="text-4xl font-extrabold mb-6">Ready to Transform Your Pet Shop?</h2>
      <p class="text-xl mb-8">Join thousands of pet shop owners who have already streamlined their operations with Pet Shop CRM.</p>
      <a href="#" class="bg-white text-blue-600 px-8 py-3 rounded-md hover:bg-blue-50 transition-colors duration-300">Start Free Trial</a>
    </div>
  </section>

  <footer id="footer" class="py-10 bg-gray-800 text-white">
    <div class="container mx-auto px-4 text-center">
      <p>&copy; 2023 Pet Shop CRM. All rights reserved.</p>
    </div>
  </footer>
</body>
</html>