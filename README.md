# Social Media API - FastAPI Backend

![Project Logo](path_to_your_logo.png)

> A powerful and efficient Social Media API built with FastAPI.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Installation](#installation)
  - [Configuration](#configuration)
- [API Documentation](#api-documentation)
- [Authentication](#authentication)
- [Endpoints](#endpoints)
- [Contributing](#contributing)
- [License](#license)

## Introduction

Welcome to the Social Media API backend project! This API is built using FastAPI and provides a platform for creating, reading, updating, and deleting social media posts. It offers powerful features while maintaining high performance.

## Features

- User registration and authentication
- Create, read, update, and delete posts
- Like and comment on posts
- User profiles and followers
- API jwt-based authentication
- Well-structured API endpoints

## Getting Started

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/social-media-api.git
   cd social-media-api

2. Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

3. Install the dependencies:

```bash
pip install -r requirements.txt
```

### Configuration
1. Create a .env file in the project root and add necessary configuration:

```env
DATABASE_URL=
SECRET_KEY=
ALGORITHM=
ACCESS_TOKEN_EXPIRE_MINUTES=
```
2. Run the migrations:
```bash
alembic upgrade head
```
3. Start the API server:
```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```
