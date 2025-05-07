# Health and Fitness Tracking Platform

## Overview
------------

The Health and Fitness Tracking Platform is a comprehensive web application designed to help users track their fitness progress, plan workouts, monitor nutrition, and achieve their health goals. The system provides personalized insights, analytics, and recommendations to enhance the user experience.

## Project Structure
---------------------

The project is organized into the following modules:

* **[com.edstem.health_and_fitness_tracker](src/main/java/com/edstem/health_and_fitness_tracker)**: The main application package.
* **[com.edstem.health_and_fitness_tracker.config](src/main/java/com/edstem/health_and_fitness_tracker/config)**: Configuration classes for the application.
* **[com.edstem.health_and_fitness_tracker.contracts](src/main/java/com/edstem/health_and_fitness_tracker/contracts)**: Data transfer objects (DTOs) for API requests and responses.
* **[com.edstem.health_and_fitness_tracker.controllers](src/main/java/com/edstem/health_and_fitness_tracker/controllers)**:REST controllers for handling API requests.
* **[com.edstem.health_and_fitness_tracker.enums](src/main/java/com/edstem/health_and_fitness_tracker/enums)**: Enumerations for various application constants.
* **[com.edstem.health_and_fitness_tracker.exceptions](src/main/java/com/edstem/health_and_fitness_tracker/exceptions)**: Custom exception classes for handling errors.
* **[com.edstem.health_and_fitness_tracker.model](src/main/java/com/edstem/health_and_fitness_tracker/models)**: Entity classes for database tables
* **[com.edstem.health_and_fitness_tracker.repository](src/main/java/com/edstem/health_and_fitness_tracker/repositories)**: Data access object (DAO) interfaces for database operations.
* **[com.edstem.health_and_fitness_tracker.services](src/main/java/com/edstem/health_and_fitness_tracker/services)**: Service classes for business logic.

## Features
------------

The application provides the following features:

1. User Management
* User registration and profile management.
* View and update personal profiles.

2. Exercise Library
* Access a database of exercises categorized by type and muscle group.
* Add new exercises to the library.

3. Workout Management

* Create and manage workout plans.
* Add exercises to workouts.
* Get personalized workout recommendations.

4. User Progress Tracking

* Log workout history and track completed workouts.
* Record body measurements and fitness progress.
* Generate analytics based on user activity.

5. Nutrition Tracking

* Track daily nutrition intake.
* Retrieve nutrition logs for specific dates.
* Analyze nutrition data for dietary insights.

6. Goals and Achievements

* Set and manage fitness goals.
* Track achievements and completed challenges.
* View and participate in fitness challenges.

## Setup and Installation
---------------------------

To set up and install the application, follow these steps:

1.  Clone the repository using Git.
2.  Open the project in IntelliJ IDEA.
3.  Configure the database connection properties in the `application.yaml` file.
4.  Run the application using the `HealthAndFitnessTrackerApplication` class.

## API Documentation
---------------------

The API documentation is available at [Swagger UI - API Documentation](http://localhost:8080/swagger-ui/index.html) after running the application.
 
