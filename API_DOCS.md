# Simpleblog API Docs
This document describes the implemented endpoints for this application.

Every endpoint will return a JSON Response.

## Dependencies
Simpleblog uses [django-restframework](https://github.com/encode/django-rest-framework) for the API Endpoints.

## Optional Settings
- SIMPLEBLOG_URL_TOKEN_REST
  - Specifies the URL path of the *API* endpoints. The default value is 'rest'.

## Endpoints
Every endpoint will be preceed by the SIMPLEBLOG_URL_TOKEN_REST. See *Optional Settings* above.

### Category
- category/
    - Overview:
        List the categories ordered by id.

    - Query Parameters:
        - limit: Integer
            Limit the returned number of results
        - start: Integer
            Indicates the offset to start returning results.

    - Example Response:
       `GET /rest/category/`

        ```HTTP 200 OK
        Allow: GET, HEAD, OPTIONS
        Content-Type: application/json
        Vary: Accept

        [
            {
                "id": 1,
                "name": "Category 1",
                "slug": "category-1",
                "seo_title": "",
                "seo_description": "",
                "url": "/blog/category/category-1/"
            },
            {
                "id": 2,
                "name": "Category 2",
                "slug": "category-2",
                "seo_title": "Cat 2",
                "seo_description": "Cat 2",
                "url": "/blog/category/category-2/"
            },
            {
                "id": 3,
                "name": "Category 3",
                "slug": "category-3",
                "seo_title": "Cat 3",
                "seo_description": "Cat 3",
                "url": "/blog/category/category-3/"
            }
        ]```


### Entry
- entry/
    - Overview:
        List the entries ordered by publication date

    - Query Parameters:
        - limit: Integer
            Limit the returned number of results
        - start: Integer
            Indicates the offset to start returning results.
        - category: String
            Allow filtering by Category slug.

    - Example Response:
        `GET /rest/entry/`

        ```HTTP 200 OK
        Allow: GET, HEAD, OPTIONS
        Content-Type: application/json
        Vary: Accept

        [
            {
                "id": 3,
                "title": "Entry-3-3",
                "slug": "entry-3-3",
                "image": "http://localhost:8002/media/blog/images/9277f1c75bcce9eda5c5f8f77b0bb7a2_BmLLtBC.jpg",
                "intro": "Quick Intro",
                "publication_date": "2019-07-01T15:39:40.851846Z",
                "seo_title": "Seo Title",
                "seo_description": "Seo Description",
                "modified": "2019-07-01T15:39:40.851949Z",
                "author": "99f60391-a283-4e3c-a119-e88f266d681f",
                "category": 3,
                "url": "/blog/entry-3-3/"
            },
            {
                "id": 2,
                "title": "Entry-2-2",
                "slug": "entry-2-2",
                "image": "http://localhost:8002/media/blog/images/imagen-11.png",
                "intro": "Quick Intro",
                "publication_date": "2019-07-01T15:39:20.629281Z",
                "seo_title": "Seo Title",
                "seo_description": "Seo Description",
                "modified": "2019-07-01T15:39:20.629372Z",
                "author": "99f60391-a283-4e3c-a119-e88f266d681f",
                "category": 2,
                "url": "/blog/entry-2-2/"
            },
            {
                "id": 1,
                "title": "Entry-1-1",
                "slug": "entry-1-1",
                "image": "http://localhost:8002/media/blog/images/lead_720_405.jpg",
                "intro": "Quick Intro",
                "publication_date": "2019-07-01T15:38:21.406302Z",
                "seo_title": "Seo Title",
                "seo_description": "Seo Description",
                "modified": "2019-07-01T15:38:21.406302Z",
                "author": "99f60391-a283-4e3c-a119-e88f266d681f",
                "category": 1,
                "url": "/blog/entry-1-1/"
            }
        ]```

- entry/<id>
    - Overview:
        Returns the detail of an Entry Object.
    
    - id:
        Represents the id of an Entry Object. Must be an integer.

    - Example Response:
        `GET /rest/entry/1/`

        ```HTTP 200 OK
        Allow: GET, HEAD, OPTIONS
        Content-Type: application/json
        Vary: Accept

        {
            "id": 1,
            "title": "Entry-1-1",
            "slug": "entry-1-1",
            "image": "http://localhost:8002/media/blog/images/lead_720_405.jpg",
            "intro": "Quick Intro",
            "content": "<p>This is the HTML Content</p>",
            "publication_date": "2019-07-01T15:38:21.406302Z",
            "seo_title": "Seo Title",
            "seo_description": "Seo Description",
            "modified": "2019-07-01T15:38:21.406302Z",
            "author": "99f60391-a283-4e3c-a119-e88f266d681f",
            "category": 1,
            "url": "/blog/entry-1-1/"
        }```


- entry/<slug>
    - Overview:
        Returns the detail of an Entry Object.

    - slug:
        Represents the slug of an Entry Object. Must be a word.
    
    - Example Response:
        `GET /rest/entry/entry-1-1/`

        ```HTTP 200 OK
        Allow: GET, HEAD, OPTIONS
        Content-Type: application/json
        Vary: Accept

        {
            "id": 1,
            "title": "Entry-1-1",
            "slug": "entry-1-1",
            "image": "http://localhost:8002/media/blog/images/lead_720_405.jpg",
            "intro": "Quick Intro",
            "content": "<p>This is the HTML Content</p>",
            "publication_date": "2019-07-01T15:38:21.406302Z",
            "seo_title": "Seo Title",
            "seo_description": "Seo Description",
            "modified": "2019-07-01T15:38:21.406302Z",
            "author": "99f60391-a283-4e3c-a119-e88f266d681f",
            "category": 1,
            "url": "/blog/entry-1-1/"
        }```