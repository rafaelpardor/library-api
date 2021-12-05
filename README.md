# Library

## Commands

```bash
docker-compose -f docker-compose.yml up --build
docker-compose -f docker-compose.yml run books_api python manage.py recreate_db
docker-compose -f docker-compose.yml run books_api python manage.py tests
```
