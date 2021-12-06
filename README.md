# Library

## Commands

```bash
docker-compose -f docker-compose.yml up --build
docker-compose -f docker-compose.yml run books_api python manage.py recreate_db
docker-compose -f docker-compose.yml run books_api python manage.py tests
```

```sql
INSERT INTO book (title, subtitle, author, category, publish_date, description, created_at, updated_at, deleted_at)
VALUES ('Book title', 'book subtitle', 'book author', 'book category', current_date, 'book description', now(), now(), null );
```
