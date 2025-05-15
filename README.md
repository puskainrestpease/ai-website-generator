# AI Website Generator 🚀

[![CI/CD](https://github.com/puskainrestpease/ai-website-generator/actions/workflows/ci-cd.yml/badge.svg)](https://github.com/puskainrestpease/ai-website-generator/actions)
[![Docker](https://img.shields.io/docker/pulls/puskainrestpease/ai-website-generator)](https://hub.docker.com/r/puskainrestpease/ai-website-generator)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Генератор сайтов на Next.js с использованием AI (Ollama).

## Features ✨
- Генерация кода через LLM (Llama2)
- JWT аутентификация
- PostgreSQL + Redis
- Rate limiting
- Полный CI/CD
- Docker-ориентированная архитектура
- Мониторинг (Sentry + Prometheus)
- Автоматическая документация API

## Быстрый старт 🚀

```bash
git clone https://github.com/yourusername/ai-website-generator.git
cd ai-website-generator

# Запуск в development режиме
docker-compose -f docker-compose.dev.yml up

# Запуск в production режиме
docker-compose up -d

(проект в разработке)