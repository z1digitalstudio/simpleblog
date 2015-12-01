# Simpleblog
Simple blog application for django framework.

# Dependencies
Simpleblog uses [django-redactoreditor](https://github.com/mazelife/django-redactoreditor) for enhancing the admin form for blog entries.

#Required Settings
- SIMPLEBLOG_TWITTER_ACCOUNT
  - Specifies the referenced *Twitter Account* when sharing a post.
- SIMPLEBLOG_FACEBOOK_SITE_NAME
  - Specifies the referenced *Facebook Site* when sharing a post.
- SIMPLEBLOG_DEFAULT_META_TITLE
  - Specifies the site title by default.
- SIMPLEBLOG_DEFAULT_META_SITE_NAME
  - Specifies the suffix that will appear after SIMPLEBLOG_DEFAULT_META_TITLE.
  - It's recommended to add a marker as ' - ' or ' | ' at the beginning.
- SIMPLEBLOG_DEFAULT_META_DESCRIPTION
  - Specifies the site description by default.
- SIMPLEBLOG_DEFAULT_META_AUTHOR
  - Specifies the fallback site author by default.

#Optional Settings
- SIMPLEBLOG_PAGINATION_LIMIT
  - Specifies the number of posts shown in each list view.
- SIMPLEBLOG_LAST_ENTRIES_NUMBER
  - Specifies the number of entries shown in *Last Entries* panel.
- SIMPLEBLOG_URL_TOKEN_CATEGORY
  - Specifies the URL path of the *Category* list view. The default value is 'category'.
- SIMPLEBLOG_URL_TOKEN_AUTHOR
  - Specifies the URL path of the *Author* list view. The default value is 'author'.
