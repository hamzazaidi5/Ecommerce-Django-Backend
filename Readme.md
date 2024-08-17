# E-Commerce Backend System

## Overview

This document provides an overview of the schema design, indexing strategy, caching layer, and scalability plan for the e-commerce backend system developed using Django and PostgreSQL.

## Schema Design

### Entities

1. **User**
   - **Fields:**
     - `id`: Primary key, auto-generated integer.
     - `username`: Unique string identifier for the user.
     - `email`: User's email address.
     - `password`: User's password (hashed).
     - `role`: Role of the user (Admin or Customer).

2. **Product**
   - **Fields:**
     - `id`: Primary key, auto-generated integer.
     - `name`: Name of the product.
     - `description`: Detailed description of the product.
     - `price`: Price of the product.
     - `stock_quantity`: Quantity of the product in stock.
     - `categories`: Categories to which the product belongs.

3. **Order**
   - **Fields:**
     - `id`: Primary key, auto-generated integer.
     - `user`: Foreign key referencing `User`.
     - `order_date`: Date and time when the order was placed.
     - `status`: Current status of the order (e.g., Pending, Shipped).
     - `total_items`: Total number of items in the order (denormalized field).

4. **OrderItem**
   - **Fields:**
     - `id`: Primary key, auto-generated integer.
     - `order`: Foreign key referencing `Order`.
     - `product`: Foreign key referencing `Product`.
     - `quantity`: Quantity of the product in the order.
     - `price_at_purchase`: Price of the product at the time of purchase.

5. **Category**
   - **Fields:**
     - `id`: Primary key, auto-generated integer.
     - `name`: Name of the category.
     - `parent`: Self-referencing foreign key for hierarchical categorization.

6. **ProductRecommendation**
   - **Fields:**
     - `id`: Primary key, auto-generated integer.
     - `product`: Foreign key referencing `Product`.
     - `recommended_product`: Foreign key referencing `Product` for recommended products.

## Indexing Strategy

To optimize query performance, the following indexes are used:

1. **Order Model:**
   - **`user` Index:** Speeds up queries filtering orders by user.
   - **`order_date` Index:** Speeds up queries filtering orders by date.

2. **OrderItem Model:**
   - **`order` Index:** Speeds up queries filtering items by order.
   - **`product` Index:** Speeds up queries filtering items by product.

## Caching Strategy

The caching layer is implemented using Django's in-memory cache to reduce database load and improve response times. Here’s how caching is handled:

1. **Products List Caching:**
   - **Cache Key:** `products_list`
   - **Cache Duration:** 15 minutes
   - **Purpose:** To cache the list of products and reduce database queries when fetching the product list.

   ```python
   from django.core.cache import cache

   def list(self, request, *args, **kwargs):
       cache_key = 'products_list'
       cached_data = cache.get(cache_key)

       if cached_data:
           return Response(cached_data)

       response = super().list(request, *args, **kwargs)
       cache.set(cache_key, response.data, timeout=60 * 15)
       return response

## Scalability Plan

### Database Scalability

1. **Read Replicas:**
   - Implement PostgreSQL read replicas to distribute read queries, enhancing performance during high traffic periods.

2. **Partitioning:**
   - Partition large tables, such as `Orders`, to efficiently manage and query extensive datasets.

### Application Scalability

1. **Horizontal Scaling:**
   - Deploy multiple instances of the application behind a load balancer to handle increased traffic and improve availability.

2. **Caching Layer:**
   - Integrate distributed caching solutions like Redis or Memcached to scale caching across multiple instances, reducing latency.

3. **Asynchronous Task Processing:**
   - Use Celery with Redis for handling background tasks, improving application responsiveness and throughput.


### Conclusion

This document details the schema design, indexing strategy, caching approach, and scalability plan for the e-commerce backend system. The outlined strategies aim to optimize data querying, maintain performance, and ensure scalability to accommodate increasing data volumes and user traffic.
